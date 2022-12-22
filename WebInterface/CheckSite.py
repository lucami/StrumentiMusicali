import time

from requests_html import HTMLSession
from bs4 import BeautifulSoup
from DBInterface.DataBaseInterface import DBInterface

debug = False

class Strumento:
    def __init__(self, link, prezzo, nome):
        self.link = link
        self.prezzo = prezzo
        self.nome = nome
        # print(f"{self.nome}, {self.prezzo}, {self.link}")

    def __repr__(self):
        return "Strumento()"

    def __str__(self):
        return f"{self.nome} {self.prezzo} {self.link}"

    def get_strumento(self):
        return self.nome, self.prezzo, self.link


class SiteInterface:
    def __init__(self):
        self.links = []
        self.strumenti = []

    def add_page(self, page):

        if isinstance(page, str):
            self.links.append(page)

    def get_pages(self):
        for l in self.links:
            print(l)

    def retrieve_elements(self):
        for l in self.links:
            self.parse_link(l)

    def parse_pri_pro_tags(self, tag_strumenti):
        i = 0
        for tags in tag_strumenti:
            try:
                soup_tag = BeautifulSoup(str(tags), "lxml")
                tag_nome = soup_tag.find_all('a', {"style": "text-transform: uppercase;"})
                tag_prezzo = soup_tag.find_all('span', {"class": "prz"})
                if debug:
                    i+=1
                    print("****************************")
                    #print(tags)
                    print(f"{i} {tag_nome[0].text}")
                    #print(tag_nome[0]['href'])
                    #print("++++++++++++++++++++++")
                    #print(float(tag_prezzo[0].text.split()[1].replace(".","").replace(",",".")))
                    pass
                s = Strumento("https://www.mercatinomusicale.com/" + tag_nome[0]['href'],
                              float(tag_prezzo[0].text.split()[1].replace(".", "").replace(",", ".")),
                              tag_nome[0].text)
                self.strumenti.append(s)
            except:
                print("Error in parse link")


    def parse_link(self, l):
        i=0
        session = HTMLSession()
        resp = session.get(l)
        resp.html.render()
        soup = BeautifulSoup(resp.html.html, "lxml")

        tag_strumenti = soup.find_all('div', {"class": "item pri"})
        self.parse_pri_pro_tags( tag_strumenti)
        tag_strumenti = soup.find_all('div', {"class": "item pro"})
        self.parse_pri_pro_tags(tag_strumenti)
        '''
        tag_strumenti = soup.find_all('div', {"class": "item pri"})
        
        for tags in tag_strumenti:
                    try:
                        soup_tag = BeautifulSoup(str(tags), "lxml")
                        tag_nome = soup_tag.find_all('a', {"style": "text-transform: uppercase;"})
                        tag_prezzo = soup_tag.find_all('span', {"class": "prz"})
                        if debug:
                            i+=1
                            print("****************************")
                            #print(tags)
                            print(f"{i} {tag_nome[0].text}")
                            #print(tag_nome[0]['href'])
                            #print("++++++++++++++++++++++")
                            #print(float(tag_prezzo[0].text.split()[1].replace(".","").replace(",",".")))
                            pass
                        s = Strumento("https://www.mercatinomusicale.com/" + tag_nome[0]['href'],
                                      float(tag_prezzo[0].text.split()[1].replace(".", "").replace(",", ".")),
                                      tag_nome[0].text)
                        self.strumenti.append(s)
                    except:
                        print("Error in parse link")
        '''

    def get_instruments(self):
        for i in self.strumenti:
            try:
                print(i)
            except:
                print("error")

    def update_db(self):
        interface = DBInterface()
        for i in self.strumenti:
            n, p, l = i.get_strumento()
            try:
                interface.insert(n, l, p, time.strftime('%Y-%m-%d'))
            except Exception as e:
                print(e)


if __name__ == '__main__':
    si = SiteInterface()
    si.add_page(
       'https://www.mercatinomusicale.com/ann/search.asp?kw=occasione&rp=2&ct=&ch=&mc=&gp=&st=&p1=&p2=&rg=&pv=&vt=&pc=&sg=&pn=&ob=prezzodesc')
    si.add_page('https://www.mercatinomusicale.com/ann/search.asp?kw=occasione&rp=2&ct=&ch=&mc=&gp=&st=&p1=&p2=&rg=&pv=&vt=&pc=&sg=&pn=&ob=data')
    si.retrieve_elements()
    si.update_db()
