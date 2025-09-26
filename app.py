import streamlit as st
from pathlib import Path

# 이미지 폴더 경로
img_path = Path("img")

# 1줄, 2줄, 3줄 이미지 및 이름 리스트
row1 = ["루테인.jpg", "비타D.jpg", "활성엽산.jpg", "이뮨베타원.jpg"]
row2 = ["수분크림.jpg", "스카더마겔.jpg", "젤클린저.jpg", "페미라이드.jpg"]
row3 = ["방수담요.png", "스와들.jpg", "아기담요.jpg", "쿠션.png"]

# Streamlit 페이지 설정
st.set_page_config(page_title="임산부 쇼핑몰", layout="wide")

# 상단: 제목
st.markdown("<h1 style='margin-bottom:0'>임산부를 위한 쇼핑몰</h1>", unsafe_allow_html=True)

# 이름, 나이, 쿠폰 적용 여부 입력
st.markdown("### 고객 정보 입력")
col_name, col_age, col_coupon = st.columns([1,1,1])
name = col_name.text_input("이름")
age = col_age.text_input("나이", value="30")  # 기본값 30, 직접 입력 가능
coupon_status = col_coupon.selectbox("쿠폰 적용 여부", options=["O", "X"])  # O=적용, X=미적용

# 안내 문구 중앙 표시
st.markdown("<p style='text-align:center; font-weight:bold; font-size:18px; margin-top:10px;'>관심있는 상품의 이미지를 클릭해주세요</p>", unsafe_allow_html=True)

# 상품 표시 함수
def display_row(row_files):
    cols = st.columns(len(row_files))
    for idx, file_name in enumerate(row_files):
        img_file = img_path / file_name
        cols[idx].image(str(img_file), use_container_width=True)
        cols[idx].markdown(f"<p style='text-align:center'>{img_file.stem}</p>", unsafe_allow_html=True)

# 상품 3줄 표시
display_row(row1)
display_row(row2)
display_row(row3)


