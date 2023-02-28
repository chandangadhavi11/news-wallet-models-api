import requests
from bs4 import BeautifulSoup
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import euclidean_distances


search_query = input()
final_search_query = search_query.replace(" ", "-")
print(final_search_query)
url = f"https://timesofindia.indiatimes.com/topic/{final_search_query}"

r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')

news_container = soup.find_all("div", class_="EW1Mb _3v379")

final_news_list = [search_query] + [i.text[1:len(i.text)-1] for i in news_container]

vectorizer = CountVectorizer()
feature = vectorizer.fit_transform(final_news_list).todense()
print(vectorizer.vocabulary_)

for i in range(len(feature)):
    print(euclidean_distances(feature[0], feature[i]), final_news_list[i])