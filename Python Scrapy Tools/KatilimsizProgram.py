import requests
import json
from bs4 import BeautifulSoup

class Program:
    def __init__(self):
        self.ProgName = False
        self.ProgUrl = []
        self.ProgLink = False
        self.ProgDate = False
        self.ProgHistory = []
        self.my_json = {"programs": []}
        with open('programdetails.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data['programs']:
            try:
                self.ProgHistory.append(item['ProgLink'])
            except:
                pass

    def UrlAl(self):
        baseurl = 'https://www.oneindir.com/kategori/program-indir/cesitli-full-program-indir/page/'
        self.id_cart = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36' }
        for i in range(2):
            page = requests.get(baseurl + str(i + 1) + '/', headers=self.id_cart)
            source = page.text
            soup = BeautifulSoup(source, 'html5lib')
            self.data = soup.find_all('ul', class_='progList')

            for item in self.data:
                self.href = item.find_all('li')
                for items in self.href:
                    a = items.find('a')['href']
                    self.ProgUrl.append(a)

        while self.ProgUrl:
            print("İşlemdeki sayfa: " + self.ProgUrl[0])
            self.response = requests.get(self.ProgUrl[0], headers=self.id_cart)
            self.whole_source = self.response.text
            self.soup = BeautifulSoup(self.whole_source, 'html.parser')
            self.VeriCek(self.soup)
            self.ProgUrl.pop(0)

    def VeriCek(self, pageurl):
        if self.ProgName in self.ProgHistory:
            print("Aynı program denk geldi.")
        else:
            if pageurl == False:
                print("Bot tüm verileri çekti program kapatılıyor.")
                exit()

        #Program adı
        name_data = pageurl.find('div', class_='tags')
        self.ProgName = name_data.text.strip()

        #ProgramDate
        date_data = pageurl.find_all('div', class_='singleProperties')
        for b in date_data:
            self.ProgDate = b.find('li').text[5:17].strip()

        #ProgramLink
        link_data = pageurl.find_all('div',class_='digerSecContent')
        for c in link_data:
            self.ProgLink = c.find_all('a')[1]['href']

        data = {
            "ProgName:": self.ProgName,
            "ProgDate": self.ProgDate,
            "ProgLink": self.ProgLink,
        }
        self.my_json["programs"].append(data)
        self.Saves()

    def Saves(self):
        with open('programdetails.json', 'w', encoding='utf-8') as file:
            json.dump(self.my_json, file, indent=2)




program = Program()
program.UrlAl()
program.VeriCek()

