from netifaces import AF_INET
import netifaces as ni

interface=ni.ifaddresses('eth0')[AF_INET][0]['addr']
port=7777
