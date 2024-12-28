import streamlit as st

st.title("halaman menabung")

#formuir input
with st.form("menabung"):
    nama = st.text_input("nama")
    jumlah = st.number_input("Jumlah (Rp.)", min_value=0, step=1000)
    tanggal = st.date_input("Tanggal")
    waktu = st.time_input("Waktu")
    submit_button = st.form_submit_button (label="menabung")

if submit_button and jumlah >= 50000:
    st.session_state["total_semua"].append({
        "Tipe" : "Menabung",
        "jumlah" : jumlah
    })
    st.success("menabung berhasil")
else:
    st.error("menabung gagal")

