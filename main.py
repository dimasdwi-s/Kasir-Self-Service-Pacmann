#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tabulate import tabulate
from transaksi import Transaksi

# Jalankan program cashier
print(tabulate([ ],headers=['Selamat Datang di Layanan Self Service Pac Mart']))

# buat input kode transaksi dengan input name user 
data_transaksi=input("Silakan Masukkan Nama Terlebih Dahulu: ").title()
print('-'*45)
print(f'Selamat Berbelanja, Kak {data_transaksi}!' )
print('-'*45)

# Jalankan menu transaksi dari modul Transaksi
data_transaksi=Transaksi()
data_transaksi.pilihan_menu()

