"""
📅 Kalender Tanam - Rice Planting Calendar
Season-based planting recommendations
"""

import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime, timedelta

st.set_page_config(page_title="Kalender Tanam", page_icon="📅", layout="wide")

st.title("📅 Kalender Tanam Padi")
st.markdown("**Rekomendasi waktu tanam berdasarkan musim dan pola hujan**")
st.markdown("---")

tab1, tab2, tab3 = st.tabs(["📅 Kalender", "🌧️ Pola Musim", "📊 Rekomendasi"])

with tab1:
    st.header("📅 Kalender Tanam Padi")
    
    # Input
    col1, col2 = st.columns(2)
    
    with col1:
        region = st.selectbox("Pilih Region", [
            "Jawa Barat", "Jawa Tengah", "Jawa Timur",
            "Sumatera Utara", "Sumatera Selatan",
            "Sulawesi Selatan", "Bali"
        ])
    
    with col2:
        irrigation = st.selectbox("Jenis Irigasi", [
            "Irigasi Teknis (Air Tersedia Sepanjang Tahun)",
            "Irigasi Sederhana (Tergantung Hujan)",
            "Tadah Hujan"
        ])
    
    st.markdown("---")
    
    # Planting calendar
    st.subheader("🗓️ Jadwal Tanam Optimal")
    
    if "Teknis" in irrigation:
        st.success("✅ **Irigasi Teknis:** Dapat tanam 2-3x per tahun")
        
        calendar_df = pd.DataFrame({
            'Musim Tanam': ['MT I (Musim Hujan)', 'MT II (Pancaroba)', 'MT III (Kemarau)'],
            'Bulan Tanam': ['Oktober - November', 'Februari - Maret', 'Juni - Juli'],
            'Bulan Panen': ['Februari - Maret', 'Juni - Juli', 'Oktober - November'],
            'Produktivitas': ['Tinggi (6-8 ton/ha)', 'Sedang (5-7 ton/ha)', 'Sedang (5-6 ton/ha)'],
            'Risiko': ['Rendah', 'Sedang (Hama)', 'Tinggi (Air)']
        })
    
    elif "Sederhana" in irrigation:
        st.warning("⚠️ **Irigasi Sederhana:** Dapat tanam 2x per tahun")
        
        calendar_df = pd.DataFrame({
            'Musim Tanam': ['MT I (Musim Hujan)', 'MT II (Pancaroba)'],
            'Bulan Tanam': ['Oktober - November', 'Februari - Maret'],
            'Bulan Panen': ['Februari - Maret', 'Juni - Juli'],
            'Produktivitas': ['Tinggi (6-7 ton/ha)', 'Sedang (5-6 ton/ha)'],
            'Risiko': ['Rendah', 'Sedang']
        })
    
    else:  # Tadah Hujan
        st.info("💧 **Tadah Hujan:** Hanya 1x per tahun (musim hujan)")
        
        calendar_df = pd.DataFrame({
            'Musim Tanam': ['MT I (Musim Hujan)'],
            'Bulan Tanam': ['Oktober - November'],
            'Bulan Panen': ['Februari - Maret'],
            'Produktivitas': ['Sedang (4-6 ton/ha)'],
            'Risiko': ['Tinggi (Kekeringan)']
        })
    
    st.dataframe(calendar_df, use_container_width=True, hide_index=True)
    
    # Timeline visualization
    st.subheader("📊 Timeline Tanam-Panen")
    
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'Mei', 'Jun', 'Jul', 'Agu', 'Sep', 'Okt', 'Nov', 'Des']
    
    if "Teknis" in irrigation:
        timeline_data = pd.DataFrame({
            'Bulan': months * 3,
            'Musim': ['MT I']*12 + ['MT II']*12 + ['MT III']*12,
            'Status': [
                '', '', 'Panen', '', '', '', '', '', '', 'Tanam', 'Tanam', '',  # MT I
                'Tanam', 'Tanam', '', '', '', 'Panen', 'Panen', '', '', '', '', '',  # MT II
                '', '', '', '', '', '', 'Tanam', '', '', 'Panen', 'Panen', ''  # MT III
            ]
        })
    else:
        timeline_data = pd.DataFrame({
            'Bulan': months * 2,
            'Musim': ['MT I']*12 + ['MT II']*12,
            'Status': [
                '', '', 'Panen', '', '', '', '', '', '', 'Tanam', 'Tanam', '',  # MT I
                'Tanam', 'Tanam', '', '', '', 'Panen', 'Panen', '', '', '', '', ''  # MT II
            ]
        })
    
    # Filter only planting and harvest
    timeline_display = timeline_data[timeline_data['Status'] != '']
    
    if not timeline_display.empty:
        chart = alt.Chart(timeline_display).mark_bar().encode(
            x=alt.X('Bulan:N', title='Bulan', sort=months),
            y=alt.Y('Musim:N', title='Musim Tanam'),
            color=alt.Color('Status:N', scale=alt.Scale(domain=['Tanam', 'Panen'], range=['#4CAF50', '#FFC107'])),
            tooltip=['Bulan', 'Musim', 'Status']
        ).properties(
            title='Timeline Tanam-Panen Sepanjang Tahun',
            height=300
        )
        
        st.altair_chart(chart, use_container_width=True)

