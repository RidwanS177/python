# -*- coding: utf-8 -*-
"""
Created on Wed Jun  9 13:59:40 2021
@author: Muhammad Ridwan Saputra
"""
print("=============================")
print("PROGRAM MENGECEK KELULUSAN")
print("=============================")
ulang = 'y'
while ulang == 'y' or 'Y':
    n = input("Masukkan Nilai Anda : ")
    if n > 100 or n < 0:
        print("Salah Input, Masukkan Nilai 0-100!")
        continue
    if int(n) > 60:
        sts = "Lulus"
    else:
        sts = "Tidak Lulus"
    print("Anda Dinyatakan " + sts)
    ulang = input("Mau Ulang Gak? Y/N : ")
    if ulang == 'n':
        break
