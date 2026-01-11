"""
💰 RAB Calculator - Rencana Anggaran Biaya Budidaya Padi
Comprehensive budget planning for rice cultivation
"""

import streamlit as st
import pandas as pd
import altair as alt

# Page config
st.set_page_config(
    page_title="RAB Calculator",
    page_icon="💰",
    layout="wide"
)

# Header
st.title("💰 RAB Calculator - Budidaya Padi")
st.markdown("**Hitung Rencana Anggaran Biaya budidaya padi secara detail**")
st.markdown("---")

# Tabs
tab1, tab2, tab3 = st.tabs(["📝 Input Data", "📊 Hasil RAB", "📈 Analisis"])

# Initialize session state
if 'rab_calculated' not in st.session_state:
    st.session_state.rab_calculated = False

with tab1:
    st.header("📝 Input Data Budidaya")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Informasi Lahan")
        luas_lahan = st.number_input("Luas Lahan (ha)", min_value=0.1, max_value=100.0, value=1.0, step=0.1)
        varietas = st.selectbox("Varietas Padi", ["IR64", "Ciherang", "Inpari 32", "Inpari 42", "Mekongga"])
        metode_tanam = st.selectbox("Metode Tanam", ["Transplanting (Pindah Tanam)", "Direct Seeding (Tabela)", "SRI (System of Rice Intensification)"])
    
    with col2:
        st.subheader("Target & Harga")
        target_produksi = st.number_input("Target Produksi (ton/ha)", min_value=1.0, max_value=15.0, value=6.0, step=0.5)
        harga_jual = st.number_input("Harga Jual Gabah (Rp/kg)", min_value=3000, max_value=10000, value=5500, step=100)
    
    st.markdown("---")
    
    # Cost inputs
    st.subheader("💵 Rincian Biaya")
    
    col_cost1, col_cost2 = st.columns(2)
    
    with col_cost1:
        st.markdown("**🌱 Persiapan Lahan & Bibit**")
        biaya_olah_tanah = st.number_input("Olah Tanah (Rp/ha)", value=2000000, step=100000)
        biaya_bibit = st.number_input("Bibit/Benih (Rp/ha)", value=1500000, step=100000)
        biaya_persemaian = st.number_input("Persemaian (Rp/ha)", value=500000, step=50000)
        
        st.markdown("**🧪 Pupuk**")
        biaya_urea = st.number_input("Urea (Rp/ha)", value=1200000, step=50000)
        biaya_npk = st.number_input("NPK/Phonska (Rp/ha)", value=1500000, step=50000)
        biaya_sp36 = st.number_input("SP-36 (Rp/ha)", value=600000, step=50000)
        biaya_organik = st.number_input("Pupuk Organik (Rp/ha)", value=800000, step=50000)
    
    with col_cost2:
        st.markdown("**💊 Pestisida & Herbisida**")
        biaya_pestisida = st.number_input("Pestisida (Rp/ha)", value=1000000, step=50000)
        biaya_herbisida = st.number_input("Herbisida (Rp/ha)", value=500000, step=50000)
        
        st.markdown("**👷 Tenaga Kerja**")
        biaya_tanam = st.number_input("Tanam/Tabela (Rp/ha)", value=2000000, step=100000)
        biaya_pemeliharaan = st.number_input("Pemeliharaan (Rp/ha)", value=1500000, step=100000)
        biaya_panen = st.number_input("Panen & Pasca Panen (Rp/ha)", value=3000000, step=100000)
        
        st.markdown("**💧 Irigasi & Lain-lain**")
        biaya_irigasi = st.number_input("Irigasi/Air (Rp/ha)", value=500000, step=50000)
        biaya_lainnya = st.number_input("Biaya Lain-lain (Rp/ha)", value=500000, step=50000)
    
    if st.button("🧮 Hitung RAB", type="primary", use_container_width=True):
        st.session_state.rab_calculated = True
        
        # Calculate totals
        total_persiapan = (biaya_olah_tanah + biaya_bibit + biaya_persemaian) * luas_lahan
        total_pupuk = (biaya_urea + biaya_npk + biaya_sp36 + biaya_organik) * luas_lahan
        total_pestisida = (biaya_pestisida + biaya_herbisida) * luas_lahan
        total_tenaga_kerja = (biaya_tanam + biaya_pemeliharaan + biaya_panen) * luas_lahan
        total_irigasi = (biaya_irigasi + biaya_lainnya) * luas_lahan
        
        total_biaya = total_persiapan + total_pupuk + total_pestisida + total_tenaga_kerja + total_irigasi
        
        # Revenue
        total_produksi = target_produksi * luas_lahan * 1000  # kg
        total_pendapatan = total_produksi * harga_jual
        
        # Profit
        keuntungan = total_pendapatan - total_biaya
        roi = (keuntungan / total_biaya * 100) if total_biaya > 0 else 0
        
        # Store in session state
        st.session_state.rab_data = {
            'luas_lahan': luas_lahan,
            'varietas': varietas,
            'metode_tanam': metode_tanam,
            'target_produksi': target_produksi,
            'harga_jual': harga_jual,
            'total_persiapan': total_persiapan,
            'total_pupuk': total_pupuk,
            'total_pestisida': total_pestisida,
            'total_tenaga_kerja': total_tenaga_kerja,
            'total_irigasi': total_irigasi,
            'total_biaya': total_biaya,
            'total_produksi': total_produksi,
            'total_pendapatan': total_pendapatan,
            'keuntungan': keuntungan,
            'roi': roi
        }
        
        st.success("✅ RAB berhasil dihitung! Lihat hasil di tab 'Hasil RAB'")

