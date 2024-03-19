
import streamlit as st
import pandas as pd
import datetime
import time


debt_data = pd.read_csv("C:\\gitcode\\first_project\\D1_20240314.csv", encoding='utf-8')
 
debt_data.columns = ['No.', '기준년도', '국가채무총계(조원)', '국가채무 GDP대비(%)', '중앙정부채무(조원)', '국채 합계(조원)','국고채권(조원)', '국민주택채권(조원)', '외평채권(조원)', '차입금(조원)', '국고채무부담행위(조원)','지방정부순채무(조원)']
important_debt_data = debt_data.drop(['No.', '중앙정부채무(조원)', '국채 합계(조원)','국고채권(조원)', '국민주택채권(조원)', '외평채권(조원)', '차입금(조원)', '국고채무부담행위(조원)','지방정부순채무(조원)'],axis=1)
important_debt_data['국가채무총계(조원)'] = debt_data['국가채무총계(조원)'].astype(str)
important_debt_data['국가채무총계(조원)'] = debt_data['국가채무총계(조원)'].str.replace(",","")
important_debt_data['국가채무 GDP대비(%)'] = debt_data['국가채무 GDP대비(%)'].astype(str)
important_debt_data['국가채무총계(조원)'] = debt_data['국가채무총계(조원)'].str.replace(",","")
recent_debt_won = float(important_debt_data.loc[0,'국가채무총계(조원)']) - float(important_debt_data.loc[1,'국가채무총계(조원)'])
recent_debt_percent = float(important_debt_data.loc[0,'국가채무 GDP대비(%)']) - float(important_debt_data.loc[1,'국가채무 GDP대비(%)'])
year_sec = 365 * 24 * 60 * 60


class Today:
    def __init__(self):
        self.start_time = datetime.datetime(2023, 1, 1, 0, 0, 0) 
        self.recent_debt_won_sec = recent_debt_won / year_sec
        self.recent_debt_percent_sec = recent_debt_percent / year_sec
        self.important_debt_data = important_debt_data

    def format_number_with_jo(value):
    # 조와 억 단위로 나누어서 포맷팅합니다.
        jo = int(value // 10000)  # '조' 단위를 계산합니다.
        eok = round(value % 10000,2)  # 남은 '억' 단위를 계산합니다.
    # 조 단위가 0이 아닐 경우 '조'와 '억'을 함께 포맷팅합니다.
        if jo > 0:
            formatted_number = f"{jo}조 {eok}억원"
        else:
            formatted_number = f"{eok}억원"
    
        return formatted_number


    def debt_realtime_clock(self, start_time, recent_debt_won_sec, important_debt_data):
        # 무한 루프로 매초마다 값을 갱신
        while True:
            # 현재 시간 가져오기
            now_time= datetime.datetime.now()
            # 지난 초 계산
            passed_time = (now_time - start_time).total_seconds()

           # 계산식 적용
            debt_won_result = (float(passed_time * recent_debt_won_sec) + float(important_debt_data.loc[0,'국가채무총계(조원)']))*10000
            formatted_won_result = Today.format_number_with_jo(debt_won_result)
            # 결과값 출력
            return formatted_won_result


    def debt_realtime_percent(self, start_time, recent_debt_percent_sec, important_debt_data):
        # 무한 루프로 매초마다 값을 갱신
        while True:
            # 현재 시간 가져오기
            now_time= datetime.datetime.now()
            # 지난 초 계산
            passed_time = (now_time - start_time).total_seconds()

            # 계산식 적용
            debt_percent_result = float(passed_time * recent_debt_percent_sec) + float(important_debt_data.loc[0,'국가채무 GDP대비(%)'])

            # 결과값 출력
            return debt_percent_result
        

    def update_results(self, start_time, recent_debt_won_sec, recent_debt_percent_sec, important_debt_data):
        # 페이지 설정
        st.header("실시간 GDP 대비 국가채무", divider='red')
        debt_percent_placeholder = st.empty()
        st.header("실시간 대한민국 국가채무", divider='red')
        debt_won_placeholder = st.empty()
        st.image('tab3_1.jpg', caption='2021년 당시 정부 전망 국가 채무')

        while True:
            debt_percent_result = self.debt_realtime_percent(start_time, recent_debt_percent_sec, important_debt_data)
            formatted_won_result = self.debt_realtime_clock(start_time, recent_debt_won_sec, important_debt_data)

            debt_percent_placeholder.subheader(f"현재 GDP 대비 국가 채무는 {debt_percent_result:.2f}%입니다.")
            debt_won_placeholder.subheader(f"현재 국가채무 총계는: {formatted_won_result}입니다.")

            time.sleep(3)  # 3초마다 결과를 업데이트
