import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Head
head_match = re.search(r'<head>.*?</head>', html, flags=re.DOTALL)
head = head_match.group(0) if head_match else ''

# 2. Hero
# The hero is the first section
hero_match = re.search(r'<section class="w-full opacity-0".*?</section>', html, flags=re.DOTALL)
hero = hero_match.group(0) if hero_match else ''

# Adapt hero text
hero = hero.replace('AI agents and workflows', 'Design System')
hero = hero.replace('you can see and control', 'and pattern library')
hero = hero.replace('Build visually, go deep with code, connect to anything. Every step of your agents\' reasoning, traceable on the canvas. Deploy on your infrastructure or ours.', 'A living documentation of the design tokens, components, typography, colors, and motion behaviors used across the application. Reusable and consistent.')
hero = hero.replace('Get started for free', 'View Typography')
hero = hero.replace('Talk to sales', 'View Colors')
hero = hero.replace('https://app.n8n.cloud/register?ps_partner_key=ZWFiZDIyYjkwZTFl&amp;ps_xid=PstqJ2A6DGeJJ8', '#typography')
hero = hero.replace('https://n8n-community.typeform.com/to/y9X2YuGa?ps_partner_key=ZWFiZDIyYjkwZTFl&amp;ps_xid=PstqJ2A6DGeJJ8&amp;ld_bookit_log_id=00DKB000000IOni2AG_1778173719348_907296738556051', '#colors')

# 3. NavBar
nav = """
<header class="fixed left-0 right-0 top-0 z-[1000] flex flex-col items-center px-layout-nav-padding transition-transform duration-300 md:px-layout-nav-padding-md xl:px-layout-nav-padding-xl" data-v-205b4218="">
  <div class="navbar-wrapper relative mt-2 flex w-full max-w-section-layout flex-col items-center justify-between rounded-2xl bg-shades-midnight-navy/70 md:mt-4 lg:mt-2 lg:bg-shades-midnight-navy/20" data-v-205b4218="">
    <nav class="flex min-h-[58px] w-full items-center justify-center gap-x-6 px-3 py-2 text-sm text-white font-geomanist opacity-90">
        <a href="#hero" class="hover:opacity-100 transition-opacity">Hero</a>
        <a href="#typography" class="hover:opacity-100 transition-opacity">Typography</a>
        <a href="#colors" class="hover:opacity-100 transition-opacity">Colors & Surfaces</a>
        <a href="#components" class="hover:opacity-100 transition-opacity">UI Components</a>
        <a href="#layout" class="hover:opacity-100 transition-opacity">Layout & Spacing</a>
        <a href="#motion" class="hover:opacity-100 transition-opacity">Motion & Interaction</a>
        <a href="#icons" class="hover:opacity-100 transition-opacity">Icons</a>
    </nav>
  </div>
</header>
"""

# Add spacer for nav padding
spacer = '<div style="padding-top: 100px;"></div>'

# 4. Content Sections

# TYPOGRAPHY
typography_section = """
<section id="typography" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">1. Typography</h2>
        <div class="flex flex-col gap-8">
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Heading 1</div>
                <div class="font-geomanist text-headline-xs md:text-headline-md lg:text-headline-md title title--white flex-1 text-center">Heading 1</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Fluid / Responsive</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Heading Gradient</div>
                <div class="font-geomanist text-headline-xs md:text-headline-md lg:text-headline-md title title--white-rainbow flex-1 text-center"><strong>Gradient Heading</strong></div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Fluid / Responsive</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Heading 2</div>
                <div class="font-geomanist text-headline-xs md:text-headline-sm lg:text-headline-sm title title--white flex-1 text-center">Heading 2</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Fluid</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Heading Gray</div>
                <div class="font-geomanist text-headline-xs md:text-headline-sm lg:text-headline-sm title title--gray flex-1 text-center">Heading Gray</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Fluid</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Heading Orange</div>
                <div class="font-geomanist text-headline-xs md:text-headline-sm lg:text-headline-sm title title--orange flex-1 text-center">Heading Orange</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Fluid</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Paragraph Text</div>
                <p class="font-geomanist text-md text-base-text-primary flex-1 text-center">This is a paragraph description text. Reusable and consistent.</p>
                <div class="text-white opacity-50 text-sm w-48 text-right">Text Md</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Nav Link Text</div>
                <div class="text-nav-link text-white opacity-70 flex-1 text-center">Nav Link Style</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Text Nav Link</div>
            </div>
            <div class="flex flex-row justify-between items-center border-b border-white/10 pb-4">
                <div class="text-white opacity-50 text-sm w-48">Small Text</div>
                <div class="text-white opacity-50 text-sm flex-1 text-center">Small Text Style</div>
                <div class="text-white opacity-50 text-sm w-48 text-right">Text Sm</div>
            </div>
        </div>
    </div>
</section>
"""

