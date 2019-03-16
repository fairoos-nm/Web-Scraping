import requests
from bs4 import BeautifulSoup
import csv
url = "https://coreyms.com/"

source_code = requests.get(url).text

soup = BeautifulSoup(source_code, 'lxml')
csv_file = open("scrape.csv", "w")
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summery', 'video_link'])
for article in soup.find_all("article"):
    headline = article.h2.a.text
    print(headline)
    
    summery = article.find('div',class_='entry-content').p.text
    print(summery )

    vid_src = article.find('iframe',class_='youtube-player')['src']
    vid_id = vid_src.split('/')[4]
    vid_id = vid_id.split('?')[0]
    youtube_link = f"https://youtube.com/watch?v={vid_id}"
    print(youtube_link)

    print()
    csv_writer.writerow([headline, summery, youtube_link])
csv_file.close()
