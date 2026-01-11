"""
🌾 Budidaya Padi - Rice Cultivation Management System
Comprehensive application for rice farming with AI, ML, and advanced analytics
"""

import streamlit as st
from datetime import datetime

# Page config
st.set_page_config(
    page_title="Budidaya Padi",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for design system
st.markdown("""
<style>
    /* Main theme colors */
    :root {
        --primary-color: #2E7D32;
        --secondary-color: #558B2F;
        --accent-color: #FDD835;
        --background: #F1F8E9;
    }
    
    /* Header styling */
    .main-header {
        background: linear-gradient(135deg, #2E7D32 0%, #558B2F 100%);
        padding: 2rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1 {
        margin: 0;
        font-size: 2.5rem;
        font-weight: 700;
    }
    
    .main-header p {
        margin: 0.5rem 0 0 0;
        font-size: 1.1rem;
        opacity: 0.9;
    }
    
    /* Card styling */
    .info-card {
        background: white;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #2E7D32;
        margin: 1rem 0;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #F1F8E9 0%, #DCEDC8 100%);
        padding: 1.5rem;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #2E7D32;
    }
    
    /* Sidebar styling */
    .css-1d391kg {
        background-color: #F1F8E9;
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #2E7D32 0%, #558B2F 100%);
        color: white;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 2rem;
        font-weight: 600;
        transition: all 0.3s;
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(46, 125, 50, 0.3);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
    }
    
    .stTabs [data-baseweb="tab"] {
        background-color: #E8F5E9;
        border-radius: 8px 8px 0 0;
        padding: 10px 20px;
        font-weight: 600;
    }
    
    .stTabs [aria-selected="true"] {
        background: linear-gradient(135deg, #2E7D32 0%, #558B2F 100%);
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.markdown("""
    <div style='text-align: center; padding: 1rem;'>
        <h1 style='color: #2E7D32; margin: 0;'>🌾</h1>
        <h2 style='color: #2E7D32; margin: 0.5rem 0;'>Budidaya Padi</h2>
        <p style='color: #666; font-size: 0.9rem;'>Rice Cultivation Management</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Module categories
    st.markdown("### 📊 Modul Utama")
    st.info("""
    **Pilih modul dari menu Pages di atas** ⬆️
    
    Atau gunakan navigasi di bawah:
    """)
    
    with st.expander("💰 Perencanaan & Keuangan"):
        st.markdown("""
        - 📋 RAB Calculator
        - 📊 Analisis Bisnis
        - 💰 ROI & Financial Analysis
        """)
    
    with st.expander("🌾 Budidaya & Teknis"):
        st.markdown("""
        - 📚 Panduan Budidaya
        - 🌾 Varietas Padi
        - 📋 SOP Lengkap
        - 🧪 Kalkulator Pupuk
        - 💧 Manajemen Air
        """)
    
    with st.expander("🐛 Hama & Penyakit"):
        st.markdown("""
        - 🐛 Database Hama & Penyakit
        - 💦 Strategi Penyemprotan
        - 📸 Deteksi Penyakit AI
        """)
    
    with st.expander("📈 Monitoring & Prediksi"):
        st.markdown("""
        - 📏 Pantau Pertumbuhan
        - 📈 Prediksi Harga
        - 🌡️ Monitoring Cuaca
        - 📅 Kalender Tanam
        """)
    
    with st.expander("🤖 AI & Machine Learning"):
        st.markdown("""
        - 🤖 AI Saran
        - 🔬 PyCaret ML Lab
        - 📊 Analytics Hub
        """)
    
    with st.expander("📊 Visualisasi & Analitik"):
        st.markdown("""
        - 📊 Visualisasi Altair
        - 📊 Statistik Penelitian
        - 📊 Dashboard & Reports
        """)
    
    with st.expander("📔 Dokumentasi"):
        st.markdown("""
        - 📔 Jurnal Harian
        - 📊 Dashboard & Reports
        """)
    
    st.markdown("---")
    
    # Quick stats
    st.markdown("### 📊 Quick Stats")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Modules", "20+", help="Total available modules")
    with col2:
        st.metric("Features", "100+", help="Total features")
    
    st.markdown("---")
    st.caption(f"© 2026 Budidaya Padi v1.0")
    st.caption(f"Last updated: {datetime.now().strftime('%Y-%m-%d')}")

# Main content
st.markdown("""
<div class='main-header'>
    <h1>🌾 Budidaya Padi</h1>
    <p>Sistem Manajemen Budidaya Padi Terpadu dengan AI & Machine Learning</p>
</div>
""", unsafe_allow_html=True)

# Welcome section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='color: #2E7D32; margin: 0;'>🎯</h2>
        <h3>Comprehensive</h3>
        <p>20+ modul lengkap untuk semua aspek budidaya padi</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='color: #2E7D32; margin: 0;'>🤖</h2>
        <h3>AI-Powered</h3>
        <p>Machine learning dengan PyCaret untuk prediksi akurat</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class='metric-card'>
        <h2 style='color: #2E7D32; margin: 0;'>📊</h2>
        <h3>Data-Driven</h3>
        <p>Visualisasi interaktif dengan Altair & analytics mendalam</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# Feature highlights
st.header("✨ Fitur Unggulan")

tab1, tab2, tab3, tab4 = st.tabs(["💰 Perencanaan", "🌾 Budidaya", "🤖 AI & ML", "📊 Analytics"])

with tab1:
    st.subheader("Perencanaan & Keuangan")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>📋 RAB Calculator</h4>
            <p>Hitung Rencana Anggaran Biaya budidaya padi secara detail dengan breakdown:</p>
            <ul>
                <li>Persiapan lahan</li>
                <li>Bibit & persemaian</li>
                <li>Pupuk (NPK, Urea, SP-36, KCl)</li>
                <li>Pestisida & herbisida</li>
                <li>Tenaga kerja</li>
                <li>Irigasi & air</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>📊 Analisis Bisnis</h4>
            <p>Analisis kelayakan usaha budidaya padi:</p>
            <ul>
                <li>Profitability analysis</li>
                <li>Break-even point</li>
                <li>ROI calculator</li>
                <li>Cash flow projection</li>
                <li>Sensitivity analysis</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab2:
    st.subheader("Panduan Budidaya Padi")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>🌾 Varietas Padi Indonesia</h4>
            <p>Database lengkap 20+ varietas padi:</p>
            <ul>
                <li>IR64, Ciherang, Inpari series</li>
                <li>Potensi hasil & durasi tanam</li>
                <li>Ketahanan terhadap hama/penyakit</li>
                <li>Kesesuaian regional</li>
                <li>Karakteristik gabah</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>💧 Manajemen Air</h4>
            <p>Sistem pengairan padi yang efisien:</p>
            <ul>
                <li>Jadwal penggenangan</li>
                <li>Alternate Wetting & Drying (AWD)</li>
                <li>Monitoring kedalaman air</li>
                <li>Kalkulator biaya irigasi</li>
                <li>Hemat air hingga 30%</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab3:
    st.subheader("AI & Machine Learning")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>🔬 PyCaret ML Lab</h4>
            <p>Automated Machine Learning untuk padi:</p>
            <ul>
                <li>Prediksi hasil panen (yield prediction)</li>
                <li>Klasifikasi kualitas gabah</li>
                <li>Auto-compare 15+ algoritma ML</li>
                <li>Hyperparameter tuning otomatis</li>
                <li>Model explainability (SHAP)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>📸 Deteksi Penyakit AI</h4>
            <p>Computer vision untuk deteksi penyakit:</p>
            <ul>
                <li>Upload foto daun/tanaman</li>
                <li>CNN-based classification</li>
                <li>Deteksi Blast, Hawar Daun, Tungro</li>
                <li>Confidence score & rekomendasi</li>
                <li>Riwayat deteksi</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

with tab4:
    st.subheader("Analytics & Visualizations")
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class='info-card'>
            <h4>📊 Visualisasi Altair</h4>
            <p>Interactive charts dengan Altair:</p>
            <ul>
                <li>Time series analysis</li>
                <li>Correlation heatmaps</li>
                <li>Distribution plots</li>
                <li>Geospatial visualizations</li>
                <li>Linked brushing & filtering</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class='info-card'>
            <h4>📊 Statistik Penelitian</h4>
            <p>Statistical analysis untuk field trials:</p>
            <ul>
                <li>ANOVA (one-way, two-way)</li>
                <li>RCBD, Latin Square Design</li>
                <li>Regression analysis</li>
                <li>Post-hoc tests (Tukey HSD)</li>
                <li>Publication-ready plots</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# Getting started
st.header("🚀 Mulai Menggunakan")

st.info("""
**Untuk memulai, pilih modul dari sidebar atau menu Pages di atas.**

Rekomendasi urutan untuk pengguna baru:
1. 📋 **RAB Calculator** - Rencanakan budget Anda
2. 📚 **Panduan Budidaya** - Pelajari teknik budidaya yang benar
3. 🌾 **Varietas Padi** - Pilih varietas yang sesuai
4. 🧪 **Kalkulator Pupuk** - Hitung kebutuhan pupuk
5. 📅 **Kalender Tanam** - Tentukan waktu tanam optimal
""")

# Quick links
st.subheader("🔗 Quick Links")

col1, col2, col3, col4 = st.columns(4)

with col1:
    if st.button("📋 RAB Calculator", use_container_width=True):
        st.info("Navigasi ke Pages → 01_💰_RAB_Calculator")

with col2:
    if st.button("🌾 Varietas Padi", use_container_width=True):
        st.info("Navigasi ke Pages → 08_🌾_Varietas_Padi")

with col3:
    if st.button("🔬 PyCaret ML Lab", use_container_width=True):
        st.info("Navigasi ke Pages → 17_🔬_PyCaret_ML_Lab")

with col4:
    if st.button("📊 Analytics Hub", use_container_width=True):
        st.info("Navigasi ke Pages → 19_📊_Analytics_Hub")

st.markdown("---")

# Footer
st.markdown("""
<div style='text-align: center; padding: 2rem; background-color: #F1F8E9; border-radius: 10px; margin-top: 2rem;'>
    <h3 style='color: #2E7D32; margin: 0;'>🌾 Budidaya Padi</h3>
    <p style='color: #666; margin: 0.5rem 0;'>Sistem Manajemen Budidaya Padi Terpadu</p>
    <p style='color: #999; font-size: 0.9rem; margin: 0;'>
        Powered by Streamlit • Altair • PyCaret • AI/ML
    </p>
    <p style='color: #999; font-size: 0.8rem; margin: 0.5rem 0 0 0;'>
        © 2026 AgriSensa • Version 1.0.0
    </p>
</div>
""", unsafe_allow_html=True)
