# -*- coding: utf-8 -*-
"""
@author: bekir
"""


import my_function
import my_connector


my_func = my_function
my_conn = my_connector

my_conn.mycursor.execute("use mydatabase")



#my_func.create_table()



my_func.löschen("Lenovo")  # urun_no(int) oder urun_adi(str) eingeben

#my_func.aktualisieren(1, "iPhone", 1)     # urun_no(int) und urun_adi(str) + kategori_numarasi(int)

#my_func.kategori_ekle("Computer")     # kategori ismini buradan gönderiyoruz

my_func.kategorileri_goster()

#my_func.urun_ekle("Lenovo", 4)     # urun ismini ve kategori numarsini buradan gönderiyoruz

my_func.urunleri_goster()

my_func.kac_urun_var()




