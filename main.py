import mysql.connector
import numpy as np

conn = mysql.connector.connect(
    host = 'localhost',
    user = 'your-username',
    password = 'your-password',
    database = 'cruds'
)

tableName = 'pegawai'
curr = conn.cursor()

def main():
    print("""
+ ========================== +
| CRUD WITH PYTHON AND MYSQL |
+ ========================== +

Code by: Bang Hans
Greet  : GreyMedia.ID

Menu:
    1.) Tambah Data
    2.) Tampilkan Data
    3.) Ganti/Update Data
    4.) Hapus Data
    5.) Exit""")
    menuInput = int(input("[1-5]> "))
    if menuInput == 1:
        tambahData()
    if menuInput == 2:
        showData()
    if menuInput == 3:
        updateData()
    if menuInput == 4:
        deleteData()
    if menuInput == 5:
        print("Terimakasih...")

def tambahData():
    print("""
+ =================== +
| Tambah Data Pegawai |
+ =================== +
""")
    namaPegawai = str(input("Nama Lengkap Pegawai> "))
    alamat = str(input("Alamat Pegawai> "))
    curr.execute('INSERT INTO {} (namaPegawai, alamat) VALUES {}'.format(tableName, (namaPegawai, alamat)))
    conn.commit()
    print(curr.rowcount, 'Data telah ditambahkan!')
    main()

def showData():
    print("""
+ ====================== +
| Tampilkan Data Pegawai |
+ ====================== +
""")
    curr.execute('SELECT * FROM pegawai')
    result = curr.fetchall()

    if curr.rowcount == 0:
        print("Tidak ada data")
        main()
    else:
        for data in result:
            print(data)
            main()

def updateData():
    print("""
+ ========================= +
| Ganti/Update Data Pegawai |
+ ========================= +
""")
    idPegawai = int(input("Masukan Id pegawai yang anda ingin ubah datanya\n> "))
    curr.execute('SELECT * FROM pegawai WHERE idPegawai={}'.format(idPegawai))
    for i in curr:
        print(np.array(i),"\n")
        namaPegawai = str(input("Nama Lengkap Pegawai (baru)> "))
        alamat = str(input("Alamat Pegawai (baru)> "))
        sql = "UPDATE pegawai SET namaPegawai=%s, alamat=%s WHERE idPegawai={}".format(idPegawai)
        val = (namaPegawai, alamat)
        curr.execute(sql, val)
        conn.commit()
        print(curr.rowcount, "Telah di-Update")
        main()

def deleteData():
    print("""
+ ================== +
| Hapus Data Pegawai |
+ ================== +
""")
    idPegawai = int(input("Masukan Id pegawai yang anda ingin hapus datanya\n> "))
    curr.execute('SELECT * FROM pegawai WHERE idPegawai={}'.format(idPegawai))
    for j in curr:
        print(j)
        confirm = str(input("Apakah anda ingin menghapusnya [Y/N]\n> "))
        if confirm == "Y" or "y":
            curr.execute('DELETE FROM pegawai WHERE idPegawai={}'.format(idPegawai))
            conn.commit()
            print("{} data berhasil dihapus".format(curr.rowcount))
            main()
        if confirm == "N" or "n":
            print("Anda membatalkan menghapus data...")
            main()
        else:
            print("Opsi yang anda masukan tak ada dalam list!")
            main()

main()
