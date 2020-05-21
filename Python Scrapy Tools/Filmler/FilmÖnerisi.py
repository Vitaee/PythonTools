import json

import requests
from bs4 import BeautifulSoup

class Filmler:
    def __init__(self):
        self.my_json = {'filmler': []}
        self.FilmName = False
        self.FilmTime = False

    def VeriCek(self):
        for i in range(5):
            url = f"https://www.filmyani.com/film-izle/yillara-gore/page/{i}"
            page = requests.get(url)
            source = page.text
            soup = BeautifulSoup(source, 'html.parser')

            data = soup.find_all('div', class_='frag-k yedi')
            for item in data:
                self.FilmName = item.find('a')['title'].strip()
                self.FilmTime  = item.find('b').text.strip()


                json_data = {
                "FilmIsmi:": self.FilmName,
                "FilmHakkinda": self.FilmTime,
                }


                with open('Filmler.json', 'w+', encoding="utf-8") as file:
                    json.dump(self.my_json, file, indent=2, ensure_ascii=False)
                    self.my_json["filmler"].append(json_data)


filmler = Filmler()
filmler.VeriCek()
