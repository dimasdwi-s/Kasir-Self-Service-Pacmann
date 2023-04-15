#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from tabulate import tabulate

class Transaksi:
  def __init__(self):
      '''
      fungsi untuk menginisialisasi dictionary list belanja
      '''
      self.list_belanja=dict()  

  def tambah_barang(self):
      '''
      fungsi untuk menambahkan barang yang akan dimasukkan ke list_belanja

      parameter
      nama_barang      : str   nama barang
      jumlah_barang    : int   jumlah barang
      harga_barang     : int   harga satuan barang
      '''
      
      nama_barang = str(input("Masukkan nama barang yang ingin dibeli: ")).title()
      if nama_barang.isdigit() == False:      
         try:
             jumlah_barang = int(input("Masukkan jumlah barang yang ingin dibeli: ")) #cek apakah jumlah adalah angka
             try:
                harga_barang= int(input("Masukkan harga satuan barang yang ingin dibeli: ")) #cek apakah harga adalah angka
             except:
                 print("Gagal memasukkan harga barang. Harga wajib berupa angka! \nSilahkan Ulangi Lagi")
             else:
                 self.list_belanja.update({nama_barang:[jumlah_barang,harga_barang,jumlah_barang*harga_barang]})
                 print("Barang berhasil dimasukkan ke dalam list belanja!")
                 self.pilihan_menu()                   
         except:
                print("Jumlah barang wajib berupa angka! \nSilahkan Ulangi Lagi")
      else:
         print("Nama barang wajib berupa text! \nSilahkan Ulangi Lagi")
              
      
  def update_nama_barang(self):
      '''
      fungsi untuk memperbaharui nama barang di dalam list_belanja
      parameters
      nama_barang   : str   nama barang yang ingin diubah
      nama_new      : str   nama barang yang baru
      '''
      
      nama_barang = input("Masukkan nama barang yang ingin diubah: ").title()
            
      try: # cek input dalam nama_barang
          nama_new = input("Masukkan nama barang baru: ").title()
          temp = self.list_belanja[nama_barang]
          self.list_belanja.pop(nama_barang)
          self.list_belanja.update({nama_new: temp})
          self.pilihan_menu()
             
      except: # nama barang tidak boleh kosong
          print("Gagal mengubah barang. \nNama barang tidak ditemukan! \nSilakan Ulangi Lagi")

  def update_jumlah_barang(self):
      '''
      fungsi untuk memperbaharui jumlah barang di dalam list_belanja
      parameters
      nama_barang      : str   nama barang yang jumlahnya ingin diubah
      jumlah_new       : int   jumlah barang yang baru
      '''
      nama_barang = input("Masukkan nama barang yang jumlahnya ingin diubah: ").title()
      try: # cek apakah barang ada di list_belanja
          jumlah_new = int(input("Masukkan jumlah barang yang baru: "))

          self.list_belanja[nama_barang][0] = jumlah_new
          self.list_belanja[nama_barang][2] = self.list_belanja[nama_barang][0] * self.list_belanja[nama_barang][1]
          self.pilihan_menu()
     
      except: # kalau barang tidak ada di list_belanja maka gagal
          print("Gagal mengubah jumlah barang. \nNama barang tidak ditemukan! \nSilahkan Ulangi Lagi")

  def update_harga_barang(self):
      '''
      fungsi untuk memperbaharui harga barang di dalam list_belanja
      parameters
      nama_barang     : str   nama barang yang harganya ingin diubah
      harga_new       : int   harga barang yang baru
      '''
      nama_barang = input("Masukkan nama barang yang harganya ingin diubah: ").title()
      try: # cek apakah barang ada di list_belanja
          harga_new = int(input("Masukkan harga barang yang baru: "))

          self.list_belanja[nama_barang][1] = harga_new
          self.list_belanja[nama_barang][2] = self.list_belanja[nama_barang][0] * self.list_belanja[nama_barang][1]
          self.pilihan_menu()
      except: # kalau barang tidak ada di list_belanja maka gagal
          print("Gagal mengubah harga barang. \nNama barang tidak ditemukan! \nSilahkan Ulangi Lagi")

  def delete_barang(self):
      '''
      fungsi untuk menghapus salah satu barang dalam list_belanja
      '''
      nama_barang = input("Masukkan nama barang yang ingin dihapus: ").title()
      try:
          del self.list_belanja[nama_barang]
          self.pilihan_menu()
      except:
          print("Gagal menghapus barang. \nNama barang tidak ditemukan.\n")

  def reset_list_belanja(self):
      '''
      fungsi untuk menghapus seluruh barang yang ada di dalam list_belanja
      '''
      self.list_belanja.clear()
      print("List belanja berhasil dikosongkan! \nSemua barang berhasil dihapus!\n ")
      self.pilihan_menu()

  def check_list_belanja(self):
      '''
      fungsi untuk menampilkan barang yang sudah diinput dan akan dibeli
      '''
      if (len(self.list_belanja) == 0):
          print('List Belanja Anda Kosong') #menampilkan pesan ketika tidak ada barang di list_belanja

      else:
            '''
            menampikan list belanja berisi barang yang sudah diinput dengan tabulate
            '''
            tabel_list_belanja = []
            headers = ['No','Nama Barang','Jumlah Barang', 'Harga Satuan', 'Jumlah']
            tabel_list_belanja.append(headers)

            n = 0
            
            for key, value in self.list_belanja.items():
                n+=1
                table_no = n
                nama_barang = key
                jumlah_barang = value[0]
                harga_barang = value[1]
                jumlah_harga = value[2]
                
                item_data = [table_no, nama_barang, jumlah_barang, harga_barang, jumlah_harga]

                tabel_list_belanja.append(item_data)
            
            print(tabulate(tabel_list_belanja, headers="firstrow"))
            

  def konfirmasi(self):
      '''
      fungsi untuk konfirmasi apakah input pada list belanja sudah sesuai dengan yang diinginkan. 
      bisa dilakukan sebelum pembayaran.
      '''
      for key, value in self.list_belanja.items():
        nama_barang = key
        jumlah_barang = value[0]
        harga_barang = value[1]
        jumlah_harga = value[2]
    
      if type(nama_barang) == str and type (jumlah_barang) == int and type(harga_barang) == int:
          print(f"Berikut list belanja kamu, periksa lagi sebelum membayar [\u2713]!")      
          self.pilihan_menu()

      else:
          print(f"'\u2715': Terdapat kesalahan input. \nSilahkan input ulang belanja Anda!")
        
  def total_belanja(self):
      '''
      fungsi untuk menghitung total belanja
      dimungkinkan untuk mendapatkan diskon jika nilai is_discounted bernilai True
      besar diskon akan dihitung pada fungsi lain
      '''
      self.total_belanja = 0
      for value in self.list_belanja.values():
          jumlah_barang = value [0]
          harga_barang = value [1]
          self.total_belanja += (jumlah_barang*harga_barang)
            
      is_discounted, discount = self.is_discounted(self.total_belanja)
      self.final_price = self.total_belanja * (1-discount)

      if is_discounted == True:
         print(f'Total belanja kamu adalah sebesar Rp {self.total_belanja:,}.')
         print(f'Selamat! Kamu mendapatkan diskon sebesar {discount*100}%.')
         print(f'Total harga setelah diskon adalah sebesar Rp {self.final_price:,}.')

      else:
           print(f'Total belanja kamu adalah sebesar Rp {self.total_belanja:,}.')
           print("Kamu akan mendapatkan potongan harga jika belanja lebih dari Rp 200.000")
    
   
  def is_discounted(self, total_belanja):
        '''
        fungsi untuk menghitung besaran diskon yang didapatkan oleh user
         '''
        self.total_belanja = total_belanja
        # tidak mendapat diskon jika total belanja < 200_000
        if self.total_belanja <= 200_000:
           is_discounted = False
           discount = 0.0
        
        else:
           is_discounted = True
           # mendapat diskon 10% jika belanja > 500_000
           if self.total_belanja > 500_000: 
              discount = 0.1
              # mendapat diskon 8% jika belanja > 300_000
           elif self.total_belanja > 300_000:
              discount = 0.08
              # mendapat diskon 5% jika belanja > 200_000
           elif self.total_belanja > 200_000:
              discount = 0.05

        return is_discounted, discount


  def pilihan_menu(self):
      print('-'*45)
      print("List belanja kamu: ")
      self.check_list_belanja()
      print('-'*45)

      list_menu = {"1": self.tambah_barang,
                   "2": self.update_jumlah_barang,
                   "3": self.update_harga_barang,
                   "4": self.delete_barang,
                   "5": self.reset_list_belanja,
                   "6": self.konfirmasi,
                   "7": self.total_belanja,
                  }
      input_pilihan = input ('Pilih Menu Transaksi yang diinginkan: \n1.Tambah Barang \n2.Update Jumlah Barang \n3.Update Harga Barang \n4.Hapus Salah Satu Barang \n5.Hapus Seluruh Barang \n6.Konfirmasi Belanja \n7.Total Bayar \nKetik disini: ')
      if input_pilihan in list_menu:
         pass
      else:
        print("Tidak ada di pilihan, silahkan input ulang!")
        self.pilihan_menu()
      return list_menu[input_pilihan]()

