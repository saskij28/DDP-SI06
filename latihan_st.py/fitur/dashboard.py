import streamlit as st

st.title("halaman dashboard")
st.image("jeongwoo.jpg", caption="jo")

def total():
    total_tabung = sum(t["jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["tipe"] == "Menabung")
    total_penarikan = sum(t["jumlah"]
                       for t in st.session_state ["total_semua"]
                       if t ["tipe"] == "Penarikan")
    saldo = total_nabung - total_penarikan, saldo
    
    return total_tabung, total_penarikan, saldo

total_semua = st.session_state["total_semua"]
total_nabung, total_penarikan, saldo = total()

st.metric("total menabung", f"Rp. {total_nabung}")
st.metric("total Penarikan", f"Rp. {total_penarikan}")
st.metric("sisa saldo", f"Rp. {saldo}")