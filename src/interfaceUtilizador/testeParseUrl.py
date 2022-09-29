"""
    source: https://docs.python.org/3/library/urllib.parse.html
"""
import regex as re
from urllib import request

def parseUrl():
    url = "bla bla bla https://iave.pt/provas-e-exames/arquivo/arquivo-provas-e-exames-finais-nacionais-es?ano=2021"

    #https://stackoverflow.com/questions/839994/extracting-a-url-in-python
    url = re.search("https?://[^\s]+", url).group(0) 

    print(url)

    siteAno = request.urlretrieve(url, "ano.html")


parseUrl()