import streamlit as st

st.title("테스트")

st.write("이름과 번호를 입력하면 안내 그룹을 확인할 수 있습니다.")

# 👉 가짜 DB (10개 데이터)
group_data = {
    "김수1234": {"group": "A그룹", "guide": "test."},
    "이희5678": {"group": "B그룹", "guide": "test"},
    "박수1111": {"group": "C그룹", "guide": "test"},
    "최준2222": {"group": "A그룹", "guide": "test."},
    "정민3333": {"group": "B그룹", "guide": "test."},
    "한별4444": {"group": "C그룹", "guide": "test."},
    "오진5555": {"group": "A그룹", "guide": "test."},
    "유찬6666": {"group": "B그룹", "guide": "test."},
    "서현7777": {"group": "C그룹", "guide": "test."},
    "강우8888": {"group": "A그룹", "guide": "test."}
}

# 👉 입력칸 (가로 배치)
col1, col2 = st.columns(2)

with col1:
    name = st.text_input("이름 (3글자)")

with col2:
    number = st.text_input("번호")

# 👉 키 생성 함수 (이름 가운데 글자 제외)
def make_key(n, num):
    n = n.strip()
    num = num.strip()

    if len(n) != 3:
        return ""
    return n[0] + n[2] + num

# 👉 조회 버튼
if st.button("조회"):
    if not name or not number:
        st.warning("이름과 번호를 모두 입력하세요.")

    elif len(name.strip()) != 3:
        st.warning("이름은 3글자만 입력하세요.")

    elif not number.strip().isdigit():
        st.warning("번호는 숫자만 입력하세요.")

    else:
        key = make_key(name, number)

        if key in group_data:
            result = group_data[key]

           #  st.success("조회 완료")
            st.write(f"👉 안내 그룹: {result['group']}")
            st.info(result["guide"])

        else:
            st.error("일치하는 정보가 없습니다.")