# COLORS & SURFACES
colors_section = """
<section id="colors" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg relative border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default relative z-10">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">2. Colors & Surfaces</h2>
        
        <h3 class="font-geomanist text-xl title title--gray mb-6">Backgrounds & Cards</h3>
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
            <div class="card--default rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--default</div>
            <div class="card--dark-navy rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--dark-navy</div>
            <div class="card--dark p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--dark</div>
            <div class="card--base rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--base</div>
            <div class="card--cta rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--cta</div>
            <div class="card--shine-blue rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--shine-blue</div>
            <div class="card--shine-dark rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--shine-dark</div>
            <div class="card--rusty rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--rusty</div>
            <div class="card--spark-red rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--spark-red</div>
            <div class="card--white-transparent rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--white-transparent</div>
            <div class="card--white-borderless rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--white-borderless</div>
            <div class="card--brown-gradient rounded-xl p-8 min-h-[200px] flex items-center justify-center text-white text-center">card--brown-gradient</div>
            
            <div class="gradient-tile gradient-tile-orange min-h-[200px] text-white">gradient-tile-orange</div>
            <div class="gradient-tile gradient-tile-default min-h-[200px] text-white">gradient-tile-default</div>
            <div class="gradient-tile gradient-tile-purple min-h-[200px] text-white">gradient-tile-purple</div>
        </div>

        <h3 class="font-geomanist text-xl title title--gray mb-6">Badges</h3>
        <div class="flex flex-wrap gap-4">
            <div class="badge badge--dark rounded-full px-4 py-2">badge--dark</div>
            <div class="badge badge--orange rounded-full px-4 py-2">badge--orange</div>
            <div class="bg-white/15 text-sm rounded-lg border border-white/20 px-3 py-1 flex items-center text-white">border-white/20 / bg-white/15</div>
        </div>
        
        <h3 class="font-geomanist text-xl title title--gray mt-16 mb-6">Global Background Elements</h3>
        <div class="relative h-[300px] w-full border border-white/20 rounded-xl overflow-hidden bg-shades-midnight-navy">
             <div class="circle-gradient-white" style="left:50%; top:50%; --tw-bg-opacity:0.07; width:200px; height:200px;"></div>
             <div class="effect-bg" style="left:20%; top:50%; width: 200px; height: 200px;"></div>
             <div class="section-bg-layer" style="inset:0;"></div>
             <div class="effect-layer-stars w-full h-full absolute inset-0"></div>
             <div class="absolute inset-0 flex items-center justify-center text-white z-10 pointer-events-none">
                 circle-gradient-white, effect-bg, section-bg-layer, effect-layer-stars
             </div>
        </div>
    </div>
</section>
"""

# UI COMPONENTS
components_section = """
<section id="components" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">3. UI Components</h2>
        
        <h3 class="font-geomanist text-xl title title--gray mb-6">Buttons</h3>
        <div class="flex flex-col gap-8 w-full max-w-2xl">
            <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Primary Button</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-primary px-5 justify-center min-h-10">Default</a>
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-primary px-5 justify-center min-h-10 opacity-50 hover:!opacity-50 hover:!rotate-0 pointer-events-none">Disabled</a>
                </div>
            </div>
            <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Primary (Icon Anim)</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-primary px-5 justify-center min-h-10 btn-anim-icon">
                        <span class="btn-label">Hover me</span>
                        <span class="btn-icon">→</span>
                    </a>
                </div>
            </div>
            <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Secondary Button</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-secondary px-5 justify-center min-h-10">Default</a>
                </div>
            </div>
            <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Tertiary Button</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-tertiary px-5 justify-center min-h-10">Default</a>
                </div>
            </div>
            <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Link Button</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-link px-5 justify-center min-h-10">Default</a>
                </div>
            </div>
             <div class="flex flex-row items-center justify-between border-b border-white/10 pb-4">
                <div class="text-white opacity-50 w-48">Chip Orange</div>
                <div class="flex gap-4">
                    <a class="btn relative flex items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-chip-orange px-5 justify-center min-h-10">Default</a>
                </div>
            </div>
        </div>

        <h3 class="font-geomanist text-xl title title--gray mt-16 mb-6">Forms & Inputs</h3>
        <form class="flex w-full flex-col gap-4 max-w-sm">
            <div class="flex flex-col gap-2">
                <label class="text-white text-sm opacity-70">Email Input</label>
                <input class="w-full rounded-lg border border-white/20 bg-white/5 px-4 py-3 text-sm text-white placeholder-white/50 focus:border-white/40 focus:outline-none focus:ring-1 focus:ring-white/40 transition-all" placeholder="Enter your email" type="email">
            </div>
        </form>
    </div>
</section>
"""

