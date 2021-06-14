# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 14:06:31 2021
@author: Muhammad Ridwan Saputra
"""
print("=======================")
print("MENAMPILKAN NILAI HURUF")
print("=======================")
ulang = 'y'
while ulang == 'y' or 'Y':
    n = input("Masukkan Nilai Anda = ")
    u = int(n)
    if u > 100 or u < 0:
        print("Salah Input, Masukkan Nilai 0-100!")
        continue
    while u<101:
        if u>80:
            status = "BAIK SEKALI"
        elif u>=65:
            status = "BAIK"
        elif u>=55:
            status = "CUKUP"
        elif u>=40:
            status = "KURANG"
        else:
            status = "KURANG SEKALI"
        print("Status = " + status)
        break
    ulang = input("Mau Ulang? Y/N : ")
    if ulang == 'n':
        break