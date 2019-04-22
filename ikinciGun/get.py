import requests
import bs4
import lxml
site = requests.get("https://stackoverflow.com/questions/1000900/how-to-keep-a-python-script-output-window-open")
soup = bs4.BeautifulSoup(site.text,"lxml")
sonuc = soup.find_all(class_ = "question-hyperlink")
for i in sonuc:
    print(i.text)
