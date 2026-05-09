import re
import json
import os

sites = [
    "canvas-visual.aura.build",
    "crewai.com",
    "instagram-slides",
    "langchain.com",
    "n8n.io (1)"
]

mega_asset_map = {}
mega_head_styles = ""
mega_head_scripts = ""
mega_footer_scripts = ""

# 1. Parse assets and head elements
for site in sites:
    # use index.html or design-system.html depending on availability
    # crewai, langchain, n8n have design-system.html, canvas and instagram have index.html
    # but index.html has the full head anyway.
    file_path = f"{site}/index.html"
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Asset Map extraction
    asset_map_match = re.search(r'var ASSET_MAP = (\{.*?\});', html, flags=re.DOTALL)
    if asset_map_match:
        try:
            am = json.loads(asset_map_match.group(1))
            for k, v in am.items():
                if v.startswith("assets/"):
                    mega_asset_map[k] = f"{site}/{v}"
                else:
                    mega_asset_map[k] = v
        except:
            pass

    # Head styles (link and style)
    head_match = re.search(r'<head>(.*?)</head>', html, flags=re.DOTALL)
    if head_match:
        head_content = head_match.group(1)
        # remove asset map script from head content
        head_content = re.sub(r'<script data-offline-resolve="1">.*?</script>', '', head_content, flags=re.DOTALL)
        
        # fix paths
        head_content = head_content.replace('href="assets/', f'href="{site}/assets/')
        head_content = head_content.replace('src="assets/', f'src="{site}/assets/')
        
        # separate scripts and styles
        styles = "".join(re.findall(r'<link[^>]*rel="stylesheet"[^>]*>|<style.*?</style>', head_content, flags=re.DOTALL))
        scripts = "".join(re.findall(r'<script[^>]*>.*?</script>', head_content, flags=re.DOTALL))
        
        mega_head_styles += f"\n<!-- STYLES FOR {site} -->\n{styles}"
        mega_head_scripts += f"\n<!-- SCRIPTS FOR {site} -->\n{scripts}"
        
    # Footer scripts
    main_end = html.find('</main>')
    if main_end == -1:
        main_end = html.rfind('</div>', 0, html.rfind('</body>'))
        
    if main_end != -1:
        footer_content = html[main_end:]
        footer_content = footer_content.replace('src="assets/', f'src="{site}/assets/')
        scripts = "".join(re.findall(r'<script[^>]*>.*?</script>', footer_content, flags=re.DOTALL))
        mega_footer_scripts += f"\n<!-- FOOTER SCRIPTS FOR {site} -->\n{scripts}"

# Create mega asset map script
asset_map_script = f"""<script data-offline-resolve="1">(function(){{
var ASSET_MAP = {json.dumps(mega_asset_map)};
// Pre-populate path+query keys
var _add = {{}};
for (var _k in ASSET_MAP) {{
  try {{ var _u = new URL(_k); _add[_u.pathname + _u.search] = ASSET_MAP[_k]; }}
  catch(e){{}}
}}
for (var _k in _add) if (!ASSET_MAP[_k]) ASSET_MAP[_k] = _add[_k];
function resolveLocal(u){{
  if (!u || typeof u !== 'string') return null;
  if (u.indexOf('data:') === 0 || u.indexOf('blob:') === 0) return null;
  if (ASSET_MAP[u]) return ASSET_MAP[u];
  try {{
    var url = new URL(u, location.href);
    var pq = url.pathname + url.search;
    if (ASSET_MAP[pq]) return ASSET_MAP[pq];
    if (/_next\\/image$/.test(url.pathname)) {{
      var t = url.searchParams.get('url');
      if (t) {{
        var dec = decodeURIComponent(t);
        if (ASSET_MAP[dec]) return ASSET_MAP[dec];
        var bare = dec.split('?')[0];
        for (var k in ASSET_MAP) {{
          if (k.split('?')[0] === bare) return ASSET_MAP[k];
        }}
      }}
    }}
  }} catch(e){{}}
  return null;
}}
function rewriteSrcset(s){{
  if (!s || typeof s !== 'string') return s;
  return s.split(',').map(function(it){{
    var p = it.trim().split(/\\s+/);
    var loc = resolveLocal(p[0]);
    if (loc) p[0] = loc;
    return p.join(' ');
  }}).join(', ');
}}
function patchSetter(klass, prop, transform){{
  if (!klass || !klass.prototype) return;
  var desc = Object.getOwnPropertyDescriptor(klass.prototype, prop);
  if (!desc || !desc.set) return;
  Object.defineProperty(klass.prototype, prop, {{
    configurable: true,
    get: desc.get,
    set: function(v){{
      try {{
        if (this.crossOrigin) {{}} 
        else if (transform === 'srcset') {{ v = rewriteSrcset(v); }} 
        else {{ var loc = resolveLocal(v); if (loc) v = loc; }}
      }} catch(e){{}}
      desc.set.call(this, v);
    }}
  }});
}}
patchSetter(window.HTMLScriptElement, 'src');
patchSetter(window.HTMLLinkElement, 'href');
patchSetter(window.HTMLImageElement, 'src');
patchSetter(window.HTMLImageElement, 'srcset', 'srcset');
patchSetter(window.HTMLSourceElement, 'src');
patchSetter(window.HTMLSourceElement, 'srcset', 'srcset');
patchSetter(window.HTMLMediaElement, 'src');
patchSetter(window.HTMLIFrameElement, 'src');
var _setAttr = Element.prototype.setAttribute;
Element.prototype.setAttribute = function(name, value){{
  try {{
    if (typeof value === 'string' && !this.crossOrigin) {{
      if (name === 'src' || name === 'href') {{ var loc = resolveLocal(value); if (loc) value = loc; }} 
      else if (name === 'srcset') {{ value = rewriteSrcset(value); }}
    }}
  }} catch(e){{}}
  return _setAttr.call(this, name, value);
}};
window.__resolveLocal = resolveLocal;
window.__rewriteSrcset = rewriteSrcset;
}})();</script>"""

