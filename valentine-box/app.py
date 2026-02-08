import streamlit as st

st.set_page_config(page_title="Sürpriz 🎁", layout="centered")

# Session state başlat
if "opened" not in st.session_state:
    st.session_state.opened = False

st.title("💝 Sana Küçük Bir Sürpriz 💝")

if not st.session_state.opened:
    name = st.text_input("İsmini yazar mısın? 💌")

    if st.button("Hediyeyi Aç 🎁"):
        if name.strip() == "":
            st.warning("Ama isim olmadan olmaz ki 🥺")
        else:
            st.session_state.name = name
            st.session_state.opened = True
            st.rerun()

else:
    st.success(f"Hoş geldin {st.session_state.name} 💖")
    st.markdown("### 🌸 Bu buket sadece sana 🌸")
    st.markdown("💐💐💐💐💐")
    st.markdown("💐💖💐💖💐")
    st.markdown("💐💐💐💐💐")
