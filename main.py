from fake_useragent import UserAgent
import requests
import time
import random
import json

ua = UserAgent()
headers = {'User-Agent': "just_STUDYING_parser by lalka"}

html = requests.get('https://www.reddit.com/r/unixporn/.json', headers=headers)
time.sleep(random.uniform(1, 5))
html.encoding = 'utf-8'
html_content = html.json()

open("page.html", "w").close()
with open('page.html', 'w', encoding='utf-8') as f:
    f.write(json.dumps(html_content, indent=2, ensure_ascii=False))
print('успехъ')
