
a = ["Bruno Silva", "Paulo Santos", "Ana Silva", "Bruna Silva Porto"]

count = 0
pos = 0
for i in a:
    if (i.find("Silva") != -1):
        #print("Printando o que acha", i.find("Silva"))
        count+=1
        print("Printando o elemento", pos)
        print("Quero printar o nome", i)

    pos +=1

print("Printando o total", count)

if "Silva" in "Bruno Silva":
    print("Foi")
else:
    print("Não foi")

count = 0
pos = 0
for i in a:
    if "Silva" in i:
        count+=1
        print("Printando o elemento", pos)
        print("Quero printar o nome", i)

    pos +=1