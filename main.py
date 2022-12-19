import time

import requests
from bs4 import BeautifulSoup
import random

from requests_html import HTMLSession


def connect():
    site = f'https://www.mercatinomusicale.com/ann/search.asp?kw=occasione&rp=2&ct=&ch=&mc=&gp=&st=&p1=&p2=&rg=&pv=&vt=&pc=&sg=&pn=&ob=prezzodesc'
    print(site)
    session = HTMLSession()
    #print(f"Session {session}")
    resp = session.get(site)
    #print(f"Resp {resp}")
    #print(f"Resp {resp.html}")

    resp.html.render()
    #print(f"links: {resp.html.links}")
    #print(f"html: {resp.html.html}")
    soup = BeautifulSoup(resp.html.html, "lxml")
    #print(f"soup {soup}")
    a_classes = soup.find_all('div', {"class":"item pri"})
    for tag in a_classes:
        print("****************************")
        print(tag)
    return

    for i in str(a_class).split():
        if "data-src" in i:
            addr = i.split('"')[1]
    print(addr)
    return addr



if __name__ == '__main__':
    connect()
