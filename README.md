# Optimasi Manajemen Berbasis Data – ITB STIKOM Bali Kampus Abiansemal  
*Portofolio Proyek Akhir S1 Sistem Informasi*  

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Afiq%20Andico-blue)](https://www.linkedin.com/in/afiqandico13)  
[![GitHub Stars](https://img.shields.io/github/stars/afiqandico13/optimasi-manajemen-itb-stkom-bali?style=social)](https://github.com/afiqandico13/optimasi-manajemen-itb-stkom-bali/stargazers)  
[![GitHub Forks](https://img.shields.io/github/forks/afiqandico13/optimasi-manajemen-itb-stkom-bali?style=social)](https://github.com/afiqandico13/optimasi-manajemen-itb-stkom-bali/network/members)  
[![GitHub Issues](https://img.shields.io/github/issues/afiqandico13/optimasi-manajemen-itb-stkom-bali)](https://github.com/afiqandico13/optimasi-manajemen-itb-stkom-bali/issues)  
[![GitHub Last Commit](https://img.shields.io/github/last-commit/afiqandico13/optimasi-manajemen-itb-stkom-bali)](https://github.com/afiqandico13/optimasi-manajemen-itb-stkom-bali/commits/main)  
[![Python Version](https://img.shields.io/badge/python-3.11%20%7C%203.12-blue)](https://www.python.org/downloads/)  
[![Orange Data Mining](https://img.shields.io/badge/Orange-Data%20Mining-green)](https://orangedatamining.com/)  

---

## 📖 Pendahuluan

Penelitian ini bertujuan mengoptimalkan tiga aspek kritis manajemen kampus — **Marketing, Sumber Daya Manusia (SDM), dan Operasional** — dengan menggunakan pendekatan *data science* berbasis klasifikasi pada platform **Orange Data Mining**. Hasil penelitian menunjukkan bahwa:

- **Marketing**: Konten *Reels* meningkatkan engagement sebesar **71 %** (akurasi model Random Forest = 94 %).  
- **SDM**: Ketidakhadiran adalah faktor dominan kinerja (akurasi Decision Tree = 77 %).  
- **Operasional**: **13,6 %** transaksi pengadaan tidak efisien (SVM/k‑NN), berpotensi menghemat **IDR 2,3 jt/bulan**.

Repository ini menyimpan seluruh artefak penelitian dalam format yang dapat dijalankan, dimodifikasi, dan dibangun kembali oleh siapa saja — khususnya praktisi data, akademisi, dan manajer institusi pendidikan yang ingin menerapkan analisis berbasis data tanpa harus menguasai pemrograman kompleks.

---

## 🏗️ Struktur Proyek

```text
optimasi-manajemen-itb-stkom-bali/
│
├─ .gitignore               # File dan folder yang diabaikan oleh Git
├─ LICENSE                  # Lisensi MIT
├─ README.md                # Dokumen ini
├─ requirements.txt         # Dependensi Python utama
├─ requirements-dev.txt     # Dependensi tambahan untuk development (testing, docs, dll.)
│
├─ data/                    # ✅ Data sintetis (anonimis) untuk demonstrasi
│   ├─ marketing_sample.csv
│   ├─ hr_sample.csv
│   └─ ops_sample.csv
│
├─ workflows/               # ⚙️ Implementasi algoritma yang diekspor dari Orange (Python)
│   ├─ marketing_reels.py          # Random Forest – prediksi engagement Instagram (Reels vs Post)
│   ├─ hr_decision_tree.py         # Decision Tree – klasifikasi kinerja staf
│   └─ ops_svm_knn.py              # SVM + k‑NN – deteksi pembelian tidak efisien
│
├─ docs/                    # 📚 Dokumentasi naratif (Markdown)
│   ├─ abstract.md          # Abstrak lengkap (ID & EN)
│   ├─ methodology.md       # Metodologi, preprocessing, modellng, evaluasi
│   ├─ results.md           # Hasil numerik, visualisasi, interpretasi
│   └─ recommendations.md   # Rekomendasi strategis berbasis temuan
│
├─ dashboard/               # 🖼️ Visualisasi & ekspor Orange
│   ├─ dashboard_preview.png   # Screenshot tampilan dashboard Orange
│   └─ dashboard_export.json   # (Opsional) file JSON yang dapat di‑import ke Orange
│
├─ scripts/                 # 🛠️ Skrip bantuan
│   ├─ demo.py              # Menjalankan ketiga workflow sekaligus & menampilkan output
│   ├─ train_and_evaluate.py # Skrip umum untuk pelatihan & evaluasi (jika diperlukan)
│   └─ demo_notebook.ipynb  # Jupyter notebook demonstrasi lengkap (visualisasi, markdown)
│
└─ results/                 # 📊 Output numerik (confusion matrix, feature importance, dll.)
    ├─ metrics_marketing.json
    ├─ feature_importance_hr.csv
    └─ ops_efficiency_summary.txt
```

> **Catatan**: Folder `data/` hanya berisi *synthetic data* untuk menunjukkan alur kerja. Data asli dari kampus tidak disebarkan karena alasan konfidentialitas dan kebijakan data institusional. Anda dapat menggantinya dengan dataset sendiri (memastikan kolom nama sama) untuk reproducing hasil penelitian sebenarnya.

---

## 🚀 Memulai (Langkah‑ demi‑Langkah)

### 1️⃣ Prasyarat

- **Python 3.11+** (disarankan menggunakan [pyenv] atau [conda])
- **Git** (untuk meng-clone repository)
- **(Opsional)** [Orange Data Mining](https://orangedatamining.com/) versi 3.36+ jika Anda ingin melihat atau mengubah workflow `.ows` asli.

### 2️⃣ Clone Repository

```bash
git clone https://github.com/afiqandico13/optimasi-manajemen-itb-stkom-bali.git
cd optimasi-manajemen-itb-stkom-bali
```

### 3️⃣ Siapkan Lingkungan Virtual (Direkomendasikan)

```bash
# Menggunakan venv bawaan Python
python -m venv venv
# Aktivasi
# Windows:
.\venv\Scripts\activate
# macOS / Linux:
source venv/bin/activate
```

### 4️⃣ Instal Dependensi

```bash
pip install --upgrade pip
pip install -r requirements.txt
# Untuk development / testing (opsional)
pip install -r requirements-dev.txt
```

`requirements.txt` berisi minimal:

```
pandas
scikit-learn
```

`requirements-dev.txt` menambahkan:

```
jupyterlab
matplotlib
seaborn
pytest
black
flake8
```

### 5️⃣ Jalankan Demonstrasi

```bash
python scripts/demo.py
```

Skrip ini akan:

1. Memuat ketiga kumpulan data sintetis dari folder `data/`.
2. Melatih dan mengevaluasi masing‑masing model:
   - `marketing_reels.py` → Random Forest
   - `hr_decision_tree.py` → Decision Tree
   - `ops_svm_knn.py` → SVM + k‑NN
3. Mencetak akurasi, laporan klasifikasi (precision, recall, f1‑score) ke terminal.
4. Menyimpan ringkasan metrik ke folder `results/` (jika Anda mengaktifkan fitur penyimpanan dalam skrip).

### 6️⃣ Melihat Dokumentasi

Buka file-file di folder `docs/` dengan teks editor atau render di GitHub:

- **Abstrak** – `docs/abstract.md`
- **Metodologi** – `docs/methodology.md` (terinci: preprocessing, pemilihan model, validasi, enkripsi data SDM, dll.)
- **Hasil** – `docs/results.md` (nilai akurasi, confusion matrix, feature importance, visualisasi)
- **Rekomendasi** – `docs/recommendations.md` (Content Calendar, SWOT, Gap Analysis, rencana tindakan)

### 7️⃣ Visualisasi Dashboard (Opsional)

Jika Anda telah menginstal Orange:

1. Buka aplikasi **Orange**.
2. `File → Open` dan pilih salah satu file `.ows` yang ada di `workflows/` (jika Anda menyertakan file asli; saat ini placeholder berupa skrip Python).
3. Atau impor `dashboard/dashboard_export.json` (jika disediakan) untuk memuat tampilan persis seperti yang digunakan dalam penelitian.
4. Lihat widget: Confusion Matrix, ROC Curve, Scatter Plot, Heatmap, dan sebagainya.

### 8️⃣ Menjalankan Notebook Demonstrasi (Jika Ingin Lebih Interaktif)

```bash
jupyter lab
```

Buka `scripts/demo_notebook.ipynb` yang berisi:

- Penjelasan langkah demi langkah pemrosesan data.
- Visualisasi distribusi fitur (sebaran likes, absensi, harga).
- Pelatihan model dengan `scikit-learn` dan plotting hasil (confusion matrix, ROC curve).
- Ekspor hasil ke format CSV/JSON untuk dokumentasi.

---

## 📊 Hasil Utama (Ringkasan)

| Domain        | Algoritma               | Akurasi (± std) | Presisi (± std) | AUC (± std) | Temuan Kunci |
|---------------|-------------------------|-----------------|-----------------|-------------|--------------|
| **Marketing** | Random Forest (n=100)   | **94 %** ±1.2%  | 92.5 % ±1.5%    | 0.96 ±0.02  | Reels meningkatkan engagement 71 % |
| **SDM**       | Decision Tree (max_depth=3) | **77 %** ±2.0%  | 75.3 % ±2.3%    | 0.81 ±0.03  | Ketidakhadiran = faktor dominan |
| **Operasional**| SVM (linear) + k‑NN (k=5) | **82 %** ±1.8%  | 80.1 % ±2.0%    | 0.88 ±0.02  | 13,6 % transaksi tidak efisien → potensi hemat IDR 2,3 jt/bulan |

> Angka di atas dihasilkan dari data asli tesis (Februari‑April 2025). Dalam demonstrasi dengan data sintetis, nilai akurasi mungkin berbeda karena ukuran sampel yang sangat kecil; struktur dan logika tetap sama.

---

## 📝 Cara Berkontribusi

Kami menyambut kontribusi dari komunitas! Jika Anda ingin:

- Memperbaiki bug
- Menambahkan fitur (misalnya, visualisasi lebih interaktif, export ke Power BI)
- Menyediakan dataset sampel yang lebih realistis
- Meningkatkan dokumentasi

Silakan ikuti alur berikut:

1. **Fork** repositori ini.
2. Buat branch baru: `git checkout -b fitur/nama-fitur`.
3. Lakukan perubahan Anda.
4. Pastikan semua test (jika ada) masih lolos: `pytest`.
5. Commit dengan pesan jelas: `git commit -m "feat: tambahkan visualisasi confusion matrix"`.
6. Push ke branch Anda: `git push origin fitur/nama-fitur`.
7. Buka **Pull Request** ke branch `main` ini.

Pastikan untuk mengikuti gaya kode yang ada (gunakan `black` dan `flake8` melalui `pre-commit` jika Anda menginstal `requirements-dev.txt`).

---

## 📄 Lisensi

Proyek ini dilisensikan di bawah [MIT License](LICENSE). Anda bebas menggunakan, menyalin, mengubah, mendistribusikan, dan menjualnya, asal mencantumkan hak cipta dan pemberitahuan lisensi tersebut.

---

## 📬 Kontak

- **Nama**: Afiq Andico Pangimpian  
- **Email**: afiqandico13@gmail.com  
- **LinkedIn**: [linkedin.com/in/afiqandico13](https://www.linkedin.com/in/afiqandico13)  
- **GitHub**: [github.com/afiqandico13](https://github.com/afiqandico13)  

Jika Anda memiliki pertanyaan mengenai metodologi, hasil, atau cara menggunakan repository ini, jangan ragu untuk menghubungi saya melalui salah satu saluran di atas.

---

## 🙏 Terima Kasih

Terima kasih telah mengeksplorasi pekerjaan ini. Semoga repository ini bermanfaat sebagai acuan untuk menerapkan analisis data yang *actionable* di lingkungan pendidikan atau organisasi lain. Jika Anda menemukan repositori ini membantu, silakan beri ⭐, fork, dan sebarkan untuk komunitas yang lebih luas!

--- 

*© 2025 Afiq Andico Pangompian. Dirilis onder Lisensi MIT.*  
*Last updated: 2025-06-29*