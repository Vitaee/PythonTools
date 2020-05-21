from bs4 import BeautifulSoup
import requests
import json
from time import sleep

class main:
    def __init__(self):

        self.BookName = False
        self.BookPages = False
        self.BookYear = False
        self.BookSize = False
        self.FirstDownloadLink = False
        self.RealDownloadLink = False

        self.user_id = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.currentDocs = []

        self.my_json = {"pdfbooks": []}
        with open('pdfbooks.json','r+',encoding='utf-8') as file:
            data = json.load(file)
        for item in data["pdfbooks"]:
            try: self.currentDocs.append(item["Kitap Link"])
            except: pass

    def VeriBelirle(self):
        i = 0
        while i < 5:
            url = f"https://www.pdfdrivetr.com/search?q=Programlama&pagecount=&pubyear=&searchin=tr&page={i+1}"
            page = requests.get(url, headers=self.user_id)
            source = page.text
            soup = BeautifulSoup(source, 'html5lib')
            data = soup.find_all('div',class_='file-right')
            for item in data:
                items = item.find('a')
                self.all_hrefs = "https://www.pdfdrivetr.com/" + items['href']
                self.VeriCek(self.all_hrefs)
            i += 1

    def VeriCek(self, source):
        if source in self.currentDocs:
            print("Aynı link denk geldi")
        else:
            page = requests.get(source, headers=self.user_id)
            source = page.text
            soup = BeautifulSoup(source, 'html5lib')

            #Kitap İsmi
            data = soup.find('h1',itemprop='name')
            self.BookName = data.text

            #Kitap Sayfa Sayısı, Tarihi, Boyutu
            data1 = soup.find_all('div',class_='ebook-file-info')
            for item in data1:
                items = item.findAll('span',class_='info-green')
                self.BookPages = items[0].text
                self.BookYear = items[1].text
                self.BookSize = items[2].text

            #Kitap İlk İndirme Linki
            data2 = soup.find_all('span', id='download-button')
            for item in data2:
                items = item.find('a')
                self.FirstDownloadLink = "https://www.pdfdrivetr.com/"+items['href']

                self.KitapIndir(self.FirstDownloadLink)

    def KitapIndir(self, source_link):
        print("Gerçek indirme linki bekleniyor.")
        #İNDİRME LİNKİ SORUNU VAR.
        page = requests.get(source_link, headers=self.user_id)
        sleep(21)
        print("Bekleme süresi bitti.")
        source = page.text
        soup = BeautifulSoup(source, 'html.parser')
        download_data = soup.find_all('div', id='alternatives')
        for item in download_data:
            items = item.find('div',class_='text-center')
            print(items)
        exit()
        data = {"Kitap İsmi":self.BookName,
                "Kitap Sayfa Sayısı":self.BookPages,
                "Kitap Yılı": self.BookYear,
                "Kitap Boyutu":self.BookSize,
                "Kitap Link":self.all_hrefs}

        self.my_json["pdfbooks"].append(data)
        self.saveResults(self.BookName, self.BookPages, self.BookYear, self.BookSize)

    def saveResults(self,BookName, BookPages, BookYear, BookSize):
        with open('pdfbooks.json','w+',encoding='UTF-8') as file:
            json.dump(self.my_json, file, indent=2, ensure_ascii=False)

if __name__ == '__main__':
    main().VeriBelirle()