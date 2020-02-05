# !python3
# este programa remove caracteres indesejados (y2mate.com - ) no nome da musica

#importando as bibliotecas
import os, shutil, re

#estabelecendo um padrao a ser encotrado
padrao_musica = re.compile(r' \w+',re.IGNORECASE)

#exibindo os arquivos no diretorio
for nome_antigo in os.listdir('.'):
    #procurando as musicas cujo o inicio coincide com o padrao
    if nome_antigo.startswith("y2mate.com - "):
        
        extracao = padrao_musica.search(nome_antigo)
        extracao = extracao.group()

        
        novo_nome = extracao.lstrip()+".mp3"
        #obtendo o caminho absoluto da pasta
        pasta_musicas = os.path.abspath('.')

        nome_antigo = os.path.join(pasta_musicas, nome_antigo)

        novo_nome = os.path.join(pasta_musicas, novo_nome)

        #print("Renomeanado %s para %s" %(nome_antigo,novo_nome))
        shutil.move(nome_antigo, novo_nome)
print("Concluído")
    
        
