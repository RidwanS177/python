# -*- coding: utf-8 -*-
"""
Created on Wed Jun  2 11:56:50 2021

@author: Ridho
"""
print("==================")
print("Menampilan Nilai X")
print("==================")
ulang = 'y'
while ulang == 'y' or 'Y':
    n = input(">> Masukkan Nilai Anda : ")
    x = int(n)
    if x > 100 or x < 0:
        print("Masukkan Nilai 0-100")
        continue
    while x > -1 and x < 101:
        if x >=91 and x<100:
            sts = "A"
        elif x >=81 and x<91:
            sts = "B"
        elif x >=71 and x<81:
            sts = "C"
        else:
            sts = "D"
        print("Nilai Kamu adalah : " + sts)
        break
    ulang = input(">> Mau Ulang Gak? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break