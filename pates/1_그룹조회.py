import streamlit as st

st.title("그룹 조회")

group_data = {
    "김수1234": {"group": "A그룹", "guide": "안내 페이지 참고"},
    "이희5678": {"group": "B그룹", "guide": "기간 내 진행"},
    "김숙5678": {"group": "B그룹", "guide": "기간 내 진행"},

  
}

name = st.text_input("이름")
number = st.text_input("번호")

def make_key(n, num):
    if len(n) == 3:
        return n[0] + n[2] + num
    return ""

if st.button("조회"):
    key = make_key(name, number)
    if key in group_data:
        st.success(group_data[key]["group"])
    else:
        st.error("없음")
