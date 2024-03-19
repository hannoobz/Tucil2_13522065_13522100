# Tucil2_13522065_13522100
Tugas Kecil 2 IF2211 Strategi Algoritma -  Divide and Conquer

## Table of Contents
* [Anggota](#anggota)
* [Deskripsi Singkat](#deskripsi-singkat)
* [Screenshots](#screenshots)
* [Cara Compile Program](#cara-compile-program)
* [Cara Menjalankan Program](#cara-menjalankan-program)
* [Usage](#usage)

## Anggota 
1. Rafiki Prawira Harianto (13522065)
2. M Hanief Fatkhan Nashrullah (13522100)

## Deskripsi Singkat
Program simulasi Bézier Curve dengan algoritma Divide and Conquer, dengan algoritma Brute Force sebagai pembanding.

## Screenshots
![Screenshot Program](https://cdn.discordapp.com/attachments/669015264242958339/1219330480990589028/image.png?ex=660ae900&is=65f87400&hm=93ddc43c129044c74aa70345f8399981e130042c48611f085a4585185f873070&)

## Cara Compile Program
1. Pastikan python3 sudah terpasang
2. Pastikan module tkinter dan pyinstaller sudah terpasang
3. Masuk ke folder ./src
4. Buka terminal
5. Jalankan perintah berikut
```
pyinstaller --onefile GUI.py
```

## Cara Menjalankan Program
- Masuk ke ./bin
- Run GUI.exe atau GUI_Ubuntu

## Usage
- Klik 2 kali pada kanvas untuk menambah poin
- Poin dapat dipindahkan dengan drag and drop
- Terdapat Options di kanan atas program sebagai pengaturan program
- Posisi setiap poin dapat diatur, pilih poin pada Control Point dan pilih XY Coordinate untuk mengatur posisi poin
- Kurva dapat diatur menggunakan Opsi Iterations. Semakin banyak iterations, semakin halus kurvanya
- Jika menggunakan checkbox "Use Brute Force?", Opsi Iterations akan berubah menjadi increment. Semakin rendah increment, semakin halus kurvanya
- Klik "Keep Previous Iteration?" Untuk menggambarkan iteration sebelumnya pada kurva. Atur Opsi Iterations setelah klik tombol ini untuk melihatnya
- Label "Points:" melambangkan jumlah poin di dalam kurva
- Label "Runtime:" melambangkan waktu eksekusi program
- Klik Tombol "Reset" untuk menghapus kanvas
