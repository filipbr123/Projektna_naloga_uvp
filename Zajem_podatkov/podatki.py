import requests
import re


def prva():
    seznam_vseh = []
    for i in range(7):
        if i == 1:
            url = 'https://www.skiresort.info/ski-resorts/alps/'
        else:
            url = f'https://www.skiresort.info/ski-resorts/alps/page/{i}/'
        besedilo = requests.get(url).text
        seznam_smučišč = []
        vzorec = r'<div class="col-sm-11 col-xs-10"><div class="h3"><a class="h3" href="https://www.skiresort.info/ski-resort/.*?Details </a>'
        for smučišče in re.finditer(vzorec, besedilo):
            seznam_smučišč.append(smučišče.group(0))
        seznam_vseh = seznam_vseh + seznam_smučišč
    return seznam_vseh



def smučišče_podatki():
    smučišča = prva()
    seznam_podatkov = []
    for smučišče in smučišča:
        podatki = {}

        vzorec_ime = r'<div class="col-sm-11 col-xs-10"><div class="h3"><a class="h3" href="https://www.skiresort.info/ski-resort/.*?/"> (.*?) </a>'

        vzorec_država = r'<div class="sub-breadcrumb"><a href="https://www.skiresort.info/ski-resorts/europe/">Europe</a> <a href="https://www.skiresort.info/ski-resorts/\w*?/">(\w*?)</a>'

        vzorec_spodnja_višina = r'</i></span></td> <td><span>\d*? m</span> \(<span>(\d*) m</span>'

        vzorec_zgornja_višina = r'</i></span></td> <td><span>\d*? m</span> \(<span>\d* m</span> - <span>(\d*) m</span>'

        vzorec_dolžina = r'<td><span class="slopeinfoitem ">([\d.]*) km'

        vzorec_dolžina_črnih = r'<span class="slopeinfoitem black">([\d.]*) km'

        vzorec_dolžina_modrih = r'<span class="slopeinfoitem blue">([\d.]*) km'

        vzorec_število_žičnic = r'<li>(\d*?)&nbsp;ski lifts</li>'

        vzorec_cena = r'€ ([\d\.]+)'
        
        ime = re.search(vzorec_ime, smučišče)
        podatki['Ime'] = ime.group(1)

        država = re.search(vzorec_država, smučišče)
        podatki['Država'] = država.group(1)

        podatki['Spodnja višina'] = float('nan')
        spodnja_višina = re.search(vzorec_spodnja_višina, smučišče)
        if spodnja_višina != None:
            podatki['Spodnja višina'] = spodnja_višina.group(1)

        podatki['Zgornja višina'] = float('nan')
        zgornja_višina = re.search(vzorec_zgornja_višina, smučišče)
        if zgornja_višina != None:
            podatki['Zgornja višina'] = zgornja_višina.group(1)

        podatki['Dolžina prog'] = float('nan')
        dolžina_prog = re.search(vzorec_dolžina, smučišče)
        if dolžina_prog != None:
            podatki['Dolžina prog'] = dolžina_prog.group(1)

        podatki['Dolžina črnih prog'] = float('nan')
        dolžina_črnih_prog = re.search(vzorec_dolžina_črnih, smučišče)
        if dolžina_črnih_prog != None:
            podatki['Dolžina črnih prog'] = dolžina_črnih_prog.group(1)

        podatki['Dolžina modrih prog'] = float('nan')
        dolžina_modrih_prog = re.search(vzorec_dolžina_modrih, smučišče)
        if dolžina_modrih_prog != None:
            podatki['Dolžina modrih prog'] = dolžina_modrih_prog.group(1)

        podatki['Število žičnic'] = 'Ni podatka'
        število_žičnic = re.search(vzorec_število_žičnic, smučišče)
        if število_žičnic != None:
            podatki['Število žičnic'] = število_žičnic.group(1)

        podatki['Cena'] = 'Ni podatka'
        cena = re.search(vzorec_cena, smučišče)
        if cena != None:
            podatki['Cena'] = cena.group(1)

        seznam_podatkov.append(podatki)

    return seznam_podatkov



def zlepi(sez):
    if len(sez) == 0:
        return ''
    else:
        return sez[0] + zlepi(sez[1:])
    
def zamenjaj(sez):
    if len(sez) == 0:
        return ''
    elif len(sez) == 1:
        return sez[0]
    else:
        return sez[0] + "'" + zlepi(sez[1:])
    
def odstrani(niz):
    vzorec1 = '&#8203;'
    vzorec2 = ' <span class="closed-resort red"> (temporarily closed)</span>'
    vzorec3 = '&#039;'
    return zamenjaj(zlepi(zlepi(niz.split(vzorec1)).split(vzorec2)).split(vzorec3))

def polepšaj():
    izluščeni_podatki = smučišče_podatki()
    slovar_držav = {'Austria': 'Avstrija', 'Switzerland': 'Švica', 'Italy': 'Italija', 'France': 'Francija', 'Slovenia': 'Slovenija', 'Germany': 'Nemčija', 'Liechtenstein': 'Lihtenštajn'}
    for slovar in izluščeni_podatki:
        slovar['Ime'] = odstrani(slovar['Ime'])
        slovar['Država'] = slovar_držav[slovar['Država']]
    return izluščeni_podatki

def končna():
    with open('Podatki/vsi_podatki.csv', 'w', encoding='UTF-8') as dat:
        končni_seznam = polepšaj()
        dat.write(f'Ime,Država,Spodnja višina [m],Zgornja višina [m],Dolžina prog [km],Dolžina črnih prog [km],Dolžina modrih prog [km],Število žičnic,Cena [€]\n')
        for slovar in končni_seznam:
            dat.write(f'{slovar['Ime']},{slovar['Država']},{slovar['Spodnja višina']},{slovar['Zgornja višina']},{slovar['Dolžina prog']},{slovar['Dolžina črnih prog']},{slovar['Dolžina modrih prog']},{slovar['Število žičnic']},{slovar['Cena']}\n')
