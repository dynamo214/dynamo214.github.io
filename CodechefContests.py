import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary

firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image', 2)
firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

driver=webdriver.Firefox(firefox_profile=firefox_profile)
driver.get('https://www.codechef.com/contests')
res=driver.execute_script("return document.documentElement.outerHTML")
driver.quit()

print('You want to know present,past or future contests of codechef?(1/2/3)')
get=input()
soup=BeautifulSoup(res,'lxml')
if get=='1':
    f=soup.find_all('table')[1]
elif get=='2':
    f=soup.find_all('table')[3]
elif get=='3':
    f=soup.find_all('table')[2]
else:
    print("No contests")

con=f.find('tbody')
rows=con.find_all('tr')
if get=='1':
    print('PRESENT CONTESTS')
elif get=='2':
    print('PAST CONTESTS')
elif get=='3':
    print('FUTURE CONTESTS')
print('   CODE      NAME               START-DATE     TIME    END-DATE    TIME')
i=0
for row in rows:
    i=i+1
    code=row.find_all('td')[0].text.strip()
    name=row.find_all('td')[1].text.strip()
    start=row.find_all('td')[2].text.strip()
    end=row.find_all('td')[3].text.strip()
    print(i,code,name,start,end)
    