﻿# -*- coding: utf-8 -*-

import sys
try:
    import cookielib
except ImportError:
    import http.cookiejar as cookielib
from urllib import request as urllib2, parse as urllib
import datetime
from datetime import datetime
import re
import os
import base64
import codecs
import xbmc
import xbmcplugin
import xbmcgui
import xbmcaddon
import xbmcvfs
import traceback
import time
import xbmc
import webbrowser

try:
    import json
except:
    import simplejson as json
  
nome_contador = "plugin.video.primevideo"
link_contador = "https://whos.amung.us/pingjs/"    


##CONFIGURAÇÕES
####  TITULO DO MENU  #################################################################
title_menu = "[COLOR blue]prime[/COLOR][B][COLOR white]video[/COLOR][/B]"
###  DESCRIÇÃO DO ADDON ###############################################################
title_descricao = "O MELHOR DO CINEMA NO SEU KODI - 100% FHD"

####  LINK DO TITULO DE MENU  #########################################################
## OBS: POR PADRÃO JÁ TEM UM MENU EM BRANCO PARA NÃO TER ERRO AO CLICAR ###############
url_b64_title = ''
url_title = base64.b64decode(url_b64_title).decode('utf-8')
url_title = ''


##### PESQUISA - get.php
#url_b64_pesquisa = ''
#url_pesquisa = base64.b64decode(url_b64_pesquisa).decode('utf-8')
url_pesquisa = 'http://teste.com/get.php'
menu_pesquisar = '[COLOR blue][B]PESQUISAR...[/B][/COLOR]'
thumb_pesquisar = 'https://png.pngtree.com/png-vector/20190115/ourlarge/pngtree-vector-search-icon-png-image_320926.jpg'
fanart_pesquisar = ''
#### Descrição Pesquisa
desc_pesquisa = 'Pesquise por filme'
## MENU CONFIGURAÇÕES
menu_configuracoes = "[B][COLOR blue]CONFIGURAÇÕES[/COLOR][/B]"
thumb_icon_config = 'https://archive.org/download/3-20211109-073854-0002/3_20211109_073854_0002.png'
desc_configuracoes = "Configurações"
## FAVORITOS
menu_favoritos = '[B][COLOR blue]|[/COLOR][COLOR blue]FAVORITOS[/COLOR][COLOR blue]|[/COLOR][/B]'
thumb_favoritos = 'https://archive.org/download/20211105-125517-0000/20211105_125517_0000.png'
desc_favoritos = 'Adicione Itens aos Favoritos, pressionando OK do controle ou clicando o direito e selecionando Adicionar aos favoritos'

#### MENU VIP ################################################################
titulo_vip = "[COLOR blue]prime[/COLOR][B][COLOR white]video[/COLOR][/B] - [COLOR orangeblue](VIP)[/COLOR][/B]"
thumbnail_vip = 'https://i.imgur.com/'
fanart_vip = 'https://i.imgur.com/'
#### DESCRIÇÃO VIP ###########################################################
vip_descricao = 'SOLICITE SEU TESTE VIP'
#### DIALOGO VIP - SERVIDOR DESATIVADO - CLICK ###################################
vip_dialogo = "[B][COLOR blue]CONFIGURE SEU ACESSO[/COLOR][/B]"
##SERIVODR VIP
url_server_vip1 = ''
url_server_vip = ''

## DOAÇÃO
menu_doar = 'MENU DOAR'
###  DESCRIÇÃO Doar ##############################################################
### OBS: PARA SALTAR UMA LINHA UTILIZE \n #############################################
url_desc_doar = 'DESC DOAR' 
##

## MULTLINK
## nome para $nome, padrão: lsname para $lsname
playlist_command = 'nome'
dialog_playlist = '[B][COLOR blue]Escolha uma opção:[/COLOR][/B]'

# user agent - Padrão: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36
useragent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'

# Base - seu link principal
url_origem = 'https://raw.githubusercontent.com/webplay10/PRIMEVIDEO/master/Categorias'
try:
    url_principal = base64.b64decode(url_origem).decode('utf-8')
except:
    url_principal = url_origem
    

#name - mensagem suporte
addon_name = xbmcaddon.Addon().getAddonInfo('name')


if sys.argv[1] == 'limparFavoritos':
    Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    arquivo = os.path.join(Path, "favorites.dat")
    exists = os.path.isfile(arquivo)
    if exists:
        try:
            os.remove(arquivo)
        except:
            pass
    xbmcgui.Dialog().ok('Sucesso', '[B][COLOR blue]Favoritos limpo com sucesso![/COLOR][/B]')
    xbmc.sleep(2000)
    exit()


if sys.argv[1] == 'SetPassword':
    addonID = xbmcaddon.Addon().getAddonInfo('id')
    addon_data_path = xbmcvfs.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
    if os.path.exists(addon_data_path)==False:
        os.mkdir(addon_data_path)
    xbmc.sleep(4)
    #Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    #arquivo = os.path.join(Path, "password.txt")
    arquivo = os.path.join(addon_data_path, "password.txt")
    exists = os.path.isfile(arquivo)
    keyboard = xbmcaddon.Addon().getSetting("keyboard")
    if exists == False:
        password = '0069'
        p_encoded = base64.b64encode(password.encode()).decode('utf-8')
        p_file1 = open(arquivo,'w')
        p_file1.write(p_encoded)
        p_file1.close()
        xbmc.sleep(4)
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if int(keyboard) == 0:
                ps2 = dialog.numeric(0, 'Insira a nova senha:')
            else:
                ps2 = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
            if ps2 != '':
                ps2_b64 = base64.b64encode(ps2.encode()).decode('utf-8')
                p_file = open(arquivo,'w')
                p_file.write(ps2_b64)
                p_file.close()
                xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','A Senha foi alterada com sucesso!')
            else:
                xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Não foi possivel alterar a senha!')
        else:
            xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    else:
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            if int(keyboard) == 0:
                ps2 = dialog.numeric(0, 'Insira a nova senha:')
            else:
                ps2 = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
            if ps2 != '':
                ps2_b64 = base64.b64encode(ps2.encode()).decode('utf-8')
                p_file = open(arquivo,'w')
                p_file.write(ps2_b64)
                p_file.close()
                xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','A Senha foi alterada com sucesso!')
            else:
                xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Não foi possivel alterar a senha!')
        else:
            xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    exit()



addon_handle = int(sys.argv[1])
__addon__ = xbmcaddon.Addon()
addon = __addon__
__addonname__ = __addon__.getAddonInfo('name')
__icon__ = __addon__.getAddonInfo('icon')
addon_version = __addon__.getAddonInfo('version')
try:
    profile = xbmcvfs.translatePath(__addon__.getAddonInfo('profile').decode('utf-8'))
except:
    profile = xbmcvfs.translatePath(__addon__.getAddonInfo('profile'))
try:
    home = xbmcvfs.translatePath(__addon__.getAddonInfo('path').decode('utf-8'))
except:
    home = xbmcvfs.translatePath(__addon__.getAddonInfo('path'))
favorites = os.path.join(profile, 'favorites.dat')
favoritos = xbmcaddon.Addon().getSetting("favoritos")


if os.path.exists(favorites)==True:
    FAV = open(favorites).read()
else:
    FAV = []


def notify(message, timeShown=5000):
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (__addonname__, message, timeShown, __icon__))

def to_unicode(text, encoding='utf-8', errors='strict'):
    """Force text to unicode"""
    if isinstance(text, bytes):
        return text.decode(encoding, errors=errors)
    return text

def get_search_string(heading='', message=''):
    """Ask the user for a search string"""
    search_string = None
    keyboard = xbmc.Keyboard(message, heading)
    keyboard.doModal()
    if keyboard.isConfirmed():
        search_string = to_unicode(keyboard.getText())
    return search_string

