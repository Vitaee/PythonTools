from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from time import sleep


class Instagram:
    def __init__(self):
        self.yorumYapan = []
        self.yorum = []

        cred = credentials.Certificate('instagramyorumlar-firebase-adminsdk-6e46q-ad8c1e8a6e.json')
        firebase_admin.initialize_app(cred)

        self.db = firestore.client()

        self.tarayıcı = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.tarayıcı.maximize_window()

    def Gıt(self):

        #self.tarayıcı.get('https://www.instagram.com/p/B_0CcDdAwof/')
        self.tarayıcı.get("https://www.instagram.com/p/B_99rNxBHSZ/")
        pyautogui.moveTo(x=1295, y=590)

        while True:
            try:
                buton = WebDriverWait(self.tarayıcı,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"span[aria-label='Load more comments']")))
                buton.click()
            except:
                print("Daha fazla yorum yok!")
                bitti = True
                break


        if bitti == True:
            sleep(3)

            self.source = self.tarayıcı.page_source
            self.soup = BeautifulSoup(self.source, 'html.parser')


            for ite in self.soup.find_all('div', class_='C4VMK'):
                for item in ite.find_all("h3", class_="_6lAjh"):
                    for veri in item.find_all('a'):
                        self.yorumYapan.append(veri.text)


            print(self.yorumYapan)


            for item in self.soup.find_all("div", class_="C4VMK"):
                for veri in item.find_all('span',class_=''):

                    self.yorum.append(veri.text)


            self.yorum.pop(0)
            print(self.yorum)


            self.tarayıcı.quit()


    def saveResults(self):
        print(len(self.yorumYapan))
        print(len(self.yorum))
        exit()

        #Saving to Firebase
        for index, item in enumerate(self.yorum, 0):

            doc_ref = self.db.collection(u'Yorumlar').document(self.yorumYapan[index])
            doc_ref.set({
                "Yorum Yapan": self.yorumYapan[index],
                #"Sure": self.yorumSure[index],
                "Yorum": self.yorum[index],
                "Database Zaman": firestore.SERVER_TIMESTAMP,

            })



insta = Instagram()
insta.Gıt()
insta.saveResults()
