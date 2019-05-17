# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:31:55 2019

@author: d805664
"""

import nltk
from nameparser.parser import HumanName

def get_human_names(text):
    tokens = nltk.tokenize.word_tokenize(text)
    pos = nltk.pos_tag(tokens)
    sentt = nltk.ne_chunk(pos, binary = False)
    person_list = []
    person = []
    name = ""
    for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
        for leaf in subtree.leaves():
            person.append(leaf[0])
        if len(person) > 1: #avoid grabbing lone surnames
            for part in person:
                name += part + ' '
            if name[:-1] not in person_list:
                person_list.append(name[:-1])
            name = ''
        person = []

    return (person_list)


if __name__ == "__main__":
        
    
    text = """
    O ministro da Educação, Abraham Weintraub, partiu para o ataque na tarde desta quarta-feira, 15, durante audiência na Câmara para explicar os cortes na Educação. Ao defender o uso de recursos recuperados de corrupção na área, afirmou ter a ficha limpa, não ter passagem pela polícia e ter sua carteira assinada. Em seguida, de forma irônica, provocou os deputados: “Fui bancário. Carteira assinada. Viu, azulzinha, não sei se vocês conhecem”, afirmou, provocando vaias de parte dos parlamentares que assistia a audiência. Um coro se formou, com deputados gritando “Demissão” - Capitais têm manifestações contra cortes na educação; acompanhe aqui).
    
    Weintraub foi convocado por parlamentares para explicar o contingenciamento na área da educação. Numa exposição de 30 minutos, uma versão revista da que ele expôs no Senado há alguns dias, o ministro defendeu a prioridade para creches e educação básica, irritando os parlamentares, por não falar diretamente sobre o contingenciamento determinado pelo governo. 
    
    Abraham Weintraub foi convocado para explicar o contingenciamento na área da educação Foto: Dida Sampaio/Estadão
    Diante as primeiras críticas ouvidas dos deputados Paulo Pimenta e Orlando Silva, Weintraub não ficou na defensiva e adotou um discurso também agressivo. Citou a ex-presidente Dilma Rousseff, numa referência a manobras nas contas que levaram ao pedido de impeachment. Mais tarde, a líder da minoria na Câmara, Jandira Feghalli (PCdoB-RJ), questionou, dentre outros temas, se o ministro havia dito e se mantinha a fala de que “comunistas mereciam uma bala na cabeça”.
    
    “Eu sou comunista e estou aqui, ministro”, disse Feghalli que no discurso, pediu a demissão. E ele, mais uma vez, Weintraub aumentou o tom. “Não tenho passagem pela polícia por ameaça, agressão. Não tenho processo trabalhista. Minha ficha é limpíssima, não tenho mácula. Tiveram que voltar 30 anos na minha vida para obter um boletim ruim porque eu tinha arrebentado o meu braço, obtido de forma ilegal”, disse. “Outra coisa, bala na cabeça, quem prega, não é esse lado aqui.” 
    
    
    
    Diante dos gritos ele elevou o tom para falar sobre o ex-presidente Lula que, ressaltou “hoje está preso.” O ministro afirmou que uma colega teria sido demitida por influência do ex-presidente, que teria pedido o cargo da funcionária à presidência do banco Santander, depois de ela fazer críticas ao ex-presidente. “O amigo do banqueiro e o Lula que pediu a cabeça da colega de profissão. Foi o Lula que humilhou e falou que era para o banco pagar o bônus para ele.” Minutos depois, mais calmo, ele disse estar “aberto ao diálogo.”
    """
    
    names = get_human_names(text)
    print("NOMES:")
    for name in names: 
        last_first = HumanName(name).first + ' ' + HumanName(name).last
        print(last_first)
    
    print(nltk.Text(text.split()).concordance("Weintraub"))
    
