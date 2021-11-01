import requests
import json
from bs4 import BeautifulSoup
import os
class main:
    def __init__(self) -> None:
        self.bountyName = []
        self.bountyDownLink = []
        self.bountyAvatar = []
        self.bountyAnalyse = []
        self.my_json = {"wallpapers": []}
        self.link_history = []

        with open('wallpapers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)

        for item in data['wallpapers']:
            try: self.link_history.append(item['Kaynak Link'])
            except: pass

    def start(self) -> None:
        for i in range(1,5):
            print("[LOG]\tWallpaper botu başladı. {}. sayfa taranıyor".format(i))
            response = requests.get("http://wallpaperswide.com/page/" + str(i))
            whole_source = response.text
            soup = BeautifulSoup(whole_source, 'html.parser')
            self.analyse(soup)

    def analyse(self, source) -> None:
        link = source.find_all('div', class_='thumb')
        for hrefs in link:
            links = hrefs.find('a')
            self.detail('http://wallpaperswide.com' + links['href'])

    def detail(self,link:str) -> None:
        if link in self.link_history:
            print("Aynı link denk geldi.")
        else:
            print("İncelenen wallpaper: {}".format(link))
            response = requests.get(link)
            whole_source = response.text
            soup = BeautifulSoup(whole_source, 'html.parser')
            self.link_history.append(link)

            #Bounty Avatar
            avatar = soup.find('div', class_='picture_wrapper_details')
            for item in avatar.find_all('img'):
                avatar = item['src']


            #Bounty down_link
            button = soup.find("div",class_="wallpaper-resolutions")
            for down in button.find_all('a',title="HD 16:9 1920 x 1080 wallpaper for FHD 1080p High Definition or Full HD displays"):
                button = 'http://wallpaperswide.com/' + down['href']

            #Bounty Name
            name = soup.find("h3", itemprop="name")
            name = name.text

            data = {"Resim": avatar,
                    "Indirme Link": button,
                    "Kaynak Link": link,
                    "Resim Ismi": name}
            self.my_json["wallpapers"].append(data)

            self.save(avatar, button, name)


    def save(self, avatar:str, button:str, name:str) -> None:
        with open('wallpapers.json', 'w+', encoding='UTF-8') as file:
            json.dump(self.my_json, file ,indent=2)