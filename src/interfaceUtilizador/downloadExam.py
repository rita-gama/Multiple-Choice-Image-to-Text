
from urllib import request


"""
    Nota: isto pode nao funcionar no futuro porque vamos buscar o url ao site, caso a 
    estrutura do site do iave mude, pode nao haver garantias que isto funcione
"""

"""
    TODO: faco alguma pesquisa para o ano? tipo binária ou eh overkill?
    ou regex? ou so um for?
"""

#nota nao faco validacao do input

def downloadExame():
    urls = open("urlsArquivo.html", "r") #equivalente a wget

    lines = urls.readlines()

    #print(lines[0])

    disciplina = input("Qual é a disciplina que queres? \n")
    ano = input("Qual é o ano? \n")

    #print(lines)

    for line in lines:
        if(ano in line):
            print(line)

    #TODO: dar parse do url especifico do ano

    #TODO: dar parse da disciplina

    fileWithCodeAno = ano + ".txt"

    print(fileWithCodeAno)

    url = "https://iave.pt/provas-e-exames/arquivo/arquivo-provas-e-exames-finais-nacionais-es/?ano=2015"

    siteAno = request.urlretrieve(url, fileWithCodeAno)

    urls.close()


downloadExame()




