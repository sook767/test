import streamlit as st

st.title("건강검사 테스트 페이지")

st.write("혈압을 입력하면 결과를 안내합니다.")

systolic = st.number_input("수축기 혈압", value=120)
diastolic = st.number_input("이완기 혈압", value=80)

if st.button("결과 보기"):
    if systolic >= 140 or diastolic >= 90:
        st.error("고혈압 범위입니다. 상담이 필요할 수 있습니다.")
    elif systolic >= 120 or diastolic >= 80:
        st.warning("주의 범위입니다. 관리가 필요합니다.")
    else:
        st.success("정상 범위입니다.")
