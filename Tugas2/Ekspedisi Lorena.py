# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 23:46:34 2021

@author: Muhammad Ridwan Saputra
"""

#Import OS Untuk Perintah Clear Screen
import os
ridwan = lambda : os.system('cls')

#Mengulang Program
ulang = 'y'
while ulang == 'y' or 'Y':
    
    #Nilai Awal
    kode =[1,2]
    kota = ['Surabaya','Bandung']
    jarak = [169,452]
    ongkirperkm = [2500,4000]

    ipt = 1
    while ipt < 2:
        ridwan()
        print ("=====================================================================")
        print("                     TRANSKASI BIAYA EKSPEDISI ")
        print ("=====================================================================")
        print(" Kode :",kode[0],"| Kota :", kota[0], "| Jarak :",jarak[0]," Km | Ongkir : Rp",format(ongkirperkm[0],',.2f'))
        print(" Kode :",kode[1],"| Kota :", kota[1], " | Jarak :",jarak[1]," Km | Ongkir : Rp",format(ongkirperkm[1],',.2f'))
        print ("=====================================================================")
        pilihan = int(input("Masukkan Kota Tujuan (1-2) = "))
        ipt = pilihan
        if ipt <= 2 :
            idx = 0
            while idx >= 0 and idx < 2 :
                idx = idx + 1
                if idx == 0 :
                    pililhan = 1
                    break
                else:
                    idx = pilihan - 1
                    break 

            ongkir = jarak[idx] * ongkirperkm[idx]         
            print('==============================')
            print('Kota         = ',kota[idx])
            print('Jarak        = ',jarak[idx],'Km')
            print('Ongkir PerKm =  Rp',format(ongkirperkm[idx],',.2f'))
            print('==============================')
            print('Total Harga  =  Rp',format(ongkir,',.2f'))          
            print('==============================')
            print("")
            ulang = input('Ingin Mengulang Transaksi? (Y/T) : ')
            if ulang == 't' or ulang == 'T':
                break
    break