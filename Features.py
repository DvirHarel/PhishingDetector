import requests
from tldextract import tldextract
import socket
import urllib

def ANumOfDots(url):
    return url.count(".")
def BSubDomainLevel(url):
    res = tldextract.extract(url)
    subdomain = res.subdomain
    if(subdomain):
        return subdomain.count('.')+1 if subdomain.count('.') > 0 else 1 if subdomain else 0
    return -1
def CPathLevel(url):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    if(path):
        ls = path.split('/')
        re_ls = []
        for item in ls:
            if item:
                re_ls.append(item)
        return len(re_ls)
    return -1
def DUrlLength(url):
    return len(url)
def ENumDash(url):
    return url.count('-')
def FNumDashInHostname(url):
    parsed_url = urllib.parse.urlparse(url)
    host_name = parsed_url.hostname
    if(host_name):
        return host_name.count('-')
    return 1
def GAtSymbol(url):
    return 1 if (url.count('@') > 0) else 0
def HTildeSymbol(url):
    return 1 if (url.count('~') > 0) else 0
def INumUnderscore(url):
    return url.count('_')
def JNumPercent(url):
    return url.count('%')
def KNumQueryComponents(url):
    parsed_url = urllib.parse.urlparse(url)
    query = parsed_url.query
    if(query):
        return query.count('=')
    return -1
def LNumAmpersand(url):
    return url.count('&')
def MNumHash(url):
    return url.count('#')
def NNumNumericChars(url):
    counter = 0
    for ch in url:
        if ch.isnumeric():
            counter+=1
    return counter
def ONoHttp(url):
    return 1 if (url.count('https') > 0) else 0
def PPopUpWindow(url):
    try:
        res = requests.get(url)
        if(not(res.ok)):
            return 0
        return 1 if (res.text.count('popup') > 0) else 0
    except:
        return -1
def QIpAddress(url):
    parsed_url = urllib.parse.urlparse(url)
    host_name = parsed_url.hostname
    if(host_name):
        try:
            ip = socket.gethostbyname(host_name)
            return 1 if ip != "0.0.0.0" else 0
        except:
            return -1
    return -1
def RDomainInSubdomains(url):
    res = tldextract.extract(url)
    subdomain = res.subdomain
    if(subdomain):
        res = tldextract.extract(subdomain)
        return 1 if res.domain else 0
    return -1
def SDomainInPaths(url):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    if(path):
        res = tldextract.extract(path)
        return 1 if res.domain else 0
    return -1
def THttpsInHostName(url):
    parsed_url = urllib.parse.urlparse(url)
    host_name = parsed_url.hostname
    if(host_name):
        return 1 if (host_name.count('https') > 0) else 0
    return -1
def UHostnameLength(url):
    parsed_url = urllib.parse.urlparse(url)
    host_name = parsed_url.hostname
    if(host_name):
        return len(host_name)
    return -1
def VPathLength(url):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    if(path):
        return len(path)
    return -1
def WQueryLength(url):
    parsed_url = urllib.parse.urlparse(url)
    query = parsed_url.query
    if(query):
        return len(query)-1
    return -1
def XDoubleSlashInPath(url):
    parsed_url = urllib.parse.urlparse(url)
    path = parsed_url.path
    if(path):
        return 1 if (path.count('//') > 0) else 0
    return -1
def YMissingTitle(url):
    try:
        res = requests.get(url)
        if(not(res.ok)):
            return -1
        return 1 if (res.text.count('<title>') > 0) else 0
    except:
        return 1
def ZSubmitInfoToEmail(url):
    try:
        res = requests.get(url)
        if(not(res.ok)):
            return -1
        return 1 if (res.text.count('mailto') > 0) else 0
    except:
        return 1
def AANumOfSensetiveWords(url):
    ls = ["secure", "account", "webscr", "login","ebayisapi", "signin", "banking", "confirm"]
    counter = 0
    for word in ls:
        counter+= url.count(word)
    return counter