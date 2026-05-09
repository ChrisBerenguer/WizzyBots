import re

with open('design_system.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. INJECT CARDS
cards_marker = '<h3 class="font-geomanist text-xl title title--gray mb-6">Backgrounds & Cards</h3>'
cards_div_start = '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">'

cards_html = """
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 mb-16">
    <!-- LangChain Style Card -->
    <div class="home_card-content is-left" style="background: rgba(255, 255, 255, 0.03); border: 1px solid rgba(255, 255, 255, 0.1); border-radius: 16px; padding: 24px; transition: transform 0.3s ease, box-shadow 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'; this.style.boxShadow='0 10px 30px -10px rgba(127,200,255,0.2)';" onmouseout="this.style.transform='translateY(0)'; this.style.boxShadow='none';">
        <div class="code_left-wrapper is-deploy max-width-100" style="margin-bottom: 20px; border-radius: 8px; overflow: hidden; height: 180px; background: #111;">
            <img src="langchain.com/assets/ea47e69058e3d900_69c17b7fa8fdfabb326f8150_agent.avif" loading="lazy" alt="" class="object-cover width-100 height-100 opacity-60" style="width: 100%; height: 100%; object-fit: cover;">
        </div>
        <div class="margin-bottom margin-xsmall">
            <h4 class="t-heading-4-rg text-c-white" style="margin-bottom: 8px; color: #fff;">LangChain Glass Card</h4>
        </div>
        <p class="t-paragraph-2-rg text-c-blue-light-900" style="color: #94a3b8;">High-fidelity card component mimicking the LangChain ecosystem with subtle hover elevation.</p>
    </div>

    <!-- Canvas Visual Style Card -->
    <div class="group relative isolate flex flex-col justify-end overflow-hidden rounded-2xl px-8 pb-8 pt-40 transition-all duration-300 hover:shadow-[0_0_40px_-10px_rgba(249,115,22,0.3)]" style="background-color: #171717; min-height: 350px; border: 1px solid #333;">
        <div class="absolute inset-0 -z-10" style="background: linear-gradient(to top, #171717, rgba(23,23,23,0.4));"></div>
        <div class="absolute inset-0 -z-10" style="background: linear-gradient(to top, #000, rgba(0,0,0,0.4));"></div>
        <h3 class="z-10 mt-3 text-2xl font-bold text-white" style="color: white; margin-bottom: 8px;">Aura Glow Card</h3>
        <div class="z-10 gap-y-1 overflow-hidden text-sm leading-6 text-neutral-300" style="color: #a3a3a3;">Stunning dark themed card with orange hover glow inspired by Canvas Visual.</div>
    </div>

    <!-- CrewAI / Minimalist Modern Card -->
    <div style="background: linear-gradient(145deg, #1e1e24 0%, #0b0b0d 100%); border: 1px solid rgba(255,255,255,0.05); border-radius: 20px; padding: 30px; position: relative; overflow: hidden;" onmouseover="this.querySelector('.glow-orb').style.opacity='1'; this.querySelector('.glow-orb').style.transform='scale(1.2)';" onmouseout="this.querySelector('.glow-orb').style.opacity='0'; this.querySelector('.glow-orb').style.transform='scale(1)';">
        <div class="glow-orb" style="position: absolute; top: -50px; right: -50px; width: 150px; height: 150px; background: radial-gradient(circle, rgba(255,60,100,0.4) 0%, transparent 70%); border-radius: 50%; opacity: 0; transition: all 0.5s ease;"></div>
        <div style="width: 48px; height: 48px; background: rgba(255,255,255,0.1); border-radius: 12px; display: flex; align-items: center; justify-content: center; margin-bottom: 24px;">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2L2 7l10 5 10-5-10-5z"/><path d="M2 17l10 5 10-5"/><path d="M2 12l10 5 10-5"/></svg>
        </div>
        <h4 style="color: white; font-size: 1.25rem; font-weight: 600; margin-bottom: 12px;">Minimalist Modern</h4>
        <p style="color: #888; font-size: 0.95rem; line-height: 1.5;">Elegant gradients and smooth micro-interactions that feel premium and responsive to user input.</p>
    </div>
"""

# Replace the empty grid with the populated one
if cards_div_start in html:
    html = html.replace(cards_div_start, cards_html)

# 2. INJECT BADGES
badges_marker = '<h3 class="font-geomanist text-xl title title--gray mb-6">Badges</h3>'
badges_div_start = '<div class="flex flex-wrap gap-4">'

badges_html = """
<div class="flex flex-wrap gap-4" style="margin-bottom: 40px; display: flex; gap: 16px;">
    <!-- N8N Classic Base Badge -->
    <span style="display: inline-flex; items-align: center; gap: 6px; border-radius: 9999px; background-color: rgba(255, 60, 100, 0.1); padding: 4px 12px; font-size: 0.875rem; font-weight: 500; color: #ff3c64; border: 1px solid rgba(255, 60, 100, 0.2);">
        <svg style="height: 8px; width: 8px; fill: #ff3c64; margin-top: 6px;" viewBox="0 0 6 6" aria-hidden="true"><circle cx="3" cy="3" r="3"></circle></svg>
        Active Workflow
    </span>

    <!-- Aura Glow Badge -->
    <span style="display: inline-flex; items-align: center; gap: 6px; border-radius: 9999px; background-color: rgba(249, 115, 22, 0.1); padding: 4px 12px; font-size: 0.875rem; font-weight: 500; color: #f97316; border: 1px solid rgba(249, 115, 22, 0.2); box-shadow: 0 0 10px rgba(249,115,22,0.2);">
        <svg style="height: 8px; width: 8px; fill: #f97316; margin-top: 6px;" viewBox="0 0 6 6" aria-hidden="true"><circle cx="3" cy="3" r="3"></circle></svg>
        Aura Pulse
    </span>

    <!-- LangChain Technical Badge -->
    <span style="display: inline-flex; items-align: center; border-radius: 6px; background-color: rgba(127, 200, 255, 0.1); padding: 4px 12px; font-size: 0.875rem; font-weight: 600; color: #7fc8ff; border: 1px solid rgba(127, 200, 255, 0.3); font-family: monospace;">
        v2.4.0-rc
    </span>

    <!-- CrewAI Solid Minimal Badge -->
    <span style="display: inline-flex; items-align: center; border-radius: 4px; background-color: #ffffff; padding: 4px 12px; font-size: 0.875rem; font-weight: 600; color: #000000; box-shadow: 0 2px 5px rgba(0,0,0,0.2);">
        Premium Feature
    </span>
    
    <!-- Outline Glow Badge -->
    <span style="display: inline-flex; items-align: center; border-radius: 9999px; background-color: transparent; padding: 4px 12px; font-size: 0.875rem; font-weight: 500; color: #fff; border: 1px solid rgba(255, 255, 255, 0.4); text-shadow: 0 0 5px rgba(255,255,255,0.5);" onmouseover="this.style.borderColor='#fff'; this.style.boxShadow='0 0 15px rgba(255,255,255,0.3)';" onmouseout="this.style.borderColor='rgba(255, 255, 255, 0.4)'; this.style.boxShadow='none';">
        Hover Me
    </span>
"""

if badges_div_start in html:
    html = html.replace(badges_div_start, badges_html)

with open('design_system.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Injected Cards and Badges successfully.")
