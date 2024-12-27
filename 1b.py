import math

def f_turunan(x: float) -> float:
    """
    Turunan dari fungsi lintasan menggambarkan gradien.  
    f'(x) = -1/2.x + 3/2 + 3.cos(x)
    """
    return -1/2*x + 3/2 + 3*math.cos(x)

def f_turunan_kedua(x: float) -> float:
    """
    Turunan kedua dari fungsi pertama.
    f''(x) =  -1/2 - 3.sin(x) + 4
    """
    return -1/2 - 3*math.sin(x)


def metode_bagi_dua(fungsi: callable, a: float, b: float, galat=1e-3)  -> float:
    """
    Metode bagi dua untuk mencari akar fungsi dalam interval [a,b] dengan syarat a < b dan f(a).f(b) < 0 (nilai kedua fungsi berbeda tanda. Berhenti jika |f(c)| < 10^-3 atau (b - a) / 2 < 10^-3 (hasil lebih kecil dari galat).
    """

    fa = fungsi(a)
    fb = fungsi(b)
    if fa * fb > 0:
        raise ValueError(f"TNA tidak memenuhi untuk interval [{a}, {b}]")

    delta = (b - a) / 2
    while delta > galat:
        # Cari titik tengah
        c = (a + b) / 2
        fc = fungsi(c)

        if abs(fc) < galat: # Hasil sudah memenuhi galat
            return c
        elif fa*fc < 0: # Pindah interval ke kiri c
            b = c
            fb = fc
        else: # Pindah interval ke kanan c
            a = c
            fa = fc
        
        delta = (b - a) / 2
    
    # Interval sudah memenuhi galat
    return c

def cari_akar(fungsi: callable, a: int, b: int) -> list:
    """
    Mencari semua akar dari fungsi dalam interval [a,b] dengan menerapkan metode bagi dua ke setiap subinterval bilangan bulat yang berubah tanda.
    """

    akar = []
    for x in range(a, b):
        if fungsi(x) * fungsi(x + 1) < 0:
            akar.append(metode_bagi_dua(fungsi, x, x + 1))

    return akar

# Cari titik kritis dan nilainya
titik_kritis = cari_akar(f_turunan_kedua, 0, 8)
titik_kritis.extend([0, 8])
kemiringan = [f_turunan(titik) for titik in titik_kritis]

# Pilih titik minimum dan uji kemiringannya
y_min = min(kemiringan)
if y_min > -math.tan(math.radians(75)):
    status = "memenuhi aturan"
else:
    status = "tidak memenuhi aturan"

# Keluarkan hasil
print(f"Kemiringan lintasan menurun {status}.") 
print(f"Kemiringan minimum pada x ≈ {titik_kritis[kemiringan.index(y_min)]:.4f} dengan kemiringan sebesar y ≈ {y_min:.4f} (≈ {math.degrees(math.atan(y_min)):.4f}°)")
