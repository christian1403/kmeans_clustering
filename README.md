# Proyek K-Means Clustering

## Deskripsi Proyek
Proyek ini merupakan implementasi algoritma **K-Means Clustering** menggunakan Python dengan library scikit-learn. Program ini dapat membaca dataset dari file Excel, melakukan clustering data menjadi beberapa kelompok, dan memvisualisasikan hasil clustering dalam bentuk scatter plot.

## Fitur Utama
- 📊 Membaca dataset dari file Excel (.xlsx)
- 🔢 Implementasi algoritma K-Means clustering
- 📈 Visualisasi data asli dan hasil clustering
- 💾 Menyimpan hasil visualisasi sebagai gambar PNG
- 🎯 Menampilkan posisi centroid untuk setiap cluster

## Struktur Proyek
```
k_means/
├── kmeans.py              # Class utama untuk K-Means clustering
├── readData.py            # Class untuk membaca data dari Excel
├── requirements.txt       # Dependencies yang diperlukan
├── README.md             # Dokumentasi proyek
├── dataset/              # Folder berisi dataset
│   └── dataset_kmeans.xlsx
├── result/               # Folder hasil visualisasi
│   ├── scatter_plotting_dataset.png
│   └── hasil_clustering_kmeans.png
└── __pycache__/          # Cache file Python
```

## Requirements
Pastikan Anda memiliki Python 3.x terinstall di sistem Anda. Dependencies yang diperlukan:

- `numpy` - Untuk operasi numerik dan array
- `pandas` - Untuk manipulasi dan analisis data
- `matplotlib` - Untuk plotting dan visualisasi
- `seaborn` - Untuk visualisasi statistik yang lebih menarik
- `scikit-learn` - Untuk implementasi algoritma K-Means
- `openpyxl` - Untuk membaca file Excel

## Instalasi

1. **Clone atau download proyek ini**
   ```bash
   git clone <repository-url>
   cd k_means
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Cara Penggunaan

### 1. Persiapan Dataset
- Pastikan file dataset (`dataset_kmeans.xlsx`) berada di folder `dataset/`
- Dataset harus berformat Excel dengan 2 kolom (koordinat X dan Y)

### 2. Menjalankan Program
```bash
python kmeans.py
```

### 3. Output Program
Program akan menghasilkan:
- **Informasi clustering** di console:
  - Jumlah cluster yang digunakan
  - Koordinat centroid untuk setiap cluster
- **Visualisasi grafik** yang akan ditampilkan secara otomatis
- **File gambar** yang disimpan di folder `result/`:
  - `scatter_plotting_dataset.png` - Visualisasi data asli
  - `hasil_clustering_kmeans.png` - Visualisasi hasil clustering

## Detail Implementasi

### Class `ReadData` (readData.py)
```python
class ReadData:
    def __init__(self, path):        # Inisialisasi dengan path file
    def readDataExcel(self):         # Membaca data dari file Excel
```

**Fungsi:**
- Membaca file Excel menggunakan pandas
- Mengkonversi data menjadi numpy array
- Mengembalikan dataset yang siap diproses

### Class `kmeans` (kmeans.py)
```python
class kmeans:
    def __init__(self, data):        # Inisialisasi dengan dataset
    def read_dataset(self, data):    # Set dataset
    def plot_dataset(self):          # Visualisasi data asli
    def run_kmeans(self, n_clusters, random_state):  # Jalankan K-Means
    def plot_clusters(self):         # Visualisasi hasil clustering
```

**Parameter K-Means:**
- `n_clusters`: Jumlah cluster (default: 3)
- `random_state`: Seed untuk reproducibility (default: 42)

## Contoh Output

### Console Output
```
K-Means berhasil dijalankan!
Jumlah Cluster: 3
Centroids:
[[ 2.5   3.2 ]
 [ 8.1   7.9 ]
 [ 5.0   1.5 ]]
```

### Visualisasi
1. **Scatter Plot Dataset Asli**: Menampilkan distribusi data sebelum clustering
2. **Hasil Clustering**: Menampilkan data yang sudah dikelompokkan dengan warna berbeda dan centroid ditandai dengan marker 'X' berwarna merah

## Kustomisasi

### Mengubah Jumlah Cluster
Edit parameter di `kmeans.py`:
```python
objkmeans.run_kmeans(n_clusters=5)  # Ubah dari 3 menjadi 5 cluster
```

### Menggunakan Dataset Berbeda
1. Tempatkan file Excel baru di folder `dataset/`
2. Update path di `kmeans.py`:
```python
objData = ReadData("dataset/nama_file_baru.xlsx")
```

## Troubleshooting

### Error: ModuleNotFoundError
```bash
pip install -r requirements.txt
```

### Error: File tidak ditemukan
- Pastikan file `dataset_kmeans.xlsx` ada di folder `dataset/`
- Periksa nama file dan path dengan benar

### Error: Folder result tidak ada
Folder `result/` akan dibuat otomatis saat program dijalankan pertama kali.
---
**Dibuat dengan ❤️ Christian Chandra - 06.2024.1.07763**