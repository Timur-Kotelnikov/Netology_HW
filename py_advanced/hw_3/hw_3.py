import requests
import bs4

url = 'https://habr.com/ru/all/'
keywords = ['дизайн', 'фото', 'web', 'python']
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/39.0.2171.95 Safari/537.36'}
article_set = set()
response = requests.get(url=url, headers=headers).text
soup = bs4.BeautifulSoup(markup=response, features='html.parser')
articles = soup.find_all('article')
for article in articles:
    for keyword in keywords:
        if article.find('h2').find('span').text.count(keyword) > 0:
            article_date = article.find(class_ = 'tm-article-snippet__datetime-published').find('time').attrs['title']
            article_title = article.find('h2').find('span').text
            article_link = 'https://habr.com/' + article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
            article_set.add(f'Date = {article_date}, title = {article_title}, link = {article_link}')
for article in articles:
    a = article.find(class_ = 'article-formatted-body article-formatted-body article-formatted-body_version-2')
    try:
        for keyword in keywords:
            if article.find(class_ = 'article-formatted-body article-formatted-body article-formatted-body_version-2').text.count(keyword) > 0:
                article_date = article.find(class_='tm-article-snippet__datetime-published').find('time').attrs['title']
                article_title = article.find('h2').find('span').text
                article_link = 'https://habr.com/' + article.find(class_ = 'tm-article-snippet__title-link').attrs['href']
                article_set.add(f'Date = {article_date}, title = {article_title}, link = {article_link}')
    except Exception:
        pass
print(article_set)