def getRequest(url, count):
    proxy_mode = addon.getSetting('proxy')
    if proxy_mode == 'true':
        try:
            import requests
            import random
            headers={'User-agent': useragent,
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Content-Type': 'text/html'}
            if int(count) > 0:
                attempt = int(count)-1
            else:
                attempt = 0
            #print('tentativa: '+str(attempt)+'')
            ### https://proxyscrape.com/free-proxy-list
            ##http
            data_proxy1 = getRequest2('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=BR&ssl=no&anonymity=all', '')
            list1 = data_proxy1.splitlines()
            total1 = len(list1)
            number_http = random.randint(0,total1-1)
            proxy_http = 'http://'+list1[number_http]
            ##https
            data_proxy2 = getRequest2('https://api.proxyscrape.com/?request=getproxies&proxytype=http&timeout=10000&country=BR&ssl=yes&anonymity=all', '')
            list2 = data_proxy2.splitlines()
            total2 = len(list2)
            number_https = random.randint(0,total2-1)
            proxy_https = 'https://'+list2[number_https]
            #print(proxy_https)
            proxyDict = {"http" : proxy_http, "https" : proxy_https}
            req = requests.get(url, headers=headers, proxies=proxyDict)
            req.encoding = 'utf-8'
            #status = req.status_code
            response = req.text
            return response
        except:
            proxy_number = addon.getSetting('proxy_try')
            if int(attempt) > 0:
                limit = int(attempt)
            elif int(count) == 1 and int(attempt) == 0:
                limit = int(proxy_number)+1+1
            if int(limit) > 1:
                #print('ativar outro proxy')
                data = getRequest(url, int(limit))
                return data
            else:
                notify('[COLOR blue]Erro ao utilizar o proxy ou servidor![/COLOR]')
                response = ''
                return response
    else:
        try:
            try:
                import urllib.request as urllib2
            except ImportError:
                import urllib2
            request_headers = {
            "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.8,ru;q=0.7,de-DE;q=0.6,de;q=0.5,de-AT;q=0.4,de-CH;q=0.3,ja;q=0.2,zh-CN;q=0.1,zh;q=0.1,zh-TW;q=0.1,es;q=0.1,ar;q=0.1,en-GB;q=0.1,hi;q=0.1,cs;q=0.1,el;q=0.1,he;q=0.1,en-US;q=0.1",
            "User-agent": useragent,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9"
            }
            request = urllib2.Request(url, headers=request_headers)
            response = urllib2.urlopen(request).read().decode('utf-8')
            return response
        except urllib2.URLError as e:
            if hasattr(e, 'code'):
                xbmc.executebuiltin("XBMC.Notification(Falha, código de erro - "+str(e.code)+",10000,"+__icon__+")")    
            elif hasattr(e, 'reason'):
                xbmc.executebuiltin("XBMC.Notification(Falha, motivo - "+str(e.reason)+",10000,"+__icon__+")")
            response = ''
            return response



def getRequest2(url,ref,userargent=False):
    try:
        if ref > '':
            ref2 = ref
        else:
            ref2 = url
        if userargent:
            client_user = userargent
        else:
            client_user = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders=[('Accept-Language', 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'),('User-Agent', client_user),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'), ('Referer', ref2)]
        data = opener.open(url).read()
        response = data.decode('utf-8')
        return response
    except:
        pass

def regex_get_all(text, start_with, end_with):
    r = re.findall("(?i)(" + start_with + "[\S\s]+?" + end_with + ")", text)
    return r



def re_me(data, re_patten):
    match = ''
    m = re.search(re_patten, data)
    if m != None:
        match = m.group(1)
    else:
        match = ''
    return match



def resolve_data(url):
    try:
        data = getRequest(url, 1)
        import gzip, binascii
        try:
            from StringIO import StringIO as BytesIO ## for Python 2
        except ImportError:            
            from io import BytesIO ## for Python 3
        if 'dnK' in data:
            data = data.split('dnK')
            buf = BytesIO(binascii.unhexlify(data[0]))
            f = gzip.GzipFile(fileobj=buf)
            data = f.read()
            data = data.decode('utf-8')
    except:
        data = getRequest(url, 1)        
    return data

def getData(url,fanart):
    adult = xbmcaddon.Addon().getSetting("adult")
    adult2 = xbmcaddon.Addon().getSetting("adult2")
    uhdtv = addon.getSetting('uhdtv')
    fhdtv = addon.getSetting('fhdtv')
    hdtv = addon.getSetting('hdtv')
    sdtv = addon.getSetting('sdtv')
    filtrar = addon.getSetting('filtrar')
    data = resolve_data(url)
    if isinstance(data, (int, str, list)):
        channels = re.compile('<channels>(.+?)</channels>',re.MULTILINE|re.DOTALL).findall(data)
        channel = re.compile('<channel>(.*?)</channel>',re.MULTILINE|re.DOTALL).findall(data)
        item = re.compile('<item>(.*?)</item>',re.MULTILINE|re.DOTALL).findall(data)
        if len(channels) >0:
            for channel in channel:
                linkedUrl=''
                lcount=0
                try:
                    linkedUrl = re.compile('<externallink>(.*?)</externallink>').findall(channel)[0]
                    lcount=len(re.compile('<externallink>(.*?)</externallink>').findall(channel))
                except: pass
                
                try:
                    linkedUrl = base64.b32decode(linkedUrl[::-1]).decode('utf-8')
                except:
                    pass 
                    

                name = re.compile('<name>(.*?)</name>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                try:
                    thumbnail = re.compile('<thumbnail>(.*?)</thumbnail>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                except:
                    thumbnail = ''
                try:
                    fanart1 = re.compile('<fanart>(.*?)</fanart>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                except:
                    fanart1 = ''

                if not fanart1:
                    if __addon__.getSetting('use_thumb') == "true":
                        fanArt = thumbnail
                    else:
                        fanArt = fanart
                else:
                    fanArt = fanart1
                if fanArt == None:
                    #raise
                    fanArt = ''

                try:
                    desc = re.compile('<info>(.*?)</info>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if desc == None:
                        #raise
                        desc = ''
                except:
                    desc = ''

                try:
                    genre = re.compile('<genre>(.*?)</genre>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if genre == None:
                        #raise
                        genre = ''
                except:
                    genre = ''

                try:
                    date = re.compile('<date>(.*?)</date>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if date == None:
                        #raise
                        date = ''
                except:
                    date = ''

                try:
                    cblueits = re.compile('<cblueits>(.*?)</cblueits>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if cblueits == None:
                        #raise
                        cblueits = ''
                except:
                    cblueits = ''

                try:
                    year = re.compile('<year>(.*?)</year>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if year == None:
                        #raise
                        year = ''
                except:
                    year = ''

                try:
                    director = re.compile('<director>(.*?)</director>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if director == None:
                        #raise
                        director = ''
                except:
                    director = ''

                try:
                    writer = re.compile('<writer>(.*?)</writer>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if writer == None:
                        #raise
                        writer = ''
                except:
                    writer = ''

                try:
                    duration = re.compile('<duration>(.*?)</duration>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if duration == None:
                        #raise
                        duration = ''
                except:
                    duration = ''

                try:
                    premieblue = re.compile('<premieblue>(.*?)</premieblue>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if premieblue == None:
                        #raise
                        premieblue = ''
                except:
                    premieblue = ''

                try:
                    studio = re.compile('<studio>(.*?)</studio>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if studio == None:
                        #raise
                        studio = ''
                except:
                    studio = ''

                try:
                    rate = re.compile('<rate>(.*?)</rate>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if rate == None:
                        #raise
                        rate = ''
                except:
                    rate = ''

                try:
                    originaltitle = re.compile('<originaltitle>(.*?)</originaltitle>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if originaltitle == None:
                        #raise
                        originaltitle = ''
                except:
                    originaltitle = ''

                try:
                    country = re.compile('<country>(.*?)</country>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if country == None:
                        #raise
                        country = ''
                except:
                    country = ''

                try:
                    rating = re.compile('<country>(.*?)</country>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if rating == None:
                        #raise
                        rating = ''
                except:
                    rating = ''

                try:
                    userrating = re.compile('<userrating>(.*?)</userrating>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if userrating == None:
                        #raise
                        userrating = ''
                except:
                    userrating = ''

                try:
                    votes = re.compile('<votes>(.*?)</votes>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if votes == None:
                        #raise
                        votes = ''
                except:
                    votes = ''

                try:
                    aiblue = re.compile('<aiblue>(.*?)</aiblue>',re.MULTILINE|re.DOTALL).findall(channel)[0]
                    if aiblue == None:
                        #raise
                        aiblue = ''
                except:
                    aiblue = ''

                try:
                    if linkedUrl=='':
                        #addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),2,thumbnail,fanArt,desc,genre,date,cblueits,True)
                        #addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),2,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
                        addDir(name.encode('utf-8', 'ignore'),'',1,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
                    else:
                        #print linkedUrl
                        #addDir(name.encode('utf-8'),linkedUrl.encode('utf-8'),1,thumbnail,fanArt,desc,genre,date,None,'source')
                        if adult == 'false' and re.search("ADULTOS",name,re.IGNORECASE) and name.find('(+18)') >=0:
                            pass
                        else:
                            addDir(name.encode('utf-8', 'ignore'),linkedUrl,1,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
                except:
                    notify('[COLOR blue]Erro ao Carregar os dados![/COLOR]')
        elif re.search("#EXTM3U",data) or re.search("#EXTINF",data):
            content = data.rstrip()
            match = re.compile(r'#EXTINF:(.+?),(.*?)[\n\r]+([^\r\n]+)').findall(content)
            for other,channel_name,stream_url in match:
                if 'tvg-logo' in other:
                    thumbnail = re_me(other,'tvg-logo=[\'"](.*?)[\'"]')
                    if thumbnail:
                        if thumbnail.startswith('http'):
                            thumbnail = thumbnail
                        #elif not addon.getSetting('logo-folderPath') == "":
                        #    logo_url = addon.getSetting('logo-folderPath')
                        #    thumbnail = logo_url + thumbnail

                        else:
                            thumbnail = ''
                    else:
                        thumbnail = ''
                else:
                    thumbnail = ''

                if 'group-title' in other:
                    cat = re_me(other,'group-title=[\'"](.*?)[\'"]')
                else:
                    cat = ''

                try:
                    #resolver_final = resolver(stream_url, channel_name, thumbnail)
                    if uhdtv == 'false' and re.search("4K",channel_name):
                        pass
                    elif fhdtv == 'false' and re.search("FHD",channel_name):
                        pass
                    elif hdtv == 'false' and re.search("HD",channel_name) and not re.search("FHD",channel_name):
                        pass
                    elif sdtv == 'false' and re.search("SD",channel_name):
                        pass
                    elif sdtv == 'false' and not re.search("SD",channel_name) and not re.search("HD",channel_name) and not re.search("4K",channel_name):
                        pass
                    #Futebol
                    elif int(filtrar) == 1 and re.search("Praia",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 1 and not re.search("SPORTV",channel_name,re.IGNORECASE) and not re.search("DAZN",channel_name,re.IGNORECASE) and not re.search("ESPN Brasil",channel_name,re.IGNORECASE) and not re.search("PREMIERE",channel_name,re.IGNORECASE) and not re.search("COPA",channel_name,re.IGNORECASE):
                        pass
                    #Esportes
                    elif int(filtrar) == 2 and re.search("Praia",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 2 and not re.search("Band Sports",channel_name,re.IGNORECASE) and not re.search("Combate",channel_name,re.IGNORECASE) and not re.search("Fox Sports",channel_name,re.IGNORECASE) and not re.search("SPORTV",channel_name,re.IGNORECASE) and not re.search("DAZN",channel_name,re.IGNORECASE) and not re.search("ESPN",channel_name,re.IGNORECASE) and not re.search("PREMIERE",channel_name,re.IGNORECASE) and not re.search("COPA",channel_name,re.IGNORECASE):
                        pass
                    #Filmes e Series
                    elif int(filtrar) == 3 and re.search("Sports",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 3 and re.search("XY Max",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 3 and not re.search("AMC",channel_name,re.IGNORECASE) and not re.search("Canal Brasil",channel_name,re.IGNORECASE) and not re.search("Cinemax",channel_name,re.IGNORECASE) and not re.search("HBO",channel_name,re.IGNORECASE) and not re.search("Max",channel_name,re.IGNORECASE) and not re.search("Megapix",channel_name,re.IGNORECASE) and not re.search("Paramount",channel_name,re.IGNORECASE) and not re.search("SPACE",channel_name,re.IGNORECASE) and not re.search("TCM",channel_name,re.IGNORECASE) and not re.search("Telecine Action",channel_name,re.IGNORECASE) and not re.search("TC Action",channel_name,re.IGNORECASE) and not re.search("Telecine Cult",channel_name,re.IGNORECASE) and not re.search("TC Cult",channel_name,re.IGNORECASE) and not re.search("TC Cult",channel_name,re.IGNORECASE) and not re.search("Telecine Fun",channel_name,re.IGNORECASE) and not re.search("TC Fun",channel_name,re.IGNORECASE) and not re.search("Telecine Pipoca",channel_name,re.IGNORECASE) and not re.search("TC Pipoca",channel_name,re.IGNORECASE) and not re.search("Telecine Premium",channel_name,re.IGNORECASE) and not re.search("TC Premium",channel_name,re.IGNORECASE) and not re.search("Telecine Touch",channel_name,re.IGNORECASE) and not re.search("TC Touch",channel_name,re.IGNORECASE) and not re.search("TNT",channel_name,re.IGNORECASE) and not re.search("A&E",channel_name,re.IGNORECASE) and not re.search("AXN",channel_name,re.IGNORECASE) and not re.search("AXN",channel_name,re.IGNORECASE) and not re.search("FOX",channel_name,re.IGNORECASE) and not re.search("FX",channel_name,re.IGNORECASE) and not re.search("SONY",channel_name,re.IGNORECASE) and not re.search("Studio Universal",channel_name,re.IGNORECASE) and not re.search("SyFy",channel_name,re.IGNORECASE) and not re.search("Universal Channel",channel_name,re.IGNORECASE) and not re.search("Universal TV",channel_name,re.IGNORECASE) and not re.search("Warner",channel_name,re.IGNORECASE):
                        pass
                    #Infantil
                    elif int(filtrar) == 4 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 4 and not re.search("Baby TV",channel_name,re.IGNORECASE) and not re.search("BOOMERANG",channel_name,re.IGNORECASE) and not re.search("CARTOON NETWORK",channel_name,re.IGNORECASE) and not re.search("DISCOVERY KIDS",channel_name,re.IGNORECASE) and not re.search("DISNEY",channel_name,re.IGNORECASE) and not re.search("GLOOB",channel_name,re.IGNORECASE) and not re.search("NAT GEO KIDS",channel_name,re.IGNORECASE) and not re.search("NICKELODEON",channel_name,re.IGNORECASE) and not re.search("NICK JR",channel_name,re.IGNORECASE) and not re.search("PLAYKIDS",channel_name,re.IGNORECASE) and not re.search("TOONCAST",channel_name,re.IGNORECASE) and not re.search("ZOOMOO",channel_name,re.IGNORECASE):
                        pass
                    #Documentario
                    elif int(filtrar) == 5  and re.search("Kids",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 5 and not re.search("Discovery",channel_name,re.IGNORECASE) and not re.search("H2 HD",channel_name,re.IGNORECASE) and not re.search("H2 SD",channel_name,re.IGNORECASE) and not re.search("H2 FHD",channel_name,re.IGNORECASE) and not re.search("History",channel_name,re.IGNORECASE) and not re.search("Nat Geo Wild",channel_name,re.IGNORECASE) and not re.search("National Geographic",channel_name,re.IGNORECASE):
                        pass
                    #Abertos
                    elif int(filtrar) == 6 and re.search("Brasileirinhas",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 6 and re.search("News",channel_name,re.IGNORECASE) or int(filtrar) == 6 and re.search("Sat",channel_name,re.IGNORECASE) or int(filtrar) == 6 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 6 and not re.search("Globo",channel_name,re.IGNORECASE) and not re.search("RECORD",channel_name,re.IGNORECASE) and not re.search("blueeTV",channel_name,re.IGNORECASE) and not re.search("bluee Vida",channel_name,re.IGNORECASE) and not re.search("SBT",channel_name,re.IGNORECASE) and not re.search("TV Brasil",channel_name,re.IGNORECASE) and not re.search("TV Cultura",channel_name,re.IGNORECASE) and not re.search("TV Diario",channel_name,re.IGNORECASE) and not re.search("BAND",channel_name,re.IGNORECASE):
                        pass
                    #Reality show
                    elif int(filtrar) == 7 and not re.search("BBB",channel_name,re.IGNORECASE) and not re.search("Big Brother Brasil",channel_name,re.IGNORECASE) and not re.search("A Fazenda",channel_name,re.IGNORECASE):
                        pass
                    #Noticias
                    elif int(filtrar) == 8 and re.search("FM",channel_name,re.IGNORECASE):
                        pass
                    elif int(filtrar) == 8 and not re.search("CNN",channel_name,re.IGNORECASE) and not re.search("NEWS",channel_name,re.IGNORECASE):
                        pass
                    elif adult2 == 'false' and re.search("Adult",cat,re.IGNORECASE) or adult2 == 'false' and re.search("ADULT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Blue Hustler",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PlayBoy",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("bluelight",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sextreme",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SexyHot",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Venus",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("AST TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ASTTV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("AST.TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BRAZZERS",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("CANDY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("CENTOXCENTO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("DORCEL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("EROXX",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PASSION",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PENTHOUSE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PINK-O",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PINK O",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PRIVATE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("RUSNOCH",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SCT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SEXT6SENSO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SHALUN TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("VIVID blue",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Porn",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Plus",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Mix",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Mad",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XXL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Desire",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Bizarre",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sexy HOT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Reality Kings",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Prive TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hustler TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Extasy",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Evil Angel",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Erox",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("DUSK",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Brazzers",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Brasileirinhas",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Pink Erotic",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Passion",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Passie",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Meiden Van Holland Hard",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sext & Senso",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Super One",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Vivid TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hustler HD",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("SCT",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Sex Ation",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hot TV",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Hot HD",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("MILF",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ANAL",channel_name,re.IGNORECASE) and not re.search("CANAL",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("PUSSY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("ROCCO",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BABES",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BABIE",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XY Max",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("TUSHY",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("BLACKED",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("FAKE TAXI",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("XXX",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("18",channel_name,re.IGNORECASE) or adult2 == 'false' and re.search("Porno",channel_name,re.IGNORECASE):
                        pass
                    elif re.search("Adult",cat,re.IGNORECASE) or re.search("ADULT",channel_name,re.IGNORECASE) or re.search("Blue Hustler",channel_name,re.IGNORECASE) or re.search("PlayBoy",channel_name,re.IGNORECASE) or re.search("bluelight",channel_name,re.IGNORECASE) or re.search("Sextreme",channel_name,re.IGNORECASE) or re.search("SexyHot",channel_name,re.IGNORECASE) or re.search("Venus",channel_name,re.IGNORECASE) or re.search("AST TV",channel_name,re.IGNORECASE) or re.search("ASTTV",channel_name,re.IGNORECASE) or re.search("AST.TV",channel_name,re.IGNORECASE) or re.search("BRAZZERS",channel_name,re.IGNORECASE) or re.search("CANDY",channel_name,re.IGNORECASE) or re.search("CENTOXCENTO",channel_name,re.IGNORECASE) or re.search("DORCEL",channel_name,re.IGNORECASE) or re.search("EROXX",channel_name,re.IGNORECASE) or re.search("PASSION",channel_name,re.IGNORECASE) or re.search("PENTHOUSE",channel_name,re.IGNORECASE) or re.search("PINK-O",channel_name,re.IGNORECASE) or re.search("PINK O",channel_name,re.IGNORECASE) or re.search("PRIVATE",channel_name,re.IGNORECASE) or re.search("RUSNOCH",channel_name,re.IGNORECASE) or re.search("SCT",channel_name,re.IGNORECASE) or re.search("SEXT6SENSO",channel_name,re.IGNORECASE) or re.search("SHALUN TV",channel_name,re.IGNORECASE) or re.search("VIVID blue",channel_name,re.IGNORECASE) or re.search("Porn",channel_name,re.IGNORECASE) or re.search("XY Plus",channel_name,re.IGNORECASE) or re.search("XY Mix",channel_name,re.IGNORECASE) or re.search("XY Mad",channel_name,re.IGNORECASE) or re.search("XXL",channel_name,re.IGNORECASE) or re.search("Desire",channel_name,re.IGNORECASE) or re.search("Bizarre",channel_name,re.IGNORECASE) or re.search("Sexy HOT",channel_name,re.IGNORECASE) or re.search("Reality Kings",channel_name,re.IGNORECASE) or re.search("Prive TV",channel_name,re.IGNORECASE) or re.search("Hustler TV",channel_name,re.IGNORECASE) or re.search("Extasy",channel_name,re.IGNORECASE) or re.search("Evil Angel",channel_name,re.IGNORECASE) or re.search("Erox",channel_name,re.IGNORECASE) or re.search("DUSK",channel_name,re.IGNORECASE) or re.search("Brazzers",channel_name,re.IGNORECASE) or re.search("Brasileirinhas",channel_name,re.IGNORECASE) or re.search("Pink Erotic",channel_name,re.IGNORECASE) or re.search("Passion",channel_name,re.IGNORECASE) or re.search("Passie",channel_name,re.IGNORECASE) or re.search("Meiden Van Holland Hard",channel_name,re.IGNORECASE) or re.search("Sext & Senso",channel_name,re.IGNORECASE) or re.search("Super One",channel_name,re.IGNORECASE) or re.search("Vivid TV",channel_name,re.IGNORECASE) or re.search("Hustler HD",channel_name,re.IGNORECASE) or re.search("SCT",channel_name,re.IGNORECASE) or re.search("Sex Ation",channel_name,re.IGNORECASE) or re.search("Hot TV",channel_name,re.IGNORECASE) or re.search("Hot HD",channel_name,re.IGNORECASE) or re.search("MILF",channel_name,re.IGNORECASE) or re.search("ANAL",channel_name,re.IGNORECASE) and not re.search("CANAL",channel_name,re.IGNORECASE) or re.search("PUSSY",channel_name,re.IGNORECASE) or re.search("ROCCO",channel_name,re.IGNORECASE) or re.search("BABES",channel_name,re.IGNORECASE) or re.search("BABIE",channel_name,re.IGNORECASE) or re.search("XY Max",channel_name,re.IGNORECASE) or re.search("TUSHY",channel_name,re.IGNORECASE) or re.search("FAKE TAXI",channel_name,re.IGNORECASE) or re.search("BLACKED",channel_name,re.IGNORECASE) or re.search("XXX",channel_name,re.IGNORECASE) or re.search("18",channel_name,re.IGNORECASE) or re.search("Porno",channel_name,re.IGNORECASE):
                        addDir2(channel_name.encode('utf-8', 'ignore'),stream_url,10,'',thumbnail,'','','','','','','','','','','','','','','','','','',False)
                    else:
                        #addLink(name1.encode('utf-8', 'ignore'),resolver_final.encode('utf-8'),'',cleaname,thumbnail,'',desc1)
                        addDir2(channel_name.encode('utf-8', 'ignore'),stream_url,18,'',thumbnail,'','','','','','','','','','','','','','','','','','',False)
                except:
                    #notify('[COLOR blue]Erro ao Carregar os dados![/COLOR]')
                    pass
        else:
            #getItems(soup('item'),fanart)
            getItems(item,fanart)
    else:
        #parse_m3u(soup)
        notify('[COLOR blue]Erro ao Carregar os dados![/COLOR]')
    if '<SetContent>' in data:
        try:
            content=re.findall('<SetContent>(.*?)<',data)[0]
            xbmcplugin.setContent(addon_handle, str(content))
        except:
            xbmcplugin.setContent(addon_handle, 'movies')
    else:
        xbmcplugin.setContent(addon_handle, 'movies')

    if '<SetViewMode>' in data:
        try:
            viewmode=re.findall('<SetViewMode>(.*?)<',data)[0]
            xbmc.executebuiltin("Container.SetViewMode(%s)"%viewmode)
            #print 'done setview',viewmode
        except: pass

def getItems(items,fanart):
    use_thumb = addon.getSetting('use_thumb')
    for item in items:
        try:
            name = re.compile('<title>(.*?)</title>',re.MULTILINE|re.DOTALL).findall(item)[0].replace(';','')
            if name == None or name == '':
                #raise
                name = 'unknown?'
        except:
            name = ''

        try:
            thumbnail = re.compile('<thumbnail>(.*?)</thumbnail>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if thumbnail == None:
                #raise
                thumbnail = ''
        except:
            thumbnail = ''

        try:
            fanart1 = re.compile('<fanart>(.*?)</fanart>',re.MULTILINE|re.DOTALL).findall(item)[0]
        except:
            fanart1 = ''

        if not fanart1:
            if __addon__.getSetting('use_thumb') == "true":
                fanArt = thumbnail
            else:
                fanArt = fanart
        else:
            fanArt = fanart1
        if fanArt == None:
            #raise
            fanArt = ''

        try:
            desc = re.compile('<info>(.*?)</info>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if desc == None:
                #raise
                desc = ''
        except:
            desc = ''

        try:
            category = re.compile('<category>(.*?)</category>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if category == None:
                #raise
                category = ''
        except:
            category = ''

        try:
            subtitle1 = re.compile('<subtitle>(.*?)</subtitle>',re.MULTILINE|re.DOTALL).findall(item)
            if len(subtitle1)>0:
                subtitle = subtitle1[0]
                subs = []
                for sub in subtitle1:
                    subs.append('<subtitle>'+sub+'</subtitle>')
                #subtitle2 = subtitle1
                subtitle2 = subs
            else:
                subtitle = ''
                subtitle2 = ''
        except:
            subtitle = ''
            subtitle2 = ''

        try:
            utube = re.compile('<utube>(.*?)</utube>',re.MULTILINE|re.DOTALL).findall(item)
            if len(utube)>0:
                utube = utube[0]
            else:
                utube = ''
        except:
            utube = ''

        try:
            utubelive = re.compile('<utubelive>(.*?)</utubelive>',re.MULTILINE|re.DOTALL).findall(item)
            if len(utubelive)>0:
                utubelive = utubelive[0]
            else:
                utubelive = ''
        except:
            utubelive = ''
            
        try:
            dm = re.compile('<dm>(.*?)</dm>',re.MULTILINE|re.DOTALL).findall(item)
            if len(dm)>0:
                dm = dm[0]
            else:
                dm = ''
        except:
            dm = ''            

        try:
            jsonrpc = re.compile('<jsonrpc>(.*?)</jsonrpc>',re.MULTILINE|re.DOTALL).findall(item)
            externallink = re.compile('<externallink>(.*?)</externallink>',re.MULTILINE|re.DOTALL).findall(item)
            link = re.compile('<link>(.*?)</link>',re.MULTILINE|re.DOTALL).findall(item)
            if len(jsonrpc)>0:
                url = jsonrpc[0]
                url2 = ''
            elif len(externallink)>0:
                url = externallink[0]
                url2 = ''
            elif len(link)>0:
                try:
                    url = link[0]
                    mylinks = []
                    for link in link:
                        mylinks.append('<link>'+link+'</link>')
                    #url2 = link
                    url2 = mylinks
                except:
                    url = link[0]
                    url2 = ''
            else:
                url = ''
                url2 = ''
        except:
            url = ''
            url2 = ''
            
        try:
            regex = re.compile('<regex>(.*?)</regex>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(item)
        except:
            regex = ''
        
        if regex !=[] and regex !='' and regex !=None:    
            regx = []
            for r in regex:
                regx.append('<regex>'+r+'</regex>')
            regex = str(regx).replace('\\n', '\n').replace('\\r', '')
        else:
            regex = 'false'

        try:
            genre = re.compile('<genre>(.*?)</genre>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if genre == None:
                #raise
                genre = ''
        except:
            genre = ''

        try:
            date = re.compile('<date>(.*?)</date>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if date == None:
                #raise
                date = ''
        except:
            date = ''

        try:
            cblueits = re.compile('<cblueits>(.*?)</cblueits>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if cblueits == None:
                #raise
                cblueits = ''
        except:
            cblueits = ''

        try:
            year = re.compile('<year>(.*?)</year>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if year == None:
                #raise
                year = ''
        except:
            year = ''

        try:
            director = re.compile('<director>(.*?)</director>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if director == None:
                #raise
                director = ''
        except:
            director = ''

        try:
            writer = re.compile('<writer>(.*?)</writer>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if writer == None:
                #raise
                writer = ''
        except:
            writer = ''

        try:
            duration = re.compile('<duration>(.*?)</duration>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if duration == None:
                #raise
                duration = ''
        except:
            duration = ''

        try:
            premieblue = re.compile('<premieblue>(.*?)</premieblue>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if premieblue == None:
                #raise
                premieblue = ''
        except:
            premieblue = ''

        try:
            studio = re.compile('<studio>(.*?)</studio>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if studio == None:
                #raise
                studio = ''
        except:
            studio = ''

        try:
            rate = re.compile('<rate>(.*?)</rate>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if rate == None:
                #raise
                rate = ''
        except:
            rate = ''

        try:
            originaltitle = re.compile('<originaltitle>(.*?)</originaltitle>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if originaltitle == None:
                #raise
                originaltitle = ''
        except:
            originaltitle = ''

        try:
            country = re.compile('<country>(.*?)</country>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if country == None:
                #raise
                country = ''
        except:
            country = ''

        try:
            rating = re.compile('<rating>(.*?)</rating>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if rating == None:
                #raise
                rating = ''
        except:
            rating = ''

        try:
            userrating = re.compile('<userrating>(.*?)</userrating>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if userrating == None:
                #raise
                userrating = ''
        except:
            userrating = ''

        try:
            votes = re.compile('<votes>(.*?)</votes>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if votes == None:
                #raise
                votes = ''
        except:
            votes = ''

        try:
            aiblue = re.compile('<aiblue>(.*?)</aiblue>',re.MULTILINE|re.DOTALL).findall(item)[0]
            if aiblue == None:
                #raise
                aiblue = ''
        except:
            aiblue = ''


        try:
            if name > '' and url == '' and not utube > '' and not utubelive > '' and not dm > '':
                addLink(name.encode('utf-8', 'ignore'),'None','',thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
            elif name > '' and url == None and not utube > '' and not utubelive > '':
                addLink(name.encode('utf-8', 'ignore'),'None','',thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
            elif category == 'Adult' and url.find('blueecanais') >= 0 and url.find('m3u8') >= 0:
                addDir2(name.encode('utf-8', 'ignore'),url,10,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif category == 'Adult' and url.find('canaismax') >= 0:
                addDir2(name.encode('utf-8', 'ignore'),url,10,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('canaismax') >= 0 and url.find('page') >= 0:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('ultracine_page') >= 0 and not len(url2) >1:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('streamtape.com') >= 0 and not len(url2) >1:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('netcine2_page') >= 0 and not len(url2) >1:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('series_canaismax') >= 0 and not len(url2) >1:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif url.find('filmes_canaismax') >= 0 and not len(url2) >1:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif utube > '' and len(utube) == 11:
                link_youtube = 'plugin://plugin.video.youtube/play/?video_id='+utube
                addLink(name.encode('utf-8', 'ignore'), link_youtube,subtitle,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
            elif utubelive > '' and len(utubelive) == 11:
                link_live = 'https://www.youtube.com/watch?v='+utubelive
                addDir2(name.encode('utf-8', 'ignore'),link_live,17,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif dm > '' and len(dm) == 7:               
                link_dm = 'plugin://plugin.video.dailymotion_com/?mode=playVideo&url='+dm
                addLink(name.encode('utf-8', 'ignore'), link_dm,subtitle,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)                
            elif len(externallink)>0:
                addDir(name.encode('utf-8', 'ignore'),resolver(url,regex),1,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
            #Multilink
            elif len(url2) >1 and len(subtitle2) >1 and re.search(playlist_command,url,re.IGNORECASE):
                name_resolve = name+'[COLOR aquamarine] ('+str(len(url2))+' itens)[/COLOR]'
                addDir2(name_resolve.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,str(subtitle2).replace(',','||'),thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
            elif len(url2) >1 and re.search(playlist_command,url,re.IGNORECASE):
                name_resolve = name+'[COLOR aquamarine] ('+str(len(url2))+' itens)[/COLOR]'
                addDir2(name_resolve.encode('utf-8', 'ignore'),str(url2).replace(',','||').replace('$'+playlist_command+'','#'+playlist_command+''),11,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)
                #addLink(name.encode('utf-8', 'ignore'),resolver(url),subtitle,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)
            elif category == 'Adult':
                addDir2(name.encode('utf-8', 'ignore'),url,10,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False)
            else:
                addDir2(name.encode('utf-8', 'ignore'),url,16,subtitle,thumbnail,fanArt,desc.encode('utf-8'),genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,False,regex)            
            if not 'doregex' in url and not len(url2) >1 and 'youtube' in url:
                resolv = resolver(url,regex)
            else:
                resolv = ''
            if resolv.startswith('plugin://plugin.video.youtube/playlist') == True or resolv.startswith('plugin://plugin.video.youtube/channel') == True or resolv.startswith('plugin://plugin.video.youtube/user') == True or resolv.startswith('Plugin://plugin.video.youtube/playlist') == True:
                addDir(name.encode('utf-8', 'ignore'),resolver(url,regex),6,thumbnail,fanArt,desc,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue)            
        except:
            notify('[COLOR blue]Erro ao Carregar os items![/COLOR]')


def adult(name, url, iconimage, description, subtitle, regex):
    try:
        Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
    except:
        Path = xbmcvfs.translatePath(xbmcaddon.Addon().getAddonInfo('profile'))
    arquivo = os.path.join(Path, "password.txt")
    exists = os.path.isfile(arquivo)
    keyboard = xbmcaddon.Addon().getSetting("keyboard")
    if exists == False:
        parental_password()
        xbmc.sleep(10)
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            urlresolver = resolver(url,regex)
            #if urlresolver.startswith("plugin://") and not 'elementum' in str(urlresolver):
            #    xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
            #elif urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
            if urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + urlresolver + ",return)")
            else:
                li = xbmcgui.ListItem(name, path=urlresolver)
                li.setArt({"icon": iconimage, "thumb": iconimage})
                li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([subtitle])
                xbmc.Player().play(item=urlresolver, listitem=li)
        else:
            xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')
    else:
        p_file = open(arquivo,'r+')
        p_file_read = p_file.read()
        p_file_b64_decode = base64.b64decode(p_file_read).decode('utf-8')
        dialog = xbmcgui.Dialog()
        if int(keyboard) == 0:
            ps = dialog.numeric(0, 'Insira a senha atual:')
        else:
            ps = dialog.input('Insira a senha atual:', option=xbmcgui.ALPHANUM_HIDE_INPUT)
        if ps == p_file_b64_decode:
            urlresolver = resolver(url,regex)
            #if urlresolver.startswith("plugin://") and not 'elementum' in str(urlresolver):
            #    xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
            #elif urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
            if urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + urlresolver + ",return)")
            else:
                li = xbmcgui.ListItem(name, path=urlresolver)
                li.setArt({"icon": iconimage, "thumb": iconimage})
                li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([subtitle])
                xbmc.Player().play(item=urlresolver, listitem=li)
        else:
            xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Senha invalida!, se não alterou utilize a senha padrão')

def playlist(name, url, iconimage, description, subtitle, regex):
    playlist_command1 = playlist_command
    dialog = xbmcgui.Dialog()
    links = re.compile('<link>([\s\S]*?)#'+playlist_command1+'', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
    names = re.compile('#'+playlist_command1+'=([\s\S]*?)</link>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
    names2 = []
    subtitles = re.compile('<subtitle>([\s\S]*?)</subtitle>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(subtitle)
    for name in names:
        myname = name.replace('+', ' ')
        names2.append(myname)
    if links !=[] and names2 !=[]:
        index = dialog.select(dialog_playlist, names2)
        if index >= 0:
            playname=names2[index]
            if playname > '':
                playname1 = playname
            else:
                playname1 = 'Desconhecido'
            playlink=links[index]
            if subtitles !=[]:
                playsub=subtitles[index]
            else:
                playsub = ''
            urlresolver = resolver(playlink,regex)
            #if urlresolver.startswith("plugin://") and not 'elementum' in str(urlresolver):
            #    xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
            #elif urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
            if urlresolver.startswith('plugin://plugin.video.youtube/playlist') == True or urlresolver.startswith('plugin://plugin.video.youtube/channel') == True or urlresolver.startswith('plugin://plugin.video.youtube/user') == True or urlresolver.startswith('Plugin://plugin.video.youtube/playlist') == True:
                xbmc.executebuiltin("ActivateWindow(10025," + urlresolver + ",return)")
            else:
                li = xbmcgui.ListItem(playname1, path=urlresolver)
                li.setArt({"icon": iconimage, "thumb": iconimage})
                li.setInfo(type='video', infoLabels={'Title': playname1, 'plot': description })
                if subtitle > '':
                    li.setSubtitles([playsub])
                xbmc.Player().play(item=urlresolver, listitem=li)



def individual_player(name, url, iconimage, description, subtitle, regex):
    urlresolver = resolver(url,regex)
    #if urlresolver.startswith("plugin://") and not 'elementum' in str(urlresolver):
    #    xbmc.executebuiltin('RunPlugin(' + urlresolver + ')')
    #else:
    li = xbmcgui.ListItem(name, path=urlresolver)
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
    if subtitle > '':
        li.setSubtitles([subtitle])
    #xbmc.Player().play(item=urlresolver, listitem=li)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)


def m3u8_player(name, url, iconimage, description, subtitle):
    #if url.startswith("plugin://") and not 'elementum' in str(url):
    #    xbmc.executebuiltin('RunPlugin(' + url + ')')
    #else:
    li = xbmcgui.ListItem(name, path=url)
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
    if subtitle > '':
        li.setSubtitles([subtitle])
    xbmc.Player().play(item=url, listitem=li)


def ascii(string):
    if isinstance(string, basestring):
        if isinstance(string, unicode):
           string = string.encode('ascii', 'ignore')
    return string
def uni(string, encoding = 'utf-8'):
    if isinstance(string, basestring):
        if not isinstance(string, unicode):
            string = unicode(string, encoding, 'ignore')
    return string
def removeNonAscii(s): return "".join(filter(lambda x: ord(x)<128, s))

def sendJSON(command):
    data = ''
    try:
        data = xbmc.executeJSONRPC(uni(command))
    except UnicodeEncodeError:
        data = xbmc.executeJSONRPC(ascii(command))

    return uni(data)


def pluginquerybyJSON(url):
    json_query = uni('{"jsonrpc":"2.0","method":"Files.GetDirectory","params":{"directory":"%s","media":"video","properties":["thumbnail","title","year","dateadded","fanart","rating","season","episode","studio"]},"id":1}') %url

    json_folder_detail = json.loads(sendJSON(json_query))
    for i in json_folder_detail['result']['files'] :
        url = i['file']
        name = removeNonAscii(i['label'])
        thumbnail = removeNonAscii(i['thumbnail'])
        try:
            fanart = removeNonAscii(i['fanart'])
        except Exception:
            fanart = ''
        try:
            date = i['year']
        except Exception:
            date = ''
        try:
            episode = i['episode']
            season = i['season']
            if episode == -1 or season == -1:
                description = ''
            else:
                description = '[COLOR yellow] S' + str(season)+'[/COLOR][COLOR hotpink] E' + str(episode) +'[/COLOR]'
        except Exception:
            description = ''
        try:
            studio = i['studio']
            if studio:
                description += '\n Studio:[COLOR steelblue] ' + studio[0] + '[/COLOR]'
        except Exception:
            studio = ''

        desc = description+'\n\nDate: '+str(date)

        if i['filetype'] == 'file':
            #addLink(url,name,thumbnail,fanart,description,'',date,'',None,'',total=len(json_folder_detail['result']['files']))
            addLink(name.encode('utf-8', 'ignore'),url.encode('utf-8'),'',thumbnail,fanart,desc,'','','','','','','','','','','','','','','','')
            #xbmc.executebuiltin("Container.SetViewMode(500)")

        else:
            #addDir(name,url,53,thumbnail,fanart,description,'',date,'')
            addDir(name.encode('utf-8', 'ignore'),url.encode('utf-8'),6,iconimage,fanart,desc,'','','','','','','','','','','','','','','','')
            #xbmc.executebuiltin("Container.SetViewMode(500)")

def youtube_live(url):
    data = getRequest2(url, 'https://www.youtube.com/')
    #print(data)
    match = re.compile('"hlsManifestUrl.+?"(.+?).m3u8', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
    if match !=[]:
        stream = match[0].replace(':\\"https:', 'https:').replace('\/', '/').replace('\n', '')+'.m3u8|Referer=https://www.youtube.com/|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
        #print(stream)
        return stream
    else:
        stream = ''
        return stream


def youtube_live_player(name, url, iconimage, description, subtitle):
    li = xbmcgui.ListItem(name, path=youtube_live(url))
    li.setArt({"icon": iconimage, "thumb": iconimage})
    li.setInfo(type='video', infoLabels={'Title': name, 'plot': description })
    if subtitle > '':
        li.setSubtitles([subtitle])
    #xbmc.Player().play(item=youtube_live(url), listitem=li)
    xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, li)



def youtube(url):
    plugin_url = url
    xbmc.executebuiltin("ActivateWindow(10025," + plugin_url + ",return)")



def youtube_resolver(url):
    link_youtube = url
    if link_youtube.startswith('https://www.youtube.com/watch?v') == True or link_youtube.startswith('https://youtube.com/watch?v') == True:
        get_id1 = re.compile('v=(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('v=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/play/?video_id='+id_video
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/play/?video_id='+id_video
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/playlist?') == True or link_youtube.startswith('https://youtube.com/playlist?') == True:
        get_id1 = re.compile('list=(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('list=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/playlist/'+id_video+'/?page=0'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/playlist/'+id_video+'/?page=0'
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/channel') == True or link_youtube.startswith('https://youtube.com/channel') == True:
        get_id1 = re.compile('channel/(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('channel/(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/channel/'+id_video+'/'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/channel/'+id_video+'/'
        else:
            resolve = ''
    elif link_youtube.startswith('https://www.youtube.com/user') == True or link_youtube.startswith('https://youtube.com/user') == True:
        get_id1 = re.compile('user/(.+?)&', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        get_id2 = re.compile('user/(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(link_youtube)
        if get_id1 !=[]:
            #print('tem')
            id_video = get_id1[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/user/'+id_video+'/'
        elif get_id2 !=[]:
            #print('tem2')
            id_video = get_id2[0]
            #print(id)
            resolve = 'plugin://plugin.video.youtube/user/'+id_video+'/'
        else:
            resolve = ''

    else:
        resolve = ''
    return resolve


def youtube_restore(url):
    if url.find('/?video_id=') >= 0:
        find_id = re.compile('/?video_id=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        normal_url = 'https://www.youtube.com/watch?v='+str(find_id[0])
    elif url.find('youtube/playlist/') >= 0:
        find_id = re.compile('/playlist/(.+?)/', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        normal_url = 'https://www.youtube.com/playlist?list='+str(find_id[0])
    else:
        normal_url = ''
    return normal_url


def data_youtube(url, ref):
    try:
        try:
            import cookielib
        except ImportError:
            import http.cookiejar as cookielib
        try:
            import urllib2
        except ImportError:
            import urllib.request as urllib2
        if ref > '':
            ref2 = ref
        else:
            ref2 = url
        cj = cookielib.CookieJar()
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
        opener.addheaders=[('Accept-Language', 'en-US,en;q=0.9;q=0.8'),('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'), ('Referer', ref2)]
        data = opener.open(url).read()
        response = data.decode('utf-8')
        return response
    except:
        #pass
        response = ''
        return response


def getPlaylistLinksYoutube(url):
    try:
        sourceCode = data_youtube(youtube_restore(url), '')
    except:
        sourceCode = ''
    ytb_re = re.compile('url":"https://i.ytimg.com/vi/(.+?)/hqdefault.+?"width":.+?,"height":.+?}]},"title".+?"text":"(.+?)"}],', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(sourceCode)
    for video_id,name in ytb_re:
        original_name = str(name).replace(r"\u0026","&").replace('\\', '')
        thumbnail = "https://img.youtube.com/vi/%s/0.jpg" % video_id
        fanart = "https://i.ytimg.com/vi/%s/hqdefault.jpg" % video_id
        plugin_url = 'plugin://plugin.video.youtube/play/?video_id='+video_id
        urlfinal = str(plugin_url)
        description = ''
        addLink(original_name.encode('utf-8', 'ignore'),urlfinal,'',str(thumbnail),str(fanart),description,'','','','','','','','','','','','','','','','')


def canaismax(url):
    try:
        page = str(re.compile('canaismax_page=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)[0])
        data = getRequest2(page,'')
        source = re.compile('source.+?"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
        source2 = re.compile('var.+?url.+?=.+?"(.+?)";', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
        if source2 !=[]:
            link = source2[0].replace('\n','').replace('\r','')
            if '.m3u8' in str(link):
                stream = str(link)
            else:
                stream = ''
        elif source !=[]:
            link = source[0].replace('\n','').replace('\r','')
            if '.m3u8' in str(link):
                stream = str(link)
            else:
                stream = ''
        else:
            stream = ''
        return stream
    except:
        stream = ''
        return stream


def netcine2(url):
    try:
        page = str(re.compile('netcine2_page=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)[0])
        data = getRequest2(page,'')
        source = re.compile('source.+?"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
        if source !=[]:
            link = source[0].replace('\n','').replace('\r','')
        else:
            link = ''
        return link
    except:
        link = ''
        return link


def ultracine(url):
    try:
        page = str(re.compile('ultracine_page=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)[0])
        data = getRequest2(page,'')
        source = re.compile('.log.+?"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
        if source !=[]:
            link = source[0].replace('\n','').replace('\r','')
        else:
            link = ''
        return link
    except:
        link = ''
        return link


def streamtape(url):
    correct_url = url.replace('streamtape.com/v/', 'streamtape.com/e/')
    data = getRequest2(correct_url,'')
    link_part1_re = re.compile('videolink.+?style="display:none;">(.*?)&token=').findall(data)
    link_part2_re = re.compile("<script>.+?token=(.*?)'.+?</script>").findall(data)
    if link_part1_re !=[] and link_part2_re !=[]:
        #link = 'https:'+link_re[0]+'&stream=1'
        #link = 'https:'+link_part1_re[0]+'&token='+link_part2_re[0]
        link = 'https:'+link_part1_re[0]+'&token='+link_part2_re[0]+'|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'
    else:
        link = ''
    return link


def series_canaismax(url):
    try:
        page = re.compile('series_canaismax=(.+?)&idioma=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        link = page[0][0]
        idioma = page[0][1]
        if 'leg' in idioma or 'Leg' in idioma or 'LEG' in idioma:
            data = getRequest2(link,'')
            tags = re.compile('javascript.+?data-id="(.+?)".+?data-episodio="(.+?)".+?data-player="(.+?)".+?<i>(.+?)</i>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            tags2 = []
            for id,episodio,player,lang in tags:
                if 'LEG' in lang:
                    tags2.append((id,episodio,player))
            if tags2 !=[]:
                data_id = tags2[0][0]
                data_episodio = tags2[0][1]
                data_player = tags2[0][2]
                data2 = getRequest2('https://canaismax.com/embed/'+data_id+'/'+data_episodio+'/'+data_player,'')
                source = str(re.compile('source.+?"(.*?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)[0])+'|Referer=https://canaismax.com/'
            else:
                source = ''
        elif 'dub' in idioma or 'Dub' in idioma or 'DUB' in idioma:
            data = getRequest2(link,'')
            tags = re.compile('javascript.+?data-id="(.+?)".+?data-episodio="(.+?)".+?data-player="(.+?)".+?<i>(.+?)</i>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            tags2 = []
            for id,episodio,player,lang in tags:
                if 'DUB' in lang:
                    tags2.append((id,episodio,player))
            if tags2 !=[]:
                data_id = tags2[0][0]
                data_episodio = tags2[0][1]
                data_player = tags2[0][2]
                data2 = getRequest2('https://canaismax.com/embed/'+data_id+'/'+data_episodio+'/'+data_player,'')
                source = str(re.compile('source.+?"(.*?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)[0])+'|Referer=https://canaismax.com/'
            else:
                source = ''
        else:
            source = ''
        return source
    except:
        source = ''
        return source


def filmes_canaismax(url):
    try:
        page = re.compile('filmes_canaismax=(.+?)&idioma=(.*)', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(url)
        link = page[0][0]
        idioma = page[0][1]
        if 'leg' in idioma or 'Leg' in idioma or 'LEG' in idioma:
            data = getRequest2(link,'')
            tags = re.compile('javascript.+?data-id="(.+?)".+?data-player="(.+?)".+?<i>(.+?)</i>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            tags2 = []
            for id,player,lang in tags:
                if 'LEG' in lang:
                    tags2.append((id,player))
            if tags2 !=[]:
                data_id = tags2[0][0]
                data_player = tags2[0][1]
                data2 = getRequest2('https://canaismax.com/embed/'+data_id+'/'+data_player,'')
                source = str(re.compile('source.+?"(.*?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)[0])+'|Referer=https://canaismax.com/'
            else:
                source = ''
        elif 'dub' in idioma or 'Dub' in idioma or 'DUB' in idioma:
            data = getRequest2(link,'')
            tags = re.compile('javascript.+?data-id="(.+?)".+?data-player="(.+?)".+?<i>(.+?)</i>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
            tags2 = []
            for id,player,lang in tags:
                if 'DUB' in lang:
                    tags2.append((id,player))
            if tags2 !=[]:
                data_id = tags2[0][0]
                data_player = tags2[0][1]
                data2 = getRequest2('https://canaismax.com/embed/'+data_id+'/'+data_player,'')
                source = str(re.compile('source.+?"(.*?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data2)[0])+'|Referer=https://canaismax.com/'
            else:
                source = ''
        else:
            source = ''
        return source
    except:
        source = ''
        return source


def doEval(fun_call):
    ret_val=''
    #print fun_call
    if functions_dir not in sys.path:
        sys.path.append(functions_dir)

#    print fun_call
    try:
        py_file='import '+fun_call.split('.')[0]
#        print py_file,sys.path
        exec( py_file)
#        print 'done'
    except:
        #print 'error in import'
        traceback.print_exc(file=sys.stdout)
#    print 'ret_val='+fun_call
    exec ('ret_val='+fun_call)
#    print ret_val
    #exec('ret_val=1+1')
    try:
        return str(ret_val)
    except: return ret_val


def getRegex(url,regex='false'):
    if not 'false' in str(regex) and '$doregex' in url:
        regex = re.compile('<regex>(.*?)</regex>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(regex)
        resolved={}
        for r in regex:
            name = re.compile('<name>(.*?)</name>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
            if name !=[]:
                name = name[0]
            else:
                name = ''                
                
            if 'page' in r:
                page = re.compile('<page>(.*?)</page>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                if page !=[]:
                    page = page[0]
                else:
                    page = ''
            else:
                page = ''
            if 'expres' in r:
                expres = re.compile('<expres>(.*?)</expres>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                if expres !=[]:
                    expres = expres[0]
                else:
                    expres = ''
            else:
                expres = ''
                    
            if not '$doregex' in page and page !='' and not '$doregex' in expres:                
                if 'page' in r:                    
                    if 'proxy' in r:
                        proxy = re.compile('<proxy>(.*?)</proxy>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                        if proxy !=[]:
                            if 'http:' in proxy[0]:
                                page = page.replace('https:', 'http:')
                            elif 'https' in proxy[0]:
                                page = page.replace('http:', 'https:')
                    if page !='':
                        #print(page)
                        req = urllib2.Request(page)
                        if 'referer' in r:
                            referer = re.compile('<referer>(.*?)</referer>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                            if referer !=[]:
                                req.add_header('Referer', referer[0])
                        if 'accept' in r:
                            accept = re.compile('<accept>(.*?)</accept>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                            if accept !=[]:
                                req.add_header('Accept', accept[0])
                        if 'agent' in r:
                            agent = re.compile('<agent>(.*?)</agent>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                            if agent !=[]:
                                req.add_header('User-agent', agent[0])
                            else:
                                req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                        else:
                            req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                                
                        if 'setcookie' in r:
                            setcookie = re.compile('<setcookie>(.*?)</setcookie>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                            if setcookie !=[]:
                                req.add_header('Cookie', setcookie[0])
                        if 'proxy' in r:
                            try:
                                if 'http:' in proxy:
                                    httpsplit = proxy.split('http://')
                                    #configura um "opener" com um proxy
                                    proxy  = urllib2.ProxyHandler({"http":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                                elif 'https:' in proxy:
                                    httpsplit = proxy.split('https://')
                                    proxy  = urllib2.ProxyHandler({"https":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                            except:
                                pass
                        if 'post' in r:
                            post = re.compile('<post>(.*?)</post>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r)
                            if post !=[]:
                                postData = post
                                splitpost=postData.split(',')
                                post={}
                                for p in splitpost:
                                    n=p.split(':')[0];
                                    v=p.split(':')[1];
                                    post[n]=v
                                post = urllib.urlencode(post).encode()   
                                response = urllib2.urlopen(req,post)
                        else:
                            response = urllib2.urlopen(req)
                        data = response.read().decode('utf8')
                    else:
                        data = ''
                else:
                    data = ''
                if expres.startswith('$pyFunction:'):
                    try:
                        func = expres.split('$pyFunction:')[1]
                        link = doEval(func)
                    except:
                        link = ''
                elif data !='' and expres !='':
                    exp = re.compile(expres).findall(data)
                    if exp !=[]:
                        link = exp[0]
                    else:
                        link = ''
                else:
                    link = ''
                if link !='':
                    resolved[name]=link
#-------------------------------------------------------------------------------------------------------------
        for r2 in regex:
            if 'page' in r2:
                page = re.compile('<page>(.*?)</page>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                if page !=[]:
                    page = page[0]
                else:
                    page = ''
            else:
                page = ''
            if 'expres' in r:
                expres = re.compile('<expres>(.*?)</expres>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                if expres !=[]:
                    expres = expres[0]
                else:
                    expres = ''
            else:
                expres = ''
            if '$doregex' in page and page !='' and not '$doregex' in expres:
                name = re.compile('<name>(.*?)</name>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                if name !=[]:
                    name = name[0]
                else:
                    name = ''
                if page !='':
                    doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(page)
                    if doRegexs !=[]:
                        for n in doRegexs:
                            page = page.replace('$doregex['+n+']', resolved[n])                    
                    
                        req = urllib2.Request(page)
                        if 'referer' in r:
                            referer = re.compile('<referer>(.*?)</referer>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                            if referer !=[]:
                                req.add_header('Referer', referer[0])
                        if 'accept' in r:
                            accept = re.compile('<accept>(.*?)</accept>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                            if accept !=[]:
                                req.add_header('Accept', accept[0])
                        if 'agent' in r:
                            agent = re.compile('<agent>(.*?)</agent>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                            if agent !=[]:
                                req.add_header('User-agent', agent[0])
                            else:
                                req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                        else:
                            req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                                
                        if 'setcookie' in r:
                            setcookie = re.compile('<setcookie>(.*?)</setcookie>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                            if setcookie !=[]:
                                req.add_header('Cookie', setcookie[0])
                        if 'proxy' in r:
                            try:
                                if 'http:' in proxy:
                                    httpsplit = proxy.split('http://')
                                    #configura um "opener" com um proxy
                                    proxy  = urllib2.ProxyHandler({"http":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                                elif 'https:' in proxy:
                                    httpsplit = proxy.split('https://')
                                    proxy  = urllib2.ProxyHandler({"https":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                            except:
                                pass
                        if 'post' in r:
                            post = re.compile('<post>(.*?)</post>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r2)
                            if post !=[]:
                                postData = post
                                splitpost=postData.split(',')
                                post={}
                                for p in splitpost:
                                    n=p.split(':')[0];
                                    v=p.split(':')[1];
                                    post[n]=v
                                post = urllib.urlencode(post).encode()   
                                response = urllib2.urlopen(req,post)
                        else:
                            response = urllib2.urlopen(req)
                        data = response.read().decode('utf8')
                else:
                    data = ''
                if expres.startswith('$pyFunction:'):
                    try:
                        func = expres.split('$pyFunction:')[1]
                        link = doEval(func)
                    except:
                        link = ''
                elif data !='' and expres !='':
                    exp = re.compile(expres).findall(data)
                    if exp !=[]:
                        link = exp[0]
                    else:
                        link = ''
                else:
                    link = ''
                if link !='':
                    resolved[name]=link
        #print(resolved)
#-------------------------------------------------------------------------------------------------------------
        for r3 in regex:
            if 'page' in r3:
                page = re.compile('<page>(.*?)</page>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                if page !=[]:
                    page = page[0]
                else:
                    page = ''
            else:
                page = ''
            if 'expres' in r:
                expres = re.compile('<expres>(.*?)</expres>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                if expres !=[]:
                    expres = expres[0]
                else:
                    expres = ''
            else:
                expres = ''

            if not '$doregex' in page and page !='' and '$doregex' in expres:
                name = re.compile('<name>(.*?)</name>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                if name !=[]:
                    name = name[0]
                else:
                    name = ''
                if page !='':
                    doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(expres)
                    if doRegexs !=[]:
                        for n in doRegexs:
                            expres = expres.replace('$doregex['+n+']', resolved[n])                    
                    
                        req = urllib2.Request(page)
                        if 'referer' in r:
                            referer = re.compile('<referer>(.*?)</referer>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                            if referer !=[]:
                                req.add_header('Referer', referer[0])
                        if 'accept' in r:
                            accept = re.compile('<accept>(.*?)</accept>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                            if accept !=[]:
                                req.add_header('Accept', accept[0])
                        if 'agent' in r:
                            agent = re.compile('<agent>(.*?)</agent>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                            if agent !=[]:
                                req.add_header('User-agent', agent[0])
                            else:
                                req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                        else:
                            req.add_header('User-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36')
                                
                        if 'setcookie' in r:
                            setcookie = re.compile('<setcookie>(.*?)</setcookie>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                            if setcookie !=[]:
                                req.add_header('Cookie', setcookie[0])
                        if 'proxy' in r:
                            try:
                                if 'http:' in proxy:
                                    httpsplit = proxy.split('http://')
                                    #configura um "opener" com um proxy
                                    proxy  = urllib2.ProxyHandler({"http":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                                elif 'https:' in proxy:
                                    httpsplit = proxy.split('https://')
                                    proxy  = urllib2.ProxyHandler({"https":httpsplit[1]})
                                    auth = urllib2.HTTPBasicAuthHandler()
                                    opener = urllib2.build_opener(proxy, auth, urllib2.HTTPHandler)
                                    urllib2.install_opener(opener)
                            except:
                                pass
                        if 'post' in r:
                            post = re.compile('<post>(.*?)</post>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r3)
                            if post !=[]:
                                postData = post
                                splitpost=postData.split(',')
                                post={}
                                for p in splitpost:
                                    n=p.split(':')[0];
                                    v=p.split(':')[1];
                                    post[n]=v
                                post = urllib.urlencode(post).encode()   
                                response = urllib2.urlopen(req,post)
                        else:
                            response = urllib2.urlopen(req)
                        data = response.read().decode('utf8')
                else:
                    data = ''
                if expres.startswith('$pyFunction:'):
                    try:
                        func = expres.split('$pyFunction:')[1]
                        link = doEval(func)
                    except:
                        link = ''
                elif data !='' and expres !='':
                    exp = re.compile(expres).findall(data)
                    if exp !=[]:
                        link = exp[0]
                    else:
                        link = ''
                else:
                    link = ''
                if link !='':
                    resolved[name]=link                   
#-------------------------------------------------------------------------------------------------------------
        for r4 in regex:
            if 'page' in r4:
                page = re.compile('<page>(.*?)</page>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r4)
                if page !=[]:
                    page = page[0]
                else:
                    page = ''
            else:
                page = ''
            if 'expres' in r:
                expres = re.compile('<expres>(.*?)</expres>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r4)
                if expres !=[]:
                    expres = expres[0]
                else:
                    expres = ''
            else:
                expres = ''          

            if not page !='' and '$doregex' in expres:
                name = re.compile('<name>(.*?)</name>', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(r4)
                if name !=[]:
                    name = name[0]
                else:
                    name = ''
                doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(expres)
                if doRegexs !=[]:
                    for n in doRegexs:
                        expres = expres.replace('$doregex['+n+']', resolved[n])
                if expres.startswith('$pyFunction:'):
                    try:
                        func = expres.split('$pyFunction:')[1]
                        link = doEval(func)
                    except:
                        link = ''
                else:
                    link = ''
                if link !='':
                    resolved[name]=link
        try:
            if '$doregex' in url:
                doRegexs = re.compile('\$doregex\[([^\]]*)\]').findall(url)
                if doRegexs !=[]:
                    for n in doRegexs:
                        url = url.replace('$doregex['+n+']', resolved[n])
        except:
            pass
    return url


def resolver(link,regex):
    #xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]',str(regex))
    if not 'false' in str(regex) and '$doregex' in link:
        link_decoded = getRegex(link,regex)
    else:    
        link_decoded = link
    try:
        if not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://drive.google.com') == True:
            #print('verdadeiro')
            resolved = link_decoded.replace('http','plugin://plugin.video.gdrive?mode=streamURL&amp;url=http')
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('http://drive.google.com') == True:
            #print('verdadeiro')
            resolved = link_decoded.replace('http','plugin://plugin.video.gdrive?mode=streamURL&amp;url=http')
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('streamtape.com') >= 0:
            link = streamtape(link_decoded)
            resolved = link
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('ultracine_page') >= 0:
            link = ultracine(link_decoded)
            resolved = link
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('netcine2_page') >= 0:
            link = netcine2(link_decoded)
            resolved = link
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('series_canaismax') >= 0:
            link_corrigido = link_decoded.replace('idioma;', 'idioma')
            link = series_canaismax(link_corrigido)
            resolved = link
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('filmes_canaismax') >= 0:
            link_corrigido = link_decoded.replace('idioma;', 'idioma')
            link = filmes_canaismax(link_corrigido)
            resolved = link
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('eu-central-1.edge.mycdn.live') >= 0:
            #print('verdadeiro')
            resolved = link_decoded
            #print(resolved)
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('canaismax_page') >= 0:
            stream = canaismax(link_decoded)
            resolved = stream+'|Referer=https://canaismax.com/|User-Agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://youtube.com/') == True or link_decoded.startswith('https://www.youtube.com/') == True:
            try:
                resultado = youtube_resolver(link_decoded)
                if resultado==None:
                    #print('vazio')
                    resolved = ''
                else:
                    resolved = resultado
            except:
                resolved = ''
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('https://photos.app') == True:
            try:
                data = getRequest2(link_decoded, 'https://photos.google.com/')
                result = re.compile('<meta property="og:video" content="(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(data)
                if result !=[]:
                    resolved = result[0].replace('-m18','-m22')
                else:
                    resolved = ''
            except:
                resolved = ''
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.startswith('magnet:?xt=') == True:
            resolved = 'plugin://plugin.video.elementum/play?uri='+link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.torrent') >= 0:
            resolved = 'plugin://plugin.video.elementum/play?uri='+link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mp4') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mkv') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.wmv') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.wma') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.avi') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.mp3') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.ac3') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin") and link_decoded.find('.rmvb') >= 0 and not link_decoded.startswith('magnet:?xt=') == True and not link_decoded.find('.torrent') >= 0:
            resolved = link_decoded
        elif not link_decoded.startswith("plugin://plugin"):
            resolved = link_decoded
        elif link_decoded.startswith("plugin://plugin"):
            resolved = link_decoded
        return resolved
    except:
        resolved = ''
        return resolved
        #pass
        #notify('[COLOR blue]Não foi possivel resolver um link![/COLOR]')



def getFavorites():
    try:
        try:
            items = json.loads(open(favorites).read())
        except:
            items = ''
        total = len(items)
        if int(total) > 0:
            for i in items:
                name = i[0]
                url = i[1]
                try:
                    urldecode = base64.b64decode(base64.b16decode(url))
                except:
                    urldecode = url
                try:
                    url2 = urldecode.decode('utf-8')
                except:
                    url2 = urldecode

                mode = i[2]
                subtitle = i[3]
                try:
                    subtitledecode = base64.b64decode(base64.b16decode(subtitle))
                except:
                    subtitledecode = subtitle
                try:
                    sub2 = subtitledecode.decode('utf-8')
                except:
                    sub2 = subtitledecode
                iconimage = i[4]
                try:
                    fanArt = i[5]
                    if fanArt == None:
                        raise
                except:
                    if addon.getSetting('use_thumb') == "true":
                        fanArt = iconimage
                    else:
                        fanArt = fanart
                description = i[6]
                
                regex = i[7]

                if mode == 0:
                    try:
                        #addLink(name.encode('utf-8', 'ignore'),url2,sub2,iconimage,fanArt,description.encode('utf-8'),'','','','','','','','','','','','','','','','')
                        addLink(name.encode('utf-8', 'ignore'),url2,sub2,iconimage,fanArt,description.encode('utf-8'),'','','','','','','','','','','','','','','','')
                    except:
                        pass
                elif mode == 11 or mode == 16 or mode == 17 or mode == 18:
                    try:
                        addDir2(str(name).encode('utf-8', 'ignore'),url2,mode,sub2,iconimage,fanArt,description.encode('utf-8'),'','','','','','','','','','','','','','','','',False,regex)
                    except:
                        pass
                elif mode > 0 and mode < 7:
                    try:
                        addDir(name.encode('utf-8', 'ignore'),url2,mode,iconimage,fanArt,description.encode('utf-8'),'','','','','','','','','','','','','','','','')
                    except:
                        pass
                else:
                    try:
                        addDir2(name.encode('utf-8', 'ignore'),url2,mode,sub2,iconimage,fanArt,description.encode('utf-8'),'','','','','','','','','','','','','','','','')
                    except:
                        pass
                xbmcplugin.setContent(addon_handle, 'movies')
                xbmcplugin.endOfDirectory(addon_handle)
        else:
            xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','Nada Adicionado nos Favoritos')
    except:
        pass


def addFavorite(name,url,fav_mode,subtitle,iconimage,fanart,description,regex):
    favList = []
    if os.path.exists(favorites)==False:
        addonID = xbmcaddon.Addon().getAddonInfo('id')
        addon_data_path = xbmcvfs.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        favList.append((name,url,fav_mode,subtitle,iconimage,fanart,description,regex))
        a = open(favorites, "w")
        a.write(json.dumps(favList))
        a.close()
        notify('Adicionado aos Favoritos do '+__addonname__)
        #xbmc.executebuiltin("XBMC.Container.Refresh")
    else:
        a = open(favorites).read()
        data = json.loads(a)
        data.append((name,url,fav_mode,subtitle,iconimage,fanart,description,regex))
        b = open(favorites, "w")
        b.write(json.dumps(data))
        b.close()
        notify('Adicionado aos Favoritos do '+__addonname__)
        #xbmc.executebuiltin("XBMC.Container.Refresh")


def rmFavorite(name):
    data = json.loads(open(favorites).read())
    for index in range(len(data)):
        if data[index][0]==name:
            del data[index]
            b = open(favorites, "w")
            b.write(json.dumps(data))
            b.close()
            break
    notify('Removido dos Favoritos do '+__addonname__)
    #xbmc.executebuiltin("XBMC.Container.Refresh")

def addDir(name,url,mode,iconimage,fanart,description,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,folder=True):
    if mode == 1:
        if url > '':
            #u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b64encode(url))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            #u=sys.argv[0]+"?url="+urllib.quote_plus(codecs.encode(base64.b32encode(base64.b16encode(url)), '\x72\x6f\x74\x31\x33'))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            #u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b32encode(url.encode('utf-8')))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            #u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
            u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8'))))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8'))))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    else:
        u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    li=xbmcgui.ListItem(name)
    if folder:
        li.setArt({"icon": "DefaultFolder.png", "thumb": iconimage})
    else:
        li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
    if date != '' and date !=None:
        description += '\n\nDate: %s' %date
    li.setInfo('video', { 'title': name, 'plot': description })
    try:
        li.setInfo('video', { 'genre': str(genre) })
    except:
        pass
    try:
        li.setInfo('video', { 'dateadded': str(date) })
    except:
        pass
    try:
        li.setInfo('video', { 'cblueits': str(cblueits) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'director': str(director) })
    except:
        pass
    try:
        li.setInfo('video', { 'writer': str(writer) })
    except:
        pass
    try:
        li.setInfo('video', { 'duration': int(duration) })
    except:
        pass
    try:
        li.setInfo('video', { 'premieblue': str(premieblue) })
    except:
        pass
    try:
        li.setInfo('video', { 'studio': str(studio) })
    except:
        pass
    try:
        li.setInfo('video', { 'mpaa': str(rate) })
    except:
        pass
    try:
        li.setInfo('video', { 'originaltitle': str(originaltitle) })
    except:
        pass
    try:
        li.setInfo('video', { 'country': str(country) })
    except:
        pass
    try:
        li.setInfo('video', { 'rating': float(rating) })
    except:
        pass
    try:
        li.setInfo('video', { 'userrating': int(userrating) })
    except:
        pass
    try:
        li.setInfo('video', { 'votes': str(votes) })
    except:
        pass
    try:
        li.setRating("imdb", float(rating), int(votes), True)
    except:
        pass
    try:
        li.setInfo('video', { 'aiblue': str(aiblue) })
    except:
        pass

    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    try:
        name_decode = name.decode('utf-8')
    except:
        name_decode = name
    try:
        name_fav = json.dumps(name_decode)
    except:
        name_fav =  name_decode
    try:
        contextMenu = []
        if favoritos == 'true' and  mode !=4 and mode !=7 and mode !=8 and mode !=9 and mode !=10 and mode !=12 and mode !=15:
            if name_fav in FAV:
                contextMenu.append(('Remover dos Favoritos do '+__addonname__,'RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
            else:
                fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&iconimage=%s&fanart=%s&description=%s&regex=false&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), '', urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), str(mode)))
                contextMenu.append(('Adicionar aos Favoritos do '+__addonname__,'RunPlugin(%s)' %fav_params))
        contextMenu.append(('Informação', 'RunPlugin(%s?mode=19&name=%s&description=%s)' % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(description))))
        li.addContextMenuItems(contextMenu)
    except:
        pass
    xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=li, isFolder=folder)

def addDir2(name,url,mode,subtitle,iconimage,fanart,description,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,folder=True,regex=False):
    if mode == 1:
        if url > '':
            u=sys.argv[0]+"?url="+urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8'))))+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)
    else:
        if regex:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&subtitle="+urllib.quote_plus(subtitle)+"&description="+urllib.quote_plus(description)+"&regex="+urllib.quote_plus(regex)
        else:
            u=sys.argv[0]+"?url="+urllib.quote_plus(url)+"&mode="+str(mode)+"&name="+urllib.quote_plus(name)+"&fanart="+urllib.quote_plus(fanart)+"&iconimage="+urllib.quote_plus(iconimage)+"&subtitle="+urllib.quote_plus(subtitle)+"&description="+urllib.quote_plus(description)
    li=xbmcgui.ListItem(name)
    if folder:
        li.setArt({"icon": "DefaultFolder.png", "thumb": iconimage})
    else:
        li.setArt({"icon": "DefaultVideo.png", "thumb": iconimage})
    if mode == 16 or mode == 17:
        li.setProperty('IsPlayable', 'true')        
    if date == '':
        date = None
    else:
        description += '\n\nDate: %s' %date
    li.setInfo('video', { 'title': name, 'plot': description })
    try:
        li.setInfo('video', { 'genre': str(genre) })
    except:
        pass
    try:
        li.setInfo('video', { 'dateadded': str(date) })
    except:
        pass
    try:
        li.setInfo('video', { 'cblueits': str(cblueits) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'director': str(director) })
    except:
        pass
    try:
        li.setInfo('video', { 'writer': str(writer) })
    except:
        pass
    try:
        li.setInfo('video', { 'duration': int(duration) })
    except:
        pass
    try:
        li.setInfo('video', { 'premieblue': str(premieblue) })
    except:
        pass
    try:
        li.setInfo('video', { 'studio': str(studio) })
    except:
        pass
    try:
        li.setInfo('video', { 'mpaa': str(rate) })
    except:
        pass
    try:
        li.setInfo('video', { 'originaltitle': str(originaltitle) })
    except:
        pass
    try:
        li.setInfo('video', { 'country': str(country) })
    except:
        pass
    try:
        li.setInfo('video', { 'rating': float(rating) })
    except:
        pass
    try:
        li.setInfo('video', { 'userrating': int(userrating) })
    except:
        pass
    try:
        li.setInfo('video', { 'votes': str(votes) })
    except:
        pass
    try:
        li.setRating("imdb", float(rating), int(votes), True)
    except:
        pass
    try:
        li.setInfo('video', { 'aiblue': str(aiblue) })
    except:
        pass
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    try:
        name_decode = name.decode('utf-8')
    except:
        name_decode = name
    try:
        name_fav = json.dumps(name_decode)
    except:
        name_fav =  name_decode
    try:
        contextMenu = []
        if favoritos == 'true' and  mode !=4 and mode !=7 and mode !=8 and mode !=9 and mode !=10 and mode !=12 and mode !=15:
            if name_fav in FAV:
                contextMenu.append(('Remover dos Favoritos do '+__addonname__,'RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
            else:
                if regex:
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&iconimage=%s&fanart=%s&description=%s&regex=%s&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), urllib.quote_plus(regex), str(mode)))
                else:
                    fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&iconimage=%s&fanart=%s&description=%s&regex=false&fav_mode=%s'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description), str(mode)))
                contextMenu.append(('Adicionar aos Favoritos do '+__addonname__,'RunPlugin(%s)' %fav_params))
        contextMenu.append(('Informação', 'RunPlugin(%s?mode=19&name=%s&description=%s)' % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(description))))
        li.addContextMenuItems(contextMenu)
    except:
        pass
    xbmcplugin.addDirectoryItem(handle=addon_handle,url=u,listitem=li, isFolder=folder)

def addLink(name,url,subtitle,iconimage,fanart,description,genre,date,cblueits,year,director,writer,duration,premieblue,studio,rate,originaltitle,country,rating,userrating,votes,aiblue,folder=False):
    if date == '':
        date = None
    else:
        description += '\n\nDate: %s' %date
    if iconimage > '':
        thumbnail = iconimage
    else:
        thumbnail = 'DefaultVideo.png'
    li=xbmcgui.ListItem(name)
    li.setArt({"icon": "DefaultVideo.png", "thumb": thumbnail})
    if url.startswith("plugin://plugin.video.f4mTester"):
        li.setProperty('IsPlayable', 'false')
    else:
        li.setProperty('IsPlayable', 'true')
    if fanart > '':
        li.setProperty('fanart_image', fanart)
    else:
        li.setProperty('fanart_image', ''+home+'/fanart.jpg')
    try:
        name_fav = json.dumps(name)
    except:
        name_fav = name
    name2_fav = name
    desc_fav = description
    li.setInfo('video', { 'plot': description })
    try:
        li.setInfo('video', { 'genre': str(genre) })
    except:
        pass
    try:
        li.setInfo('video', { 'dateadded': str(date) })
    except:
        pass
    try:
        li.setInfo('video', { 'cblueits': str(cblueits) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'year': int(year) })
    except:
        pass
    try:
        li.setInfo('video', { 'director': str(director) })
    except:
        pass
    try:
        li.setInfo('video', { 'writer': str(writer) })
    except:
        pass
    try:
        li.setInfo('video', { 'duration': int(duration) })
    except:
        pass
    try:
        li.setInfo('video', { 'premieblue': str(premieblue) })
    except:
        pass
    try:
        li.setInfo('video', { 'studio': str(studio) })
    except:
        pass
    try:
        li.setInfo('video', { 'mpaa': str(rate) })
    except:
        pass
    try:
        li.setInfo('video', { 'originaltitle': str(originaltitle) })
    except:
        pass
    try:
        li.setInfo('video', { 'country': str(country) })
    except:
        pass
    try:
        li.setInfo('video', { 'rating': float(rating) })
    except:
        pass
    try:
        li.setInfo('video', { 'userrating': int(userrating) })
    except:
        pass
    try:
        li.setInfo('video', { 'votes': str(votes) })
    except:
        pass
    try:
        li.setRating("imdb", float(rating), int(votes), True)
    except:
        pass
    try:
        li.setInfo('video', { 'aiblue': str(aiblue) })
    except:
        pass

    if subtitle > '':
        li.setSubtitles([subtitle])
    try:
        name_decode = name.decode('utf-8')
    except:
        name_decode = name
    try:
        name_fav = json.dumps(name_decode)
    except:
        name_fav =  name_decode
    try:
        contextMenu = []
        if favoritos == 'true':
            if name_fav in FAV:
                contextMenu.append(('Remover dos Favoritos do '+__addonname__,'RunPlugin(%s?mode=14&name=%s)'%(sys.argv[0], urllib.quote_plus(name))))
            else:
                fav_params = ('%s?mode=13&name=%s&url=%s&subtitle=%s&iconimage=%s&fanart=%s&description=%s&regex=false&fav_mode=0'%(sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(base64.b16encode(base64.b64encode(url.encode('utf-8')))), urllib.quote_plus(base64.b16encode(base64.b64encode(subtitle.encode('utf-8')))), urllib.quote_plus(iconimage), urllib.quote_plus(fanart), urllib.quote_plus(description)))
                contextMenu.append(('Adicionar aos Favoritos do '+__addonname__,'RunPlugin(%s)' %fav_params))
        contextMenu.append(('Informação', 'RunPlugin(%s?mode=19&name=%s&description=%s)' % (sys.argv[0], urllib.quote_plus(name), urllib.quote_plus(description))))
        li.addContextMenuItems(contextMenu)
    except:
        pass
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=url, listitem=li, isFolder=folder)

def parental_password():
    try:
        addonID = xbmcaddon.Addon().getAddonInfo('id')
        addon_data_path = xbmc.translatePath(os.path.join('special://home/userdata/addon_data', addonID))
        if os.path.exists(addon_data_path)==False:
            os.mkdir(addon_data_path)
        xbmc.sleep(7)
        #Path = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo('profile')).decode("utf-8")
        #arquivo = os.path.join(Path, "password.txt")
        arquivo = os.path.join(addon_data_path, "password.txt")
        exists = os.path.isfile(arquivo)
        if exists == False:
            password = '0069'
            p_encoded = base64.b64encode(password.encode()).decode('utf-8')
            p_file = open(arquivo,'w')
            p_file.write(p_encoded)
            p_file.close()
    except:
        pass

     


def time_convert(timestamp):
    try:
        if timestamp > '':
            dt_object = datetime.fromtimestamp(int(timestamp))
            time_br = dt_object.strftime('%d/%m/%Y às %H:%M:%S')
            return str(time_br)
        else:
            valor = ''
            return valor
    except:
        valor = ''
        return valor

def info_vip():
    username_vip = addon.getSetting('username')
    password_vip = addon.getSetting('password')
    if username_vip > '' and password_vip > '':
        try:
            url_info = url_server_vip.replace('/get.php', '')+'/player_api.php?username=%s&password=%s'%(username_vip,password_vip)
            dados_vip = getRequest2(url_info, '')
            filtrar_info = re.compile('"status":"(.+?)".+?"exp_date":"(.+?)".+?"is_trial":"(.+?)".+?"created_at":"(.+?)".+?max_connections":"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(dados_vip)
            if filtrar_info !=[]:
                status = str(filtrar_info[0][0])
                exp_date = str(filtrar_info[0][1])
                trial = str(filtrar_info[0][2])
                created = str(filtrar_info[0][3])
                max_connection = str(filtrar_info[0][4])
                #status do usuario
                if status > '' and status == 'Active':
                    status_result = 'Ativo'
                else:
                    status_result = 'Expirado'
                #Validade do vip
                if exp_date > '':
                    expires = time_convert(str(exp_date))
                else:
                    expires = ''
                #usuario de teste
                if trial > '' and trial == '0':
                    vip_trial = 'Não'
                else:
                    vip_trial = 'Sim'
                #criado
                if created > '':
                    created_time = time_convert(str(created))
                else:
                    created_time = ''
                #limite de conexoes
                if max_connection > '':
                    limite_conexao = max_connection
                else:
                    limite_conexao = ''

                try:
                    xbmcaddon.Addon().setSetting("status_vip", status_result)
                    xbmcaddon.Addon().setSetting("created_at", created_time)
                    xbmcaddon.Addon().setSetting("exp_date", expires)
                    xbmcaddon.Addon().setSetting("is_trial", vip_trial)
                    xbmcaddon.Addon().setSetting("max_connection", limite_conexao)
                except:
                    pass
        except:
            try:
                xbmcaddon.Addon().setSetting("status_vip", '')
                xbmcaddon.Addon().setSetting("created_at", '')
                xbmcaddon.Addon().setSetting("exp_date", '')
                xbmcaddon.Addon().setSetting("is_trial", '')
                xbmcaddon.Addon().setSetting("max_connection", '')
            except:
                pass

def vip():
    username_vip = addon.getSetting('username')
    password_vip = addon.getSetting('password')
    #tipo_servidor = addon.getSetting('servidor')
    vip_menu = addon.getSetting('exibirvip')
    saida_transmissao = addon.getSetting('saida')
    if username_vip > '' and password_vip > '':
        info_vip()
    if int(saida_transmissao) == 1:
        saida_canal = 'm3u8'
    else:
        saida_canal = 'ts'
    if vip_menu == 'true':
        if username_vip > '' and password_vip > '':
            url = ''+url_server_vip+'?username=%s&password=%s&type=m3u_plus&output=%s'%(username_vip,password_vip,saida_canal)
            #addDir(name,url,mode,iconimage,fanart,description)
            addDir(titulo_vip,url,1,thumbnail_vip,fanart_vip,vip_descricao,'','','','','','','','','','','','','','','','')
        else:
            #if tipo_servidor=='Desativado':
            #addDir(name,url,mode,iconimage,fanart,description)
            addDir(titulo_vip,'',9,thumbnail_vip,fanart_vip,vip_descricao,'','','','','','','','','','','','','','','','')

def Pesquisa():
    vq = get_search_string(heading="Digite algo para pesquisar")
    if ( not vq ): return False, 0
    title = urllib.quote_plus(vq)
    addDir('[COLOR blue][B]PESQUISAR NOVAMENTE...[/B][/COLOR]','',7,thumb_pesquisar,fanart_pesquisar,desc_pesquisa,'','','','','','','','','','','','','','','','')
    try:
        getData(url_pesquisa+'?pesquisar='+title, '')
    except:
        pass
    xbmcplugin.endOfDirectory(addon_handle)

def SetView(name):
    if name == 'Wall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(500)')
        except:
            pass
    if name == 'List':
        try:
            xbmc.executebuiltin('Container.SetViewMode(50)')
        except:
            pass
    if name == 'Poster':
        try:
            xbmc.executebuiltin('Container.SetViewMode(51)')
        except:
            pass
    if name == 'Shift':
        try:
            xbmc.executebuiltin('Container.SetViewMode(53)')
        except:
            pass
    if name == 'InfoWall':
        try:
            xbmc.executebuiltin('Container.SetViewMode(54)')
        except:
            pass
    if name == 'WideList':
        try:
            xbmc.executebuiltin('Container.SetViewMode(55)')
        except:
            pass
    if name == 'Fanart':
        try:
            xbmc.executebuiltin('Container.SetViewMode(502)')
        except:
            pass

    
def contador():
    try:
        import platform
        if platform.system() == 'Linux':
            sistema_operacional = 'Android 9; Mobile; rv:68.0'
        elif platform.system() == 'Windows':
           sistema_operacional = 'Windows NT 6.1; WOW64; rv:54.0'
        elif platform.system() == 'IOS':
           sistema_operacional = 'iPhone; CPU iPhone OS 12_2 like Mac OS X'
        else:
            sistema_operacional = ''
        request_headers = {    
        "Accept-Language": "en-US,en;q=0.5",
        "\x55\x73\x65\x72\x2d\x61\x67\x65\x6e\x74": sistema_operacional,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,/;q=0.8",
        "Connection": "keep-alive" 
        }
        opener = urllib2.build_opener()
        opener.addheaders=[('Accept-Language', 'pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7'),('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36'),('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'), ('Referer', nome_contador)]
        data = opener.open(link_contador).read()
    except:
        pass
contador()

def check_addon():
    try:
        check_file = xbmc.translatePath(home+'/check.txt')
        exists = os.path.isfile(check_file)
        check_addon = addon.getSetting('check_addon')
        #check_file = 'check.txt'
        if exists == True:
            #print('existe')
            fcheck = open(check_file,'r+')
            elementum = addon.getSetting('elementum')
            youtube = addon.getSetting('youtube')
            if fcheck and fcheck.read() == '1' and check_addon == 'true':
                #print('valor 1')
                fcheck.close()
                link = getRequest2('https://raw.githubusercontent.com/zoreu/zoreu.github.io/master/kodi/verificar_addons_matrix.txt','').replace('\n','').replace('\r','')
                match = re.compile('addon_name="(.+?)".+?ddon_id="(.+?)".+?ir="(.+?)".+?rl_zip="(.+?)".+?escription="(.+?)"').findall(link)
                for addon_name,addon_id,directory,url_zip,description in match:
                    if addon_id == 'plugin.video.elementum' and elementum == 'false':
                        pass
                    elif addon_id == 'script.module.six' and youtube == 'false':
                        pass
                    elif addon_id == 'plugin.video.youtube' and youtube == 'false':
                        pass
                    else:
                        existe = xbmc.translatePath(directory)
                        #print('Path dir:'+existe)
                        if os.path.exists(existe)==False:
                            install_wizard(addon_name,addon_id,url_zip,directory,description)
                            if addon_id == 'plugin.video.elementum':
                                xbmcgui.Dialog().ok()
                        else:
                            pass
        elif check_addon == 'true':
            #print('nao existe')
            fcheck = open(check_file,'w')
            fcheck.write('1')
            fcheck.close()
            xbmcgui.Dialog().ok()
    except:
        pass


def install_wizard(name,addon_id,url,directory,description):
    try:
        import downloader
        import extract
        import ntpath
        path = xbmc.translatePath(os.path.join('special://','home/','addons', 'packages'))
        filename = ntpath.basename(url)
        dp = xbmcgui.DialogProgress()
        dp.create("Instalador de Complementos","Baixando & Instalando "+name+",\nPor favor aguarde....")
        lib=os.path.join(path, filename)
        try:
            os.remove(lib)
        except:
            pass
        downloader.download(url, lib, dp)
        addonfolder = xbmc.translatePath(os.path.join('special://','home/','addons'))
        xbmc.sleep(100)
        dp.update(0,"Instalando "+name+", Por Favor Espere")
        try:
            xbmc.executebuiltin("Extract("+lib+","+addonfolder+")")
        except:
            extract.all(lib,addonfolder,dp)
        #############
        #time.sleep(2)
        xbmc.sleep(100)
        xbmc.executebuiltin("XBMC.UpdateLocalAddons()")
        notify(name+' Instalado com Sucesso!')
        import database
        database.enable_addon(addon_id)
        if addon_id == 'plugin.video.elementum':
            database.enable_addon('repository.elementum')
        #xbmc.executebuiltin("XBMC.Container.Refresh()")
        xbmc.executebuiltin("XBMC.Container.Update()")
        xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]',''+name+' instalado com sucesso!\nObservação;\nÉ necessário Forçar Fechar o KODI para iniciar o Elementum no menu a seguir.\nFeche e abra o Kodi novamente!')
        kill_kodi()
    except:
        notify('Erro ao baixar o complemento')
        
    
                
def kill_kodi():
    dialog = xbmcgui.Dialog()
    link = dialog.select('[B][COLOR blue]FINALIZANDO INSTALAÇÃO DO ELEMENTUM[/COLOR][/B]', ['[COLOR blue]SIM POR FAVOR! [/COLOR][COLOR orange]|[/COLOR] [COLOR lime]FORÇAR FECHAR[/COLOR]','[COLOR blue]NÃO POR FAVOR! [/COLOR][COLOR orange]|[/COLOR] [COLOR blue]NÃO CANCELAR[/COLOR]'])    
            
    if link == 0:
     xbmcplugin.endOfDirectory(int(os._exit(1)))

    if link == 1:
     xbmcplugin.endOfDirectory(int(sys.argv[1])) 

def info_vip():
    username_vip = addon.getSetting('username')
    password_vip = addon.getSetting('password')
    if username_vip > '' and password_vip > '':
        try:
            url_info = url_server_vip.replace('/get.php', '')+'/player_api.php?username=%s&password=%s'%(username_vip,password_vip)
            dados_vip = getRequest2(url_info, '')
            filtrar_info = re.compile('"status":"(.+?)".+?"exp_date":"(.+?)".+?"is_trial":"(.+?)".+?"created_at":"(.+?)".+?max_connections":"(.+?)"', re.MULTILINE|re.DOTALL|re.IGNORECASE).findall(dados_vip)
            if filtrar_info !=[]:
                status = str(filtrar_info[0][0])
                exp_date = str(filtrar_info[0][1])
                trial = str(filtrar_info[0][2])
                created = str(filtrar_info[0][3])
                max_connection = str(filtrar_info[0][4])
                #status do usuario
                if status > '' and status == 'Active':
                    status_result = 'Ativo'
                else:
                    status_result = 'Expirado'
                #Validade do vip
                if exp_date > '':
                    expires = time_convert(str(exp_date))
                else:
                    expires = ''
                #usuario de teste
                if trial > '' and trial == '0':
                    vip_trial = 'Não'
                else:
                    vip_trial = 'Sim'
                #criado
                if created > '':
                    created_time = time_convert(str(created))
                else:
                    created_time = ''
                #limite de conexoes
                if max_connection > '':
                    limite_conexao = max_connection
                else:
                    limite_conexao = ''

                try:
                    xbmcaddon.Addon().setSetting("status_vip", status_result)
                    xbmcaddon.Addon().setSetting("created_at", created_time)
                    xbmcaddon.Addon().setSetting("exp_date", expires)
                    xbmcaddon.Addon().setSetting("is_trial", vip_trial)
                    xbmcaddon.Addon().setSetting("max_connection", limite_conexao)
                except:
                    pass
        except:
            try:
                xbmcaddon.Addon().setSetting("status_vip", '')
                xbmcaddon.Addon().setSetting("created_at", '')
                xbmcaddon.Addon().setSetting("exp_date", '')
                xbmcaddon.Addon().setSetting("is_trial", '')
                xbmcaddon.Addon().setSetting("max_connection", '')
            except:
                pass       

			
def init_SKindex(msg):
   status_mensagem1 = addon.getSetting('mensagem1')
   if status_mensagem1 == 'true':
    dialog = xbmcgui.Dialog()
    link = dialog.select('SEJAM [COLOR  azure] BEM - VINDOS AO [/COLOR][B][COLOR azure] WEB[/COLOR][COLOR blue]PLAY![/COLOR][/B]', ['[B][COLOR azure] WEB[/COLOR][COLOR blue]PLAY:[/COLOR][/B] MERCADO PAGO', '[B][COLOR azure] WEB[/COLOR][COLOR blue]PLAY:[/COLOR][/B] PAGSEGURO', '[B][COLOR azure] WEB[/COLOR][COLOR blue]PLAY:[/COLOR][/B] WHATSAPP', '[B][COLOR azure] WEB[/COLOR][COLOR blue]PLAY:[/COLOR][/B] FACEBOOK', '[B][COLOR azure]ACESSAR [/COLOR] [COLOR blue] AQUI[/COLOR] [/B]'])
      
    if link == 0:
     if xbmc . getCondVisibility ( 'system.platform.android' ) :
         xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://plugin.video.primevideo' ) )
     else:
        ost = webbrowser . open ( 'https://plugin.video.primevideo' )
 
    if link == 1:
     if xbmc . getCondVisibility ( 'system.platform.android' ) :
         xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://plugin.video.primevideo' ) )
     else:
        ost = webbrowser . open ( 'https://' )
    
    if link == 2:
     if xbmc . getCondVisibility ( 'system.platform.android' ) :
         ost = xbmc . executebuiltin ( 'StartAndroidActivity(,android.intent.action.VIEW,,%s)' % ( 'https://plugin.video.primevideo' ) )
     else:
        webbrowser . open ( 'https://plugin.video.primevideo' ) 

    if link == 4:
     xbmc.executebuiltin("XBMC.Container.Refresh('close()')")
     xbmcplugin.endOfDirectory(int(sys.argv[1]))


def mensagem(msg):
   status_mensagem2 = addon.getSetting('mensagem2')
   if status_mensagem2 == 'true':     
    xbmc.executebuiltin("Notification({0}, {1}, 10000, {2})".format(__addonname__,getRequest2('https://raw.githubusercontent.com/webplay10/PRIMEVIDEO/master/Alarme', ''), __icon__))     


def SKindex():
    #addDir(name,url,mode,iconimage,fanart,description)
    addDir(title_menu,url_title,20,__icon__,'',title_descricao,'','','','','','','','','','','','','','','','')
    if favoritos == 'true':
        addDir(menu_favoritos,'',15,__icon__,'',desc_favoritos,'','','','','','','','','','','','','','','','')
    vip()        
    getData(url_principal, '')
    addDir(menu_configuracoes,'',4,thumb_icon_config,'',desc_configuracoes,'','','','','','','','','','','','','','','','')	
    init_SKindex(True)
    mensagem(True)    
    xbmcplugin.endOfDirectory(addon_handle)

def get_params():
    param=[]
    paramstring=sys.argv[2]
    if len(paramstring)>=2:
        params=sys.argv[2]
        cleanedparams=params.replace('?','')
        if (params[len(params)-1]=='/'):
            params=params[0:len(params)-2]
        pairsofparams=cleanedparams.split('&')
        param={}
        for i in range(len(pairsofparams)):
            splitparams={}
            splitparams=pairsofparams[i].split('=')
            if (len(splitparams))==2:
                param[splitparams[0]]=splitparams[1]

    return param

params=get_params()
url=None
name=None
mode=None
iconimage=None
fanart=None
description=None
subtitle=None
regex='true'

try:
    url=urllib.unquote(params["url"])
    #url=urllib.unquote_plus(params["url"]).decode('utf-8')
except:
    pass

try:
    #name=urllib.unquote(params["name"])
    name=urllib.unquote_plus(params["name"])
except:
    pass

try:
    #iconimage=urllib.unquote(params["iconimage"])
    iconimage=urllib.unquote_plus(params["iconimage"])
except:
    pass

try:
    mode=int(params["mode"])
except:
    pass

try:
    #fanart=urllib.unquote(params["fanart"])
    fanart=urllib.unquote_plus(params["fanart"])
except:
    pass

try:
    #description=urllib.unquote(params["description"])
    description=urllib.unquote_plus(params["description"])
except:
    pass

try:
    subtitle=urllib.unquote_plus(params["subtitle"])
except:
    pass
    
try:
    regex=urllib.unquote_plus(params["regex"])
except:
    pass    

try:
    fav_mode=int(params["fav_mode"])
except:
    pass

if mode==None:
    xbmcplugin.setContent(addon_handle, 'movies')
    check_addon()
    parental_password()
    SKindex()
    SetView('List')

elif mode==1:
    #url = base64.b16decode(base64.b32decode(codecs.decode(url, '\x72\x6f\x74\x31\x33')))
    #url = base64.b64decode(url)
    url = base64.b64decode(base64.b16decode(url))
    try:
        url = url.decode('utf-8')
    except:
        pass
    getData(url, fanart)
    xbmcplugin.endOfDirectory(addon_handle)

#elif mode==2:
#    getChannelItems(name,url,fanart)
#    xbmcplugin.endOfDirectory(addon_handle)

#elif mode==3:
#    getSubChannelItems(name,url,fanart)
#    xbmcplugin.endOfDirectory(addon_handle)

#Configurações
elif mode==4:   
    xbmcaddon.Addon().openSettings()
    xbmcgui.Dialog().ok('[B][COLOR blue]AVISO IMPORTANTE![/COLOR][/B]','[B][COLOR orange]|[/COLOR][/B][COLOR blue] POR FAVOR SAIR DO ADD-ON E ENTRE NOVAMENTE,[B] [COLOR orange]|[/COLOR][/B] PARA ATUALIZAR AS CONFIGURAÇÕES![B] [COLOR orange]|[/COLOR][/B]')
    xbmc.executebuiltin("XBMC.Container.Refresh()")

#Link Vazio
elif mode==5:
    Init_CheckUpdate(True)   
    xbmc.executebuiltin("XBMC.Container.Refresh()")

elif mode==6:
    ytbmode = addon.getSetting('ytbmode')
    if int(ytbmode) == 0:
        pluginquerybyJSON(url)
    elif int(ytbmode) == 1:
        getPlaylistLinksYoutube(url)
    else:
        youtube(url)
    xbmcplugin.endOfDirectory(addon_handle)

#elif mode==7:
#    Pesquisa()

elif mode==9:
    xbmcgui.Dialog().ok(titulo_vip, vip_dialogo)
    xbmcaddon.Addon().openSettings()
    xbmcgui.Dialog().ok('[B][COLOR blue]AVISO[/COLOR][/B]','FECHE O KODI E ABRA NOVAMENTE PARA ATUALIZAR AS CONFIGURAÇÕES')
    xbmc.executebuiltin("XBMC.Container.Refresh")

elif mode==10:
    adult(name, url, iconimage, description, subtitle, regex)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==11:
    playlist(name, url, iconimage, description, subtitle, regex)
    xbmcplugin.endOfDirectory(addon_handle)

elif mode==12:
    CheckUpdate(True)
    xbmc.executebuiltin("XBMC.Container.Refresh()")

elif mode==13:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    addFavorite(name,url,fav_mode,subtitle,iconimage,fanart,description,regex)

elif mode==14:
    try:
        name = name.split('\\ ')[1]
    except:
        pass
    try:
        name = name.split('  - ')[0]
    except:
        pass
    rmFavorite(name)

elif mode==15:
    #xbmcplugin.setContent(addon_handle, 'movies')
    getFavorites()
    #xbmcplugin.endOfDirectory(addon_handle)

elif mode==16:
    individual_player(name, url, iconimage, description, subtitle, regex)
    #xbmcplugin.endOfDirectory(addon_handle)

elif mode==17:
    youtube_live_player(name, url, iconimage, description, subtitle)
    #xbmcplugin.endOfDirectory(addon_handle)

elif mode==18:
    m3u8_player(name, url, iconimage, description, subtitle)
    #xbmcplugin.endOfDirectory(addon_handle)

elif mode==19:
    xbmcgui.Dialog().textviewer('Informação: '+name, description)
  