from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
class Eczane:
    def __init__(self):
        self.eczaneIsim = []
        self.eczaneSokak = []
        self.EczaneTel = []
        self.EczaneSaat = []


        self.tarayıcı = webdriver.Chrome(executable_path=f"C:\\Program Files (x86)\\Google\\chromedriver.exe")
        self.tarayıcı.maximize_window()
        self.tarayıcı.get('http://www.kteb.org/')

        self.Xpath = ['//*[@id="intro2"]/div[2]/section[1]/div[1]/div[2]/ul/li[1]/a', '//*[@id="intro2"]/div[2]/section[1]/div[1]/div[2]/ul/li[2]/a',
                      '//*[@id="intro2"]/div[2]/section[1]/div[1]/div[2]/ul/li[3]/a', '//*[@id="intro2"]/div[2]/section[1]/div[1]/div[2]/ul/li[4]/a',
                      '//*[@id="intro2"]/div[2]/section[1]/div[1]/div[2]/ul/li[5]/a']
    def VeriCek(self):

        while self.Xpath != []:

            sehirler = WebDriverWait(self.tarayıcı,10).until(EC.element_to_be_clickable((By.XPATH, self.Xpath[0])))
            sehirler.click()
            sleep(5)
            self.source = self.tarayıcı.page_source
            self.soup = BeautifulSoup(self.source, 'html.parser')


            for veri in self.soup.find_all('div', class_='rc-info'):
                for isim in veri.find_all('h4'):
                    self.eczaneIsim.append(isim.text)
            self.eczaneIsim.append('bu eczane bitti')

            print(self.eczaneIsim)

            for veri in self.soup.find_all('div', class_= 'rc-info'):
                for sokak in veri.find('p'):
                    if len(sokak) < 32:
                        pass
                    else:
                        self.eczaneSokak.append(sokak)
            self.eczaneSokak.append('bu eczane bitti')

            print(self.eczaneSokak)

            for veri in self.soup.find_all('div', class_= 'rc-info'):
                for saat in veri.find_all('p')[-1]:
                    if len(saat) < 29:
                        pass
                    else:
                        self.EczaneSaat.append(saat)
            self.EczaneSaat.append('bu eczane bitti')
            print(self.EczaneSaat)

            for veri in self.soup.find_all('div', class_= 'rc-info'):
                for telno in veri.find_all('p')[-2]:
                    if len(telno) < 10:
                        pass
                    else:
                        self.EczaneTel.append(telno)
            self.EczaneTel.append('bu eczane bitti')
            print(self.EczaneTel)
            del self.Xpath[0]

            self.tarayıcı.back()
        self.tarayıcı.quit()

eczane = Eczane()
eczane.VeriCek()
