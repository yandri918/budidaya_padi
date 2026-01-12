"""
🌾 Budidaya Padi - Rice Cultivation Management System
Comprehensive application for rice farming with AI, ML, and advanced analytics
"""

import streamlit as st
import pandas as pd
import altair as alt
from datetime import datetime
import time
import random

# Page config
st.set_page_config(
    page_title="AgriSensa Padi",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dashboard
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #2E7D32;
        --secondary-color: #558B2F;
        --accent-color: #FDD835;
        --card-bg: #FFFFFF;
        --bg-color: #F8F9FA;
    }
    
    .stApp {
        background-color: var(--bg-color);
    }
    
    /* Dashboard Header */
    .dashboard-header {
        background: linear-gradient(135deg, #2E7D32 0%, #1B5E20 100%);
        padding: 2rem;
        border-radius: 16px;
        color: white;
        margin-bottom: 2rem;
        box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    }
    
    .dashboard-header h1 {
        color: white !important;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .weather-widget {
        background: rgba(255, 255, 255, 0.2);
        padding: 10px 20px;
        border-radius: 12px;
        display: inline-block;
        backdrop-filter: blur(5px);
        margin-top: 10px;
    }

    /* Cards */
    .stat-card {
        background-color: var(--card-bg);
        border-radius: 12px;
        padding: 1.5rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        border-left: 5px solid var(--primary-color);
        transition: transform 0.2s;
    }
    
    .stat-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 15px rgba(0,0,0,0.1);
    }
    
    .alert-card {
        background-color: #FFF3E0;
        border-left: 5px solid #FF9800;
        padding: 1rem;
        border-radius: 8px;
        color: #E65100;
        margin-bottom: 1rem;
    }

    /* Price Ticker */
    .price-ticker {
        background-color: #E8F5E9;
        color: #2E7D32;
        padding: 10px;
        border-radius: 8px;
        font-weight: bold;
        text-align: center;
        margin-bottom: 20px;
        border: 1px solid #C8E6C9;
    }
    
    /* Feature Buttons */
    .feature-btn {
        text-align: center;
        padding: 20px;
        background: white;
        border-radius: 12px;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        cursor: pointer;
        border: 1px solid #eee;
    }
    
    .feature-btn h3 {
        font-size: 1.1rem;
        margin-top: 10px;
        color: #333;
    }
    
    .feature-btn:hover {
        border-color: #2E7D32;
        background-color: #F1F8E9;
    }

</style>
""", unsafe_allow_html=True)

# Helper for Time Greeting
def get_greeting():
    hour = datetime.now().hour
    if 5 <= hour < 11: return "Sugeng Enjang (Selamat Pagi)"
    elif 11 <= hour < 15: return "Sugeng Siang (Selamat Siang)"
    elif 15 <= hour < 18: return "Sugeng Sonten (Selamat Sore)"
    else: return "Sugeng Dalu (Selamat Malam)"

# Helper for Primbon
def get_pasaran():
    epoch = datetime(2024, 1, 1) # Monday Pahing
    today = datetime.now()
    delta = (today - epoch).days
    pasarans = ["Pahing", "Pon", "Wage", "Kliwon", "Legi"]
    return pasarans[delta % 5]

# --- DASHBOARD CONTENT ---

# Initialize services
import sys
from pathlib import Path
if str(Path(__file__).parent) not in sys.path:
    sys.path.append(str(Path(__file__).parent))

from services.market_service import MarketService

@st.cache_data(ttl=3600) # Cache for 1 hour
def fetch_market_data():
    service = MarketService()
    return service.get_rice_prices()

market_data = fetch_market_data()

# 1. Header Section
greeting = get_greeting()
pasaran = get_pasaran()
today_str = datetime.now().strftime("%A, %d %B %Y")

st.markdown(f"""
<div class='dashboard-header'>
    <h1>🌾 {greeting}, Pak Tani!</h1>
    <p>Selamat datang di Command Center AgriSensa. Mari cek kondisi lahan hari ini.</p>
    <div class='weather-widget'>
        📅 {today_str} • 🕉️ {pasaran} • ⛅ Cerah Berawan (28°C)
    </div>
</div>
""", unsafe_allow_html=True)

# 2. Main Metrics & Alerts
col_alert, col_market = st.columns([2, 1])

with col_alert:
    # Pranata Mangsa Alert (Simulated logic from Calendar Module)
    st.markdown("""
    <div class='alert-card'>
        <strong>⚠️ Peringatan Dini (Mangsa Kalima):</strong><br>
        Curah hujan mulai tinggi. Waspada serangan <strong>Wereng Coklat</strong> dan penyakit <strong>Blas</strong>. 
        Segera cek drainase sawah!
    </div>
    """, unsafe_allow_html=True)
    
    # Financial Summary (Mock from Logbook)
    st.markdown("### 💰 Status Keuangan Bulan Ini")
    f_col1, f_col2, f_col3 = st.columns(3)
    f_col1.metric("Pengeluaran", "Rp 1.500.000", "Pupuk & Upah")
    f_col2.metric("Pemasukan (Est)", "Rp 0", "-")
    f_col3.metric("Saldo Kas", "Rp 8.500.000", "Aman")

with col_market:
    # Build dynamic HTML for prices
    gkp = market_data['gkp']
    beras = market_data['beras_medium']
    
    gkp_arrow = "▲" if gkp['change'] >= 0 else "▼"
    gkp_color = "green" if gkp['change'] >= 0 else "red"
    
    beras_arrow = "▲" if beras['change'] >= 0 else "▼"
    beras_color = "green" if beras['change'] >= 0 else "red"
    
    st.markdown("### 📈 Harga Pasar (Live)")
    st.markdown(f"""
    <div class='price-ticker'>
        🌾 GKP (Gabah Kering Panen)<br>
        <span style='font-size: 1.5rem'>Rp {gkp['price']:,.0f} / kg</span><br>
        <span style='color: {gkp_color}'>{gkp_arrow} Rp {abs(gkp['change']):,.0f} (Hari ini)</span>
    </div>
    <div class='price-ticker'>
        🍚 Beras Medium<br>
        <span style='font-size: 1.5rem'>Rp {beras['price']:,.0f} / kg</span><br>
        <span style='color: {beras_color}'>{beras_arrow} Rp {abs(beras['change']):,.0f} (Hari ini)</span>
    </div>
    """, unsafe_allow_html=True)
    st.caption("Sumber: Bapanas (Nasional)")

# 3. Quick Actions Grid
st.markdown("---")
st.header("🚀 Menu Cepat (Quick Actions)")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown("### 🧪 Analisis")
    st.info("Cek status hara tanah & rekomendasi pupuk")
    st.image("https://img.icons8.com/color/96/soil-analysis.png", width=60)
    st.markdown("**Module 10: Analisis Tanah**")

with c2:
    st.markdown("### 🐛 Dokter Tanaman")
    st.info("Identifikasi hama & cari obatnya")
    st.image("https://img.icons8.com/color/96/bug.png", width=60)
    st.markdown("**Module 03: Hama & Penyakit**")

with c3:
    st.markdown("### 🗓️ Kalender")
    st.info("Cek hari baik & jadwal tanam")
    st.image("https://img.icons8.com/color/96/calendar.png", width=60)
    st.markdown("**Module 06: Kalender Tanam**")

with c4:
    st.markdown("### 📝 Jurnal")
    st.info("Catat pengeluaran & kegiatan hari ini")
    st.image("https://img.icons8.com/color/96/notebook.png", width=60)
    st.markdown("**Module 12: Logbook**")

# 4. Chart Visualization (Mini Dashboard)
st.markdown("---")
st.header("📊 Tren Pertumbuhan & Cuaca")

chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    # Dummy Growth Data
    growth_data = pd.DataFrame({
        'HST': [10, 20, 30, 40, 50],
        'Tinggi (cm)': [15, 25, 45, 60, 85]
    })
    
    chart = alt.Chart(growth_data).mark_line(point=True, color='#2E7D32').encode(
        x='HST',
        y='Tinggi (cm)',
        tooltip=['HST', 'Tinggi (cm)']
    ).properties(title="Grafik Tinggi Tanaman (Petak A)")
    st.altair_chart(chart, use_container_width=True)

with chart_col2:
    # Mock Weather Forecast
    weather_df = pd.DataFrame({
        'Hari': ['Sen', 'Sel', 'Rab', 'Kam', 'Jum'],
        'Peluang Hujan (%)': [80, 60, 20, 10, 40],
        'Suhu (°C)': [27, 28, 30, 31, 29]
    })
    
    bar = alt.Chart(weather_df).mark_bar(color='#90CAF9').encode(
        x=alt.X('Hari', sort=None),
        y='Peluang Hujan (%)',
        tooltip=['Hari', 'Peluang Hujan (%)']
    ).properties(title="Prakiraan Hujan 5 Hari Kedepan")
    st.altair_chart(bar, use_container_width=True)

# Footer
st.markdown("---")
st.caption("© 2026 AgriSensa Padi - Sistem Cerdas Sahabat Petani")
