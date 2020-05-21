from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from AllXpath import Web, Prog, Database, Grapdesign, OSsystem, Comptech, Gameprog, Securityy, Softwaree
from googletrans import Translator

class PdfBooks:

    def __init__(self):
        self.DC = []
        self.DCname = []
        self.DCavatar = []
        self.DClink = []
        self.DCbio =[]
        self.DCauthor = []

        cred = credentials.Certificate('pdf-kitaplar-firebase-adminsdk-p2r3c-5cebe0c664.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

        self.browser = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.browser.maximize_window()

    def WebDevelopment(self):

        self.browser.get('http://www.allitebooks.org/web-development/')

        while Web != []:
            page = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Web[0])))
            page.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')


            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break


            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Web[0])))
                page.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')



            for index in soup.find_all('div',class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])


            del Web[0]
            self.browser.back()


    def Programming(self):
        self.browser.get('http://www.allitebooks.org/programming/')

        while Prog != []:
            page_prog = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Prog[0])))
            page_prog.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break


            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_prog = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Prog[0])))
                page_prog.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div',class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])


            del Prog[0]
            self.browser.back()


    def DataBase(self):
        self.browser.get('http://www.allitebooks.org/datebases/')

        while Database != []:
            page_db = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Database[0])))
            page_db.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break


            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_db = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Database[0])))
                page_db.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div',class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])


            del Database[0]
            self.browser.back()


    def GraphDesign(self):
        self.browser.get('http://www.allitebooks.org/graphics-design/')
        while Grapdesign != []:

            page_graph = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Grapdesign[0])))
            page_graph.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break


            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_graph = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Grapdesign[0])))
                page_graph.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div',class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])


            del Grapdesign[0]
            self.browser.back()


    def OsSystems(self):
        self.browser.get('http://www.allitebooks.org/operating-systems/')

        while OSsystem != []:
            page_os = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, OSsystem[0])))
            page_os.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break


            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_os = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, OSsystem[0])))
                page_os.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div',class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])


            del OSsystem[0]
            self.browser.back()

    def CompTech(self):
        self.browser.get('http://www.allitebooks.org/computers-technology/')
        while Comptech != []:
            page_comp = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Comptech[0])))
            page_comp.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break

            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_comp = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Comptech[0])))
                page_comp.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div', class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])

            del Comptech[0]
            self.browser.back()


    def GameProg(self):
        self.browser.get('http://www.allitebooks.org/game-programming/')

        while Gameprog != []:
            page_game = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Gameprog[0])))
            page_game.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break

            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_game = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Gameprog[0])))
                page_game.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div', class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])

            del Gameprog[0]
            self.browser.back()


    def Security(self):
        self.browser.get('http://www.allitebooks.org/security/')
        while Securityy != []:
            page_sec = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Securityy[0])))
            page_sec.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break

            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_sec = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Securityy[0])))
                page_sec.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('link yok!!')


            for index in soup.find_all('div', class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])

            del Securityy[0]
            self.browser.back()


    def Software(self):
        self.browser.get('http://www.allitebooks.org/software/')

        while Softwaree != []:
            page_soft = WebDriverWait(self.browser,10).until(EC.element_to_be_clickable((By.XPATH, Softwaree[0])))
            page_soft.click()

            page_source = self.browser.page_source
            soup = BeautifulSoup(page_source, 'html.parser')

            for index in soup.find_all('div', attrs={'class': 'book-detail'}):
                for author in index.find_all('dd'):
                    self.DCauthor.append(author.text)
                    break

            try:
                for index in soup.find('h1', class_='single-title'):
                    self.DCname.append(index)
            except:
                page_soft = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, Softwaree[0])))
                page_soft.click()

            try:
                link = self.browser.find_element_by_css_selector('.download-links a').get_attribute('href')
                self.DClink.append(link)
            except:
                print('error')

            for index in soup.find_all('div', class_='entry-body-thumbnail hover-thumb'):
                for image in index.find_all('img'):
                    self.DCavatar.append(image['src'])

            del Softwaree[0]
            self.browser.back()

    def Translate(self):
        translator = Translator()
        translated = translator.translate(self.DCname,src = "en", dest = "tr")
        for trans in translated:
            print(f'{trans.origin} -> {trans.text}')


    def SaveData(self):
        print(self.DCauthor)
        print(self.DCname)
        print(self.DClink)
        print(self.DCavatar)
        print(len(self.DCauthor))
        print(len(self.DCname))
        print(len(self.DClink))
        print(len(self.DCavatar))

        # Saving to Firebase
        for index, item in enumerate(self.DClink, 0):
            doc_ref = self.db.collection(u'PDF Kitaplar').document(self.DCname[index])
            doc_ref.set({
                "Yazar": self.DCauthor[index],
                "Kitap İsmi": self.DCname[index],
                "PDF Link": self.DClink[index],
                "Kitap Avatarı":self.DCavatar,
                "Database Zaman": firestore.SERVER_TIMESTAMP,

            })


pdf = PdfBooks()
pdf.WebDevelopment()
pdf.Programming()
pdf.DataBase()
pdf.GraphDesign()
pdf.OsSystems()
pdf.CompTech()
pdf.GameProg()
pdf.Security()
pdf.Software()

pdf.SaveData()


