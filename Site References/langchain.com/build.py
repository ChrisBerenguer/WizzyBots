import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Head
head_match = html.find('</head>')
if head_match != -1:
    head = html[:head_match + len('</head>')]
else:
    head = ''

# 2. Nav + Banner
# The top-banner and navbar2_component are at the top of the body
# Let's just find the start of the hero, and grab everything inside page-wrapper up to hero
hero_start = html.find('<section class="home_hero-section">')
hero_end = html.find('</section>', hero_start) + len('</section>')

body_start = html.find('<body')
body_start_close = html.find('>', body_start) + 1

nav = html[body_start_close:hero_start]

# Modify Nav to include anchor links (we can just replace the product dropdown or add a new menu)
# The nav has a bunch of links. We'll find the <nav class="navbar2_menu..."> and replace its inner HTML.
nav = re.sub(r'<nav class="navbar2_menu[^>]*>.*?</nav>', 
'''<nav class="navbar2_menu is-page-height-tablet w-nav-menu" role="navigation">
<div class="navbar-menu-wrapper" style="display:flex; align-items:center; gap:24px;">
    <a href="#hero" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Hero</a>
    <a href="#typography" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Typography</a>
    <a href="#colors" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Colors</a>
    <a href="#components" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Components</a>
    <a href="#layout" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Layout</a>
    <a href="#motion" class="navbar2_link t-label-1-rg w-nav-link" style="color:white;">Motion</a>
</div>
</nav>''', nav, flags=re.DOTALL)

# 3. Hero
hero = html[hero_start:hero_end]
# Adapt hero text
hero = hero.replace('Ship agents that <span class="word-swap"><span class="word-old">work</span><span class="word-new">wow</span></span>', 'Design System <span class="word-swap"><span class="word-old">UI</span><span class="word-new">Library</span></span>')
hero = hero.replace('LangSmith is the unified DevOps platform for developing, collaborating, testing, deploying, and monitoring LLM applications.', 'A living documentation of the design tokens, components, typography, colors, and motion behaviors used across the application.')

# 4. Content Sections

# TYPOGRAPHY
typography_section = """
<section id="typography" class="v2-padding-global" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 80px; padding-bottom: 80px;">
    <div class="w-layout-blockcontainer v2-container w-container">
        <h2 class="t-heading-3-rg text-c-white" style="margin-bottom: 40px;">1. Typography</h2>
        <div style="display: flex; flex-direction: column; gap: 32px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 1</div>
                <div style="flex: 1; text-align: center;"><h1 class="t-heading-1-rg color-t-7fc8ff">Heading 1</h1></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-1-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 2</div>
                <div style="flex: 1; text-align: center;"><h2 class="t-heading-2-rg text-c-blue-light-900">Heading 2</h2></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-2-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 3</div>
                <div style="flex: 1; text-align: center;"><h3 class="t-heading-3-rg text-c-white">Heading 3</h3></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-3-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 4</div>
                <div style="flex: 1; text-align: center;"><h4 class="t-heading-4-rg text-c-blue-light-900">Heading 4</h4></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-4-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 5</div>
                <div style="flex: 1; text-align: center;"><h5 class="t-heading-5-rg text-c-white">Heading 5</h5></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-5-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Heading 6</div>
                <div style="flex: 1; text-align: center;"><h6 class="t-heading-6-rg text-c-white">Heading 6</h6></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-heading-6-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Paragraph 1</div>
                <div style="flex: 1; text-align: center;"><p class="t-paragraph-1-rg text-c-white">Large paragraph text.</p></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-paragraph-1-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Paragraph 2</div>
                <div style="flex: 1; text-align: center;"><p class="t-paragraph-2-rg text-c-white">Medium paragraph text.</p></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-paragraph-2-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Paragraph 3</div>
                <div style="flex: 1; text-align: center;"><p class="t-paragraph-3-rg text-c-white">Small paragraph text.</p></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-paragraph-3-rg</div>
            </div>
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Label 1</div>
                <div style="flex: 1; text-align: center;"><p class="t-label-1-rg text-c-white">Label text.</p></div>
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px; text-align: right;">.t-label-1-rg</div>
            </div>
        </div>
    </div>
</section>
"""

# COLORS & SURFACES
colors_section = """
<section id="colors" class="v2-padding-global" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 80px; padding-bottom: 80px;">
    <div class="w-layout-blockcontainer v2-container w-container">
        <h2 class="t-heading-3-rg text-c-white" style="margin-bottom: 40px;">2. Colors & Surfaces</h2>
        
        <h3 class="t-heading-5-rg text-c-white" style="margin-bottom: 24px;">Cards & Backgrounds</h3>
        <div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 24px; margin-bottom: 64px;">
            <div class="home_card-content" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                <span class="t-label-1-rg text-c-white">.home_card-content</span>
            </div>
            <div class="code_left-wrapper" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                <span class="t-label-1-rg text-c-white">.code_left-wrapper</span>
            </div>
            <div class="card-bg-gradient" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center; border: 1px solid rgba(255,255,255,0.1); border-radius: 12px; background: linear-gradient(180deg, #1A1A1A 0%, #000 100%);">
                <span class="t-label-1-rg text-c-white">linear-gradient</span>
            </div>
            <div class="home_text-animation-wrapper" style="min-height: 200px; display: flex; align-items: center; justify-content: center; text-align: center;">
                <span class="t-label-1-rg text-c-white">.home_text-animation-wrapper</span>
            </div>
        </div>
    </div>
</section>
"""

