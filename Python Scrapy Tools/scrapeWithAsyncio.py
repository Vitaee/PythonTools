import asyncio, pandas, json, time, aiohttp
from bs4 import BeautifulSoup

global json_data 
global headers
headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'}

json_data = { "course_data" : [] }

async def save_course_detail_to_csv(data):
    df = pandas.DataFrame(data)
    df.to_csv("data.csv", index=False, header=True)


async def scrape_course_details(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        temp_json = {}
        async with session.get(url, ssl=False) as response:
            body = await response.text()

            html = BeautifulSoup(body, 'html.parser')

            print("\n\n", url, "\n\n")

            lecture_details_html = html.find('div','rc-CDPSchemaMarkup')
            if lecture_details_html is not None:
                if lecture_details_html.find('script').text is not None:
                    lecture_details_html = lecture_details_html.find('script').text

            if lecture_details_html is None:
                try:
                    lecture_details_html = html.find('div', class_='rc-S12nXDPSchemaMarkup').find('script').text
                except AttributeError as e:
                    try:
                        lecture_details_html = html.find('script', attrs={"type":"application/ld+json"}).text
                    except AttributeError:
                        try:
                            lecture_details_html = html.find('div', class_='rc-CDPSchemaMarkup').find('script').text
                        except:
                            lecture_details_html = None
                            
            if lecture_details_html is not None:
                
                lecture_details_json = json.loads(lecture_details_html)

                
                try:
                    temp_json["Course Name"] = lecture_details_json["@graph"][1]["name"]
                except KeyError as e:
                    temp_json["Course Name"] = ""

                try:
                    temp_json["Course Provider"] = lecture_details_json["@graph"][1]["provider"]["name"]
                except:
                    try:
                        temp_json["Course Provider"] = lecture_details_json["@graph"][1]["provider"][0]["name"]
                    except KeyError as e:
                        try: 
                            temp_json["Course Provider"] = html.find('div' , class_='_1qfi0x77 instructor-count-display').text
                        except:
                            temp_json["Course Provider"] = ""


                try:
                    temp_json["Course Description"] = lecture_details_json["@graph"][1]["hasCourseInstance"]["description"].split("...")[0]
                except KeyError as e:
                    try:
                        temp_json["Course Description"] = lecture_details_json["@graph"][1]["description"].split("...")[0]
                    except KeyError:
                        temp_json["Course Description"] = ""


                try:
                    temp_json["# of Students Enrolled"] = html.find('div', class_='rc-ProductMetrics').text.split(" ")[0]
                except AttributeError:
                    try:
                        temp_json["# of Students Enrolled"] =  html.find_all('div', class_='css-oj3vzs')[0].text.split(" ")[2]
                    except IndexError as e:
                        temp_json["# of Students Enrolled"] = "0"


                try:
                    temp_json["# of Ratings"] = lecture_details_json["@graph"][1]["aggregateRating"]["reviewCount"]
                except KeyError as e:
                    try:
                        temp_json["# of Ratings"] = html.find('div', class_= "_wmgtrl9 color-white ratings-count-expertise-style").text.split(" ")[0]
                    except AttributeError as e:
                        try:
                            temp_json["# of Ratings"] = html.find_all('div', class_='css-oj3vzs')[0].text.split(" ")[0]
                        except IndexError:
                            temp_json["# of Ratings"] = "0.0"

                if temp_json["Course Name"]:
                    json_data["course_data"].append(temp_json)
    
    
async def scrape_category_course_urls(url):
    async with aiohttp.ClientSession(headers=headers) as session:
        async with session.get(url) as resp:
            body = await resp.text()
            soup = BeautifulSoup(body, 'html.parser')

            data_class = soup.find_all('div', class_='rc-CollectionItem-wrapper')[4:]
            tasks = []
            for item in data_class:
               
                if item.find('a') is not None:
                    if item.find('a')['href'][0:5] == "https":
                        task = asyncio.create_task(scrape_course_details(item.find('a')['href']))
                    else:
                        task = asyncio.create_task(scrape_course_details("https://www.coursera.org"+item.find('a')['href']))
                    tasks.append(task)
            
            await asyncio.gather(*tasks)


async def main(dynamic_url):
    start_time = time.time()

    await scrape_category_course_urls(f"https://www.coursera.org/browse/{dynamic_url}")
    
    await save_course_detail_to_csv(json_data["course_data"])

    json_data["course_data"].clear()
    time_difference = time.time() - start_time
    print(f'Scraping time: %.2f seconds.' % time_difference)

asyncio.run(main("math-and-logic"))