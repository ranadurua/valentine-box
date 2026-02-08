import streamlit as st

st.set_page_config(page_title="Bir Hediye 💜", layout="centered")

st.markdown(
    """
    <style>
    body {
        background-color: #1a001a;
    }
    .box {
        width: 200px;
        height: 200px;
        background-color: #5a001a;
        margin: auto;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 20px;
        cursor: pointer;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🎁")

if "opened" not in st.session_state:
    st.session_state.opened = False

if not st.session_state.opened:
    if st.button("KUTUYU AÇ"):
        name = st.text_input("İsmini gir")
        if name == "İLKER":
            st.session_state.opened = True
        elif name != "":
            st.error("Yanlış isim 😛")
else:
    st.success("💐")
    st.markdown("### 💜 Büyük Mor Bir Buket 💜")
    if st.button("💌 Zarfı Aç"):
        st.write("**senin için hazırlandııı<3 -Duru**")