# UI COMPONENTS
components_section = """
<section id="components" class="v2-padding-global" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 80px; padding-bottom: 80px;">
    <div class="w-layout-blockcontainer v2-container w-container">
        <h2 class="t-heading-3-rg text-c-white" style="margin-bottom: 40px;">3. UI Components</h2>
        
        <h3 class="t-heading-5-rg text-c-white" style="margin-bottom: 24px;">Buttons</h3>
        <div style="display: flex; flex-direction: column; gap: 32px; max-width: 800px;">
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Primary Button V2</div>
                <div style="display: flex; gap: 16px;">
                    <a href="#" class="button-v2 w-variant-cc2081e2-2f66-fa48-5d36-c70458cedec9 w-inline-block"><div>Primary Button</div></a>
                </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Secondary Arrow Button</div>
                <div style="display: flex; gap: 16px;">
                    <a href="#" class="button-v2 w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0 w-inline-block"><div class="no-wrap-arrow w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0">Secondary Button</div></a>
                </div>
            </div>
            
            <div style="display: flex; justify-content: space-between; align-items: center; border-bottom: 1px solid rgba(255,255,255,0.1); padding-bottom: 16px;">
                <div class="t-label-1-rg" style="opacity: 0.5; width: 200px;">Arrow No Hover Button</div>
                <div style="display: flex; gap: 16px;">
                    <a href="#" class="button-arrow-no-hover w-inline-block"><div>No Hover Button</div></a>
                </div>
            </div>
        </div>

        <h3 class="t-heading-5-rg text-c-white" style="margin-top: 64px; margin-bottom: 24px;">Cards</h3>
        <div class="home_card-grid more-gap" style="max-width: 800px;">
            <div class="home_card-content">
                <div class="home_card-logo">
                    <div class="t-label-1-rg blue-light-900">Card Label</div>
                </div>
                <div class="spacer-16"></div>
                <h4 class="t-heading-5-rg text-c-white">Card Title</h4>
                <div class="spacer-16"></div>
                <p class="t-paragraph-3-rg text-c-white-60-p">This is the description content of the card.</p>
                <div class="spacer-40 _32-landscape"></div>
                <a class="button-v2 w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0 w-inline-block" href="#">
                    <div class="no-wrap-arrow w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0">Card Button</div>
                </a>
            </div>
        </div>
    </div>
</section>
"""

# LAYOUT & SPACING
layout_section = """
<section id="layout" class="v2-padding-global" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 80px; padding-bottom: 80px;">
    <div class="w-layout-blockcontainer v2-container w-container">
        <h2 class="t-heading-3-rg text-c-white" style="margin-bottom: 40px;">4. Layout & Spacing</h2>
        
        <h3 class="t-heading-5-rg text-c-white" style="margin-bottom: 24px;">Global Container (.v2-container)</h3>
        <div class="v2-container" style="border: 1px dashed rgba(255,255,255,0.2); padding: 20px;">
            <div class="t-label-1-rg text-c-white">Max-width constrained container with responsive padding.</div>
        </div>

        <h3 class="t-heading-5-rg text-c-white" style="margin-top: 64px; margin-bottom: 24px;">Card Grid Layout (.home_card-grid)</h3>
        <div class="home_card-grid more-gap" style="border: 1px dashed rgba(255,255,255,0.2); padding: 20px;">
            <div style="height: 100px; background: rgba(255,255,255,0.1); border-radius: 8px;"></div>
            <div style="height: 100px; background: rgba(255,255,255,0.1); border-radius: 8px;"></div>
            <div style="height: 100px; background: rgba(255,255,255,0.1); border-radius: 8px;"></div>
        </div>
    </div>
</section>
"""

# MOTION & INTERACTION
motion_section = """
<section id="motion" class="v2-padding-global" style="background-color: #000; border-top: 1px solid rgba(255,255,255,0.1); padding-top: 80px; padding-bottom: 80px;">
    <div class="w-layout-blockcontainer v2-container w-container">
        <h2 class="t-heading-3-rg text-c-white" style="margin-bottom: 40px;">5. Motion & Interaction</h2>
        
        <h3 class="t-heading-5-rg text-c-white" style="margin-bottom: 24px;">Word Swap Animation</h3>
        <h1 class="t-heading-1-rg color-t-7fc8ff">Design <span class="word-swap"><span class="word-old">System</span><span class="word-new">Library</span></span></h1>

        <h3 class="t-heading-5-rg text-c-white" style="margin-top: 64px; margin-bottom: 24px;">Button Hover States</h3>
        <div style="display: flex; gap: 24px;">
            <a href="#" class="button-v2 w-variant-cc2081e2-2f66-fa48-5d36-c70458cedec9 w-inline-block"><div>Hover Me</div></a>
            <a href="#" class="button-v2 w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0 w-inline-block"><div class="no-wrap-arrow w-variant-f44e612c-d93f-d147-e6a4-fd7888246ef0">Hover Me Arrow</div></a>
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

# Langchain has <body class="body-v2"> so I should start with that.
full_html = head + '<body class="body-v2"><div class="page-wrapper">' + nav + '<main>' + hero + typography_section + colors_section + components_section + layout_section + motion_section + '</main></div>' + footer

with open('design-system.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
print('Done!')