with tab2:
    st.header("📊 Hasil Rencana Anggaran Biaya")
    
    if st.session_state.rab_calculated:
        data = st.session_state.rab_data
        
        # Summary cards
        col_sum1, col_sum2, col_sum3, col_sum4 = st.columns(4)
        
        with col_sum1:
            st.metric("Total Biaya", f"Rp {data['total_biaya']:,.0f}")
        
        with col_sum2:
            st.metric("Total Pendapatan", f"Rp {data['total_pendapatan']:,.0f}")
        
        with col_sum3:
            st.metric("Keuntungan", f"Rp {data['keuntungan']:,.0f}", 
                     delta=f"{data['roi']:.1f}% ROI")
        
        with col_sum4:
            st.metric("Produksi", f"{data['total_produksi']/1000:.1f} ton")
        
        st.markdown("---")
        
        # Cost breakdown
        st.subheader("💰 Rincian Biaya per Kategori")
        
        breakdown_df = pd.DataFrame({
            'Kategori': ['Persiapan Lahan & Bibit', 'Pupuk', 'Pestisida & Herbisida', 
                        'Tenaga Kerja', 'Irigasi & Lain-lain'],
            'Biaya': [data['total_persiapan'], data['total_pupuk'], data['total_pestisida'],
                     data['total_tenaga_kerja'], data['total_irigasi']],
            'Persentase': [
                data['total_persiapan']/data['total_biaya']*100,
                data['total_pupuk']/data['total_biaya']*100,
                data['total_pestisida']/data['total_biaya']*100,
                data['total_tenaga_kerja']/data['total_biaya']*100,
                data['total_irigasi']/data['total_biaya']*100
            ]
        })
        
        col_table, col_chart = st.columns([1, 1])
        
        with col_table:
            st.dataframe(breakdown_df.style.format({
                'Biaya': 'Rp {:,.0f}',
                'Persentase': '{:.1f}%'
            }), use_container_width=True, hide_index=True)
        
        with col_chart:
            # Altair pie chart
            pie_chart = alt.Chart(breakdown_df).mark_arc().encode(
                theta=alt.Theta(field="Biaya", type="quantitative"),
                color=alt.Color(field="Kategori", type="nominal", 
                               scale=alt.Scale(scheme='category10')),
                tooltip=['Kategori', 'Biaya', 'Persentase']
            ).properties(
                title='Distribusi Biaya',
                height=300
            )
            st.altair_chart(pie_chart, use_container_width=True)
        
        # Detailed table
        st.subheader("📋 Tabel Lengkap RAB")
        
        detailed_df = pd.DataFrame({
            'Item': [
                'Luas Lahan', 'Varietas', 'Metode Tanam', 'Target Produksi',
                '', 'BIAYA PRODUKSI', 
                '1. Persiapan Lahan & Bibit', '2. Pupuk', '3. Pestisida & Herbisida',
                '4. Tenaga Kerja', '5. Irigasi & Lain-lain', 'TOTAL BIAYA',
                '', 'PENDAPATAN',
                'Produksi (kg)', 'Harga Jual (Rp/kg)', 'TOTAL PENDAPATAN',
                '', 'ANALISIS',
                'Keuntungan Bersih', 'ROI (%)', 'Biaya per kg', 'Margin per kg'
            ],
            'Nilai': [
                f"{data['luas_lahan']} ha", data['varietas'], data['metode_tanam'], 
                f"{data['target_produksi']} ton/ha",
                '', '',
                f"Rp {data['total_persiapan']:,.0f}",
                f"Rp {data['total_pupuk']:,.0f}",
                f"Rp {data['total_pestisida']:,.0f}",
                f"Rp {data['total_tenaga_kerja']:,.0f}",
                f"Rp {data['total_irigasi']:,.0f}",
                f"Rp {data['total_biaya']:,.0f}",
                '', '',
                f"{data['total_produksi']:,.0f}",
                f"Rp {data['harga_jual']:,.0f}",
                f"Rp {data['total_pendapatan']:,.0f}",
                '', '',
                f"Rp {data['keuntungan']:,.0f}",
                f"{data['roi']:.1f}%",
                f"Rp {data['total_biaya']/data['total_produksi']:,.0f}",
                f"Rp {data['keuntungan']/data['total_produksi']:,.0f}"
            ]
        })
        
        st.dataframe(detailed_df, use_container_width=True, hide_index=True)
        
        # Export button
        if st.button("📥 Export ke Excel", use_container_width=True):
            st.info("Feature export akan segera ditambahkan!")
    
    else:
        st.info("👈 Silakan input data dan hitung RAB di tab 'Input Data' terlebih dahulu")

