# Super_Cashier_Pacmann
Super Cashier adalah program yang dibuat untuk membantu toko dalam menyediakan layanan self-service. Sehingga dimanapun pelanggan berada dapat melakukan pembelian di toko tanpa harus datang secara langsung.

## Requirements / Objectives
1. Menambahkan barang yang akan dibeli.
2. Menampilkan list barang yang akan dibeli.
3. Edit barang yang akan dibeli pada list:
    - Update nama barang,
    - Update jumlah barang,
    - Update harga,
4. Menghapus barang yang akan dibeli pada list:
    - Delete, atau hapus salah satu barang yang tidak jadi dibeli.
    - Reset, atau hapus semua barang dalam list.
5. Check order barang yang akan dibeli.
    - Jika benar, menampilkan pesan “Pemesanan sudah benar.”
    - Jika salah, menampilkan pesan “Terdapat kesalahan input data.”
6. Menampilkan konfirmasi akhir list belanja (check out).
7. Menampilkan harga total belanja.
8. Memberikan diskon.
    - Jika pembelian > Rp 200.000 mendapatkan diskon 5%
    - Jika pembelian > Rp 300.000 mendapatkan diskon 8%
    - Jika pembelian > Rp 500.000 mendapatkan diskon 10%
   
## Alur Program

## Penjelasan Code

### 1. Inisiasi Class

![1. Inisiasi Kelas.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/1.%20Inisiasi%20Kelas.PNG)

### 2. Main Menu

![2. Main Menu.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/2.%20Main%20Menu.PNG)

### 3. Tambah Barang

![3. Tambah Barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/3.%20Tambah%20Barang.PNG)

### 4. Update Nama barang

![4. Update Nama barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/4.%20Update%20Nama%20barang.PNG)

### 5. Update Jumlah Barang

![5. Update Jumlah Barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/5.%20Update%20Jumlah%20Barang.PNG)

### 6. Update Harga Barang

![6. Update Harga Barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/6.%20Update%20Harga%20Barang.PNG)

### 7. Delete Barang

![7. Delete Barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/7.%20Delete%20Barang.PNG)

### 8. Reset Barang

![8. Reset Barang.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/8.%20Reset%20Barang.PNG)

### 9. Check Belanja

![9. Check Belanja.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/9.%20Check%20Belanja.PNG)

### 10. Konfirmasi

![10. Konfirmasi.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/10.%20Konfirmasi.PNG)

### 11. Total Belanja

![11. Total Belanja.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/11.%20Total%20Belanja.PNG)

### 12. Discount

![12. Discount.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Snippet%20Codes/12.%20Discount.PNG)


## Test Case

### Test Case 1

Customer ingin menambahkan 2 item baru, yaitu:
    - Ayam Goreng, jumlahnya 2, dengan harga 20.000
    - Pasta Gigi, jumlahnya 3, dengan harga 15.000
    
![Test 1.1.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/Test%201.1.PNG)

![Test 1.2.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/Test%201.2.PNG)

### Test Case 2

Customer ingin menghapus Pasta Gigi.

![Test 2.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/Test%202.PNG)

### Test Case 3

Customer ingin menghapus semua belanjanya.

![Test 3.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/Test%203.PNG)

### Test Case 4

Customer ingin menghitung total belanjanya.

![test 4.1.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/test%204.1.PNG)

![Test 4.2.PNG](https://github.com/dimasdwi-s/Super_Cashier_Pacmann/blob/main/Test%20Case/Test%204.2.PNG)

## Future Works

1. Customer tidak perlu input harga, karena sudah ada databasenya.
2. Hapus barang perlu konfirmasi terlebih dahulu, untuk memastikan bukan ketidaksengajaan.
3. Nama barang bisa duplicate tanpa overwrite data sebelumnya (hanya menambahkan jumlahnya saja).
4. Membuat code yang lebih 'clean' .
