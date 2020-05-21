import requests
from bs4 import BeautifulSoup

class main:
    def __init__(self):
        self.user_id = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"}
        self.base_url = "https://flipboard.com/section/teknoloji-a0isdrb4bs8bb7n1"

        self.NewsTitle = []
        self.NewsShortContent = []
        self.SourceWebSite = []
        self.NewsAvatar = []


    def VeriBelirle(self):
        print("Veriler belirleniyor.")
        page = requests.get(self.base_url, headers=self.user_id)
        source = page.text
        soup = BeautifulSoup(source, 'html.parser')

        #Href belirle
        data = soup.find_all("h1",class_="post__title article-text--title--large")
        for item in data:
            items = item.find('a')
            self.VeriCek("https://flipboard.com"+items['href'])

    def VeriCek(self,url):
        print("Veriler çekiliyor..")
        try:self.page = requests.get(url, headers=self.user_id)
        except: pass

        source = self.page.text
        soup = BeautifulSoup(source, 'html.parser')

        #HaberBaslik ve Haber KaynakURL
        data = soup.find_all('h1', class_='post__title article-text--title--large')
        for item in data:
            items = item.find('a')
            self.NewsTitle.append(items.text)
            self.SourceWebSite.append(items['href'])

        #Haber kısa bilgi
        data = soup.find_all('p', class_='post__excerpt')
        for item in data:
            items = item.find('a')
            self.NewsShortContent.append(items.text)

        #Haber Avatarı
        data = soup.find_all('a',class_='post__media post__media--image media-link outbound-link')
        for item in data:
            items = item.find('img')
            self.NewsAvatar.append(items['src'])


        self.VeriGoster()
    def VeriGoster(self):
        #print(self.NewsTitle)
        pass

        
if __name__ == '__main__':
    main().VeriBelirle()
