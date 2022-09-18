import datetime as dt

# DATABASE BUKU
dtbs = {
    'F001A' : ["Sebuah Kisah Lama", "Eka Kurniawan", "2001","Fiction","Available"],
    'N001B' : ["Ratu Preman Kedua", "Evita Hanny", "2009","Non Fiction","Issued"],
    'F007Z' : ["Bayangan Kematian", "Lexie Xu","2016","Fiction","Available"]
}

# CHECKOUT LIST
indexx = [1, 2]
nama = ['Elin Gunawan', 'Mahira Hana']
nohp = ['082122848490', '0218093152']
bookid = ['N001B', 'F007Z']
status = ['Issued', 'Available']
checkout = [dt.datetime(2020,5,17).strftime('%Y-%m-%d'),dt.datetime(2022,5,11).strftime('%Y-%m-%d')]
checkin = ['-', dt.datetime(2022,6,17).strftime('%Y-%m-%d')]

# DEF untuk fungsi yang akan sering dipanggil
def tabel (a=0,b=0) :
    if a == 0 :
        print(f'\nBook ID\t   | Title\t\t\t| Author\t| Year\t|Type\t\t| Status')
        for i in dtbs :
            print(f'{i}\t   | {dtbs[i][0]}\t\t| {dtbs[i][1]}\t| {dtbs[i][2]}\t| {dtbs[i][3]}\t| {dtbs[i][4]}')
    elif a == 1 :
        print(f'\nBook ID\t   | Title\t\t\t| Author\t| Year\t| Type\t\t| Status')
        print(f'{b}\t   | {dtbs[b][0]}\t\t| {dtbs[b][1]}\t| {dtbs[b][2]}\t| {dtbs[b][3]}\t| {dtbs[b][4]}')
    elif a == 3 :
        print ("\nIDX\t| Nama\t\t| No. HP\t| BOOK ID | Status\t| Check-out\t| Check-in")
        for b in range (0,len(indexx),1) :
            print (str(indexx[b]) +  "\t| " + nama[b] + " \t| " + (nohp [b]) + "\t| " + (bookid[b]) + "\t  | " + (status[b]) + "\t| " + checkout[b] + "\t| " + checkin[b])
    elif a == 4 :
        print ("\nIDX\t| Nama\t\t| No. HP\t| BOOK ID | Status\t| Check-out\t| Check-in")
        print (str(indexx[b]) +  "\t| " + nama[b] + " \t| " + (nohp [b]) + "\t| " + (bookid[b]) + "\t  | " + (status[b]) + "\t| " + checkout[b] + "\t| " + checkin[b])

def keluar (a=0,b=0) :
    if a == 0 :
        exit = input ("Apakah Anda benar-benar ingin keluar dari program? (ya/tidak) ").lower()
        if exit == "ya" :
            print ("\nTerima kasih! Sampai jumpa kembali!")
        elif exit == "tidak":
            menu ()
        else :
            print ("Input Invalid.")
            menu ()
    elif a == 1 :
        exit = input ("Apakah Anda benar-benar ingin keluar dari sub-menu ini? (ya/tidak) ").lower()
        if exit == "ya" :
            menu()
        elif exit == "tidak" :
            b()
        else :
            print ("Input invalid.")
            b()

