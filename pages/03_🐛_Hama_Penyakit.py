"""
🐛 Hama & Penyakit Padi - Rice Pest and Disease Database
Comprehensive guide for pest and disease management
"""

import streamlit as st
import pandas as pd
import altair as alt

st.set_page_config(page_title="Hama & Penyakit", page_icon="🐛", layout="wide")

st.title("🐛 Hama & Penyakit Padi")
st.markdown("**Database lengkap hama dan penyakit padi dengan cara pengendalian**")
st.markdown("---")

# Pest and Disease Database
PESTS = {
    'Wereng Coklat': {
        'type': 'Hama',
        'latin': 'Nilaparvata lugens',
        'symptoms': 'Hopperburn (tanaman menguning dan mengering), tanaman kerdil',
        'damage': 'Menghisap cairan tanaman, menularkan virus tungro',
        'control': [
            'Gunakan varietas tahan (Inpari 32, 42, 43)',
            'Tanam serentak dalam satu hamparan',
            'Pergiliran tanaman',
            'Insektisida: Imidakloprid, Buprofezin'
        ],
        'prevention': 'Hindari pemupukan N berlebihan, jaga sanitasi lahan',
        'critical_period': '30-60 HST'
    },
    'Penggerek Batang': {
        'type': 'Hama',
        'latin': 'Scirpophaga incertulas',
        'symptoms': 'Sundep (anakan mati), beluk (malai hampa)',
        'damage': 'Larva menggerek batang, merusak jaringan pengangkut',
        'control': [
            'Sanitasi: kumpulkan dan musnahkan jerami',
            'Perangkap feromon',
            'Musuh alami: Trichogramma',
            'Insektisida: Karbofuran, Fipronil'
        ],
        'prevention': 'Tanam serentak, pergiliran tanaman, varietas tahan',
        'critical_period': '0-40 HST'
    },
    'Walang Sangit': {
        'type': 'Hama',
        'latin': 'Leptocorisa oratorius',
        'symptoms': 'Gabah hampa, beras hitam, bau tidak sedap',
        'damage': 'Menghisap bulir padi yang sedang masak susu',
        'control': [
            'Hand picking (pungut manual)',
            'Perangkap jaring',
            'Insektisida: Sipermetrin, Deltametrin',
            'Aplikasi saat pagi/sore hari'
        ],
        'prevention': 'Tanam serentak, jaga kebersihan pematang',
        'critical_period': '80-100 HST'
    },
    'Tikus': {
        'type': 'Hama',
        'latin': 'Rattus argentiventer',
        'symptoms': 'Batang terpotong, bulir habis dimakan',
        'damage': 'Memakan bulir dan batang padi',
        'control': [
            'Gropyokan (perburuan massal)',
            'Perangkap (bubu, jebakan)',
            'Rodentisida: Klerat, Racumin',
            'TBS (Trap Barrier System)'
        ],
        'prevention': 'Buat pagar keliling, sanitasi sarang, tanam serentak',
        'critical_period': 'Sepanjang musim'
    }
}

DISEASES = {
    'Blast (Blas)': {
        'type': 'Penyakit',
        'pathogen': 'Pyricularia oryzae (jamur)',
        'symptoms': 'Bercak coklat berbentuk belah ketupat pada daun, leher malai patah',
        'damage': 'Daun mati, malai hampa, puso',
        'control': [
            'Varietas tahan: Inpari 32, 42, 43',
            'Fungisida: Triklorfosmethyl, Isoprothiolane',
            'Aplikasi saat gejala awal',
            'Rotasi fungisida'
        ],
        'prevention': 'Pemupukan berimbang, hindari N berlebih, drainase baik',
        'critical_period': '40-80 HST'
    },
    'Hawar Daun Bakteri': {
        'type': 'Penyakit',
        'pathogen': 'Xanthomonas oryzae (bakteri)',
        'symptoms': 'Daun menguning dari ujung, mengering seperti terbakar',
        'damage': 'Daun mati, anakan berkurang, hasil turun 20-30%',
        'control': [
            'Varietas tahan: Inpari 13, Ciherang',
            'Bakterisida: Streptomisin, Oksitetrasiklin',
            'Sanitasi: musnahkan jerami terinfeksi',
            'Atur pengairan (tidak tergenang terus)'
        ],
        'prevention': 'Gunakan benih sehat, hindari luka mekanis',
        'critical_period': '30-60 HST'
    },
    'Tungro': {
        'type': 'Penyakit',
        'pathogen': 'Rice Tungro Virus (virus)',
        'symptoms': 'Daun kuning-oranye, tanaman kerdil, anakan sedikit',
        'damage': 'Tanaman kerdil, gabah hampa, puso',
        'control': [
            'Kendalikan wereng hijau (vektor)',
            'Cabut dan musnahkan tanaman sakit',
            'Varietas tahan: Inpari 33, Ciherang',
            'Insektisida untuk wereng'
        ],
        'prevention': 'Tanam serentak, varietas tahan, kendalikan wereng',
        'critical_period': '0-40 HST'
    },
    'Busuk Batang': {
        'type': 'Penyakit',
        'pathogen': 'Rhizoctonia solani (jamur)',
        'symptoms': 'Bercak hitam pada pelepah daun dekat permukaan air',
        'damage': 'Batang busuk, tanaman rebah, hasil turun',
        'control': [
            'Fungisida: Validamycin, Hexaconazole',
            'Drainase berkala',
            'Kurangi pemupukan N',
            'Aplikasi saat gejala awal'
        ],
        'prevention': 'Jarak tanam tidak terlalu rapat, drainase baik',
        'critical_period': '50-80 HST'
    }
}

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["🐛 Hama", "🦠 Penyakit", "📊 Perbandingan", "💊 Jadwal Pengendalian"])

