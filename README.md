# Proyek Mini Matematika

Repositori ini digunakan untuk menyediakan solusi pemprograman dari Proyek Mini yang dibuat untuk memenuhi tugas mata kuliah Matematika Dasar 1.

## Soal
Seorang insinyur mendesain sebuah lintasan wahana halilintar (*roller coaster*) menggunakan grafik
fungsi

$$
f(x) = -\frac{1}{4} x^2 + \frac{3}{2} x + 3 \sin{x} + 4 \quad \text{untuk} \quad 0 \leq x \leq 8 \text{.}
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
Untuk mencari titik tertinggi (maksimum) dan terendah (minimum) dari lintasan halilintar, kita terlebih dahulu perlu mencari titik kritis dari fungsi tersebut. Titik kritis dalam kasus ini bisa dipersempit menjadi titik stasioner, di mana terbentuk ketika $f\prime (x) = 0$.

Pertama-tama, hitung turunan fungsi tersebut:

$$
f\prime (x) = -\frac{1}{2}x + \frac{3}{2} + 3 \cos{x} \quad \text{untuk} \quad 0 \leq x \leq 8 \text{.}
$$

Untuk menyelesaikan persamaan tersebut, kita menggunakan pendekatan Metode Bagi Dua dengan algoritma sebagai berikut:
1. Untuk setiap interval $[a, b]$, tentukan titik tengah $c = \frac{a + b}{2}$.
2. Jika $|f\prime (c)| < 10^{-3}$ atau $\frac{b - a}{2} < 10^{-3}$, maka pendekatan sudah cukup akurat, berhenti dan keluarkan akar $x = c$.
3. Jika tidak, pilih subinterval $[a, c]$ atau $[b, c]$ di mana terdapat akar dengan ketentuan:
    - Jika $f\prime (a)$ dan $f\prime (c)$ berbeda tanda, pilih subinterval $[a, c]$.
    - Jika tidak, maka $f\prime (c)$ dan $f\prime (b)$ berbeda tanda, pilih subinterval $[c, b]$.
4. Ulangi hingga didapat hasil yang cukup akurat.

Metode ini hanya dapat berlaku berdasarkan Teorema Nilai Antara, di mana $f\prime (a)$ dan $f\prime (b)$ harus berbeda tanda. Sehingga untuk dapat menerapkan metode ini, diperlukan tambahan langkah:
1. Bagi interval awal $[0, 8]$ menjadi subinterval kecil $[i, i + 1]$ dengan $i$ bilangan bulat di antara interval tersebut.
2. Untuk setiap subinterval, cek apakah ada perbedaan tanda dari nilai fungsi keduanya, jika ada, gunakan Metode Bagi Dua.

Setelah menemukan semua titik stasioner, masukkan ke nilai fungsi awal. Nilai maksimum dan minimum bisa ditemukan dengan melihat nilai fungsi pada titik stasioner.

Dari hasil program, didapatkan nilai berikut:  
    
    Perkiraan titik stasioner:
    x0 ≈ 1.7754 | f(x0) ≈ 8.8125
    x1 ≈ 5.0645 | f(x1) ≈ 2.3685
    x2 ≈ 7.1016 | f(x2) ≈ 4.2344
    Perkiraan titik tertinggi: (1.7754, 8.8125)
    Perkiraan titik terendah: (5.0645, 2.3685)


### Subsoal (b)
Misalkan $y = f(x)$ menyatakan ketinggian lintasan diukur dari garis horizontal pada posisi $x$ dari awal lintasan. Perhatikan bahawa tangen sudut kemiringan antara garis singgung pada lintasan menurun dengan garis horizontal (sumbu x) sama dengan gradien garis singgung itu sendiri:

$$
\tan{\theta} = |f\prime (x)| = \frac{dy}{dx}
$$

Aturan menyatakan bahwa lintasan **menurun** tidak boleh memiliki kemiringan lebih dari $75^\circ$, maka bisa dinyatakan:

$$
f\prime (x) \geq - \tan{75^\circ}
$$

Maka untuk memeriksa pemenuhan aturan ini, kita hanya perlu mencari titik ekstrimum minimum dari $f\prime (x)$. Untuk itu, kita perlu mengetahui turunan kedua fungsi awal kita:

$$
f{\prime \prime} (x) = -\frac{1}{2} - 3\sin{x}
$$

Kemudian, dengan cara serupa untuk subsoal (a), kita bisa mendapatkan titik minimum. Selanjutnya, uji kemiringan titik tersebut dengan memasukkannya ke fungsi ke turunan pertama $f\prime (x)$.

Dari hasil program, didapat:

    Kemiringan lintasan menurun memenuhi aturan.
    Kemiringan minimum pada x ≈ 3.3105 dengan kemiringan sebesar y ≈ -3.1126 (≈ -72.1889°)

### Subsoal (c)
Subsoal (c) dapat diselesaikan dengan kalkulator biasa tanpa pemprograman. Secara ringkas, untuk memastikan lintasan mulus di $x = 8$, kita hanya perlu memastikan bahwa $h(x)$ kontinu dan juga  turunannya di $x = 8$. Dengan demikian, dengan menyelesaikan sistem persamaan:

$$
\begin{cases}
h(8) = f(8) \\
h\prime (8) = f\prime (8) \\
\end{cases}
$$

akan didapatkan sistem persamaan dua variabel:

$$
\begin{cases}
Ae^{8B} = -\frac{1}{4} \cdot 8^2 + \frac{3}{2} \cdot 8 + 3 \sin{8} + 4 \\
8Ae^{8B} = -\frac{1}{2} \cdot 8 + \frac{3}{2} + 3 \cos{8} \\
\end{cases}
$$

Dengan galat mutlak kurang dari $10^{-3}$, dapat ditaksir nilai $A$ dan $B$ sebagai berikut:

    A ≈ 8133
    B ≈ -0.989

### Selesai
