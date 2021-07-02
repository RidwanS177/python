# -*- coding: utf-8 -*-
"""
Created on Fri Jul  2 01:45:10 2021

@author: Muhammad Ridwan Saputra | 20083000177
"""
import os
ridwan = lambda : os.system('cls')
def saputra(x):
  return list(dict.fromkeys(x))

ulang = 'y'
while (ulang == 'y' or ulang == 'Y'):
    
        #Set Nilai Awal / Default | Ketika Transaksi Baru, Semuanya akan Hilang
        cash = 0
        payback = 0
        makanan = ["Nasi Goreng","Lontong Goreng","Bakso Goreng","Rujak Goreng","Rujak Bakso","Rujak Bakso Pecel"]
        harga_makanan = [15000,14900,12900,13000,15000,17000]
        minuman = ["Teh Dingin/Hangat/Panas","Kopi Dingin","Kopi Teh Panas","Coca Cola Dingin","Coca Cola Panas"]
        harga_minuman = [2500,5000,6500,3500,5000]
        makananku = []
        harga_makananku = []
        porsi_makanan = []
        total_makananku = []
        minumanku = []
        harga_minumanku = []
        porsi_minuman = []
        total_minumanku = []
        pesan = 'y'
        total = []
        mainmenu = ["Makanan","Minuman"]
        
        print("Welcome! Nama Kamu akan kami data sebagai buyer :)")
        nama = input("Siapa Nama Kamu? >> ")
        print("~ Halo " + str(nama) + "! Selamat Berbelanja di Kantin Fakultas Teknologi Informasi!")
        enter = input("~ Klik Enter Untuk Melihat Menu")
        print()
        while (pesan == 'y' or pesan == 'Y'):
            ridwan()
            print("=========================================")
            print(">> KANTIN FAKULTAS TEKNOLOGI INFORMASI <<")
            print(">>>>>> UNIVERSITAS  MERDEKA MALANG <<<<<<")
            print("=========================================")
            cash = sum(total)
            print("Total Belanja Kamu Saat ini = Rp." + format(cash,',.2f'))
            print("=========================================")
            no = 1
            for main in mainmenu:
                print("|>   " + str(no) + ". " + "{:15}".format(str(main)) + "  |")
                no = no + 1
            print("|========================|")
            menu = int(input(">> Btw, Silahkan Pilih Menu yang tersedia >> "))
            print()
            ridwan()
            while menu == 1:
                print("=========================================")
                print(">>>>>>        LIST MAKANAN         <<<<<<")
                print(">> KANTIN FAKULTAS TEKNOLOGI INFORMASI <<")
                print("=========================================")
                a = 1
                b = 0
                print("| = = = NAMA MENU = = = | = = HARGA = = |")
                print("|---------------------------------------|")
                for food in makanan:
                    mkn = harga_makanan[b]
                    print("| "+ str(a) + ". " + "{:19}".format(str(food)) + "|  Rp." + format(mkn,',.2f') + " |")
                    b = b + 1
                    a = a + 1
                print("| 0. Kembali                            |")
                print("=========================================")
                buyfood = int(input(">> Mau Beli Apa (0-6) ? |> "))
                
                if buyfood > len(makanan):
                    print("Menu Tidak Tersedia!")
                    cancel = input("Klik Enter untuk Kembali")
                while (buyfood > 0 and buyfood < len(makanan) + 1):
                    if buyfood == 1:
                        idx = 0
                    if buyfood == 2:
                        idx = 1
                    if buyfood == 3:
                        idx = 2
                    if buyfood == 4:
                        idx = 3
                    if buyfood == 5:
                        idx = 4
                    if buyfood == 6:
                        idx = 5
                    print("NOTE : KAMU TIDAK BISA MEMBELI MENU YANG SAMA LAGI!")
                    confirm = input("Apakah Anda Yakin ingin Membeli " + str(makanan[idx]) + "? (Y/T) >> ")
                    if confirm == 't' or confirm == 'T':
                        cancel = input("Klik Enter untuk Cancel")
                        break
                    else:
                        porsi = int(input("Mau Beli Berapa Porsi? > "))
                        bayar = harga_makanan[idx] * porsi
                        print("Kamu Baru saja membeli " + str(makanan[idx]) + " Sebanyak " + str(porsi) + " Porsi.")
                        total.append(bayar)
                        porsi_makanan.append(porsi)
                        makananku.append(makanan[idx])
                        makanan.pop(idx)
                        harga_makananku.append(harga_makanan[idx])
                        total_makananku.append(harga_makanan[idx] * porsi)
                        harga_makanan.pop(idx)
                        mainmenu.append("Bayar Sekarang")
                        mainmenu = saputra(mainmenu)
                        enter = input("~ Klik Enter Untuk Membeli Menu lain ataupun Bayar")
                        break
                    break
                break
                
                if buyfood == 0:
                    break
                break
                
                
            while menu == 2:
                print("===============================================")
                print(">>>>>>>>>        LIST MINUMAN         <<<<<<<<<")
                print(">>>>> KANTIN FAKULTAS TEKNOLOGI INFORMASI <<<<<")
                print("===============================================")
                a = 1
                b = 0
                print("| = = = = .NAMA MENU. = = = = | = = HARGA = = |")
                print("|---------------------------------------------|")
                for drink in minuman:
                    mnm = harga_minuman[b]
                    print("| "+ str(a) + ". " + "{:25}".format(str(drink)) + "|  Rp." + format(mnm,',.2f') + "  |")
                    b = b + 1
                    a = a + 1
                print("| 0. Kembali                                  |")
                print("===============================================")
                buydrink = int(input(">> Mau Beli Apa (0-5) ? |> "))
                
                if buydrink > len(minuman):
                    print("Menu Tidak Tersedia!")
                    cancel = input("Klik Enter untuk Kembali")
                while (buydrink > 0 and buydrink < len(minuman) + 1):
                    if buydrink == 1:
                        idx = 0
                    if buydrink == 2:
                        idx = 1
                    if buydrink == 3:
                        idx = 2
                    if buydrink == 4:
                        idx = 3
                    if buydrink == 5:
                        idx = 4
                    if buydrink == 6:
                        idx = 5
                    print("NOTE : KAMU TIDAK BISA MEMBELI MENU YANG SAMA LAGI!")
                    confirm = input("Apakah Anda Yakin ingin Membeli " + str(minuman[idx]) + "? (Y/T) >> ")
                    if confirm == 't' or confirm == 'T':
                        cancel = input("Klik Enter untuk Cancel")
                        break
                    else:
                        porsi = int(input("Mau Beli Berapa Porsi? > "))
                        bayar = harga_minuman[idx] * porsi
                        print("Kamu Baru saja membeli " + str(minuman[idx]) + " Sebanyak " + str(porsi) + " Porsi.")
                        total.append(bayar)
                        porsi_minuman.append(porsi)
                        minumanku.append(minuman[idx])
                        minuman.pop(idx)
                        harga_minumanku.append(harga_minuman[idx])
                        total_minumanku.append(harga_minuman[idx] * porsi)
                        harga_minuman.pop(idx)
                        mainmenu.append("Bayar Sekarang")
                        mainmenu = saputra(mainmenu)
                        enter = input("~ Klik Enter Untuk Membeli Menu lain ataupun Bayar")
                        break
                    break
                break
                
                if buydrink == 0:
                    break
                break
                     
            if menu == 3:
                if cash == 0:
                    continue
                else: 
                    confirm = input("Yakin Mau Bayar Sekarang? (Y/T) >> ")
                    if confirm == 't' or confirm == 'T':
                        continue
                    else:
                        print("Total Keseluruhan Belanjanya yaitu Rp." + format(cash,',.2f'))
                        uang = int(input("Masukkan Jumlah Uang Kamu >> "))
                        if uang < cash:
                            print("Uang Anda Tidak Cukup!")
                            enter = input("Anda akan dialihkan ke Menu Utama! Klik Enter.")
                            continue
                        else:
                            payback = uang - cash
                            break
        print("Terima Kasih telah belanja di Kantin Fakultas Teknologi Informasi, " + str(nama) + ".")
        enter = input("Klik Enter Untuk Melihat Rincian Belanja Anda!")
        ridwan()
        print("  STRUK INI SEBAGAI BUKTI PEMBAYARAN YANG SAH")
        print("----------------------------------------------")
        while len(makananku) != 0:
            a = 0
            for foods in makananku:
                pmkn = porsi_makanan[a]
                mknn = harga_makananku[a]
                hmkn = total_makananku[a]
                print("| > " + "{:18}".format(foods),"|")
                print("|   " + str(pmkn) + " X Rp." + format(mknn,',.2f') + "   |   Rp." + format(hmkn,',.2f'))
                print("{:23}".format("|") + "|")
                a = a + 1
            break
        while len(minumanku) != 0:
            a = 0
            for drinks in minumanku:
                pmnm = porsi_minuman[a]
                mnmn = harga_minumanku[a]
                hmnm = total_minumanku[a]
                print("| > " + "{:18}".format(drinks),"|")
                print("|   " + str(pmnm) + " X Rp." + format(mnmn,',.2f') + "    |   Rp." + format(hmnm,',.2f'))
                print("{:23}".format("|") + "|")
                a = a + 1
            break
        print("----------------------------------------------")
        print("|> Nama Pembeli        :   " + str(nama))
        print("|> Total Harga         :   Rp." + format(cash,',.2f'))
        print("|> Bayar (Cash)        :   Rp." + format(uang,',.2f'))
        print("|> Kembali             :   Rp." + format(payback,',.2f'))
        print("----------------------------------------------")
        ulang = input("Mau Membuat Transaksi Baru? (Y/T) >> ")
        if ulang == 't' or ulang == 'T':
            break
        else:
            continue
    
    
                
