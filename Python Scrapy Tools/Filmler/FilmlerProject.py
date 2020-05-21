from bs4 import BeautifulSoup
import requests
import json
import matplotlib.pyplot as plt
from auth import connection as baglanti
from random import randrange
class Filmler:
    def __init__(self):
        self.url = "https://www.fullhdfilmizlesene.com/"
        self.user_id = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}

        self.FilmName = []
        self.FilmType = []
        self.FilmIMDB = []
        self.FilmYear = []
        self.FilmUrl = []

        #TO-DO: veriler json dosyasına yazılacak, aynı filmler veri olarak çekilmeyecek.


    def veriCek(self):
        print("[LOG]\tFilm Verileri Alınıyor..")
        i = 0
        while i < 7:
            url = self.url + f"yeni-filmler/{i+1}"
            self.page = requests.get(url, headers=self.user_id)
            self.whole_source = self.page.text
            self.soup = BeautifulSoup(self.whole_source, 'html.parser')

            data = self.soup.find_all("div", class_='dty')

            #Film URL ve İsim Al
            for item in data:
                items = item.find('a')
                self.FilmUrl.append(items['href'])
                self.FilmName.append(items.text.strip())

            #Film Türünü Al
            for item in data:
                items = item.find('span')
                self.FilmType.append(items.text)

            #Film Yılını ve IMDB Al
            for item in data:
                items =item.find_all('span')
                self.FilmYear.append(items[2].text[:4])
                self.FilmIMDB.append(items[3].text[5:])
            i += 1


    def saveResults(self):

        data={
            "Film Ismi": self.FilmName,
            "Film Turu": self.FilmType,
            "Film Yil": self.FilmYear,
            "Film IMDB": self.FilmIMDB,
            "Film URL": self.FilmUrl
        }
        print(json.dumps(data,indent=2,  ensure_ascii=False))

    def SaveSQL(self):
        conn = baglanti()
        # TO-DO SQLdeki veri aynı ise sql'e veri girmesin.
        #İlk önce db'deki veriyi çek sonra veri listen ile kontrol et.
        # Saving to SQLite
        filmName = []
        filmURL = []
        self.IMDB = []

        curr = conn.cursor()
        curr.execute("SELECT * FROM Filmsdata")
        rows = curr.fetchall()
        for fow in rows:  # SQL lite deneme.
            filmName.append(fow[1])
            filmURL.append(fow[5])
            self.IMDB.append(fow[4])

        i = 0
        while i < 10:
            if self.FilmName[i] == filmName[i]:
                print("veriler aynı")
                i += 1
            else:
                print("aynı değil")

                #print("Rasgele film seçiyorum..")
                #random_index = randrange(len(filmName))
                #item = filmName[random_index]
                #print(item)
                #print(f"Film URL'si bu: {filmURL[random_index]}")


                for index, item in enumerate(self.FilmName, 0):
                    sqlQuery = """INSERT INTO Filmsdata
                                          (FilmIsmi, FilmTuru, FilmYil, FilmIMDB, FilmURL) 
                                          VALUES (?, ?, ?, ?, ?);"""
                    data = (self.FilmName[index], self.FilmType[index], self.FilmYear[index], self.FilmIMDB[index], self.FilmUrl[index])
                    conn.cursor().execute(sqlQuery, data)
                    conn.commit()
                    i += 1


    def ShowGraph(self):
        results = list(map(float, self.IMDB))
        buyuk = []
        kucuk = []
        orta = []
        while results:
            if results[0] > 5.0 and results[0] <= 6.4:
                orta.append(results[0])

            elif results[0] >= 7.0 or results[0] >= 6.5:
                buyuk.append(results[0])

            elif results[0] <= 5.0:
                kucuk.append(results[0])

            results.pop(0)


        left = [1, 2, 3]
        height = [len(kucuk), len(orta),len(buyuk)]

        tick_label = ['IMDB Düşük', 'IMDB Orta' ,'IMDB Yüksek']

        plt.bar(left, height, tick_label=tick_label,
                width=0.3, color=['red', 'green'])

        plt.xlabel('x - ekseni')
        plt.ylabel('y - ekseni')

        plt.title('Film IMDB Analizi')
        plt.show()

veri = Filmler()
veri.veriCek()
#veri.saveResults()
veri.SaveSQL()
#veri.FetchData()
#veri.ShowGraph()