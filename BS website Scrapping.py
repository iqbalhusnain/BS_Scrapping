from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.sbp.org.pk/smefd/circulars/2020/index.htm'

r = requests.get(url)
#r = requests.get('https://www.crummy.com/software/BeautifulSoup/bs4/doc/#')

soup = BeautifulSoup(r.content, 'html.parser')

#anchor = soup.find_all('a',href = re.compile('http://www.sbp.org.pk'))

anchor = soup.find_all('a',href = re.compile('2020'))


file_name = "Circulars.csv"
f = open(file_name,'w')
header = 'Cir_Name ,Links\n'
f.write(header)

for link in anchor:
    href = link.get('href')
    text = link.getText()
    text1 = text.replace("\n", "")
    f.write(text1.replace(',','|') + "," + href.replace("," ,"|") +"\n")

print("Done")