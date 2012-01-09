from urllib2 import urlopen
from BeautifulSoup import BeautifulSoup
import re

def returnSoup(url=''):
    if(url != ''):
        webpage = urlopen(url)
        soup = BeautifulSoup(webpage)
    else:
        soup = BeautifulSoup('')

    return soup

def find(url='', pattern=''):
    if(url == ''):
        return False

    soup = returnSoup(url)
    element = re.findall(pattern, str(soup))

    return element
