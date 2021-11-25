print("Bem vindo a minha proto agenda")

print("O que vc deseja fazer?")

def Inserir():
    nome = input("Me diga seu nome: ")
    end = input("Me diga seu endereço: ")
    tel = input("Me diga seu telefone: ")
    dados = nome+" /"+tel+"/"+ end
    print("Seus dados são: ", dados)
    arquivo = open("contatos.txt","a")
    arquivo.writelines(dados)

a = input("Digite Inserir/Buscar/Remover/Editar \n")

if (a == "Inserir"):
    Inserir()
elif(a == "Buscar"):
    pass
elif(a == "Remover"):
    pass
elif(a == "Editar"):
    pass
else:
    print("Essa opção não existe")