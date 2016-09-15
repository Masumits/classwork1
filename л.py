import urllib.request
import re

def function():
    req = urllib.request.Request('https://yandex.ru/pogoda/moscow')
    with urllib.request.urlopen(req) as response:
        html = response.read()
        html = html.decode('utf-8')
    r = re.compile (
    a = r. finall(html)
    print(html[:200])

function()