with tab2:
    st.header("🌧️ Pola Musim Indonesia")
    
    st.markdown("""
    ### Karakteristik Musim
    
    **Musim Hujan (Oktober - Maret):**
    - Curah hujan tinggi (200-400 mm/bulan)
    - Cocok untuk tanam padi sawah
    - Risiko banjir di dataran rendah
    - Hama/penyakit lebih aktif
    
    **Musim Kemarau (April - September):**
    - Curah hujan rendah (<100 mm/bulan)
    - Perlu irigasi memadai
    - Risiko kekeringan
    - Hama tikus meningkat
    
    **Pancaroba (Maret-April, September-Oktober):**
    - Peralihan musim
    - Curah hujan tidak menentu
    - Perlu monitoring cuaca
    """)
    
    # Rainfall pattern
    rainfall_df = pd.DataFrame({
        'Bulan': months,
        'Curah Hujan (mm)': [350, 300, 250, 150, 100, 80, 60, 50, 80, 150, 250, 350]
    })
    
    rainfall_chart = alt.Chart(rainfall_df).mark_area(
        line={'color': '#1976D2'},
        color=alt.Gradient(
            gradient='linear',
            stops=[alt.GradientStop(color='white', offset=0),
                   alt.GradientStop(color='#1976D2', offset=1)],
            x1=0, x2=0, y1=1, y2=0
        )
    ).encode(
        x=alt.X('Bulan:N', title='Bulan', sort=months),
        y=alt.Y('Curah Hujan (mm):Q', title='Curah Hujan (mm)'),
        tooltip=['Bulan', 'Curah Hujan (mm)']
    ).properties(
        title='Pola Curah Hujan Rata-rata',
        height=300
    )
    
    st.altair_chart(rainfall_chart, use_container_width=True)

with tab3:
    st.header("📊 Rekomendasi Tanam")
    
    st.subheader("✅ Waktu Tanam Terbaik")
    
    col_rec1, col_rec2 = st.columns(2)
    
    with col_rec1:
        st.markdown("""
        ### MT I (Oktober-November)
        **Keunggulan:**
        - Air melimpah dari hujan
        - Produktivitas tertinggi
        - Biaya irigasi rendah
        
        **Risiko:**
        - Banjir (dataran rendah)
        - Hama/penyakit aktif
        - Harga jual rendah (panen massal)
        
        **Rekomendasi:**
        ✅ Sangat direkomendasikan untuk semua jenis irigasi
        """)
    
    with col_rec2:
        st.markdown("""
        ### MT II (Februari-Maret)
        **Keunggulan:**
        - Cuaca masih mendukung
        - Harga jual lebih baik
        - Hama lebih terkendali
        
        **Risiko:**
        - Perlu irigasi tambahan
        - Produktivitas sedikit turun
        
        **Rekomendasi:**
        ✅ Direkomendasikan untuk irigasi teknis/sederhana
        """)
    
    st.markdown("---")
    
    st.subheader("💡 Tips Pemilihan Waktu Tanam")
    
    tips = [
        "**Tanam serentak** dalam satu hamparan untuk kendalikan hama",
        "**Perhatikan prakiraan cuaca** sebelum tanam",
        "**Hindari tanam** saat puncak musim kemarau (Juli-Agustus)",
        "**Koordinasi dengan kelompok tani** untuk jadwal tanam bersama",
        "**Pilih varietas** sesuai umur tanam dan musim",
        "**Siapkan cadangan air** untuk musim kemarau"
    ]
    
    for tip in tips:
        st.info(tip)

st.markdown("---")
st.success("💡 **Kesimpulan:** Waktu tanam optimal adalah Oktober-November (MT I) untuk semua jenis irigasi")
