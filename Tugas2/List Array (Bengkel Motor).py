# -*- coding: utf-8 -*-
"""
Created on Tue Jun 15 19:51:16 2021

@author: Muhammad Ridwan Saputra
"""

#MENGULANG PROGRAM
ulang = 'y'
while ulang == 'y' or 'Y':
    
    #NILAI AWAL
    diskon = 0.05
    ppn = 0.01
    mindiskon = 200000

    #Harga Awal
    merk = ['Duration SW20',"Castrol Magnatec","Federal Supreme XX","Yamalube","Shell"]
    harga = [53000,50000,54000,45000,46000]
    
    #JUDUL PROGRAM
    print("{:^38}".format("================"))
    print("{:^38}".format("BENGKEL MOTOR UD"))
    print("{:^38}".format("================"))
    
    #ISI LIST merk DAN HARGA
    print("")
    print("{:^38}".format(">> LIST HARGA OLI <<"))
    print("======================================")
    nmr = 1
    a = 0
    for oli in merk:
        hrg = harga[a]
        print(str(nmr) + ". " + "{:19}".format(str(oli)) + " |  Rp." + format(hrg,',.2f'))
        nmr = nmr + 1
        a = a + 1
    print("======================================")

    #INPUT PEMILIHAN
    pilihan = int(input("Mau Beli Oli yang Mana? (1-5) : "))
    print()
    
    if pilihan < 1 or pilihan > 5:
        print("SALAH INPUT!")
        print()
        continue
    while pilihan > 0 and pilihan < 6:
        if pilihan == 1:
            idx = 0
        elif pilihan == 2:
            idx = 1
        elif pilihan == 3:
            idx = 2
        elif pilihan == 4:
            idx = 3
        elif pilihan == 5:
            idx = 4
            
        print("Anda Akan Membeli Oli " + str(merk[idx]) + " Seharga Rp" + format(harga[idx],',.2f'))

        liter = int(input("Mau Beli Berapa Liter? >> "))

        potongan = liter * int(harga[idx])
        
        if potongan > mindiskon:
            getdisc = potongan * diskon
            sts = ">> Kamu Hemat Rp" + format(getdisc,',.2f') + " (Disc 5%)"
            sts2 = "   NOTE : Karena Pembelian diatas Rp" + format(mindiskon,',.2f')
        else:
            getdisc = 0
            sts = ">> Kamu Tidak Mendapat Diskon!"
            sts2 = "   NOTE : Karena Pembelian dibawah Rp" + format(mindiskon,',.2f')
        
        total = potongan - getdisc
        pajak = total * ppn
        subtotal = total + pajak
        print()
        print()
        print("{:^44}".format("./ STRUK PEMBAYARAN \."))
        print("=============================================")
        print(">> Oli yang Anda Beli    : " + merk[idx])
        print(">> Anda Membeli Sebanyak : " + str(liter) + " Liter")
        print(">> Harga Normal          : Rp" + format(potongan,',.2f'))
        print(sts)
        print(sts2)
        print(">> Total Tanpa PPN       : Rp" + format(total,',.2f'))
        print("================================")
        print(">> PPN = 1%")
        print(">> Kamu Kena Pajak   : Rp" + format(pajak,',.2f'))
        print(">> Total Keseluruhan : Rp" + format(subtotal,',.2f'))
        print("=================================")        
        break
    
    ulang = input(">> Mau Ulang Gak? Y/T : ")
    if ulang == 't' or ulang == 'T':
        break
    else:
        print("\n" * 15)
