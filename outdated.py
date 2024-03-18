# 한국판 부채 시계 만들기
# 재정열림 api 가져오기
# ㄴ국가 총 부채 가져오기(실시간)
# ㄴ 실시간 변화를 위해서 변화량 측정 값이 필요함
#(최대한 짧은 주기로 기록된 최신 부채데이터- 바로 전 주기의 부채데이터)
# ---------------------------------------------------------------- = 이 수치만큼 초마다 올라가는걸로 하자
# 해당 주기의 시간
#
# ㄴ MBS의 증가규모 가져오기(2000년도와 지금 비교)
# 인베스팅 닷컴 api 가져오기
#(해당 사이트에선 api를 제공치 않음. investpy 패키지로 정정)
# ㄴ 원유가격 (2000년도 원유가와 지금가격의 비율 비교)
# ㄴ 금가격 (2000년도 금은가격과 지금가격 비율 비교)
#import streamlit as st
#st.markdown("""
#    <style>
#    .title {
#        text-align: center;
#    }
#    </style>
#    <h1 class="title">Korea Debt clock</h1>
#    """, unsafe_allow_html=True)

#import numpy as np
#import pandas as pd
#import datetime
#import requests
#import xmltodict
#import json
#from dotenv import dotenv_values
#datetime.datetime.today()
#datetime.datetime.now()


#def get_government_debt_year(year):
    # API 요청 URL
#    URL = "https://openapi.openfiscaldata.go.kr/GovernmentDebtYear"
    
    # .env 파일에서 API 키 불러오기
#    config = dotenv_values('.env')
#    korean_debt_api = config.get('korean_debt_key')
#    if not korean_debt_api:
#        return "API 키를 찾을 수 없습니다."

    # 요청 인자 설정
#    params = {
#        'Key': korean_debt_api,  # 인증키
#        'Type': 'xml',  
#        'pIndex': 1,  # 페이지 위치
#        'pSize': 100,  # 페이지 당 요청 숫자
#        'OJ_YY': year,  # 기준년도
#    }
    
    # API 요청
#    response = requests.get(URL, params=params)
    
    # 요청 성공 여부 확인
#    if response.status_code == 200:
        # XML을 JSON으로 변환
#        debt_data_dict = xmltodict.parse(response.content)
#        return debt_data_dict
#    else:
#        return "API 요청에 실패했습니다. 상태 코드: {}".format(response.status_code)

#def find_recent_year_data():
#    today = datetime.date.today()
#    now_year = today.year
#    recent_year = now_year - 1
#    recent_debt = None
#    previous_debt = None





#def find_recent_year_data():
#    current_year = datetime.date.today()
#    recent_year = current_year - 1  # 가장 최근 완료된 년도
#    recent_debt = previous_debt = None

#    while recent_year >= current_year - 3:  # 최대 3년 전까지만 확인
#        if not recent_debt:
#            recent_debt = get_government_debt_year(recent_year)
#        elif not previous_debt:
#            previous_debt = get_government_debt_year(recent_year)
#            break  # 두 데이터를 모두 찾았으니 반복을 종료합니다.
#        recent_year -= 1

#    if recent_debt and previous_debt:
#        print(f"가장 최근년도 부채 총액: {recent_debt}, 이전년도 부채 총액: {previous_debt}")
#    else:
#        print("필요한 데이터를 찾지 못했습니다.")
#    return