with tab3:
    st.header("📈 Analisis Kelayakan")
    
    if st.session_state.rab_calculated:
        data = st.session_state.rab_data
        
        # Profitability analysis
        st.subheader("💹 Analisis Profitabilitas")
        
        if data['roi'] > 50:
            st.success(f"✅ **Sangat Menguntungkan** - ROI {data['roi']:.1f}% sangat baik untuk budidaya padi")
        elif data['roi'] > 30:
            st.success(f"✅ **Menguntungkan** - ROI {data['roi']:.1f}% cukup baik")
        elif data['roi'] > 10:
            st.warning(f"⚠️ **Cukup Menguntungkan** - ROI {data['roi']:.1f}% masih layak namun bisa dioptimalkan")
        else:
            st.error(f"❌ **Kurang Menguntungkan** - ROI {data['roi']:.1f}% perlu evaluasi ulang")
        
        # Break-even analysis
        st.subheader("⚖️ Break-Even Analysis")
        
        biaya_per_kg = data['total_biaya'] / data['total_produksi']
        break_even_price = biaya_per_kg
        margin = data['harga_jual'] - biaya_per_kg
        
        col_be1, col_be2, col_be3 = st.columns(3)
        
        with col_be1:
            st.metric("Biaya Produksi per kg", f"Rp {biaya_per_kg:,.0f}")
        
        with col_be2:
            st.metric("Harga Break-Even", f"Rp {break_even_price:,.0f}")
        
        with col_be3:
            st.metric("Margin per kg", f"Rp {margin:,.0f}")
        
        # Recommendations
        st.subheader("💡 Rekomendasi")
        
        recommendations = []
        
        if data['total_pupuk']/data['total_biaya'] > 0.25:
            recommendations.append("🧪 Biaya pupuk tinggi (>25%). Pertimbangkan pupuk organik atau beli dalam jumlah besar")
        
        if data['total_tenaga_kerja']/data['total_biaya'] > 0.35:
            recommendations.append("👷 Biaya tenaga kerja tinggi (>35%). Pertimbangkan mekanisasi atau sistem bagi hasil")
        
        if data['roi'] < 30:
            recommendations.append("📈 ROI masih rendah. Tingkatkan produktivitas atau cari pasar dengan harga lebih baik")
        
        if biaya_per_kg > 4000:
            recommendations.append("💰 Biaya produksi per kg tinggi. Lakukan efisiensi di semua aspek")
        
        if recommendations:
            for rec in recommendations:
                st.info(rec)
        else:
            st.success("✅ Rencana budidaya Anda sudah optimal!")
    
    else:
        st.info("👈 Silakan input data dan hitung RAB di tab 'Input Data' terlebih dahulu")

# Footer
st.markdown("---")
st.caption("💡 **Tips:** Selalu update harga sesuai kondisi pasar terkini untuk hasil RAB yang akurat")
