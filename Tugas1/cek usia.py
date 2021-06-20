# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:06:31 2021
@author: Muhammad Ridwan Saputra
"""

print("=============================")
print("PROGRAM MENGECEK TINGKAT USIA")
print("=============================")
ulang = 'y'
while ulang == 'y' or 'Y':
    usia = input("Masukkan Usia Anda : ")
    u = int(usia)
    if u >= 60:
        sts = "Lansia"
    elif u >= 35:
        sts = "Dewasa"
    elif u >= 18:
        sts = "Pemuda"
    elif u >= 15:
        sts = "Remaja"
    else:
        sts = "Anak-Anak"
    print("Status Usiamu Yaitu " + sts)
    ulang = input("Mau Ulang Gak? Y/N : ")
    if ulang == 'n':
        break
