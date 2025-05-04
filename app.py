import streamlit as st
from PIL import Image
from utils import gri_donusum, ikili_donusum, dondur_degistir, kirp,zoom,histogram_esitleme,rgb_to_hsv,cift_esikleme, kenar_bulma,gurultu_ekle_sap, mean_filtre, median_filtre,erozyon,acma,genisleme,kapama,motion_blur,resim_carpma,resim_cikarma,kontrast_azalt
import base64
import io
import time
st.set_page_config(page_title=" Görüntü İşleme Paneli", layout="wide", page_icon="✨")
if "ilk_karsilama" not in st.session_state:
    st.session_state.ilk_karsilama = True
st.markdown("""
<div class="navbar">
    <h1> Görüntü İşleme Paneli</h1>
    <span> Mayıs-2025</span>
</div>
""", unsafe_allow_html=True)
st.markdown("""
<style>
header [data-testid="stToolbar"] {
    visibility: hidden;
}
button[title="Main menu"] {
    visibility: hidden;
}
section[data-testid="stSidebar"] ~ div button[title="Hide sidebar"] svg {
    stroke: #ffffff !important;
    fill: #0d47a1 !important;
    background-color: #0d47a1;
    border-radius: 50%;
    padding: 6px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.3);
    transition: all 0.3s ease;
}

section[data-testid="stSidebar"] ~ div button[title="Hide sidebar"]:hover svg {
    fill: #1976d2 !important;
    transform: scale(1.1);
}
</style>
""", unsafe_allow_html=True)
if "ilk_acilis" not in st.session_state:
    st.session_state.ilk_acilis = True

if st.session_state.ilk_acilis:
    st.code("""
# 🎯 Görüntü İşleme Başlıyor...

import numpy as np
import matplotlib.pyplot as plt

def init_portfolio():
    developer = {
        "name": ["Sude", "Bilal", "Ezgi", "Yılmaz"],
        "project": "Görüntü İşleme Projemiz",
    }
    return developer

# Executing...
init_portfolio()
""", language="python")

