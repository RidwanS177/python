# -*- coding: utf-8 -*-
"""
Created on Mon Jun 14 23:11:20 2021

@author: Muhammad Ridwan Saputra
"""

print("====================================")
print(" JASA KIRIM BARANG EKSPEDISI LORENA ")
print("====================================")
print(">> SILAHKAN PILIH LOKASI TUJUAN ANDA")
print("====================================")
print("1. SURABAYA | 169 KM | Rp2500 per KM")
print("2. BANDUNG  | 452 KM | Rp4000 per KM")
print("3. SEMARANG | 385 KM | Rp3500 per KM")
print("4. DENPASAR | 215 KM | Rp4500 per KM")
print("====================================")

# Mengulang Program
ulang = 'y'
while ulang == 'y' or 'Y':
    
    # Input
    pilih = int(input(">> Pilih Lokasi Tujuan (1 - 4) : "))
    
    # Jika Pilih Bukan 1-4, Muncul Pesan Error
    if pilih < 1 or pilih > 4 :
        print("Salah Input, Masukkan Angka 1-4 !")
        continue
        
    # Lakukan Selama Pilih 1-4
    while pilih > 0 and pilih < 5:
        if pilih == 1:
            x = 0
        elif pilih == 2:
            x = 1
        elif pilih == 3:
            x = 2
        else:
            x = 3
        
        kota = ['Surabaya','Bandung','Semarang','Denpasar']
        jarak = [169, 452, 385, 215]
        tarif = [2500, 4000, 3500, 4500]
        
        # Menghitung
        total = jarak[x] * tarif[x]
        
        # Tampilan Hasil
        print("====================================")
        print(">> Kota Tujuan Anda : " + kota[x])
        print(">> Jarak Kota " + kota[x] + " : " + str(jarak[x]) + " KM")
        print(">> Harga Ongkir Per KM dari " + kota[x] + " : Rp" + str(tarif[x]))
        print("====================================")
        print("Total Keseluruhan Ongkir : Rp" + str(total))
        print("====================================")        
        break
    
    # Konfirmasi Ulang Program
    ulang = input(">> Mau Ulang Gak? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break
