import json
import os.path
import sys
from typing import List

from sqlalchemy import null

def obter_dados() -> list:
    '''
    Essa função carrega os dados dos produtos e retorna uma lista de dicionários, onde cada dicionário representa um produto.
    NÃO MODIFIQUE essa função.
    '''
    with open(os.path.join(sys.path[0], 'dados.json'), 'r') as arq:
        dados = json.loads(arq.read())
    return dados

def listar_categorias(dados:list)-> list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista contendo todas as categorias dos diferentes produtos.
    Cuidado para não retornar categorias repetidas.    
    '''
    lista_cate=[]
    
    for i in dados:
        if i["categoria"] not in lista_cate:
            lista_cate.append(i["categoria"])
        else:
            continue
    
    return lista_cate
    

def listar_por_categoria(dados:list, categoria:str) ->list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar uma lista contendo todos os produtos pertencentes à categoria dada.
    '''
    lista_prod=[]
    for i in dados:
        if i["categoria"]==categoria:
            lista_prod.append(i)
        else:
            pass
    return lista_prod
    

def produto_mais_caro(dados:list, categoria:str) ->dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais caro da categoria dada.
    '''
    dados_categoria=listar_por_categoria(dados, categoria)
    dados_sorted=sorted(dados_categoria,key=lambda x: (float(x["preco"])),reverse=True)
    return dados_sorted[0]



def produto_mais_barato(dados:list, categoria:str) ->dict:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um dicionário representando o produto mais barato da categoria dada.
    '''
    dados_categoria=listar_por_categoria(dados, categoria)
    dados_sorted=sorted(dados_categoria,key=lambda x: (float(x["preco"])),reverse=False)
    return dados_sorted[0]


def top_10_caros(dados:list) ->list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais caros.
    '''
    dados_sorted=sorted(dados,key=lambda x: float(x["preco"]),reverse=True)
    return dados_sorted[:10]


def top_10_baratos(dados:list) ->list:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá retornar uma lista de dicionários representando os 10 produtos mais baratos.
    '''
    dados_sorted=sorted(dados,key=lambda x: float(x["preco"]))
    return dados_sorted[:10]

def verifica_categoria(dados:list,categoria:str) ->bool:
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    O parâmetro "categoria" é uma string contendo o nome de uma categoria.
    Essa função deverá retornar um booleano dizendo se a categoria existe na lista.
    '''
    if categoria in listar_categorias(dados):
        return True
    else:
        return False

def print_retorno(retorno:list):
    '''
    O parâmetro "retorno" pode ser uma lista de strings, uma lista de dicionário ou um dicionário.
    Essa função não tem retorno, apenas imprime os valores na tela.
    '''

    if type(retorno)==list:
        if type(retorno[0])==dict:
            print(f"\n id | preco | categoria\n")
            for i in retorno:
                id=i["id"]
                preco=i["preco"]
                categoria=i["categoria"]
                print(f" {id} | {preco} | {categoria}\n")
        else:
            print("Categorias disponíveis")
            for i in retorno:
                print("\n",i)
            
    elif type(retorno)==dict:
        print(f"\n id | preco | categoria\n")
        id=retorno["id"]
        preco=retorno["preco"]
        categoria=retorno["categoria"]
        print(f" {id} | {preco} | {categoria}\n")
        
def menu(dados:list) :
    '''
    O parâmetro "dados" deve ser uma lista de dicionários representando os produtos.
    Essa função deverá, em loop, realizar as seguintes ações:
    - Exibir as seguintes opções:
       1. Listar categorias
        2. Listar produtos de uma categoria
        3. Produto mais caro por categoria
        4. Produto mais barato por categoria
        5. Top 10 produtos mais caros
        6. Top 10 produtos mais baratos
        0. Sair 
    - Ler a opção do usuário.
    - No caso de opção inválida, imprima uma mensagem de erro.
    - No caso das opções 2, 3 ou 4, pedir para o usuário digitar a categoria desejada.
    - Chamar a função adequada para tratar o pedido do usuário e salvar seu retorno.
    - Imprimir o retorno salvo. 
    O loop encerra quando a opção do usuário for 0.
    '''
    entrada=10
    while entrada!=0:
        entrada=input("Escolha um número abaixo:\n 1. Listar categorias\n 2. Listar produtos de uma categoria\n 3. Produto mais caro por categoria\n 4. Produto mais barato por categoria\n 5. Top 10 produtos mais caros\n 6. Top 10 produtos mais baratos\n 0. Sair\n")
        if entrada.isdigit():
            entrada=int(entrada)
        if entrada in [0,1,2,3,4,5,6]:
            if entrada==1:      
                retorno=listar_categorias(dados)
            elif entrada==2:
                categoria=input("digite a categoria desejada: ")
                if verifica_categoria(dados,categoria):
                    print(f"\nLista de produtos da categoria {categoria}\n")
                    retorno=listar_por_categoria(dados, categoria)
                else:
                    print("Categoria inválida\n")
                    continue
            elif entrada==3:
                categoria=input("digite a categoria desejada: ")
                if verifica_categoria(dados,categoria):
                    print(f"\nProduto mais caro da categoria {categoria}\n")
                    retorno=produto_mais_caro(dados, categoria)
                else:
                    print("Categoria inválida\n")
                    continue
            elif entrada==4:
                categoria=input("digite a categoria desejada: ")
                if verifica_categoria(dados,categoria):
                    print(f"\nProduto mais barato da categoria {categoria}\n")
                    retorno=produto_mais_barato(dados, categoria)
                else:
                    print("Categoria inválida\n")
                    continue
            elif entrada==5:
                print("\nTop 10 produtos mais caros\n")
                retorno=top_10_caros(dados)
            elif entrada==6:
                print("\nTop 10 produtos mais baratos\n")
                retorno=top_10_baratos(dados)
            elif entrada==0:
                continue  
            print_retorno(retorno)  
               
        else:
            print("Entrada inválida\n")



# Programa Principal - não modificar!
dados = obter_dados()
dados=menu(dados)
