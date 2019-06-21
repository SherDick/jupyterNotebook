import requests
import re

def test_02():
    content = requests.get('https://book.douban.com/').text
    pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
    results = re.findall(pattern, content)
    for result in results:
        url, name, author, date = result
        author = re.sub('\s', '', author)
        date = re.sub('\s', '', date)
        print(url, name, author, date)

if __name__ == '__main__':
    test_02()
