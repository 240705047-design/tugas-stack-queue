import os
from queue import LifoQueue
from collections import deque

print()
maxsize = int(input("Masukkan jumlah data yang ingin ditambahkan: "))

dequestack = deque()
lifostack = LifoQueue(maxsize=maxsize)

cek = True

while cek:
    os.system('cls')
    print('--- Masukkan Pilihan Anda ---')
    print('1. stack menggunakan deque')
    print('2. stack menggunakan LifoQueue')
    print('0. Keluar')
    
    pil = int(input('Masukkan pilihan Anda: '))

    if pil == 1:
        os.system('cls')
        i = 1
        temp = True
        while temp:
            print()
            print('--- Masukkan Pilihan Anda ---')
            print('1. Tambahkan Data dengan Deque')
            print('2. Hapus Data Deque')
            print('3. Tampilkan Data Deque')
            print('4. jumlah Data Dueque.')
            print('0. Keluar')
            pilmenu = int(input('Masukkan pilihan Anda: ')) 
            print()

            if pilmenu == 1:    
                if len(dequestack) < maxsize:
                    while i <= maxsize:
                        item = input(f'Masukkan data ke-{i}: ')
                        dequestack.append(item)
                        i += 1
                else:
                    print('Data tidak bisa tambah. Stack sudah penuh!!')
            elif pilmenu == 2:
                if len(dequestack) != 0:
                    print(f'Elemen terakhir: {dequestack.pop()} telah dihapus')
                else:
                    print('Stack kosong, tidak ada elemen untuk dihapus!!')
            elif pilmenu == 3:
                print('data dalam stack adalah: ')
                print(dequestack)
            elif pilmenu == 4:
                print(f'Jumlah data dalam stack adalah: {len(dequestack)}')
            else:
                pilmenu = False
                break 
    elif pil == 2:
        os.system('cls')
        temp = True
        while temp:
            print()
            print('--- Masukkan Pilihan Anda ---')
            print('1. Tambahkan Data dengan LifoQueue')
            print('2. Hapus Data LifoQueue')
            print('3. Tampilkan Data LifoQueue')
            print('4. jumlah Data LifoQueue.')
            print('0. Keluar')
            pilmenu = int(input('Masukkan pilihan Anda: '))
            print()
            if pilmenu == 1:
                if lifostack.qsize()==0:
                    i = 1
                else:
                    i = lifostack.qsize()+1
                if lifostack.full() == False:
                    while i <= maxsize:
                        item = input(f'Masukkan data ke-{i}: ')
                        lifostack.put(item)
                        i += 1
                    i=1 # reset counter
                else:
                    print('Data tidak bisa tambah. Stack sudah penuh!!')    
            elif pilmenu == 2:
                if lifostack.empty() == False:
                    print(f'Elemen terakhir: {lifostack.get()} telah dihapus')  
                else:
                    print('Stack kosong, tidak ada elemen untuk dihapus!!')     
            elif pilmenu == 3:
                isi = list(lifostack.queue)
                print('Data dalam stack adalah: ')
                print(isi)
            elif pilmenu == 4:
                print(f'Jumlah data dalam stack adalah: {lifostack.qsize()}')   
            else:
                pilmenu = False
                break
    elif pil == 0:
        pil = False
        break
    else:
        print('Pilihan tidak ada')