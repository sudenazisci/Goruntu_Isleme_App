from PIL import Image
def gri_donusum(resim: Image.Image) -> Image.Image:
    genislik, yukseklik = resim.size
    yeni_resim = Image.new("RGB", (genislik, yukseklik))
    orijinal = resim.load()
    yeni = yeni_resim.load()
    for x in range(genislik):
        for y in range(yukseklik):
            r, g, b = orijinal[x, y]
            gri = (r + g + b) // 3
            yeni[x, y] = (gri, gri, gri)

    return yeni_resim

def ikili_donusum(resim: Image.Image, esik: int = 128) -> Image.Image:
    gri = gri_donusum(resim)
    pikseller = gri.load()
    genislik, yukseklik = gri.size
    for x in range(genislik):
        for y in range(yukseklik):
            gri_deger = pikseller[x, y][0]
            deger = 255 if gri_deger >= esik else 0
            pikseller[x, y] = (deger, deger, deger)
    return gri

def dondur_degistir(resim: Image.Image, derece: int) -> Image.Image:
    genislik, yukseklik = resim.size
    orijinal = resim.load()

    if derece == 90:
        yeni_resim = Image.new("RGB", (yukseklik, genislik))
        yeni = yeni_resim.load()
        for x in range(genislik):
            for y in range(yukseklik):
                yeni[y, yukseklik - 1 - x] = orijinal[x, y]

    elif derece == 180:
        yeni_resim = Image.new("RGB", (genislik, yukseklik))
        yeni = yeni_resim.load()
        for x in range(genislik):
            for y in range(yukseklik):
                yeni[genislik - 1 - x, yukseklik - 1 - y] = orijinal[x, y]

    elif derece == 270:
        yeni_resim = Image.new("RGB", (yukseklik, genislik))
        yeni = yeni_resim.load()
        for x in range(genislik):
            for y in range(yukseklik):
                yeni[yukseklik - 1 - y, x] = orijinal[x, y]
    else:
        return resim  

    return yeni_resim

def kirp(resim: Image.Image, x1: int, y1: int, x2: int, y2: int) -> Image.Image:
    genislik, yukseklik = resim.size
    x1 = max(0, min(x1, genislik - 1))
    x2 = max(0, min(x2, genislik))
    y1 = max(0, min(y1, yukseklik - 1))
    y2 = max(0, min(y2, yukseklik))
    if x1 >= x2 or y1 >= y2:
        return resim  
    yeni_resim = Image.new("RGB", (x2 - x1, y2 - y1))
    orijinal = resim.load()
    yeni = yeni_resim.load()

    for x in range(x2 - x1):
        for y in range(y2 - y1):
            yeni[x, y] = orijinal[x + x1, y + y1]

    return yeni_resim
def zoom(resim: Image.Image, oran: float) -> Image.Image:
    genislik, yukseklik = resim.size
    orijinal = resim.load()
    yeni_genislik = int(genislik * oran)
    yeni_yukseklik = int(yukseklik * oran)
    yeni_resim = Image.new("RGB", (yeni_genislik, yeni_yukseklik))
    yeni = yeni_resim.load()
    for x in range(yeni_genislik):
        for y in range(yeni_yukseklik):
            eski_x = int(x / oran)
            eski_y = int(y / oran)
            eski_x = min(eski_x, genislik - 1)
            eski_y = min(eski_y, yukseklik - 1)
            yeni[x, y] = orijinal[eski_x, eski_y]

    return yeni_resim
def histogram_esitleme(resim: Image.Image) -> Image.Image:
    gri = resim.convert("L")  # Gri formata çevir
    pikseller = gri.load()
    genislik, yukseklik = gri.size

    histogram = [0] * 256
    for x in range(genislik):
        for y in range(yukseklik):
            deger = pikseller[x, y]
            histogram[deger] += 1

    cdf = [0] * 256
    cdf[0] = histogram[0]
    for i in range(1, 256):
        cdf[i] = cdf[i - 1] + histogram[i]

    toplam_piksel = genislik * yukseklik
    cdf_min = next((val for val in cdf if val > 0), 0)
    esitleme_tablosu = [0] * 256
    for i in range(256):
        if toplam_piksel - cdf_min > 0:
            esitleme_tablosu[i] = round((cdf[i] - cdf_min) * 255 / (toplam_piksel - cdf_min))
        else:
            esitleme_tablosu[i] = 0

    yeni = Image.new("L", (genislik, yukseklik))
    yeni_pikseller = yeni.load()
    for x in range(genislik):
        for y in range(yukseklik):
            eski = pikseller[x, y]
            yeni_pikseller[x, y] = esitleme_tablosu[eski]
    return yeni.convert("RGB")

