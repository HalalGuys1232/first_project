# first_project
# 프로젝트 개발 사유
얼마전 모든 선진국들의 부채가 매우 높다는 뉴스를 보고, 경각심을 가질 필요가 있다고 생각함.
경각심을 가지게 할 수 있는 수단으로 뭐가 있을까? 고민하던 중 기후 위기까지 남은 시간을 실시간으로 알려주는 기후 위기 시계를 보고,
국가채무를 실시간으로 갱신하는 기능을 가진 웹페이지를 만들기로 결심함.

# 기술적 난제
알고있는 웹 앱 기술은 streamlit 단 하나뿐인 상황이었음.
하지만 streamlit의 경우, 사용자의 버튼 클릭 등 상호작용이 있을 때, 갱신되고 반응하는 형태라 실시간으로 계속해서 갱신되어야하는 프로젝트에 해당 기술을 적용하기 힘들었음.
streamlit가 제공하는 디자인이나 그래프 등은 세밀하게 변경하기 힘듬.
유지보수를 위해 open api를 활용하여 월간 데이터를 주기적으로 갱신하고자 하였으나 json이나 xml에 대한 이해가 부족


# 해결 및 타협
open api로 월간 데이터를 받지 않고, csv파일로 되어있는 연간 데이터를 해당 레포지토리에 보관하는 방식을 채택.
그 결과 계절성 요인을 제거되었고, open api를 실시간으로 불러와 매초 or 매분마다 계산하는 방식의 경우 과도하게 api를 호출한다는 부작용을 회피할 수 있었음.
streamlit에서 기본적으로 제공하는 차트 관련 모듈 대신 mathplot 라이브러리에서 제공하는 모듈을 채택.
