import socket
import os
import threading
use_threads = False

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hosts = []
sock.settimeout(5)

def try_connect(ip):
    try:
        sock.connect((ip, 80))
        hosts.append((ip,True))
        sock.close()
    except:
        hosts.append((ip, False))

def save():
    print(f'Dumping hosts into {os.path.abspath("hosts.txt")}')
    with open("hosts.txt", "a+") as f:
        for host in hosts:
            f.write(f'{host[0]} {int(host[1])}\n')

print("Internet pinger lol")
try:
    for i in range(2,256,1):
        for j in range(256):
            for k in range(256):
                for l in range(256):
                    ip = f'{i}.{k}.{j}.{l}'
                    #print(ip)
                    if use_threads:
                        threading.Thread(target=lambda: try_connect(ip)).start()
                    else:
                        try_connect(ip)
                        
                print(f"Cleared {i}.{j}.{k}.* Address Space")
            print(f"Cleared {i}.{j}.*.* Address Space")
            
        print(f"Cleared {i}.*.*.* Address Space")
        save()
        hosts = []
    print(f"Cleared *.*.*.* Address Space")
except KeyboardInterrupt:
    print(f'Interrupted after {len(hosts)} IPs')
import os
save()
