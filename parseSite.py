import requests
from bs4 import BeautifulSoup

url = requests.get("https://www.n11.com/telefon-ve-aksesuarlari?pg=1")
r  = requests.get(url)
soup = BeautifulSoup(r.content,"lxml")
urunler = soup.find_all("li",attrs={"class":"column"})
for urun in urunler:
    urunAdi = urun.a.get("title")
    urunLink = urun.a.get("href")

    urun_r = reqests.get(urunLink)
    print(urun.r.status_code)
