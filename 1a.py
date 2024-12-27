import math

def f(x: float) -> float:
    """
    Fungsi lintasan halilintar.  
    f(x) =  -1/4.x^2 + 3/2.x + 3.sin(x) + 4
    """
    return -1/4*x**2 + 3/2*x + 3*math.sin(x) + 4

def f_turunan(x: float) -> float:
    """
    Turunan dari fungsi lintasan menggambarkan gradien.  
    f'(x) = -1/2.x + 3/2 + 3.cos(x)
    """
    return -1/2*x + 3/2 + 3*math.cos(x)


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

# Cari titik stasioner dan nilainya
titik_stasioner = cari_akar(f_turunan, 0, 8)
nilai_akar = [f(titik) for titik in titik_stasioner]

# Cari pasangan titik maksimum dan minimum
y_maks = max(nilai_akar)
y_min = min(nilai_akar)
x_maks = titik_stasioner[nilai_akar.index(y_maks)]
x_min = titik_stasioner[nilai_akar.index(y_min)]

# Keluarkan hasil
print("Perkiraan titik stasioner:")
for i in range(len(titik_stasioner)):
    print(f"x{i} ≈ {titik_stasioner[i]:.4f} | f(x{i}) ≈ {nilai_akar[i]:.4f}")

print(f"Perkiraan titik tertinggi: ({x_maks:.4f}, {y_maks:.4f})")
print(f"Perkiraan titik terendah: ({x_min:.4f}, {y_min:.4f})")