import requests
from bs4 import BeautifulSoup
url="https://movie.naver.com/movie/bi/mi/point.nhn?code=154255#tab"
result = requests.get(url)
soup = BeautifulSoup(result.text, "html.parser")

score_result = soup.find('dev', class_='score_result')

for li in score_result.find_all('li'):
    review = li.find('div', class_='score_reple').find('p').text
    print(review)

url_start ='https://movie.naver.com/movie/bi/mi/pointWriteFormList.nhn?code=154255&' \
           'type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready='\
          'false&isMileageSubscriptionReject=false&page='

url_page = 1

url = url_start + str(url_page)

reviews=[]
for page in range(1,30):
    url = url_start + str(url_page)

    result = requests.get(url)
    soup = BeautifulSoup(result.text, "html.parser")

    score_result = soup.find('dev', class_='score_result')

    for li in score_result.find_all('li'):
        review = li.find('div', class_='score_reple').find('p').text
        print(review)
        reviews.append(review)