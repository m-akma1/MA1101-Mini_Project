# Proyek Mini Matematika


## Deskripsi
Repositori ini digunakan untuk menyediakan solusi pemprograman dari  Proyek Mini yang dibuat untuk memenuhi tugas mata kuliah Matematika Dasar 1.

## Soal
Seorang insinyur mendesain sebuah lintasan wahana halilintar (*roller coaster*) menggunakan grafik
fungsi

$$
f(x) = -\frac{1}{4} x^2 + \frac{3}{2} x + 3 \sin(x) + 4 \quad \text{untuk} \quad 0 \leq x \leq 8 \text{.}
$$

### Subsoal (a)
Tentukan titik tertinggi dan terendah dari lintasan *roller coaster* tersebut pada interval $[0, 8]$ Gunakan metode bagi dua (berdasarkan Teorema Nilai Antara) untuk menaksir titik stasioner dengan galat mutlak kurang dari $10^{-3}$.

### Subsoal (b)
Agar turunan lintasan tidak terlalu curam, terdapat aturan keselamatan yang menyatakan bahwa sudut yang dibentuk oleh garis singgung pada titik di lintasan menurun dengan garis horisontal tidak boleh lebih dari $75^\circ$. Periksa apakah lintasan di atas memenuhi aturan tersebut atau tidak.

(Petunjuk: Kandidat titik dengan kemiringan minimum dapat ditaksir dengan metode bagi dua.)

### Subsoal (c)
Anda diminta oleh insinyur tersebut untuk mendesain lanjutan dari lintasan tersebut untuk $8 ≤ x ≤ 12$ Agar cepat melandai, dipilih fungsi eksponensial, yakni 

$$
h(x) = Ae^{Bx} \quad \text{untuk} \quad 8 \leq x \leq 12 \text{.}
$$

Tentukan nilai A dan B agar lintasan tersebut tetap mulus di $x = 8$. Berikan jawaban Anda dalam bentuk taksiran nilai A dan B dengan galat mutlak kurang dari $10^{-3}$.

## Solusi
### Subsoal (a)
Untuk mencari titik tertinggi (maksimum) dan terendah (minimum) dari lintasan halilintar, kita terlebih dahulu perlu mencari titik kritis dari fungsi tersebut. Titik kritis dalam kasus ini bisa dipersempit menjadi titik stasioner, di mana terbentuk ketika $f'(x) = 0$.

Pertama-tama, hitung turunan fungsi tersebut:

$$
f'(x) = -\frac{1}{2}x + \frac{3}{2} + 3 \cos(x) \quad \text{untuk} \quad 0 \leq x \leq 8 \text{.}
$$

Untuk menyelesaikan persamaan tersebut, kita menggunakan pendekatan Metode Bagi Dua dengan algoritma sebagai berikut:
1. Untuk setiap interval $[a, b]$, tentukan titik tengah $c = \frac{a + b}{2}$.
2. Jika $|f'(c)| < 10^{-3}$ atau $\frac{b - a}{2} < 10^{-3}$, maka pendekatan sudah cukup akurat, berhenti dan keluarkan akar $x = c$.
3. Jika tidak, pilih subinterval $[a, c]$ atau $[b, c]$ di mana terdapat akar dengan ketentuan:
    - Jika $f'(a)$ dan $f'(c)$ berbeda tanda, pilih subinterval $[a, c]$.
    - Jika tidak, maka $f'(c)$ dan $f'(b)$ berbeda tanda, pilih subinterval $[c, b]$.
4. Ulangi hingga didapat hasil yang cukup akurat.

Metode ini hanya dapat berlaku berdasarkan Teorema Nilai Antara, di mana $f'(a)$ dan $f'(b)$ harus berbeda tanda. Sehingga untuk dapat menerapkan metode ini, diperlukan tambahan langkah:
1. Bagi interval awal $[0, 8]$ menjadi subinterval kecil $[i, i + 1]$ dengan $i$ bilangan bulat di antara interval tersebut.
2. Untuk setiap subinterval, cek apakah ada perbedaan tanda dari nilai fungsi keduanya, jika ada, gunakan Metode Bagi Dua.

Setelah menemukan semua titik stasioner, masukkan ke nilai fungsi awal. Nilai maksimum dan minimum bisa ditemukan dengan melihat nilai fungsi pada titik stasioner.