# LAYOUT & SPACING
layout_section = """
<section id="layout" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">4. Layout & Spacing</h2>
        
        <h3 class="font-geomanist text-xl title title--gray mb-6">Grid Pattern (Logos)</h3>
        <p class="text-white/60 mb-4 text-sm">Real layout from index.html: grid-cols-[repeat(auto-fill,minmax(212px,1fr))]</p>
        <div class="relative grid w-full grid-cols-[repeat(auto-fill,minmax(212px,1fr))] items-center gap-y-2 gap-x-2 md:gap-y-4 border border-white/10 rounded-xl p-4 bg-white/5">
             <div class="flex h-16 w-full items-center justify-center p-3 opacity-60 transition-all duration-300 hover:opacity-100 md:h-20 md:p-4 bg-white/10 rounded-lg text-white">Logo 1</div>
             <div class="flex h-16 w-full items-center justify-center p-3 opacity-60 transition-all duration-300 hover:opacity-100 md:h-20 md:p-4 bg-white/10 rounded-lg text-white">Logo 2</div>
             <div class="flex h-16 w-full items-center justify-center p-3 opacity-60 transition-all duration-300 hover:opacity-100 md:h-20 md:p-4 bg-white/10 rounded-lg text-white">Logo 3</div>
             <div class="flex h-16 w-full items-center justify-center p-3 opacity-60 transition-all duration-300 hover:opacity-100 md:h-20 md:p-4 bg-white/10 rounded-lg text-white">Logo 4</div>
        </div>

        <h3 class="font-geomanist text-xl title title--gray mt-16 mb-6">Split Section (Content / Visual)</h3>
        <div class="flex flex-col gap-10 lg:flex-row lg:items-center border border-white/10 p-8 rounded-xl bg-white/5">
            <div class="flex flex-col gap-6 lg:w-[45%]">
                <h2 class="font-geomanist text-headline-xs title title--white">Left Column Content</h2>
                <p class="font-geomanist text-md text-base-text-primary">This is the description. Reusable layout for split content.</p>
                <div><a class="btn relative flex w-fit items-center whitespace-nowrap rounded-lg text-white text-sm disabled:cursor-not-allowed btn-tertiary px-5 justify-center min-h-10">Read more</a></div>
            </div>
            <div class="lg:w-[55%] min-h-[200px] bg-white/10 rounded-xl flex items-center justify-center text-white/50">
                Visual Area
            </div>
        </div>
    </div>
</section>
"""

# MOTION & INTERACTION
motion_section = """
<section id="motion" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg overflow-hidden border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">5. Motion & Interaction</h2>
        
        <h3 class="font-geomanist text-xl title title--gray mb-6">Hover Shadow Effect & Button Lifts</h3>
        <div class="flex flex-wrap gap-8 items-center mb-16">
            <div class="effect-hover-shadow card--base w-64 h-32 rounded-xl flex items-center justify-center text-white transition-all cursor-pointer">
                effect-hover-shadow
            </div>
            <div class="card--default rounded-xl p-8 h-32 flex items-center justify-center text-white cursor-pointer hover:-translate-y-2 transition-transform duration-300">
                Hover lift (-translate-y-2)
            </div>
        </div>

        <h3 class="font-geomanist text-xl title title--gray mt-16 mb-6">Marquee (.c-marquee)</h3>
        <div class="c-marquee w-full overflow-hidden border-y border-white/10 py-4">
            <div class="c-marquee-inner flex w-max gap-4 pb-2 pt-2 md:gap-6" style="animation: marquee-94185631 10s linear infinite;">
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 1</div>
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 2</div>
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 3</div>
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 4</div>
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 5</div>
                <div class="bg-white/10 text-white px-8 py-4 rounded-xl">Marquee Item 6</div>
            </div>
        </div>
    </div>
</section>
"""

