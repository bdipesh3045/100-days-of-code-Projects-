import time
import threading
import requests
from bs4 import BeautifulSoup
from requests import request
import requests
from curses.ascii import BS
from pyBSDate import convert_AD_to_BS
from datetime import date

def run():
    # print('''Note to write correct date!''')
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%Y-%m-%e")
    date=date.replace(" ", "")
    date_list=date.split('-')
    bs_date = convert_AD_to_BS(int(date_list[0]), int(date_list[1]),int(date_list[2]))
    Bs_li=[]
    for x in bs_date:
        Bs_li.append(x)
    year_nepali=int(Bs_li[0])
    month_nepali=int(Bs_li[1])
    url=f"https://www.hamropatro.com/calendar/{year_nepali}/{month_nepali}"
    print(url)
    li=[]
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    soup= soup.find('li',{"id":date})
    h1=soup.find('span' , {"class":'event'})
    h1=h1.get_text(strip = True)
    li.append(h1)
    for i in range(1,4):
        a=f"col{i}"
        if(i==1):
            div= soup.find('div' , {"class":a})
            sp1=div.find('span')
            li.append(sp1.get_text(strip = True))
        elif(a=="col2"):
            div= soup.find('div' , {"class":a})
            li.append(div.get_text(strip = True))
        else:
            div= soup.find('div' , {"class":"panchangaWrapper"})
            li.append(div.get_text(strip = True))
    # print(li)
    

def moon():
    url=f"https://www.timeanddate.com/astronomy/nepal/kathmandu"
    li=[]
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    soup= soup.find('div' , {"id":"cs-dl"})
    span=soup.find_all('span' )
    p=soup.find_all('p')
    for y in p:
        li.append(y.get_text(strip = True))
    # print(li)

def weather():
    a=[]
    url=f"https://www.iqair.com/nepal/central-region/kathmandu"
    data=requests.get(url)
    soup=BeautifulSoup(data.text,'html.parser')
    air= soup.find('div' , {"class":"aqi-overview-detail"})
    air= air.find('p' , {"class":"who-guideline__text"})
    a.append(air.get_text(strip = True))
    temp= soup.find_all('div' , {"class":"weather"})
    # print(temp.get_text(strip = True))
    for tem in temp:
        dat=(tem.find_all('tr'))
        for i in dat:
            a.append(i.get_text(strip = True))
    # print(a)
start =time.perf_counter()
def b():
  run()
  moon()
  weather()
b()
finish=time.perf_counter()
print(f"The program finished in {round(finish-start,2)} Seconds")
p =time.perf_counter()
def a():
  t1=threading.Thread(target=run)
  t2=threading.Thread(target=moon)
  t3=threading.Thread(target=weather)
  t1.start()
  t2.start()
  t3.start()
  t1.join()
  t2.join()
  t3.join()
a()
q=time.perf_counter()
print(f"The program finished in {round(q-p,2)} Seconds")
