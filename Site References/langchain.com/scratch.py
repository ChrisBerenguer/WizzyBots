import re
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_end = html.find('</main>')
print("main end:", main_end)

footer_start = html.find('<footer')
if footer_start == -1:
    footer_start = html.find('<div class="footer')

print("footer start:", footer_start)
if footer_start != -1:
    footer_end = html.find('</footer>', footer_start)
    if footer_end == -1:
        # maybe it's a div
        pass
    print("footer start snippet:", html[footer_start:footer_start+200])

scripts_start = html.rfind('<script src="assets/f7f6a5894f1d19dd_jquery')
print("jquery script:", scripts_start)
if scripts_start != -1:
    print("after jquery snippet:", html[scripts_start:scripts_start+200])

