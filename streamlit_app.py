import streamlit as st
import requests

# NewsAPI 키 (NewsAPI에서 발급받은 API 키를 여기에 입력)
api_key = 'e19c176dce9e444b8d78ca264f87468d'

# ESG 관련 뉴스 가져오는 함수
def get_esg_news():
    url = f'https://newsapi.org/v2/everything?q=ESG&language=ko&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200 and 'articles' in data:
        return data['articles'][:5]  # 최신 5개의 뉴스 기사만 반환
    else:
        return []

# Streamlit 앱 인터페이스 설정
st.title('오늘의 ESG 뉴스')

# ESG 뉴스 가져오기 버튼
if st.button('실시간 ESG 뉴스 가져오기'):
    articles = get_esg_news()
    
    if articles:
        for i, article in enumerate(articles):
            st.subheader(f"{i + 1}. {article['title']}")
            st.write(f"출처: {article['source']['name']}")
            st.write(f"링크: {article['url']}")
            st.write()
    else:
        st.write("ESG 관련 뉴스가 없습니다.")

        