mega_head = f"<head>\n{asset_map_script}\n{mega_head_styles}\n{mega_head_scripts}\n</head>"

# Body Structure
# We will use n8n body structure, and inject sections
n8n_body = ""
with open("n8n.io (1)/design-system.html", "r", encoding="utf-8") as f:
    n8n_ds = f.read()
    b_start = n8n_ds.find('<body')
    b_end = n8n_ds.find('</body>')
    n8n_body = n8n_ds[b_start:b_end]

# Rewrite n8n assets
n8n_body = n8n_body.replace('src="assets/', 'src="n8n.io (1)/assets/')

# NOW: We inject mega hero into n8n_body!
# The n8n hero is a `<section id="hero"` or `<div id="hero"`.
# Let's find it.
hero_start = n8n_body.find('<div id="hero"')
if hero_start == -1:
    hero_start = n8n_body.find('<section id="hero"')

mega_hero = """
<section id="mega-hero" style="position:relative; width:100%; min-height: 100vh; overflow:hidden; display:flex; flex-direction:column; align-items:center; justify-content:center; background-color:#000;">
    <!-- CANVAS VISUAL BACKGROUND -->
    <div class="aura-background-component top-0 w-full h-screen -z-10 saturate-0 brightness-50 mix-blend-screen absolute" data-alpha-mask="80" style="mask-image: linear-gradient(to bottom, transparent, black 0%, black 80%, transparent); -webkit-mask-image: linear-gradient(to bottom, transparent, black 0%, black 80%, transparent)">
        <div class="aura-background-component top-0 w-full -z-10 absolute h-full">
            <div class="absolute w-full h-full left-0 top-0 -z-10" data-us-project="fbC2LfIKPWAtosLcp0kG"></div>
        </div>
    </div>
    
    <!-- CREW AI MARQUEE BACKGROUND -->
    <div class="hero-marquee-wrapper" style="position:absolute; top: 20%; width:100%; opacity:0.3;">
        <div class="marquee" style="border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 20px 0;">
            <div class="marquee-images-wrapper">
                <div class="marquee-images-holder">
                    <h3 class="text-color-white" style="padding: 0 40px;">VIBE</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">DESIGN</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">MEGA</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">SYSTEM</h3>
                </div>
                <div class="marquee-images-holder">
                    <h3 class="text-color-white" style="padding: 0 40px;">VIBE</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">DESIGN</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">MEGA</h3>
                    <h3 class="text-color-white" style="padding: 0 40px;">SYSTEM</h3>
                </div>
            </div>
        </div>
    </div>

    <!-- MAIN CONTENT -->
    <div style="z-index: 10; text-align: center; max-width: 800px; padding: 2rem;">
        <!-- LANGCHAIN ANIMATED TITLE -->
        <h1 class="t-heading-1-rg color-t-7fc8ff homepage" style="font-size: 5rem; margin-bottom: 2rem;">Mega <span class="word-swap"><span class="word-old">UI</span><span class="word-new">Library</span></span></h1>
        
        <p class="text-color-white text-size-large" style="margin-bottom: 3rem;">A creative blend of Canvas Visual, CrewAI, LangChain, Instagram Slides and n8n.</p>
        
        <!-- N8N / CANVAS BUTTONS -->
        <div style="display:flex; gap:20px; justify-content:center;">
            <a href="#typography" class="button-v2 w-variant-cc2081e2-2f66-fa48-5d36-c70458cedec9 w-inline-block">
                <div>Explore Typography</div>
            </a>
            
            <a class="group relative isolate inline-flex items-center justify-center gap-2 overflow-hidden rounded-none bg-transparent pt-2.5 pr-5 pb-2.5 pl-5 text-sm font-semibold text-white transition-all duration-300 hover:shadow-[0_0_30px_-5px_rgba(249,115,22,0.3)]" href="#components" style="--spread: 90deg; --shimmer-color: #F97316; --speed: 3s; --cut: 1px;">
                <div class="absolute inset-0 -z-20 overflow-hidden">
                    <div class="absolute inset-[-100%] animate-[spin_var(--speed)_linear_infinite] [background:conic-gradient(from_var(--spread),transparent_0,var(--shimmer-color)_50%,transparent_100%)]"></div>
                </div>
                <div class="absolute inset-[var(--cut)] -z-10 bg-black"></div>
                Explore Components
            </a>
        </div>
    </div>
</section>
"""

# Replace n8n hero with mega hero
if hero_start != -1:
    hero_end = n8n_body.find('</section>', hero_start)
    if hero_end != -1:
        n8n_body = n8n_body[:hero_start] + mega_hero + n8n_body[hero_end+10:]
    else:
        # try div
        hero_end = n8n_body.find('</div>', hero_start)
        n8n_body = n8n_body[:hero_start] + mega_hero + n8n_body[hero_end+6:]

# Final assembly
full_html = f"<!DOCTYPE html>\n<html>\n{mega_head}\n{n8n_body}\n{mega_footer_scripts}\n</body>\n</html>"

with open("design_system.html", "w", encoding="utf-8") as f:
    f.write(full_html)

print("Mega design system created!")