st.markdown("""
    <style>
 <div class="navbar">
    <h1> Görüntü İşleme Paneli</h1>
    <span>AI Projesi - 2025</span>           
</div>

  .navbar {
    width: 100%;
    background-color: #0d1b2a;
    padding: 15px 30px;
    box-shadow: 0 2px 10px rgba(0,0,0,0.25);
    border-radius: 0 0 12px 12px;
    margin-bottom: 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.navbar h1 {
    color: white;
    font-size: 1.6rem;
    margin: 0;
}
.navbar span {
    color: #dee2e6;
    font-size: 1rem;
}
       div[data-testid="stApp"] {
        background: linear-gradient(135deg, #2196f3, #03a9f4, #b2ebf2);
        background-size: 300% 300%;
        animation: gradientMove 15s ease infinite;
        .navbar {
            background-color: #006064;
            padding: 10px 20px;
            border-radius: 0 0 10px 10px;
            box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
        }
    section[data-testid="stSidebar"] .stFileUploader, 
    section[data-testid="stSidebar"] .stSelectbox {
    background-color: #0d1b2a !important; 
    border-radius: 10px !important;
    padding: 10px !important;
    color: #ffffff !important;
    border: 1px solid #1b263b !important;
}

section[data-testid="stSidebar"] label {
    color: #89c2d9 !important;
    font-weight: bold !important;
    font-size: 0.95rem;
}
        .navbar h1 {
            color: #ffffff;
            font-size: 1.6rem;
            margin: 0;
            display: inline-block;
            vertical-align: middle;
        }
        .navbar span {
            float: right;
            color: #b2ebf2;
            font-size: 1rem;
            margin-top: 4px;
        }
        .big-title {
            font-size: 3rem;
            font-weight: bold;
            color: #01579B;
            text-align: center;
            animation: fadein 2s ease-in;
        }
        .subtitle {
            font-size: 1.2rem;
            text-align: center;
            color: #37474F;
            margin-bottom: 2rem;
            animation: slideup 2s ease-in-out;
        }
        .highlight-box {
            background: linear-gradient(145deg, #b3e5fc, #b2dfdb);
            padding: 30px;
            border-radius: 15px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
            margin-bottom: 30px;
        }
        .btn-custom, .download-btn {
            background-color: #039BE5;
            color: white;
            padding: 10px 25px;
            border: none;
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }
        .process-box {
            background: linear-gradient(135deg, #b3e5fc, #e1f5fe);
            padding: 20px;
            border-radius: 15px;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
            text-align: center;
            margin-top: 2rem;
        }
        .image-card {
            border: 2px solid #b2ebf2;
            border-radius: 15px;
            padding: 15px;
            background: #ffffff;
            box-shadow: 0 5px 15px rgba(0,0,0,0.08);
            text-align: center;
            transition: transform 0.3s ease;
        }
        .image-card:hover {
            transform: scale(1.01);
        }
        .sidebar-container {
            background: linear-gradient(145deg, #e3f2fd, #b3e5fc);
            padding: 25px;
            border-radius: 20px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
            margin-top: 15px;
        }
        .sidebar-title {
            color: #01579B;
            font-size: 1.6rem;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .sidebar-subtitle {
            color: #0277BD;
            font-size: 1rem;
            text-align: center;
            margin-bottom: 1rem;
        }
        .sidebar-section {
            margin-bottom: 20px;
        }
        .sidebar-label {
            color: #01579B;
            font-weight: 600;
            margin-bottom: 5px;
            font-size: 0.95rem;
        }
        .css-1cpxqw2 {
            background-color: #e1f5fe !important;
            border-radius: 8px !important;
            border: 1px solid #81d4fa !important;
            padding: 5px 10px !important;
        }   
        section[data-testid="stSidebar"] > div:first-child {
         background: linear-gradient(145deg, #0d47a1, #1565c0);  /* koyu mavi degrade */
          padding: 25px;
          border-radius: 15px;
          box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}
section[data-testid="stSidebar"] label {
    color: #ffffff !important;
    font-weight: bold;
    font-size: 1rem;
}
section[data-testid="stSidebar"] .stSelectbox,
section[data-testid="stSidebar"] .stFileUploader,
section[data-testid="stSidebar"] .stSlider {
    background-color: #0b3c91 !important;
    color: white !important;
    border-radius: 10px !important;
    border: 1px solid #90caf9 !important;
    padding: 10px;
}
section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}
    </style>
""", unsafe_allow_html=True)
st.markdown("""
<style>
h1 {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-weight: bold;
    text-shadow: 1px 1px 3px rgba(0,0,0,0.4);
}
   .stImage img {
    transition: transform 0.3s ease-in-out;
}
.stImage img:hover {
    transform: scale(1.03);
            
</style>
""", unsafe_allow_html=True)
with st.sidebar:
    st.markdown("### 👋 Hoş Geldin!")
    st.markdown("""
    <style>
    input {
        border: 2px solid #ffcc00 !important;
        border-radius: 8px !important;
        padding: 6px !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)
    isim = st.text_input("🧑‍💻 Lütfen adınızı girin:")
    st.header("🎛️ İşlem Ayarları")
    dosya = st.file_uploader(" Görsel Yükle", type=["jpg", "jpeg", "png"])
    islem = st.selectbox(" İşlem Seç", [
        "Gri Dönüşüm",      "Binary Dönüşüm", "Görüntü Döndürme","Görüntü Kırpma",      "Yakınlaştır/Uzaklaştır",      "Histogram Germe",      "Renk Uzayı Dönüşümü",  "Çift Eşikleme", "Kenar Bulma", "Gürültü Ekle (Salt & Pepper)","Gürültü Temizle (Mean Filtre)","Gürültü Temizle (Median Filtre)","Morfolojik İşlem: Erozyon","Morfolojik İşlem: Genişleme","Morfolojik İşlem: Açma","Morfolojik İşlem: Kapama","Hareket Filtresi (Motion Blur)","Resim Çıkarma","Resim Çarpma","Kontrast Azaltma",
  ])
    basla = st.button("✨ İşlemi Başlat", use_container_width=True)
if isim and st.session_state.ilk_karsilama:
    st.toast(f"🎉 Hoş geldin {isim}! Görsel işlemeye hazırsın.")
    st.balloons()
    st.success(f"💡 Hoş geldin {isim}! Şimdi görsel yükleyip işlemeye başlayabilirsin.")
    st.session_state.ilk_karsilama = False 
elif not isim:
    st.warning("👈 Lütfen sol panelden adınızı giriniz!") 
    esik = derece = x1 = y1 = x2 = y2 = oran = blur_boyut = alt_esik = ust_esik = None

if islem == "Binary Dönüşüm":
    st.markdown('<div class="sidebar-label"> Eşik Değeri</div>', unsafe_allow_html=True)
    esik = st.slider("", 0, 255, 128)

elif islem == "Görüntü Döndürme":
    st.markdown('<div class="sidebar-label"> Döndürme Açısı</div>', unsafe_allow_html=True)
    derece = st.selectbox("", [90, 180, 270])

elif islem == "Görüntü Kırpma":
    st.markdown('<div class="sidebar-label"> Kırpma Koordinatları</div>', unsafe_allow_html=True)
    x1 = st.number_input("Başlangıç X", min_value=0, step=1, value=0)
    y1 = st.number_input("Başlangıç Y", min_value=0, step=1, value=0)
    x2 = st.number_input("Bitiş X", min_value=1, step=1, value=100)
    y2 = st.number_input("Bitiş Y", min_value=1, step=1, value=100)

elif islem == "Yakınlaştır/Uzaklaştır":
    st.markdown('<div class="sidebar-label"> Yakınlaştırma Oranı</div>', unsafe_allow_html=True)
    oran = st.slider("", 0.1, 3.0, 1.0, 0.1)

elif islem == "Çift Eşikleme":
    st.markdown('<div class="sidebar-label">Eşik Aralığı</div>', unsafe_allow_html=True)
    alt_esik = st.slider("Alt Eşik", 0, 255, 85)
    ust_esik = st.slider("Üst Eşik", 0, 255, 170)

elif islem == "Gürültü Ekle (Salt & Pepper)":
    st.markdown('<div class="sidebar-label">Gürültü Oranı</div>', unsafe_allow_html=True)
    oran = st.slider("", 0.0, 0.1, 0.02, 0.01)

elif islem == "Hareket Filtresi (Motion Blur)":
    st.markdown('<div class="sidebar-label"> Filtre Boyutu</div>', unsafe_allow_html=True)
    blur_boyut = st.slider("", 3, 15, 9, 2)

elif islem in ["Resim Çıkarma", "Resim Çarpma"]:
    st.markdown('<div class="sidebar-label">🖼️ İkinci Görsel Seçin</div>', unsafe_allow_html=True)
    ikinci_dosya = st.file_uploader("📂", type=["jpg", "jpeg", "png"], key="ikinci")

elif islem == "Kontrast Azaltma":
    st.markdown('<div class="sidebar-label"> Kontrast Oranı</div>', unsafe_allow_html=True)
    oran = st.slider("", 0.0, 1.0, 0.5, 0.05) 
if dosya:
    st.markdown("""
        <style>
            .image-card {
                border: 2px solid #b2dfdb;
                border-radius: 15px;
                padding: 15px;
                background: #ffffffee;
                box-shadow: 0 5px 15px rgba(0,0,0,0.08);
                text-align: center;
                transition: transform 0.3s ease;
            }
            .image-card:hover {
                transform: scale(1.01);
            }
            .process-box {
                background: linear-gradient(135deg, #e1bee7, #b3e5fc);
                padding: 20px;
                border-radius: 15px;
                box-shadow: 0 10px 25px rgba(0, 0, 0, 0.1);
                text-align: center;
                margin-top: 2rem;
            }
            .download-btn {
                background-color: #7E57C2;
                color: white;
                padding: 12px 25px;
                border-radius: 8px;
                text-decoration: none;
                font-weight: bold;
                box-shadow: 0 5px 10px rgba(0,0,0,0.1);
            }
        </style>
    """, unsafe_allow_html=True)

    resim = Image.open(dosya).convert("RGB")
    st.markdown("### 📷 Yüklenen Görsel ve Sonuç")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="image-card">', unsafe_allow_html=True)
        st.image(resim, caption="🎯 Orijinal Görsel", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    if basla:      
        st.markdown("### ⏳ İşlem Gerçekleştiriliyor...")         
        start = time.time()
        with st.spinner("🔄 Lütfen bekleyin..."):
            if islem == "Gri Dönüşüm":
                sonuc = gri_donusum(resim.copy())
            elif islem == "Binary Dönüşüm":
                sonuc = ikili_donusum(resim.copy(), esik)
            elif islem == "Görüntü Döndürme":
                sonuc = dondur_degistir(resim.copy(), derece)
            elif islem == "Görüntü Kırpma":
                sonuc = kirp(resim.copy(), x1, y1, x2, y2)
            elif islem == "Yakınlaştır/Uzaklaştır":
                sonuc = zoom(resim.copy(), oran)
            elif islem == "Renk Uzayı Dönüşümü":
                sonuc = rgb_to_hsv(resim.copy())
            elif islem == "Çift Eşikleme":
                sonuc = cift_esikleme(resim.copy(), alt_esik, ust_esik)
            elif islem == "Kenar Bulma":
                sonuc = kenar_bulma(resim.copy())
            elif islem == "Gürültü Ekle (Salt & Pepper)":
                sonuc = gurultu_ekle_sap(resim.copy(), oran)
            elif islem == "Gürültü Temizle (Mean Filtre)":
                sonuc = mean_filtre(resim.copy())
            elif islem == "Gürültü Temizle (Median Filtre)":
                sonuc = median_filtre(resim.copy())
            elif islem == "Morfolojik İşlem: Erozyon":
                sonuc = erozyon(resim.copy())
            elif islem == "Morfolojik İşlem: Genişleme":
                sonuc = genisleme(resim.copy())
            elif islem == "Morfolojik İşlem: Açma":
                sonuc = acma(resim.copy())
            elif islem == "Morfolojik İşlem: Kapama":
                sonuc = kapama(resim.copy())    
            elif islem == "Hareket Filtresi (Motion Blur)":   
                sonuc = motion_blur(resim.copy(), blur_boyut)
            elif islem == "Kontrast Azaltma":
                sonuc = kontrast_azalt(resim.copy(), oran)
            elif islem == "Resim Çıkarma" and ikinci_dosya:
                resim2 = Image.open(ikinci_dosya).convert("RGB").resize(resim.size)
                sonuc = resim_cikarma(resim.copy(), resim2)
            elif islem == "Resim Çarpma" and ikinci_dosya:
                resim2 = Image.open(ikinci_dosya).convert("RGB").resize(resim.size)
                sonuc = resim_carpma(resim.copy(), resim2)
            elif islem == "Histogram Germe":
                sonuc = histogram_esitleme(resim.copy())
            else:
                st.warning("İşlem için gerekli ayarları yapmalısınız.")
                sonuc = None
        end = time.time()
if 'sonuc' in locals() and sonuc:
    with col2:
        st.markdown('<div class="image-card">', unsafe_allow_html=True)
        if islem == "Yakınlaştır/Uzaklaştır":
            st.image(sonuc, caption="✨ İşlenmiş Görsel", width=sonuc.width)
        else:
            st.image(sonuc, caption="✨ İşlenmiş Görsel", use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="process-box" style="color: #0d1b2a;">
        <h4>✅ İşlem başarıyla tamamlandı!</h4>
        <p>🕒 Süre: <b>{end - start:.2f} saniye</b></p>
        <p>📐 Görüntü Boyutu: <b>{resim.size[0]}x{resim.size[1]}</b></p>
        <p>⚙️ Uygulanan İşlem: <b>{islem}</b></p>
    </div>
    """, unsafe_allow_html=True)

    buf = io.BytesIO()
    sonuc.save(buf, format="PNG")
    byte_im = buf.getvalue()
    b64 = base64.b64encode(byte_im).decode()
    st.markdown(f"""
        <div style="text-align: center; margin-top: 1rem;">
            <a href="data:file/png;base64,{b64}" download="islenmis_gorsel.png" class="download-btn">
                💾 Görseli İndir
            </a>
        </div>
    """, unsafe_allow_html=True)