def rgb_to_hsv(resim: Image.Image) -> Image.Image:
    genislik, yukseklik = resim.size
    pikseller = resim.load()

    yeni_resim = Image.new("RGB", (genislik, yukseklik))
    yeni = yeni_resim.load()

    for x in range(genislik):
        for y in range(yukseklik):
            r, g, b = [v / 255.0 for v in pikseller[x, y]]
            mx = max(r, g, b)
            mn = min(r, g, b)
            df = mx - mn

            if df == 0:
                h = 0
            elif mx == r:
                h = (60 * ((g - b) / df) + 360) % 360
            elif mx == g:
                h = (60 * ((b - r) / df) + 120) % 360
            elif mx == b:
                h = (60 * ((r - g) / df) + 240) % 360

            s = 0 if mx == 0 else (df / mx)
            v = mx

            h_renk = int(h / 360 * 255)
            s_renk = int(s * 255)
            v_renk = int(v * 255)
            yeni[x, y] = (h_renk, s_renk, v_renk)
    return yeni_resim
def cift_esikleme(resim: Image.Image, alt_esik: int, ust_esik: int) -> Image.Image:
    gri = gri_donusum(resim)
    pikseller = gri.load()
    genislik, yukseklik = gri.size

    for x in range(genislik):
        for y in range(yukseklik):
            deger = pikseller[x, y][0]
            if deger < alt_esik:
                yeni = 0
            elif deger > ust_esik:
                yeni = 255
            else:
                yeni = 128
            pikseller[x, y] = (yeni, yeni, yeni)

    return gri
def kenar_bulma(resim: Image.Image) -> Image.Image:
    gri = gri_donusum(resim.copy())
    genislik, yukseklik = gri.size
    orijinal = gri.load()
    yeni_resim = Image.new("RGB", (genislik, yukseklik))
    yeni = yeni_resim.load()
    gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    gy = [[1, 2, 1], [0, 0, 0], [-1, -2, -1]]
    for x in range(1, genislik - 1):
        for y in range(1, yukseklik - 1):
            toplam_gx = 0
            toplam_gy = 0

            for i in range(-1, 2):
                for j in range(-1, 2):
                    piksel = orijinal[x + i, y + j][0]
                    toplam_gx += piksel * gx[j + 1][i + 1]
                    toplam_gy += piksel * gy[j + 1][i + 1]

            kenar = int((toplam_gx**2 + toplam_gy**2) ** 0.5)
            kenar = max(0, min(255, kenar))
            yeni[x, y] = (kenar, kenar, kenar)

    return yeni_resim
import random

def gurultu_ekle_sap(resim: Image.Image, oran: float) -> Image.Image:
    genislik, yukseklik = resim.size
    pikseller = resim.load()
    toplam_piksel = genislik * yukseklik
    gürültü_sayisi = int(toplam_piksel * oran)

    for _ in range(gürültü_sayisi):
        x = random.randint(0, genislik - 1)
        y = random.randint(0, yukseklik - 1)
        deger = 255 if random.random() < 0.5 else 0
        pikseller[x, y] = (deger, deger, deger)
    return resim

def mean_filtre(resim: Image.Image) -> Image.Image:
    genislik, yukseklik = resim.size
    gri = gri_donusum(resim.copy())
    orijinal = gri.load()

    yeni = Image.new("RGB", (genislik, yukseklik))
    yeni_pikseller = yeni.load()

    for x in range(1, genislik - 1):
        for y in range(1, yukseklik - 1):
            toplam = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    toplam += orijinal[x + i, y + j][0]
            ort = toplam // 9
            yeni_pikseller[x, y] = (ort, ort, ort)

    return yeni
def median_filtre(resim: Image.Image) -> Image.Image:
    genislik, yukseklik = resim.size
    gri = gri_donusum(resim.copy())
    orijinal = gri.load()
    yeni = Image.new("RGB", (genislik, yukseklik))
    yeni_pikseller = yeni.load()

    for x in range(1, genislik - 1):
        for y in range(1, yukseklik - 1):
            komsular = []
            for i in range(-1, 2):
                for j in range(-1, 2):
                    komsular.append(orijinal[x + i, y + j][0])
            komsular.sort()
            medyan = komsular[4]
            yeni_pikseller[x, y] = (medyan, medyan, medyan)
    return yeni
