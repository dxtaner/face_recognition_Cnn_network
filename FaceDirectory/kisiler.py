import sqlite3
import time

class Kisi():

    def __init__(self,kisi_id,kisi_isim):
        self.kisi_id=kisi_id
        self.kisi_isim=kisi_isim

    def __str__(self):
        return "Kisi id : {}\nKisi İsmi: {}\n".\
            format(self.kisi_id,self.kisi_isim)

class Kisiler():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):

        self.baglanti = sqlite3.connect("kisiler.db")

        self.cursor = self.baglanti.cursor()

        sorgu = "Create Table If not exists kisiler (kisi_id INT primary key,kisi_isim TEXT)"

        self.cursor.execute(sorgu)

        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kisiekle(self,kisi):
        sorgu="Insert into kisiler Values(?,?)"
        self.cursor.execute(sorgu,(kisi.kisi_id,kisi.kisi_isim))
        self.baglanti.commit()

    def isimverisiniCek(self, yuzid):
        sorgu = "Select * From kisiler where kisi_id = ?"
        self.cursor.execute(sorgu, (yuzid,))
        veri=self.cursor.fetchone()

        ad=veri[1]
        return ad

