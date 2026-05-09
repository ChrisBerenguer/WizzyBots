import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Head
head_match = html.find('</head>')
if head_match != -1:
    head = html[:head_match + len('</head>')]
else:
    head = ''

# 2. Hero
# The hero is the section_hero
hero_match = re.search(r'<section class="section_hero">.*?</section>', html, flags=re.DOTALL)
hero = hero_match.group(0) if hero_match else ''

# Adapt hero text
hero = hero.replace('Accelerate AI agent adoption and start delivering production value', 'Design System & Pattern Library')
hero = hero.replace('CrewAI makes it easy for enterprises to operate teams of AI agents that perform complex tasks autonomously, reliably and with full control.', 'A living documentation of the design tokens, components, typography, colors, and motion behaviors used across the application. Reusable and consistent.')

# 3. NavBar
# Replace navbar links to point to design system sections
nav_match = re.search(r'<div class="navbar-no-shadow.*?<main class="main-wrapper smooth-content">', html, flags=re.DOTALL)
if nav_match:
    nav = nav_match.group(0)
    nav = nav.replace('<main class="main-wrapper smooth-content">', '')
else:
    nav = ''

# Modify Nav to include anchor links
nav = re.sub(r'<ul class="nav-menu w-list-unstyled" role="list">.*?</ul>', 
'''<ul class="nav-menu w-list-unstyled" role="list">
<li><a class="nav-link transition" href="#hero" style="color: rgb(255, 255, 255);">Hero</a></li>
<li><a class="nav-link transition" href="#typography" style="color: rgb(255, 255, 255);">Typography</a></li>
<li><a class="nav-link transition" href="#colors" style="color: rgb(255, 255, 255);">Colors</a></li>
<li><a class="nav-link transition" href="#components" style="color: rgb(255, 255, 255);">Components</a></li>
<li><a class="nav-link transition" href="#layout" style="color: rgb(255, 255, 255);">Layout</a></li>
<li><a class="nav-link transition" href="#motion" style="color: rgb(255, 255, 255);">Motion</a></li>
</ul>''', nav, flags=re.DOTALL)

# Add spacer for nav padding if needed
spacer = '<div style="padding-top: 100px;"></div>'

# 4. Content Sections

# TYPOGRAPHY
typography_section = """
<section id="typography" class="section" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="padding-global padding-section-medium">
        <div class="w-layout-blockcontainer container-large w-container">
            <h2 class="text-color-white" style="margin-bottom: 40px;">1. Typography</h2>
            <div style="display: flex; flex-direction: column; gap: 32px;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Heading 1</div>
                    <div style="flex: 1; text-align: center;"><h1>Heading 1</h1></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">Fluid</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Heading 2</div>
                    <div style="flex: 1; text-align: center;"><h2 class="text-color-white">Heading 2</h2></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">Fluid</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Heading 3</div>
                    <div style="flex: 1; text-align: center;"><h3 class="text-color-white">Heading 3</h3></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">Fluid</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Gradient Text</div>
                    <div style="flex: 1; text-align: center;"><h2 class="text-color-white"><span class="gradient-text">Gradient Text</span></h2></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">.gradient-text</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Text Large</div>
                    <div style="flex: 1; text-align: center;"><p class="text-size-large text-color-white">Large paragraph text.</p></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">.text-size-large</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Text Medium</div>
                    <div style="flex: 1; text-align: center;"><p class="text-size-medium text-color-invert">Medium description text.</p></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">.text-size-medium</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Text Small</div>
                    <div style="flex: 1; text-align: center;"><p class="text-size-small text-color-white">Small detail text.</p></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">.text-size-small</div>
                </div>
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Text Tiny / All Caps</div>
                    <div style="flex: 1; text-align: center;"><p class="text-size-tiny text-style-allcaps text-color-white">Tiny all caps text</p></div>
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px; text-align: right;">.text-size-tiny .text-style-allcaps</div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# COLORS & SURFACES
colors_section = """
<section id="colors" class="section" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="padding-global padding-section-medium">
        <div class="w-layout-blockcontainer container-large w-container">
            <h2 class="text-color-white" style="margin-bottom: 40px;">2. Colors & Surfaces</h2>
            
            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Cards & Backgrounds</h3>
            <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; margin-bottom: 64px;">
                <div class="card" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                    <span class="text-color-white">.card</span>
                </div>
                <div class="succeed-card" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                    <span class="text-color-white">.succeed-card</span>
                </div>
                <div class="management_platform-card" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                    <span class="text-color-white">.management_platform-card</span>
                </div>
                <div class="how-it-works-right-card" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center; position: relative;">
                    <span class="text-color-white">.how-it-works-right-card</span>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# UI COMPONENTS
