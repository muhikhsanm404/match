#!/data/data/com.termux/files/usr/bin/python2
import os
import sys
from random import *
import time

def loading(): #fungsi loading
    l = "LOADING        "
    o = "OADING        L"
    a = "ADING        LO"
    d = "DING        LOA"
    i = "ING        LOAD"
    n = "NG        LOADI"
    g = "G        LOADIN"
    for s in range(48):
        time.sleep(0.1)
        sys.stdout.write("\r\033[1;90m[\033[1;94m" +l[s % len(l)]+o[s % len(o)]+a[s % len(a)]+d[s % len(d)]+i[s % len(i)]+n[s % len(n)]+g[s % len(g)]+"\033[1;90m]\033[0m")
        sys.stdout.flush()

loading() #untuk menjalankan fungsi loading

os.system("clear")
print("\033[1;100;94m Python Program Created By: \033[1;104;90m AnIllusion-ShadowMind \033[1;0m")
os.system("toilet -f lean -F metal Past")
os.system("toilet -f lean -F metal  \ Quiz")
os.system("toilet -f wideterm -F metal _____________________________ ")

def write(y):#fungsi mengetik
    for x in y + "\n":
        sys.stdout.write(x)
        sys.stdout.flush()
        time.sleep(random() * 0.1) #kecepatan mengetik

def match(): #fungsi
	bil = [1, 2, 3, 4, 5, 6, 7, 8, 9] #variabel untuk list / data angka
	bil0 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	bil1 = choice(bil) #memilih secara random data dari variabel "bil"
	bil2 = choice(bil0)
	rumus = int(bil1 * bil2) #rumus operasi bilangan yang ditampilkan, python hanya akan menampilkan hasil dari operasi bilangan
	jawab = int(raw_input("\n\033[1;97m %d * %d = " % (bil1, bil2))) #tampilan operasi bilangan dan pengambilan input jawaban
	if jawab == rumus :
		print"\n\033[1;94m Jawaban Anda Benar, mau coba lagi? (y/n)"
		a = raw_input("pilih: ")
		if a == "y" :
			os.system("clear")
			match() #perintah untuk menampilkan fungsi
		if a == "n" :
		    write("\033[1;97m Thanks For Using_^") #kata yang diketik
		    sys.exit()
		else :
			print(" \033[0m %s \033[1;91m Not Found" % (a))
			write("\033[1;97m Thanks For Using_^")
	else :
		print"\n\033[1;90m Jawaban Anda tidak tepat, mau coba lagi? (y/n)"
		a = raw_input("pilih: ")
		if a == "y" :
			os.system("clear")
			match()
		if a == "n" :
		    write("\033[1;97m Thanks For Using_^")
		    sys.exit()
		else :
			print(" \033[0m %s \033[1;91m Not Found" % (a))
			write("\033[1;97m Thanks For Using_^")

match() #untuk menjalankan fungsi match
