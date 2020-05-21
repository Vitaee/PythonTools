from bs4 import BeautifulSoup
import requests
from kuponer.auth import connection as baglanti

class main:
    def __init__(self):
        self.FilmIsmi = []
        self.FilmYil = []
        self.FilmIMDB = []
        self.imdb = None
        self.User_id = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.url = "https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm"
        self.page = requests.get(self.url, headers=self.User_id)
        self.whole_source = self.page.text
        self.soup = BeautifulSoup(self.whole_source,'html.parser')


    def veriCek(self):
        print("veri alınıyor..")

        #Film Yılını Al
        data = self.soup.find_all('td',class_="titleColumn")
        for item in data:
            items = item.find('span')
            self.FilmYil.append(items.text.strip())

        #Film İsmini Al
        for item in data:
            items = item.find('a')
            self.FilmIsmi.append(items.text)

        #Film IMDB Puanı Al
        data1 = self.soup.find_all('td',class_='ratingColumn imdbRating')
        for item in data1:
            self.imdb = item.find('strong')
            if self.imdb == None:
                self.FilmIMDB.append("IMDB Yok")
                continue

            if self.imdb != None:
                self.FilmIMDB.append(self.imdb.text.strip())


        print(len(self.FilmYil))
        print(len(self.FilmIMDB))
        print(len(self.FilmIsmi))

        self.saveResults()
    def saveResults(self):

        conn = baglanti()
        #date = datetime.now().strftime("%x")

        # Saving to SQLite
        for index, item in enumerate(self.FilmIsmi, 0):
            sqlQuery = """INSERT INTO Deneme
                                        (FilmIsmi, FilmYil, FilmIMDB) 
                                        VALUES (?, ?, ?);"""
            data = (
            self.FilmIsmi[index], self.FilmYil[index], self.FilmIMDB[index])
            conn.cursor().execute(sqlQuery, data)
            conn.commit()

if __name__ == '__main__':
    main().veriCek()



