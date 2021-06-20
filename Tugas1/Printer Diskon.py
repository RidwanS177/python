# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 00:39:30 2021

@author: Muhammad Ridwan Saputra
"""

print("================================================")
print("      PROGRAM MENGHITUNG TRANSAKSI PRINTER      ")
print("================================================")
print("       HARGA PRINTER EPSON T20 : Rp660.000      ")
print("PROMO ! BELANJA DIATAS 1.5 JUTA DAPAT DISKON 15%")
print("================================================")
# Mengulang Program
ulang = 'y'
while ulang == 'y' or 'Y':
    
    # Nilai Awal 
    unit = 0
    harga = 660000
    diskon = 0.15
    
    # Input Pembelian
    unit = int(input(">> Jumlah Printer yang dibeli =  "))
    
    # Hitung Total Harga
    total = unit * harga
    
    # Cek Diskon
    if total > 1500000:
        total2 = total * diskon
    else:
        total2 = 0
    
    #Hitung Keseluruhan
    subtotal = total - total2
    
    #Tampilkan Hasil Transaksi
    print("====================================")
    print(">> Anda Telah Membeli " + str(unit) + " Buah Printer")
    print(">> Seharga Rp" + str(total))
    print("======================")
    print("Kamu Hemat Rp" + str(total2))
    print("Subtotal Rp" + str(subtotal))
    print("======================")
    
    #Konfirmasi Ulang Program
    ulang = input("Mau Ulang Gak? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break
