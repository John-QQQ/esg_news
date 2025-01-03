import streamlit as st
import requests
from beautifulsoup4 import BeautifulSoup

# 네이버 뉴스 크롤링
def get_naver_news(query):
    url = f"https://search.naver.com/search.naver?&where=news&query={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', {'class': 'news_tit'})
    news = []
    for article in articles[:5]:
        news.append({'title': article['title'], 'url': article['href']})
    return news

# 다음 뉴스 크롤링
def get_daum_news(query):
    url = f"https://search.daum.net/search?w=news&DA=PGD&enc=utf8&q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', {'class': 'f_link_b'})
    news = []
    for article in articles[:5]:
        news.append({'title': article['title'], 'url': article['href']})
    return news

# CNN 뉴스 크롤링
def get_cnn_news(query):
    url = f"https://edition.cnn.com/search?q={query}&size=10"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('h3', {'class': 'cnn-search__result-headline'})
    news = []
    for article in articles[:5]:
        news.append({'title': article.get_text(), 'url': 'https://edition.cnn.com' + article.a['href']})
    return news

# BBC 뉴스 크롤링
def get_bbc_news(query):
    url = f"https://www.bbc.com/search?q={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', {'class': 'css-1g8txd7'})
    news = []
    for article in articles[:5]:
        news.append({'title': article.get_text(), 'url': 'https://www.bbc.com' + article['href']})
    return news

# Reuters 뉴스 크롤링
def get_reuters_news(query):
    url = f"https://www.reuters.com/search/news?blob={query}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    articles = soup.find_all('a', {'class': 'search-result-indiv-link'})
    news = []
    for article in articles[:5]:
        news.append({'title': article.get_text(), 'url': 'https://www.reuters.com' + article['href']})
    return news

# Streamlit 앱 설정
st.title("ESG 뉴스 크롤링")

# 사용자 입력 받기
query = st.text_input("검색어를 입력하세요 (예: ESG)", "ESG")

# 뉴스 크롤링 버튼
if st.button('국내 뉴스 보기'):
    st.subheader("국내 뉴스")
    # 네이버 뉴스와 다음 뉴스 크롤링
    naver_news = get_naver_news(query)
    daum_news = get_daum_news(query)
    
    for i, article in enumerate(naver_news):
        st.markdown(f"{i+1}. [{article['title']}]({article['url']})")
        
    for i, article in enumerate(daum_news):
        st.markdown(f"{i+1}. [{article['title']}]({article['url']})")

if st.button('국외 뉴스 보기'):
    st.subheader("국외 뉴스")
    # CNN, BBC, Reuters 뉴스 크롤링
    cnn_news = get_cnn_news(query)
    bbc_news = get_bbc_news(query)
    reuters_news = get_reuters_news(query)
    
    for i, article in enumerate(cnn_news):
        st.markdown(f"{i+1}. [{article['title']}]({article['url']})")
        
    for i, article in enumerate(bbc_news):
        st.markdown(f"{i+1}. [{article['title']}]({article['url']})")
        
    for i, article in enumerate(reuters_news):
        st.markdown(f"{i+1}. [{article['title']}]({article['url']})")
