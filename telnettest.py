import getpass
import sys
import telnetlib


HOST = "192.168.1.1"
user = raw_input("Enter your remote account: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until("Login: ")
tn.write(user + "\n")
if password:
    tn.read_until("Password: ")
    tn.write(password + "\n")

tn.write("ifconfig\n")
tn.read_until("inet addr:192.168.1.1 ")
tn.write("route add 192.168.52.1 255.255.255.0 gw 192.168.51.99 dev atm4.1\n")
tn.read_until(">")
tn.write("route show")
tn.read_until(">")
tn.read_untill("192.168.51.1      *               255.255.255.0 U    0      0        0 atm4.1")

print tn.read_all()

tn.close()