with tab1:
    st.header("🐛 Database Hama Padi")
    
    for name, data in PESTS.items():
        with st.expander(f"🐛 {name} ({data['latin']})", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Gejala & Kerusakan")
                st.write(f"**Gejala:** {data['symptoms']}")
                st.write(f"**Kerusakan:** {data['damage']}")
                st.warning(f"⚠️ **Periode Kritis:** {data['critical_period']}")
            
            with col2:
                st.markdown("### Pengendalian")
                for i, control in enumerate(data['control'], 1):
                    st.write(f"{i}. {control}")
                
                st.info(f"💡 **Pencegahan:** {data['prevention']}")

with tab2:
    st.header("🦠 Database Penyakit Padi")
    
    for name, data in DISEASES.items():
        with st.expander(f"🦠 {name} - {data['pathogen']}", expanded=False):
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("### Gejala & Kerusakan")
                st.write(f"**Gejala:** {data['symptoms']}")
                st.write(f"**Kerusakan:** {data['damage']}")
                st.warning(f"⚠️ **Periode Kritis:** {data['critical_period']}")
            
            with col2:
                st.markdown("### Pengendalian")
                for i, control in enumerate(data['control'], 1):
                    st.write(f"{i}. {control}")
                
                st.info(f"💡 **Pencegahan:** {data['prevention']}")

with tab3:
    st.header("📊 Perbandingan Hama & Penyakit")
    
    # Create comparison dataframe
    all_items = []
    for name, data in PESTS.items():
        all_items.append({
            'Nama': name,
            'Jenis': 'Hama',
            'Periode Kritis': data['critical_period'],
            'Tingkat Bahaya': 'Tinggi' if 'Wereng' in name or 'Tikus' in name else 'Sedang'
        })
    
    for name, data in DISEASES.items():
        all_items.append({
            'Nama': name,
            'Jenis': 'Penyakit',
            'Periode Kritis': data['critical_period'],
            'Tingkat Bahaya': 'Tinggi' if 'Blast' in name or 'Tungro' in name else 'Sedang'
        })
    
    comparison_df = pd.DataFrame(all_items)
    st.dataframe(comparison_df, use_container_width=True, hide_index=True)
    
    # Chart
    chart = alt.Chart(comparison_df).mark_bar().encode(
        x=alt.X('Jenis:N', title='Jenis'),
        y=alt.Y('count():Q', title='Jumlah'),
        color='Tingkat Bahaya:N',
        tooltip=['Jenis', 'count()', 'Tingkat Bahaya']
    ).properties(
        title='Distribusi Hama & Penyakit',
        height=300
    )
    
    st.altair_chart(chart, use_container_width=True)

with tab4:
    st.header("💊 Jadwal Pengendalian Terpadu")
    
    st.markdown("""
    ### Strategi PHT (Pengendalian Hama Terpadu)
    
    **Prinsip PHT:**
    1. Pencegahan (preventif) lebih baik dari pengobatan
    2. Gunakan musuh alami
    3. Pestisida sebagai pilihan terakhir
    4. Monitoring rutin
    """)
    
    schedule_df = pd.DataFrame({
        'Periode (HST)': ['0-20', '20-40', '40-60', '60-80', '80-100', '100-120'],
        'Target Utama': [
            'Tikus, Keong',
            'Penggerek batang, Tungro',
            'Wereng, Blast',
            'Blast, Hawar daun',
            'Walang sangit',
            'Tikus, Burung'
        ],
        'Tindakan': [
            'Gropyokan, sanitasi',
            'Monitoring, perangkap',
            'Monitoring, fungisida',
            'Fungisida, bakterisida',
            'Hand picking, insektisida',
            'Pengusiran, jaring'
        ]
    })
    
    st.dataframe(schedule_df, use_container_width=True, hide_index=True)
    
    st.success("""
    💡 **Tips Pengendalian Efektif:**
    - Monitoring rutin 2x seminggu
    - Catat populasi hama/intensitas penyakit
    - Aplikasi pestisida sesuai ambang ekonomi
    - Rotasi pestisida untuk hindari resistensi
    - Gunakan APD saat aplikasi
    """)

st.markdown("---")
st.caption("⚠️ **Penting:** Selalu ikuti dosis dan cara aplikasi pestisida sesuai label")