# DEF tiap menu
def lihat () :
    print ('''\nSub-Menu 1: Lihat Database Buku 
    1. Lihat semua data buku
    2. Lihat data salah satu buku
    3. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")

    if pilih == '1' :
        if len(dtbs.keys()) == 0 :
            print ("\nTidak ada data pada database buku :(")
            return lihat ()
        else :
            tabel(0,0)
            return lihat ()

    elif pilih == '2' : 
        if len(dtbs.keys()) == 0 :
            print ("\nTidak ada data pada database buku :(")
            return lihat ()
        else :
            kunci =  (input("Masukkan Book ID dari buku yang Anda ingin lihat datanya! ")).upper()
            if kunci in dtbs.keys() :
                tabel(1,kunci)
                return lihat()
            else :
                print (f"Tidak ada data dengan Book ID {kunci}")
                return lihat()

    elif pilih == '3' : 
        keluar (1,lihat)

    else :
        print (f"Input invalid. Tidak ada program pada pilihan {pilih}")
        return lihat()

def tambah () :
    print ('''\nSub-Menu 2: Tambah buku ke database 
    1. Tambah
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        kunci = input("Masukkan BOOK ID baru untuk data buku yang baru: ").upper()
        if len(kunci) != 5 and kunci.isalnum != True :
            print ("Input Invalid. Book ID harus berupa huruf/angka/kombinasi yang berisi 5 karakter!")
            return tambah()
        elif kunci in dtbs.keys() :
            print ("Input invalid. Terdapat BOOK ID eksisting dengan kombinasi yang sama.")
            return tambah()
        else :
            print("Book ID diterima!")
            title0 = input("Masukkan judul buku : ")
            author = input ("Masukkan nama pengarang : ")
            while True :
                year = input ("Masukkan tahun publikasi buku : ")
                if year.isdigit() != True :
                    print ("Input invalid. ")
                    continue
                else :
                    break
            while True:
                type = (input ("Masukkan tipe buku (Fiction/Non Fiction) : ")).title()
                if type == "Fiction" or type == "Non Fiction":      # memastikan input benar
                    break
                else :
                    print ("Input invalid")
                    continue
            
            yakin = (input(f"\nApakah Anda yakin ingin menambah buku ke database dengan spesifiksi:\n{kunci}\n{title0}\n{author}\n{year}\n{type}\nAvailable\n\n(Ya/Tidak) ")).lower()
            if yakin == "ya":
                dtbs[kunci] = [title0, author, year, type,"Available"]
                print ("\nData berhasil dimasukkan!")
                tabel(1,kunci)
                return tambah()
            else :
                print ("\nData tidak dimasukkan.")
                return tambah()
    elif pilih == '2':
        return keluar (1,tambah)
    else :
        print ("Input invalid")
        return tambah()

def hapus () :
    print ('''\nSub-Menu 3: Hapus buku dari database 
    1. Menghapus Data
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        kunci = (input("Masukkan BOOK ID data buku yang ingin dihapus : ")).upper()
        if kunci in dtbs.keys() :
            print ("Berikut merupakan data tabel yang ingin dihapus\n")
            tabel(1,kunci)
        else :
            print ("Data tidak tersedia.")
            return hapus()
        print ("\nReminder: Menghapus data buku dapat menyebabkan data tidak sinkron dengan 'Check Out List'")
        yakin = (input (f"Apakah Anda yakin ingin menghapus data ini? (ya/tidak) ")).lower()
        if yakin == "ya" :
            dtbs.pop(kunci)
            print ("Data sudah dihapus!")
            return hapus()
        else :
            print ("\nData tidak berhasil dihapus")
            return hapus()
    elif pilih == '2' :
            return keluar (1,hapus)
    else :
        print (f"Input invalid. Tidak ada program pada pilihan {pilih}")
        return hapus ()

def update () :
    print ('''\nSub-Menu 4: Perbarui data
    1. Perbarui data salah satu buku
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        kunci = (input("Masukkan BOOK ID dari data buku yang ingin diperbarui : ")).upper()
        if kunci in dtbs.keys() :
            print ("Berikut merupakan data tabel yang ingin diperbarui\n")
            tabel(1,kunci)
            kolom = input ('''\nPilih kolom yang ingin diubah :
            1. Title
            2. Author
            3. Year
            4. Type
            5. Status\n
            ''')
            if kolom not in {'1','2','3','4','5'} :
                print ("Input invalid\n")
                return update()
            while True :
                newdata = input("Masukkan data yang ingin diubah : ")
                if kolom == '1' or kolom == '2' :
                    break
                elif kolom == '3' and newdata.isdigit() != True :
                    print ("Input invalid. Data 'Year' harus berupa digit.")
                    continue
                elif kolom == '4' :
                    newdata = newdata.title()
                    if newdata == "Fiction" or newdata == "Non Fiction" :
                        break
                    else :
                        print ("Input invalid. Data 'Type' harus berupa Fiction atau Non Fiction")
                        continue
                elif kolom == '5' :
                    newdata = newdata.capitalize ()
                    if newdata == "Issued" or newdata == "Available" :
                        print ("\nReminder: Mengubah status buku dapat menyebabkan data tidak sinkron dengan 'Check Out List'\nPengubahan status buku disarankan lewat Menu Peminjaman atau Pengembalian Buku")
                        break
                    else :
                        print ("Input invalid. Data 'Status' harus berupa Available atau Issued")
                else :
                    break

            yakin = (input(f"Apakah Anda benar-benar ingin mengubah data pada BOOK ID {kunci} dari:\n{dtbs[kunci][int(kolom)-1]} menjadi {newdata}?\n(ya/tidak) ")).lower()
            if yakin == "ya" :
                dtbs[kunci][int(kolom)-1] = newdata
                tabel (1,kunci) 
                print ("\nData sudah diubah")
                return update()
            else :
                print ("\nData tidak diubah")
                return update()
        else :
            print ("Data tidak tersedia.")
            return update()
    elif pilih == '2' :
        return keluar (1,update)
    else :
        print (f"\nInput invalid. Tidak ada program pada pilihan {pilih}")
        return update()

def pinjam () :
    print ('''\nSub-Menu 5: Peminjaman buku
    1. Pinjam Buku
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        kunci = (input("Masukkan BOOK ID dari data buku yang akan dipinjam : ")).upper()
        if kunci in dtbs.keys() and dtbs[kunci][4] == "Available":
            input_name = input("Masukkan nama peminjam : ")
            while True :
                input_nohp = input ("Masukkan nomor HP peminjam : ")
                if input_nohp.isdigit() != True :
                    print ("Input Invalid. No Hp harus berupa angka.")
                    continue
                else :
                    break
            yakin = (input (f"\nApakah Anda yakin akan menambah data peminjaman dengan spesifikasi :\nBOOKID: {kunci}\nNama Peminjam: {input_name}\nNo. HP Peminjam: {input_nohp}\n\nPastikan seluruh data sudah benar!\n(ya/tidak) ")).lower()
            if yakin == "ya":
                indexx.append (len(indexx)+1)
                nama.append(input_name)
                nohp.append (input_nohp)
                bookid.append (kunci)
                status.append ("Issued")
                checkout.append (dt.datetime.today().strftime('%Y-%m-%d'))
                checkin.append ("-")
                dtbs[kunci][4] = "Issued"
                tabel (4,len(indexx)-1)
                print ("Data berhasil disimpan!")
                return pinjam()
            else :
                print ("Data tidak dimasukkan")
                return pinjam()
        elif kunci in dtbs.keys() and dtbs[kunci][4] == "Issued":
            print (f"BookID {kunci} sedang dipinjam.")
            return pinjam()
        else :
            print (f"Input Invalid. Tidak ada buku dengan BOOK ID {kunci}")
            return pinjam()
    elif pilih == '2' :
        return keluar (1,pinjam)
    else :
        print ("Input invalid")
        return pinjam()

def kembalikan () :
    print ('''\nSub-Menu 6: Pengembalian buku
    1. Pengembalian Buku yang sedang Dipinjam
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        kunci = (input("Masukkan BOOK ID dari data buku yang ingin diperbarui : ")).upper()
        A = False
        for i in indexx [::-1] :
            if bookid[i-1] == kunci and status[i-1] == "Issued":
                A = True
                B = i-1
                break
        if A == False :
            print ("Input Invalid")
            return kembalikan()
        elif A == True and kunci not in dtbs.keys() :
            print ("Data antara Database dan Check List tidak sinkron! Cek apabila sebelumnya Anda menghapus data secara manual.")
            return kembalikan()
        elif A == True and dtbs[kunci][4] == "Available":
            print ("Data antara Database dan Check List tidak sinkron! Cek apabila sebelumnya Anda mengubah status buku pada database secara manual")
            return kembalikan()
        elif A == True and dtbs[kunci][4] == "Issued":
            yakin = (input (f"Apakah Anda yakin akan menambah data bahwa {bookid[B]} sudah dikembalikan? (ya/tidak) ")).lower()
            if yakin == "ya":
                checkin[B] = dt.datetime.today().strftime('%Y-%m-%d')
                status[B]="Available"
                dtbs[kunci][4]="Available"
                tabel (4,B)
                return kembalikan()
            else :
                print ("Data tidak jadi disimpan!")
                return kembalikan()
    elif pilih == '2':
        keluar (1, kembalikan)
    else :
        print ("Input Invalid")
        return kembalikan()

def lihat2 ():
    print ('''\nSub-Menu 7: Check In & Out List Buku
    1. Lihat Check list Peminjaman Buku
    2. Kembali\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        tabel (3,0)
        return lihat2()
    if pilih == '2' :
        keluar (1,lihat2)
    else :
        print ("Input invalid.")
        return lihat2()

# DEF menu
def menu () :
    print ('''\nMenu\n1. Lihat database buku\n2. Tambah data ke database buku\n3. Hapus data dari database buku\n4. Update data pada database buku\n5. Peminjaman buku\n6. Pengembalian buku\n7. Lihat Check In & Out List Buku\n8. Keluar dari program\n''')
    pilih = input("Masukkan nomor program yang ingin dijalankan : ")
    if pilih == '1' :
        lihat ()
    elif pilih == '2' :
        tambah ()
    elif pilih == '3' :
        hapus()
    elif pilih == '4' :
        update()
    elif pilih == '5' :
        pinjam()
    elif pilih == '6' :
        kembalikan()
    elif pilih == '7':
        lihat2 ()
    elif pilih == '8' :
        keluar (0,0)
    else :
        print ("Input invalid")
        return menu ()

# MENJALANKAN PROGRAM
print ("Halo Librarian! Selamat datang di Perpustakaan Purwadhika!")
menu()