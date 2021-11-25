nome = input("Me diga seu nome: ")
end = input("Me diga seu endereço: ")
tel = input("Me diga seu telefone: ")
print("Seu nome é: "+nome)

#permissao de escrita -> w
#permissao de leitura -> r
# permissao de escrita acumulada -> a

dados = nome+"-"+end+"-"+tel+" \n"
arquivo = open("contatos.txt","a")
arquivo.writelines(dados)

#quero ler da agenda 

arquivo = open("contatos.txt","r")
print(arquivo.readlines())