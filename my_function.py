

import my_connector

conn = my_connector



def create_database():
  conn.mycursor.execute("CREATE DATABASE mydatabase")


def show_database():
  conn.mycursor.execute("show databases")


def create_table():
  #mycursor.execute("create table kategoriler (kategori_no INT AUTO_INCREMENT PRIMARY KEY, kategori_adi varchar(100) NOT NULL)")
  

  conn.mycursor.execute("""create table urunler(
                      urun_no INT AUTO_INCREMENT PRIMARY KEY, 
                      urun_adi varchar(100) NOT NULL, 
                      kategori_numarasi INT, 
                      CONSTRAINT fk_kategori 
                          FOREIGN KEY (kategori_numarasi) REFERENCES kategoriler(kategori_no)
                              ON UPDATE CASCADE
                              ON DELETE CASCADE
  )""")



def show_table():
  print("**********  Tables  **********")
  conn.mycursor.execute("show tables")
  for x in conn.mycursor:
    print(x)


def kac_urun_var():
  sql = "SELECT COUNT(urun_no) FROM urunler"
  conn.mycursor.execute(sql)
  for x in conn.mycursor:
    print("Listedeki ürün sayisi: " + str(x))


def aktualisieren(urun_no, urun_adi, ktg_no):
    sql = "UPDATE urunler SET urun_adi = %s, kategori_numarasi = %s WHERE urun_no = %s"
    val = (urun_adi, ktg_no, urun_no)
    conn.mycursor.execute(sql, val)
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "record(s) affected")
  
    
  
def löschen(gelen_deger):

  print(type(gelen_deger))

  if type(gelen_deger) == int:
    sql = "DELETE FROM urunler WHERE urun_no = %s"
    val = (gelen_deger,)
    conn.mycursor.execute(sql, val)
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "record(s) deleted")

  elif type(gelen_deger) == str:
    sql = "DELETE FROM urunler WHERE urun_adi = %s"
    val = (gelen_deger,)
    conn.mycursor.execute(sql, val)
    conn.mydb.commit()
    print(conn.mycursor.rowcount, "record(s) deleted")
  else:
    pass




def kategori_ekle(kategori_name):
  sql = "INSERT INTO kategoriler (kategori_adi) VALUES (%s)"
  val = (kategori_name,)
  conn.mycursor.execute(sql, val)
  conn.mydb.commit()
  print(conn.mycursor.rowcount, "record inserted.")



def kategorileri_goster():
  print("**********  Kategories  **********")
  conn.mycursor.execute("SELECT * FROM kategoriler")

  myresult = conn.mycursor.fetchall()

  for x in myresult:
    print(x)



def urun_ekle(isim, numara):
  sql = "INSERT INTO urunler (urun_adi, kategori_numarasi) VALUES (%s, %s)"
  #val = ("iPhone",1)
  val = (isim,numara)
  conn.mycursor.execute(sql, val)
  conn.mydb.commit()
  print(conn.mycursor.rowcount, "record inserted.")



def urunleri_goster():
  print("**********  Produkten  **********")
  conn.mycursor.execute("SELECT * FROM urunler")

  myresult = conn.mycursor.fetchall()

  for x in myresult:
    print(x)




