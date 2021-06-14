# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 00:27:12 2021

@author: Muhammad Ridwan Saputra
"""

print("====================================")
print("PROGRAM MENGHITUNG TRANSAKSI PRINTER")
print("====================================")
print("HARGA PRINTER EPSON T20 : Rp660.000")
print("====================================")
# Mengulang Program
ulang = 'y'
while ulang == 'y' or 'Y':
    
    # Nilai Awal 
    unit = 0
    harga = 660000
    
    # Input Pembelian
    unit = int(input(">> Jumlah Printer yang dibeli =  "))
    
    # Hitung Total Harga
    total = unit * harga
    
    #Tampilkan Hasil Transaksi
    print("====================================")
    print(">> Anda Telah Membeli " + str(unit) + " Buah Printer")
    print(">> Seharga Rp" + str(total))
    
    #Konfirmasi Ulang Program
    ulang = input("Mau Ulang Gak? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break