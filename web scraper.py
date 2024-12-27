import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.edge.service import Service

driver_path = 'C:/Users/farha/OneDrive/Desktop/Class 37/MOD3/CIS 403/Week 17/Project3/edgedriver_win64/msedgedriver.exe'
service = Service(driver_path)

driver = webdriver.Edge(service=service)
driver.get('https://www.yearupalumni.org/s/1841/interior.aspx?sid=1841&gid=2&pgid=440')


results = []
other_results = []
content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll(attrs='title'):
    name = a.find('a')
    if name not in results:
        results.append(name.text)

for b in soup.findAll(attrs='more'):
    button = b.find('a')
    if button not in results:
        other_results.append(name.text)

df = pd.DataFrame({'Names': results, 'Buttons': other_results})
df.to_csv('names.csv', index=False, encoding='utf-8')

