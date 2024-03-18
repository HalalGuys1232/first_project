from today import Today
import pandas as pd
import datetime
import time
import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

# 한글 폰트 경로 직접 지정
font_path = "c:/Windows/Fonts/malgun.ttf"  # 'malgun.ttf'는 '맑은 고딕' 폰트의 파일명입니다. 시스템에 따라 경로가 다를 수 있으니 확인이 필요합니다.
font_name = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font_name)




today_debt = Today()
if __name__ == "__main__":

    st.title("국가부채 이대로 괜찮아보이십니까?")

tab1, tab2, tab3 = st.tabs(["연도별 국가 채무 추이", "건전재정은 왜 필요한가?", "실시간 국가 채무"])

# Streamlit에서 사용할 경우, tab1과 같은 컨텍스트 내부에 코드를 넣어주세요.
with tab1:
    tab1.subheader("국가 채무 추이 (1997 - 2022)")
    total_Debt_data = today_debt.important_debt_data[['기준년도', '국가채무총계(조원)']]
    # '기준년도' 열을 숫자로 변환
    total_Debt_data.loc[:, '기준년도'] = pd.to_numeric(total_Debt_data['기준년도'], errors='coerce')
    # '국가채무총계(조원)' 열을 숫자로 변환
    total_Debt_data.loc[:, '국가채무총계(조원)'] = pd.to_numeric(total_Debt_data['국가채무총계(조원)'], errors='coerce')

    # Pandas의 plot 메서드를 사용하여 그래프 그리기
    # 기준년도를 인덱스로 설정
    total_Debt_data.set_index('기준년도', inplace=True)
    fig, ax = plt.subplots()
    total_Debt_data.plot(ax=ax)

    # x축의 범위 설정
    plt.xlim(1997, 2022) # 여기서는 1997년부터 2022년까지로 설정

    # 그래프 제목과 축 이름 설정
    plt.title('total National debt (1997 - 2022)')
    plt.xlabel('year')
    plt.ylabel('total National debt')

    # Streamlit에 그래프 표시
    tab1.pyplot(fig)

   
with tab2:
     st.header("건전재정은 왜 필요한가")  
     st.text("건전해야하기때문입니다.")


with tab3:
    today_debt.update_results(today_debt.start_time, today_debt.recent_debt_won_sec, today_debt.recent_debt_percent_sec, today_debt.important_debt_data)

