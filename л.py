import urllib.request
import re

def function():
    req = urllib.request.Request('http://udivitelno.com/animals/item/625-kapibara-samyj')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html = html.decode('utf-8')
    r = re.compile (
    a = r. finall(html)
    print(html[:200])

function()
#эээээээээээээээээ
    