def get_binary(resim: Image.Image) -> list:
    pikseller = resim.load()
    w, h = resim.size
    matris = []
    for y in range(h):
        satir = []
        for x in range(w):
            deger = pikseller[x, y][0]
            satir.append(1 if deger == 255 else 0)
        matris.append(satir)
    return matris

def to_image(matris: list) -> Image.Image:
    h = len(matris)
    w = len(matris[0])
    yeni = Image.new("RGB", (w, h))
    pikseller = yeni.load()
    for y in range(h):
        for x in range(w):
            v = 255 if matris[y][x] else 0
            pikseller[x, y] = (v, v, v)
    return yeni

def erozyon(resim: Image.Image) -> Image.Image:
    matris = get_binary(ikili_donusum(resim.copy()))
    h, w = len(matris), len(matris[0])
    sonuc = [[0]*w for _ in range(h)]

    for y in range(1, h-1):
        for x in range(1, w-1):
            komsu = [matris[y+j][x+i] for j in [-1,0,1] for i in [-1,0,1]]
            sonuc[y][x] = 1 if all(komsu) else 0

    return to_image(sonuc)
def genisleme(resim: Image.Image) -> Image.Image:
    matris = get_binary(ikili_donusum(resim.copy()))
    h, w = len(matris), len(matris[0])
    sonuc = [[0]*w for _ in range(h)]

    for y in range(1, h-1):
        for x in range(1, w-1):
            komsu = [matris[y+j][x+i] for j in [-1,0,1] for i in [-1,0,1]]
            sonuc[y][x] = 1 if any(komsu) else 0
    return to_image(sonuc)
def acma(resim: Image.Image) -> Image.Image:
    return genisleme(erozyon(resim.copy()))
def kapama(resim: Image.Image) -> Image.Image:
    return erozyon(genisleme(resim.copy()))
def motion_blur(resim: Image.Image, boyut: int = 9) -> Image.Image:
    genislik, yukseklik = resim.size
    gri = gri_donusum(resim.copy())
    orijinal = gri.load()

    yeni = Image.new("RGB", (genislik, yukseklik))
    yeni_pikseller = yeni.load()
    yarim = boyut // 2
    for x in range(yarim, genislik - yarim):
        for y in range(yukseklik):
            toplam = 0
            for k in range(-yarim, yarim + 1):
                toplam += orijinal[x + k, y][0]
            ort = toplam // boyut
            yeni_pikseller[x, y] = (ort, ort, ort)

    return yeni
def resim_cikarma(resim1: Image.Image, resim2: Image.Image) -> Image.Image:
    gen1 = gri_donusum(resim1.copy())
    gen2 = gri_donusum(resim2.copy())

    w, h = gen1.size
    cikis = Image.new("RGB", (w, h))
    p1, p2, pc = gen1.load(), gen2.load(), cikis.load()

    for x in range(w):
        for y in range(h):
            fark = abs(p1[x, y][0] - p2[x, y][0])
            pc[x, y] = (fark, fark, fark)
    return cikis
def resim_carpma(resim1: Image.Image, resim2: Image.Image) -> Image.Image:
    gen1 = gri_donusum(resim1.copy())
    gen2 = gri_donusum(resim2.copy())

    w, h = gen1.size
    cikis = Image.new("RGB", (w, h))
    p1, p2, pc = gen1.load(), gen2.load(), cikis.load()

    for x in range(w):
        for y in range(h):
            carp = (p1[x, y][0] * p2[x, y][0]) // 255
            carp = max(0, min(255, carp))
            pc[x, y] = (carp, carp, carp)
    return cikis
def kontrast_azalt(resim: Image.Image, oran: float = 0.5) -> Image.Image:
    oran = max(0, min(1, oran))
    genislik, yukseklik = resim.size
    pikseller = resim.load()
    for x in range(genislik):
        for y in range(yukseklik):
            r, g, b = pikseller[x, y]
            ort = (r + g + b) // 3
            r_yeni = int(r * oran + ort * (1 - oran))
            g_yeni = int(g * oran + ort * (1 - oran))
            b_yeni = int(b * oran + ort * (1 - oran))
            pikseller[x, y] = (r_yeni, g_yeni, b_yeni)
    return resim










