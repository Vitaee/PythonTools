from bs4 import BeautifulSoup
import requests, re
from kuponer.auth import connection as baglanti
from datetime import datetime
from google.cloud import firestore


class main:
    def __init__(self):
        self.egitimBaslik = []
        self.egitimLink = []
        self.egitimFotograf = []
        self.egitimAciklama = []
        self.egitimFiyat = []
        self.egitimVeren = []
        import firebase_admin
        from firebase_admin import credentials
        from firebase_admin import firestore

        # Use the application default credentials
        cred = credentials.ApplicationDefault()
        cred = credentials.Certificate('pythondeneme-14e92-44e0170fe986.json')
        firebase_admin.initialize_app(cred)


        self.db = firestore.client()

    def getCourses(self):
        print("Başladı.")
        self.courseBriefData = ""
        self.pagePath = "https://www.discudemy.com/language/turkish"
        self.response = requests.get(self.pagePath)
        self.whole_source = self.response.text
        self.soup = BeautifulSoup(self.whole_source, 'html.parser')


        for item in self.soup.find_all("div", class_="meta"):
            for veri in item.find_all('span', attrs={'style': 'color: rgb(33, 186, 69);'}):
                if str(veri.text).isalnum():
                    self.egitimFiyat.append(veri.text)

        for item in self.soup.find_all("amp-img", class_= "ui full-width image"):
            print("Fotoğraf verisi: ", item['src'])
            self.egitimFotograf.append(item['src'])

        for heading in self.soup.find_all('a', class_="card-header"):
           try: self.egitimBaslik.append(heading.text)
           except: self.egitimBaslik.append("Başlık yok")
           self.egitimVeren.append("")
           self.CourseBrief(heading['href'])
           self.getCourseDetail(heading['href'])
        self.saveResults()
        print("Mesai biter bu adam kaçar.")

    def getCourseDetail(self, courseLink):
        print("Bana gelen link: " , courseLink)
        self.response = requests.get(courseLink)
        self.whole_source = self.response.text
        self.soup = BeautifulSoup(self.whole_source, "html.parser")

        for detail in self.soup.find_all("a", class_="ui big inverted green button discBtn"):
           self.getCourseCoupon(detail['href'])

    def getCourseCoupon(self, courseLink):
        print("Şu linkten kuponu alıyorum: ", courseLink)
        self.response = requests.get(courseLink)
        self.whole_source = self.response.text
        self.soup = BeautifulSoup(self.whole_source, "html.parser")

        for item in self.soup.find_all('div', class_="ui segment"):
            for data in item.find_all('a'):
                try: self.egitimLink.append(data['href'])
                except: self.egitimLink.append("Kupon Yok")
                print("Kurs bu linkte ücretsiz: ", data['href'])

    def CourseBrief(self, courseLink):
        self.courseBriefData = ""

        reqs = requests.get(courseLink)
        soup = BeautifulSoup(reqs.text, 'html.parser')
        for item in soup.find_all('div', class_="ui attached segment"):
            for data in item.find_all('p'):
                if "Course Language" in str(data.text) or "Publisher" in str(data.text):
                    pass
                elif len(str(data.text)) > 10:
                    self.courseBriefData = self.courseBriefData + data.text + "\n\n"
            self.egitimAciklama.append(self.courseBriefData)
        print("Kursun Detayı: ", self.courseBriefData)


    def saveResults(self):
        conn = baglanti()
        date = datetime.now().strftime("%x")

        #Saving to SQLite
        for index, item in enumerate(self.egitimLink, 0):
            sqlQuery = """INSERT INTO couponData
                                  (couponName, couponLink, couponDate, couponPrice, couponDetail, couponAuthor)
                                  VALUES (?, ?, ?, ?, ?, ?);"""
            data = (self.egitimBaslik[index],self.egitimLink[index],date, self.egitimFiyat[index],self.egitimAciklama[index],'1')
            conn.cursor().execute(sqlQuery, data)
            conn.commit()


        #Saving to Firebase
            doc_ref = self.db.collection(u'Egitimler').document(self.egitimBaslik[index])
            doc_ref.set({
                "Name": self.egitimBaslik[index],
                "Link": self.egitimLink[index],
                "Author": self.egitimVeren[index],
                "Date": firestore.SERVER_TIMESTAMP,
                "Detail": self.egitimAciklama[index],
                "Avatar": self.egitimFotograf[index]
            })
if __name__ == '__main__':
    main().getCourses()