# ICONS
icons_section = """
<section id="icons" class="w-full py-20 bg-shades-midnight-navy px-section-gap-x md:px-section-gap-x-md lg:px-section-gap-x-lg border-t border-white/10">
    <div class="mx-auto w-full max-w-section-default">
        <h2 class="font-geomanist text-headline-sm title title--white mb-10">6. Icons</h2>
        
        <div class="flex flex-wrap gap-8 items-center bg-white/5 p-8 rounded-xl border border-white/10">
            <div class="flex flex-col items-center gap-2">
                <svg aria-hidden="true" class="iconify iconify--n8n text-white" height="1em" style="font-size: 32px;" viewbox="0 0 20 20" width="1em" xmlns="http://www.w3.org/2000/svg"><g fill="none"><path d="M2.742 5.833 10 10m0 0 7.258-4.167M10 10v8.333m7.5-5V6.666a1.667 1.667 0 0 0-.833-1.441L10.833 1.89a1.666 1.666 0 0 0-1.666 0L3.333 5.225A1.667 1.667 0 0 0 2.5 6.666v6.667a1.667 1.667 0 0 0 .833 1.442l5.834 3.333a1.666 1.666 0 0 0 1.666 0l5.834-3.333a1.667 1.667 0 0 0 .833-1.442z" stroke="#fff" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
                <span class="text-white/50 text-sm">Product</span>
            </div>
            <div class="flex flex-col items-center gap-2">
                 <svg aria-hidden="true" class="iconify iconify--n8n text-white" height="1em" style="font-size: 32px;" viewbox="0 0 20 20" width="1em" xmlns="http://www.w3.org/2000/svg"><g fill="none"><path d="M8.333 18.333v-12.5A.833.833 0 0 0 7.5 5H3.333a1.667 1.667 0 0 0-1.667 1.667v10a1.667 1.667 0 0 0 1.667 1.666h10A1.667 1.667 0 0 0 15 16.667V12.5a.834.834 0 0 0-.834-.833h-12.5M17.5 1.668h-5a.833.833 0 0 0-.834.833v5c0 .46.374.834.834.834h5c.46 0 .833-.373.833-.834v-5a.833.833 0 0 0-.833-.833z" stroke="#fff" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
                <span class="text-white/50 text-sm">Integrations</span>
            </div>
            <div class="flex flex-col items-center gap-2">
                <svg aria-hidden="true" class="iconify iconify--n8n text-white" height="1em" style="font-size: 32px;" viewbox="0 0 20 20" width="1em" xmlns="http://www.w3.org/2000/svg"><g fill="none"><path d="M8.28 12.918a1.667 1.667 0 0 0-1.197-1.197l-5.112-1.319a.416.416 0 0 1 0-.801l5.112-1.32a1.667 1.667 0 0 0 1.198-1.196l1.318-5.113a.417.417 0 0 1 .803 0l1.317 5.113a1.667 1.667 0 0 0 1.198 1.197L18.029 9.6a.417.417 0 0 1 0 .803l-5.112 1.318a1.667 1.667 0 0 0-1.198 1.197l-1.318 5.113a.416.416 0 0 1-.803 0l-1.317-5.113zM16.666 2.5v3.333M18.333 4.168H15M3.333 14.168v1.667M4.167 15H2.5" stroke="#fff" stroke-linecap="round" stroke-linejoin="round"></path></g></svg>
                <span class="text-white/50 text-sm">AI</span>
            </div>
            <div class="flex flex-col items-center gap-2">
                <svg aria-hidden="true" class="iconify iconify--ph" height="1em" style="font-size: 32px; color: white;" viewbox="0 0 256 256" width="1em" xmlns="http://www.w3.org/2000/svg"><path d="m221.66 133.66l-72 72a8 8 0 0 1-11.32-11.32L196.69 136H40a8 8 0 0 1 0-16h156.69l-58.35-58.34a8 8 0 0 1 11.32-11.32l72 72a8 8 0 0 1 0 11.32" fill="currentColor"></path></svg>
                <span class="text-white/50 text-sm">Arrow</span>
            </div>
        </div>
    </div>
</section>
"""

# Close body and html
footer = '</body></html>'

full_html = head + '<body class="antialiased bg-shades-midnight-navy">' + nav + spacer + hero + typography_section + colors_section + components_section + layout_section + motion_section + icons_section + footer

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print('Done!')
