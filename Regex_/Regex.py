import requests
import re
import time

def test_01():
    content = requests.get('https://book.douban.com/').text
    # print(content)
    # pattern = re.compile('<li.*?title="(.*?)".*?</li>', re.S)
    pattern = re.compile('<li.*?cover.*?href="(.*?)" title="(.*?)">', re.S)
    # pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?</li>', re.S)
    # pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author">(.*?)</span>.*?year">(.*?)</span>.*?</li>', re.S)
    print('start...')
    results = re.findall(pattern, content)
    print('end...')
    # print(results.group(1), results.group(2))
    # print(results.group(1).strip(), results.group(2).strip(), results.group(3).strip(), results.group(4))
    # print(results)
    for result in results:
        url, name = result
        print(url, name)

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
    test_01()