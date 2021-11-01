import requests,time, json
from bs4 import BeautifulSoup

class TechNews:
    def __init__(self) -> None:
        self.user_id = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.base_url = "https://flipboard.com/section/teknoloji-a0isdrb4bs8bb7n1"

        self.NewsTitle = []
        self.NewsShortContent = []
        self.SourceWebSite = []
        self.NewsAvatar = []


    def VeriBelirle(self) -> None:
        print("Veriler belirleniyor.")

        page = requests.get(self.base_url, headers=self.user_id)
        source = page.text
        soup = BeautifulSoup(source, 'html.parser')

        """
        script_datas = soup.find_all('script')
        script_text = script_datas[10].text

        script_text = script_text.replace('window.__PRELOADED_STATE__ = ', '')
        script_text = script_text.replace('"\\"','')

        y = json.dumps(script_text, ensure_ascii=False)

        with open('./bookdetails.json', 'w') as outfile:
            json.dump(y, outfile,ensure_ascii=False)

        exit()
        
        """

        #Href belirle
        to_data = soup.find_all('div', class_= 'post-attribution__link-container')
        for item in to_data:
            data = "https://flipboard.com" + item.find("a",class_="post-attribution__link")['href']
            self.VeriCek(data)

    def VeriCek(self,url:str) -> None:
        print()
        print("Veriler çekiliyor.." + " --> " + url) 
        print()
        try:self.page = requests.get(url, headers=self.user_id)
        except: pass

        source = self.page.text
        soup = BeautifulSoup(source, 'html.parser')

        #HaberBaslik ve Haber KaynakURL
        text_data = soup.find('h1', class_='article-text--title--large item-details__title')
        self.NewsTitle.append(text_data.text)
        
        source_url = soup.find('p', class_='read-more-in-source') 
        self.SourceWebSite.append(source_url.find('a')['href'])

        #Haber kısa bilgi
        short_info = soup.find('p', class_='post__excerpt')
        self.NewsShortContent.append(short_info.text)

        #Haber Avatarı
        img_data = soup.find('picture',class_='css-1opdvho e1kiqfk30')

        self.NewsAvatar.append(img_data.find('img')['src'])


        self.VeriGoster()
    
    def VeriGoster(self):
        print(self.NewsTitle)

        

scrapper = TechNews()
scrapper.VeriBelirle()
