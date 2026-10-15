import os  #importando a biblioteca para limpar o terminal
os.system ("cls" if os.name == "nt" else "clear" )

def linha (): 
    print ("-" * 50)

linha () #chamando a função linha ex: -------------

# entrada de dados, nome do produto e quantidade
nome_produto = input("Digite o nome do produto: ")
quantidade = int (input("Digite a quantidade do produto: "))


#Criando a função verificar minimo com condição if e else
def verificar_minimo ():
    if quantidade < 5:
        print (f"Alerta: O produto {nome_produto} precisa de reposição!")

    else:
        print(f"Estoque de {nome_produto} está em nível seguro.")    


# chamando a função verificar minimo 
verificar_minimo ()
linha()