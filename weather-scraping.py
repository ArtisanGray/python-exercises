from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time
#driver = webdriver.Chrome('C:\WinPython-64bit-3.6.3.0Qt5\chromedriver.exe')
# Specify the URL
#driver.get("https://weather.com/weather/5day/l/USOK0412:1:US")
#FOR GRABBING RESOURCES AND HTML TAG NAMES
url = 'https://weather.com/weather/5day/l/USOK0412:1:US'
r = requests.get(url)
r_html = r.text

#use the requests code from before

soup = BeautifulSoup(r_html,"lxml")
#link = soup.find_all('span', class_="date-time")
links = [Item.get_text().strip() for Item in soup.find_all('span', class_='date-time')]
link2 = soup.find_all('td', class_='description')
str_list = list()
for i in links: #takes items in links and converts them to strings, which are stored into a list.
    wee = str(i)#ignore name, but converts current iterated item into a string.
    str_list.append(wee)#adds converted item to list
pub_int = int(0)#pre-assigned int to be used in a loop.
for x in link2:#prints a nice forecast.
    print(str_list[pub_int])#prints day at x's location in the list.
    print(x.get('title', 'no title attribute'))#prints forecast for that day.
    pub_int += 1

#Time taken with trial and error: 3h 47mins
