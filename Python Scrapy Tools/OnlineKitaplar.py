from bs4 import BeautifulSoup
import json

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep


class EBooks:
    def __init__(self):
        self.BookHistory = []
        self.BooksLink = []
        self.CurrentBooks = []
        self.Languages = ["Python","Java"]
        self.BookName = False
        self.BookAuthor = False
        self.DownloadLink = False
        self.BookYear = False
        self.my_json = {'books': []}
        with open('bookdetails.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data['books']:
            try: self.BookHistory.append(item['BookName'])
            except:pass

    def KaynakLink(self):

        self.tarayici = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.tarayici.maximize_window()
        self.tarayici.get('https://singlelogin.org/?logoutAll')

        email_gir = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.ID, 'username')))
        email_gir.click()
        email_gir.send_keys("canilguu@gmail.com")

        sifre_gir = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.ID, 'password')))
        sifre_gir.click()
        sifre_gir.send_keys("siteKullanıcı_şifre")

        siteye_gir = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.NAME, 'submit')))
        siteye_gir.click()


        arama_yap = WebDriverWait(self.tarayici, 10).until(EC.element_to_be_clickable((By.ID, 'searchFieldx')))
        arama_yap.send_keys(self.Languages[0])
        arama_yap.send_keys(Keys.ENTER)

        while self.Languages != []:
            for i in range(3):
                self.tarayici.get(f"https://b-ok.cc/s/{self.Languages[0]}?page={i}")
                sleep(3)
                source = self.tarayici.page_source
                soup = BeautifulSoup(source, 'html.parser')

                data = soup.find_all('h3', itemprop='name')
                for item in data:
                    names = item.find('a')
                    self.BooksLink.append(f"https://b-ok.cc/{names['href']}")
            a = len(self.BooksLink)
            print(f"{self.Languages[0]} Aramasında Çıkan ilk {a} Kitap Listeye Aktarıldı.")

            self.Languages.pop(0)


    def VeriBelirle(self):
        while self.BooksLink:
            self.tarayici.get(self.BooksLink[0])
            sleep(2)
            self.whole_source = self.tarayici.page_source
            soup = BeautifulSoup(self.whole_source, 'html.parser')
            self.Pdf_Detector(soup)
            print(f"Bu siteden veri çekiliyor: {self.BooksLink[0]}")
            self.BooksLink.pop(0)

    def Pdf_Detector(self, pageurl):
        if self.BookName in self.BookHistory:
            print("Aynı kitap denk geldi.")
        else:
            if pageurl == False:
                self.tarayici.quit()
                print("Bot tüm verileri çekti program kapatılıyor.")
                exit()

            # Kitap ismini bul.
            for item in pageurl.find_all('h1', itemprop='name'):
                self.BookName = item.text

            #Kitap Yazarını bul.
            data = pageurl.find_all('div',class_='col-sm-9')
            for item in data:
                items = item.find('i')
                self.BookAuthor = items.text

            #Kitap indirme linki alınamıyor. Giriş Yapmak gerekiyor.
            downnload_links = pageurl.find_all('div',class_="btn-group")
            for item in downnload_links:
                items = item.find('a',href=True)
                self.DownloadLink = items['href']
                break

            #Kitap Yılı
            book_name = pageurl.find_all('div',class_='bookProperty property_year')
            for item in book_name:
                items = item.find('div',class_='property_value')
                self.BookYear = items.text
                break

            data = {
                "BookName:": self.BookName,
                "BookAuthor": self.BookAuthor,
                "DownloadLink": self.DownloadLink,
                "BookYear": self.BookYear
            }
            self.my_json["books"].append(data)
            self.Saves()

    def Saves(self):
        with open('bookdetails.json', 'w+', encoding='utf-8') as file:
            json.dump(self.my_json, file, indent=2)


kitaplar = EBooks()
kitaplar.KaynakLink()
kitaplar.VeriBelirle()
kitaplar.Pdf_Detector(pageurl=False)
kitaplar.Saves()