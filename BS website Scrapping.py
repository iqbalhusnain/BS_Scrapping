from bs4 import BeautifulSoup
import requests

r = requests.get('https://www.sbp.org.pk/smefd/circulars/2020/index.htm')
#r = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#')

soup = BeautifulSoup(r.content, 'html.parser')

paras =soup.find_all('p',class_ = 'headerlink')

anchor =soup.find_all('a')
for link in anchor:
    href = link.get('href')
    print(href)


print(soup.title.text)
print("Done")
