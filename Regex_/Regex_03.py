import json
import requests
from multiprocessing import Pool
from requests.exceptions import RequestException
import re

def getOnePage(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except RequestException:
        return None

def parseOnePage(html):
    pattern = re.compile('<dd>.*?board-index.*?>(\d+)</i>.*?data-src="(.*?)".*?name"><a'
                         +'.*?>(.*?)</a>.*?star">(.*?)</p>.*?releasetime">(.*?)</p>'
                         +'.*?integer">(.*?)</i>.*?fraction">(.*?)</i>.*?</dd>', re.S)
    items = re.findall(pattern, html)
    # print(items)
    for item in items:
        yield {
            'index': item[0],
            'image_url': item[1],
            'film_name': item[2],
            'actor': item[3].strip()[3:],
            'time': item[4].strip()[5:],
            'score': item[5] + item[6]
        }

def writeToFile(content):
    with open('filmInfo.txt', 'a', encoding='utf-8') as f:
        f.write(json.dumps(content, ensure_ascii=False) + '\n')
        f.close()

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = getOnePage(url)
    for item in parseOnePage(html):
        print(item)
        writeToFile(item)


if __name__ == '__main__':
    for i in range(10):
        main(i * 10)
    # pool = Pool()
    # pool.map(main, [i * 10 for i in range(10)])