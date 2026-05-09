import re

with open('design_system.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the Global Background Elements section
bg_marker = '<h3 class="font-geomanist text-xl title title--gray mt-16 mb-6">Global Background Elements</h3>'
start_idx = html.find(bg_marker)

if start_idx != -1:
    # Find the div immediately following the marker
    div_start_idx = html.find('<div', start_idx + len(bg_marker))
    
    # We need to find the matching closing </div> for this relative h-[300px] div
    # It's safer to just replace the specific div we know is there:
    target_div_start = '<div class="relative h-[300px] w-full border border-white/20 rounded-xl overflow-hidden bg-shades-midnight-navy">'
    
    if target_div_start in html[start_idx:]:
        
        new_backgrounds_html = """
<div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-16">
    
    <!-- 1. Aura Visual Glow Engine -->
    <div class="relative h-[400px] w-full border border-white/10 rounded-2xl overflow-hidden group">
        <div class="absolute inset-0 z-10 flex items-center justify-center pointer-events-none">
            <h4 class="text-white text-xl font-bold tracking-widest uppercase" style="text-shadow: 0 4px 20px rgba(0,0,0,0.8);">Aura Visual Engine</h4>
        </div>
        <div class="absolute inset-0 bg-[#0a0a0a]"></div>
        <div class="absolute inset-0 opacity-50 mix-blend-screen transition-opacity duration-700 group-hover:opacity-100" style="background: radial-gradient(circle at 50% 50%, rgba(249,115,22,0.3) 0%, transparent 60%);"></div>
        <div class="aura-background-component absolute inset-0 w-full h-full saturate-100 brightness-75 mix-blend-screen" data-alpha-mask="80" style="mask-image: linear-gradient(to bottom, transparent, black 10%, black 90%, transparent); -webkit-mask-image: linear-gradient(to bottom, transparent, black 10%, black 90%, transparent)">
            <div class="absolute w-full h-full left-0 top-0" style="background: repeating-linear-gradient(90deg, rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 1px, transparent 1px, transparent 40px), repeating-linear-gradient(0deg, rgba(255,255,255,0.03) 0px, rgba(255,255,255,0.03) 1px, transparent 1px, transparent 40px);"></div>
            <div class="absolute left-1/4 top-1/4 w-[200px] h-[200px] bg-[#F97316] rounded-full blur-[80px] opacity-20 animate-pulse"></div>
            <div class="absolute right-1/4 bottom-1/4 w-[250px] h-[250px] bg-[#ff3c64] rounded-full blur-[100px] opacity-10"></div>
        </div>
    </div>

    <!-- 2. N8N Deep Space Stars -->
    <div class="relative h-[400px] w-full border border-white/10 rounded-2xl overflow-hidden bg-shades-midnight-navy group">
        <div class="absolute inset-0 z-10 flex items-center justify-center pointer-events-none">
            <h4 class="text-white text-xl font-bold tracking-widest uppercase" style="text-shadow: 0 4px 20px rgba(0,0,0,0.8);">Deep Space Grid</h4>
        </div>
        <div class="absolute inset-0" style="background-image: url('n8n.io (1)/assets/4de1faa1763536c7_stars-bg.svg'); background-size: cover; background-position: center; opacity: 0.6;"></div>
        <div class="absolute inset-0" style="background: radial-gradient(circle at center, transparent 0%, #000 100%); opacity: 0.8;"></div>
        <div class="absolute inset-0" style="background: repeating-linear-gradient(90deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 50px), repeating-linear-gradient(0deg, rgba(255,255,255,0.02) 0px, rgba(255,255,255,0.02) 1px, transparent 1px, transparent 50px); transform: perspective(500px) rotateX(60deg) translateY(-100px) translateZ(-200px); transform-origin: top center; border-top: 1px solid rgba(255, 60, 100, 0.3);"></div>
        <div class="absolute top-0 left-1/2 -translate-x-1/2 w-3/4 h-[2px]" style="background: linear-gradient(90deg, transparent, #ff3c64, transparent); box-shadow: 0 0 20px #ff3c64, 0 0 40px #ff3c64;"></div>
        <div class="circle-gradient-white transition-transform duration-1000 group-hover:scale-150" style="left:50%; top:50%; --tw-bg-opacity:0.15; width:300px; height:300px; transform: translate(-50%, -50%);"></div>
    </div>

    <!-- 3. LangChain Data Flow -->
    <div class="relative h-[400px] w-full border border-white/10 rounded-2xl overflow-hidden group" style="background: #0f172a;">
        <div class="absolute inset-0 z-10 flex items-center justify-center pointer-events-none">
            <h4 class="text-white text-xl font-bold tracking-widest uppercase" style="text-shadow: 0 4px 20px rgba(0,0,0,0.8);">Data Flow Matrix</h4>
        </div>
        <div class="absolute inset-0 opacity-20" style="background-image: radial-gradient(#7fc8ff 1px, transparent 1px); background-size: 24px 24px;"></div>
        <div class="absolute inset-0" style="background: linear-gradient(to right, rgba(15,23,42,1) 0%, rgba(15,23,42,0) 50%, rgba(15,23,42,1) 100%);"></div>
        <div class="absolute inset-0" style="background: linear-gradient(to bottom, rgba(15,23,42,1) 0%, rgba(15,23,42,0) 50%, rgba(15,23,42,1) 100%);"></div>
        <div class="absolute top-1/4 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-[#7fc8ff] to-transparent opacity-50"></div>
        <div class="absolute top-3/4 left-0 w-full h-[1px] bg-gradient-to-r from-transparent via-[#7fc8ff] to-transparent opacity-30"></div>
        <div class="absolute left-1/3 top-0 w-[1px] h-full bg-gradient-to-b from-transparent via-[#7fc8ff] to-transparent opacity-40"></div>
        <div class="absolute right-1/3 top-0 w-[1px] h-full bg-gradient-to-b from-transparent via-[#7fc8ff] to-transparent opacity-60"></div>
        
        <!-- Glowing nodes -->
        <div class="absolute left-1/3 top-1/4 w-3 h-3 bg-[#7fc8ff] rounded-full -translate-x-[5px] -translate-y-[5px] shadow-[0_0_15px_#7fc8ff] transition-all duration-300 group-hover:scale-150 group-hover:shadow-[0_0_25px_#7fc8ff]"></div>
        <div class="absolute right-1/3 top-3/4 w-3 h-3 bg-[#7fc8ff] rounded-full -translate-x-[5px] -translate-y-[5px] shadow-[0_0_15px_#7fc8ff] transition-all duration-300 group-hover:scale-150 group-hover:shadow-[0_0_25px_#7fc8ff]"></div>
    </div>

    <!-- 4. CrewAI Cinematic Light Leak -->
    <div class="relative h-[400px] w-full border border-white/10 rounded-2xl overflow-hidden group" style="background: #000;">
        <div class="absolute inset-0 z-10 flex items-center justify-center pointer-events-none">
            <h4 class="text-white text-xl font-bold tracking-widest uppercase" style="text-shadow: 0 4px 20px rgba(0,0,0,0.8);">Cinematic Leak</h4>
        </div>
        <div class="absolute -top-[20%] -right-[10%] w-[70%] h-[70%] rounded-full opacity-30 transition-all duration-[2s] group-hover:opacity-50 group-hover:rotate-12" style="background: radial-gradient(ellipse at center, #ff5e62 0%, transparent 70%); filter: blur(60px); transform-origin: center;"></div>
        <div class="absolute -bottom-[20%] -left-[10%] w-[80%] h-[80%] rounded-full opacity-20 transition-all duration-[3s] group-hover:opacity-40 group-hover:-rotate-12" style="background: radial-gradient(ellipse at center, #ff9966 0%, transparent 70%); filter: blur(80px); transform-origin: center;"></div>
        <div class="absolute inset-0" style="background: linear-gradient(135deg, rgba(255,255,255,0.05) 0%, transparent 50%, rgba(255,255,255,0.02) 100%); mix-blend-mode: overlay;"></div>
        <div class="absolute inset-0 opacity-10" style="background-image: url('data:image/svg+xml,%3Csvg viewBox=%220 0 200 200%22 xmlns=%22http://www.w3.org/2000/svg%22%3E%3Cfilter id=%22noiseFilter%22%3E%3CfeTurbulence type=%22fractalNoise%22 baseFrequency=%220.65%22 numOctaves=%223%22 stitchTiles=%22stitch%22/%3E%3C/filter%3E%3Crect width=%22100%25%22 height=%22100%25%22 filter=%22url(%23noiseFilter)%22/%3E%3C/svg%3E'); mix-blend-mode: overlay;"></div>
    </div>
</div>
"""
        # We need to replace the old div with the new html.
        # Let's find the exact end of the old div. Since it's nested, it's safer to use regex or string manipulation.
        old_div_start_index = html.find(target_div_start)
        
        # We know the old div structure:
        old_div_end_index = html.find('</div>', html.find('class="effect-layer-stars', old_div_start_index)) + 6
        # wait, there's another closing div for the relative h-[300px] parent!
        old_div_end_index = html.find('</div>', old_div_end_index) + 6
        
        html = html[:old_div_start_index] + new_backgrounds_html + html[old_div_end_index:]
        
        with open('design_system.html', 'w', encoding='utf-8') as f:
            f.write(html)
        print("Injected Backgrounds successfully.")
    else:
        print("Target div not found.")
else:
    print("Background Elements header not found.")
