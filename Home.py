import streamlit as st
import base64

st.set_page_config(page_title="PhonePe Pulse", layout="wide")

with st.container():
    img_col, tit_col = st.columns(2)
    with img_col:
        file_ = open("Images/phonepe_map.png", "rb")
        contents = file_.read()
        data_url = base64.b64encode(contents).decode("utf-8")
        file_.close()
        st.markdown(f'<img src="data:image/png; base64,{data_url}" alt="data png" width=85%>',unsafe_allow_html=True,)
    with tit_col:
        st.title(":violet[PhonePe Pulse]")
        st.write("The Indian digital payments story has truly captured the world's imagination. From the largest towns to the remotest villages, there is a payments revolution being driven by the penetration of mobile phones and data.")
        st.write("PhonePe Pulse is your window to the world of how India transacts with interesting trends, deep insights and in-depth analysis based on our data put together by the PhonePe team.")
        st.write("This year as we became India's largest digital payments platform with 46% UPI market share, we decided to demystify the what, why and how of digital payments in India.")