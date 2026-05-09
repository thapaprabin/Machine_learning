import requests 
from bs4 import BeautifulSoup
import sys
import locale

# Force UTF-8 for stdout/stderr
sys.stdout = open(sys.stdout.fileno(), mode='w', encoding='utf-8', buffering=1)
sys.stderr = open(sys.stderr.fileno(), mode='w', encoding='utf-8', buffering=1)

# Set locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


def get_headlines():
    url="https://merolagani.com/"
    headers={'User-Agent':'Mozilla/5.0'}
    response=requests.get(url,headers=headers)
    soup=BeautifulSoup(response.text,'html.parser')

    headlines=soup.find_all('h4',class_='headlineTitle')
    #we save the news to a list 
    all_recent_news=[]
    for headline in headlines:
        try:

            title=headline.find('a').text.strip()
            date=headline.find('span',class_='media-label-recent-news').text.strip()
            all_recent_news.append({'title':title,'date':date})

        except:
            continue
    return all_recent_news
        
news=get_headlines()

print('\n RECENT NEWS FROM MEROLAAGANI')
for i,headline in enumerate(news,1):
    print(f"{i}.{headline['title']}")
    print(f"{headline['date']}\n")

#PROBLEMS FACED DURING:
    #terminal didn't supported Unicode(UTF-8) characters properly  
#SOLVED:
    #stored in a file 
'''import json
with open('news.json','w',encoding='utf-8') as f:
    json.dump(news,f,ensure_ascii=False,indent=2)
print(f"SAVED {len(news)} news to news.json")'''