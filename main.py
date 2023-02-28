import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances

search_query = str(input())
URL = f"https://www.google.com/search?q={search_query}&tbm=nws&start=0"
r = requests.get(URL)
soup = BeautifulSoup(r.text, 'html.parser')

news_headline = soup.find_all("div", class_="BNeawe vvjwJb AP7Wnd")
news_provider_title = soup.find_all("div", class_="BNeawe UPmit AP7Wnd")

news_whole_div = soup.find_all("div", class_="Gx5Zad fP1Qef xpd EtOod pkphOe")

for i in range(len(news_headline)):
    print(news_provider_title[i].text + ": " + news_headline[i].text)

# news_list = [str(i.text) for i in news_headline]
#
# final_list = [search_query] + news_list
#
#
# vectorizer = CountVectorizer()
# feature = vectorizer.fit_transform(final_list).todense()
# print(vectorizer.vocabulary_)
#
#
# for i in range(len(feature)):
#     print(euclidean_distances(feature[0], feature[i]), final_list[i])

    # Alia Bhatt and Ranbir Kapoor announce pregnancy, couple share 'our baby..coming soon'. Alia Bhatt and Ranbir Kapoor to welcome their first child together