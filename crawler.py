
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import json
import random
import re
with open('news2.json','r') as f:
     dic = json.load(fp=f)
cnt=1
for epoch in range(9,30):
    driver = webdriver.Chrome()
    driver.get(
        f'https://news.sina.com.cn/roll/#pageid=153&lid=2515&etime=1669392000&stime=1669478400&ctime=1669478400&date=2022-11-{epoch+1}&k=&num=50&page=1')
    soup = BeautifulSoup(driver.page_source, features='lxml')
    urls = [url.find('a')['href']
            for url in soup.find_all('span', class_='c_tit')]
    for url in urls:
        if cnt > 5500:
            exit()
        driver.get(url=url)
        soup = BeautifulSoup(driver.page_source, features='lxml')
        if soup.find('h1', class_='main-title')==None:
            continue
        title = soup.find('h1', class_='main-title').get_text()
        content = soup.find('div', class_='article')
        text = content.get_text()
        if soup.find(class_='source ent-source')==None:
            src = ''
        else:
            src = soup.find(class_='source ent-source').get_text()
        pics = content.find_all('img')
        pics = ['https:'+pic['src'] for pic in pics]
        if soup.find('div', class_='keywords')==None:
            keys = []
        else:   
            keys = [key.get_text() for key in soup.find(
            'div', class_='keywords').find_all('a')]
        if soup.find('span', class_='num').get_text() == '':
            comments = 0
        else:
            comments = int(re.match('\d+', soup.find('span', class_='num').get_text()).group())
        art_time = soup.find('span',class_='date').get_text()
        art = {
            'title':title,
            'source':src,
            'text':text,
            'pictures':pics,
            'keys':keys,
            'comments':comments,
            'time':art_time,
        }
        dic[cnt]=art
        with open('news2.json','w') as f:
            json.dump(dic,f)
        time.sleep(random.uniform(1,2))
        print(f'-----passage {cnt} finished-----')
        cnt+=1
    print(epoch)
        