components_section = """
<section id="components" class="section" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="padding-global padding-section-medium">
        <div class="w-layout-blockcontainer container-large w-container">
            <h2 class="text-color-white" style="margin-bottom: 40px;">3. UI Components</h2>
            
            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Buttons</h3>
            <div style="display: flex; flex-direction: column; gap: 32px; max-width: 800px;">
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Primary Button</div>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" class="button w-inline-block"><div class="button-content-wrap"><div class="relative">Primary Button</div></div><div class="button-broder-holder" style="opacity: 0;"><div class="bg-color"></div></div></a>
                    </div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Secondary Button</div>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" class="button w-inline-block"><div class="button-content-wrap is-secondary"><div class="relative text-color-white">Secondary Button</div></div><div class="button-broder-holder border-solid-color" style="opacity: 0;"><div class="bg-color white"></div></div></a>
                    </div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">White Button</div>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" class="button is-white w-inline-block"><div class="button-content-wrap text-color-black top-bottom-padding"><div class="relative">White Button</div></div><div class="button-broder-holder width new-button" style="opacity: 0;"><div class="bg-color white"></div></div></a>
                    </div>
                </div>

                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">New Button (Blue)</div>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" class="button w-inline-block"><div class="button-content-wrap new-button blue-color"><div class="relative">Request a demo</div><div class="button-arrow-wrapper"><img src="assets/a587df414488b541_69a111972d2e0bbcc6adb98f_SVG_2.svg" class="button-icon-2" alt=""><img src="assets/a587df414488b541_69a111972d2e0bbcc6adb98f_SVG_2.svg" class="button-icon-1" alt=""></div></div><div class="button-broder-holder" style="opacity: 0;"><div class="bg-color blue-bg blue-color"></div></div></a>
                    </div>
                </div>
                
                <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                    <div class="text-size-small text-color-white" style="opacity: 0.5; width: 200px;">Card Button</div>
                    <div style="display: flex; gap: 16px;">
                        <a href="#" class="card-button w-inline-block"><div class="text-size-small">Sign in</div><div class="card-button-gradient-border" style="opacity: 0;"></div></a>
                    </div>
                </div>
            </div>

            <h3 class="text-color-white text-size-medium" style="margin-top: 64px; margin-bottom: 24px;">Forms & Inputs</h3>
            <div style="max-width: 400px;">
                <input type="email" class="pop-up-form-field text-weight-normal busienss-email-field w-input" placeholder="Business email*" style="margin-bottom: 16px; background-color: #1a1a1a; color: white;">
                <input type="text" class="pop-up-form-field text-weight-normal w-input" placeholder="Company name*" style="margin-bottom: 16px; background-color: #1a1a1a; color: white;">
                <textarea class="pop-up-form-field text-weight-normal height w-input" placeholder="Anything else you would like to discuss?" style="background-color: #1a1a1a; color: white;"></textarea>
            </div>
        </div>
    </div>
</section>
"""

# LAYOUT & SPACING
layout_section = """
<section id="layout" class="section" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="padding-global padding-section-medium">
        <div class="w-layout-blockcontainer container-large w-container">
            <h2 class="text-color-white" style="margin-bottom: 40px;">4. Layout & Spacing</h2>
            
            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Grid 5 Columns</h3>
            <div class="management_platform-card-bottom grid-5" style="margin-bottom: 64px;">
                <div class="management_platform-card"><div class="text-size-mobile--875">Item 1</div></div>
                <div class="management_platform-card"><div class="text-size-mobile--875">Item 2</div></div>
                <div class="management_platform-card"><div class="text-size-mobile--875">Item 3</div></div>
                <div class="management_platform-card"><div class="text-size-mobile--875">Item 4</div></div>
                <div class="management_platform-card"><div class="text-size-mobile--875">Item 5</div></div>
            </div>

            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Split Section Layout (.how-it-works-main-wrapper)</h3>
            <div class="how-it-works-main-wrapper" style="border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; padding: 20px;">
                <div class="how-it-works-left" style="border: 1px dashed rgba(255,255,255,0.2);">
                    <div class="text-color-white" style="padding: 20px;">Left Sticky Column</div>
                </div>
                <div class="how-it-works-right" style="border: 1px dashed rgba(255,255,255,0.2); min-height: 300px;">
                    <div class="text-color-white" style="padding: 20px;">Right Scrolling Column</div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# MOTION & INTERACTION
motion_section = """
<section id="motion" class="section" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1);">
    <div class="padding-global padding-section-medium">
        <div class="w-layout-blockcontainer container-large w-container">
            <h2 class="text-color-white" style="margin-bottom: 40px;">5. Motion & Interaction</h2>
            
            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Button Hover Effects</h3>
            <div style="display: flex; gap: 24px; margin-bottom: 64px;">
                <a href="#" class="button w-inline-block"><div class="button-content-wrap new-button"><div class="relative">Hover Me</div><div class="button-arrow-wrapper"><img src="assets/a587df414488b541_69a111972d2e0bbcc6adb98f_SVG_2.svg" class="button-icon-2" alt=""><img src="assets/a587df414488b541_69a111972d2e0bbcc6adb98f_SVG_2.svg" class="button-icon-1" alt=""></div></div><div class="button-broder-holder" style="opacity: 0;"><div class="bg-color"></div></div></a>
            </div>

            <h3 class="text-color-white text-size-medium" style="margin-bottom: 24px;">Marquee</h3>
            <div class="hero-marquee-wrapper">
                <div class="marquee" style="border-top: 1px solid rgba(255,255,255,0.1); border-bottom: 1px solid rgba(255,255,255,0.1); padding: 20px 0;">
                    <div class="marquee-images-wrapper">
                        <div class="marquee-images-holder">
                            <h3 class="text-color-white" style="padding: 0 40px;">CrewAI</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">Design</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">System</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">Showcase</h3>
                        </div>
                        <div class="marquee-images-holder">
                            <h3 class="text-color-white" style="padding: 0 40px;">CrewAI</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">Design</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">System</h3>
                            <h3 class="text-color-white" style="padding: 0 40px;">Showcase</h3>
                        </div>
                    </div>
                    <div class="marquee-left-overlay"></div>
                    <div class="marquee-right-overlay"></div>
                </div>
            </div>
        </div>
    </div>
</section>
"""

# Close body and html
main_end = html.find('</main>')
if main_end != -1:
    footer = html[main_end + len('</main>'):]
else:
    footer = '</body></html>'

full_html = head + '<body class="vsc-initialized">' + nav + spacer + '<main class="main-wrapper smooth-content">' + hero + typography_section + colors_section + components_section + layout_section + motion_section + '</main>' + footer

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print('Done!')
