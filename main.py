

import variaveis

# começando código
materias = []
hsg: int
c = hsg = ht = hqa = hqi = hsx = hsb = 0

print("Bem vindo ao Gerenciador de horários escolares \n vamos ajudar você a organizar seu horário de estudo!! \n \n "
      "primeiro forneça algumas informações para que possamos ajudar a montar seu horário, (escolha de 1 a 4 por dia)")
##horários da segunda
hsg = int(input("Quantos horários você quer estudar na segunda? "))
while 1 > hsg or hsg > 4:
    hsg = int(input("por favor insira um valor válido: "))

#horários da terça
ht = int(input("Quantos horários você quer estudar na terça? "))
while ht < 1 or ht > 4:
    ht = int(input("por favor insira um valor válido: "))
#Horários da quarta
hqa = int(input("Quantos horários você quer estudar na quarta? "))
while hqa < 1 or hqa > 4:
    hqa = int(input("por favor insira um valor válido: "))
#Horários da quinta
hqi = int(input("Quantos horários você quer estudar na quinta? "))
while hqi < 1 or hqi > 4:
    hqi = int(input("por favor insira um valor válido: "))
#Horários da sexta
hsx = int(input("Quantos horários você quer estudar na sexta? "))
while hsx < 1 or hsx > 4:
    hsx = int(input("por favor insira um valor válido: "))
#Horários do sábado
hsb = int(input("Quantos horários você quer estudar na sábado? "))
while hsb < 1 or hsb > 4:
    hsb = int(input("por favor insira um valor válido: "))
print(
    "Preparamos uma tabela com contéudos que mais caem em vestibulares, caso tenha interesse em ver digite 1 para sim "
    "ou 2 para não")
sn = input()
while sn > "2" or sn < "1":
    ##caso ele queira sugestão faça isso
    sn = input("escolha uma opção válida : ")
if sn == "1":
    print(
        "Para auxiliar a montagem do seu cronograma, precisamos que escolha as matérias da qual tem interesse de ver "
        "conteúdos: ")
    sina = "s"
    while sina == "s":
        print(
            "escolha entre \n 1- História, \n 2- Geografia \n 3- Filosofia \n 4- Biologia \n 5-Quimica \n 6- Fisica \n "
            "7- Portugues \n 8- Matematica")
        temp_m = input()
        if temp_m == "1":
            materias.append(variaveis.hist)
        elif temp_m == "2":
            materias.append(variaveis.geo)
        elif temp_m == "3":
            materias.append(variaveis.filo)
        elif temp_m == "4":
            materias.append(variaveis.bil)
        elif temp_m == "5":
            materias.append(variaveis.quim)
        elif temp_m == "6":
            materias.append(variaveis.fis)
        elif temp_m == "7":
            materias.append(variaveis.port)
        elif temp_m == "8":
            materias.append(variaveis.mat)
        else:
                temp_m = input("insira um valor válido: ")
        print("Deseja inserir outra matéria? (s para sim ou n para não)")
        sina = input()
    print(
        "Separamos os conteúdos por: \n ESSENCIAL \n NECESSÁRIO \n IMPORTANTE \n OS CONTEÚDOS DOS QUAIS VOCÊ QUER "
        "SUGESTÃO É:  ")
    if materias.count("historia") == 1:
        print("\n \n HISTÓRIA \n")
        print("\n ESSENCIAL \n")
        with open("historiaessencial.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print("\n NECESSÁRIO\n")
        with open("historia nesessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print("\n IMPORTANTES \n")
        with open("historia importante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)


    if materias.count("geografia") == 1:
        print(" \n \n GEOGRAFIA \n ")
        print(" \n ESSENCIAL \n")
        with open("geografiaessencial.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("geografianecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("geografiaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)


    if materias.count("filosofia") == 1:

        print(" \n \n FILOSOFIA \n ")
        print(" \n ESSENCIAL \n")
        with open("filosofiaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("filosofiaenecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("filosofiaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)

    if materias.count("biologia") == 1:
        print(" \n \n Biologia \n ")
        print(" \n ESSENCIAL \n")
        with open("biologiaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("biologianecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("biologiaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)

    if materias.count("quimica") == 1:
        print(" \n \n QUIMICA \n ")
        print(" \n ESSENCIAL \n")
        with open("quimicaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("quimicanecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("quimicaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
    if materias.count("fisica") == 1:
        print(" \n \n FISICA \n ")
        print(" \n ESSENCIAL \n")
        with open("fisicaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("fisicanecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("fisicaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)

    if materias.count("portugues") == 1:
        print(" \n \n PORTUGUES \n ")
        print(" \n ESSENCIAL \n")
        with open("fisicaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("fisicanecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("fisicaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
    if materias.count("matematica") == 1:
        print(" \n \n MATEMATICA \n ")
        print(" \n ESSENCIAL \n")
        with open("matematicaessencial.txt", "r", encoding="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n NECESSÁRIO \n ")
        with open("matematicanecessaria.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print(" \n IMPORTANTES \n ")
        with open("matematicaimportante.txt", "r", encoding ="utf-8") as arquivo:
            texto = arquivo.read()
        print(texto)
        print("\n\n\n")

print("Tudo bem, vamos escolher as matérias a ser estudadas, escolha as matérias nas ordem dos  horários e dias q "
      "quer.(serão escolhidas as matérias na mesma quantidade de horários escolhidos no total)!")
materias.clear()
sina = "s"
ma = 0
hsg_temp = hsg
ht_temp = ht
hqa_temp = hqa
hqi_temp =hqi
hsx_temp = hsx
hsb_temp = hsb
hgerais = hsg_temp+ht_temp+hqa_temp+hqi_temp+hsx_temp+hsb_temp
while ma <= hgerais:
    print( "escolha entre \n 1- História, \n 2- Geografia \n 3- Filosofia \n 4- Biologia \n 5-Quimica \n 6- "
               "Fisica \n " "7- Portugues \n 8- Matematica")
    temp_m = input()
    if temp_m == "1":
        materias.append(variaveis.hist)
        ma += 1
    elif temp_m == "2":
        materias.append(variaveis.geo)
        ma += 1
    elif temp_m == "3":
        ma += 1
        materias.append(variaveis.filo)
    elif temp_m == "4":
        materias.append(variaveis.bil)
        ma += 1
    elif temp_m == "5":
        materias.append(variaveis.quim)
        ma += 1
    elif temp_m == "6":
        materias.append(variaveis.fis)
        ma += 1
    elif temp_m == "7":
        materias.append(variaveis.port)
        ma += 1
    elif temp_m == "8":
        materias.append(variaveis.mat)
        ma += 1
    else:
        temp_m = input("insira um valor válido: ")
#Calculo para divisao de horarios
mat_c = len(materias)


hsg, ht, hqa, hqi, hsx, hsb = (0, 0, 0, 0, 0, 0)
#horario de segunda
while hsg_temp >= 1:
    controletemp = mat_c / hsg_temp
    if controletemp != 1:
        hsg += 1
        hsg_temp -= 1
        mat_c -= 1
        #horario de terça
    else: hsg += 1
while ht_temp >= 1:
        controletemp = mat_c / ht_temp
        if controletemp != 1:
            ht += 1
            ht_temp -= 1
            mat_c -= 1
        else:
            ht += 1
        #horario de quarta

while hqa_temp >= 1:
        controletemp = mat_c / hqa_temp
        if controletemp != 1:
            hqa += 1
            hqa_temp -= 1
            mat_c -= 1
        else:
            hqa += 1
        #horario de quinta
while hqi_temp >= 1:
    controletemp = mat_c / hqi_temp
    if controletemp != 1:
        hqi += 1
        hqi_temp -= 1
        mat_c -= 1
    else:
        hqi += 1
        #horario de sexta
while hsx_temp >= 1:
    controletemp = mat_c / hsx_temp
    if controletemp != 1:
        hsx += 1
        hsx_temp -= 1
        mat_c -= 1
    else:
        hsx += 1
        #horario de sábado
while hsb_temp >= 1:
    controletemp = mat_c / hsb_temp
    if controletemp != 1:
        hsb += 1
        hsb_temp -= 1
        mat_c -= 1
    else:
        hsb += 1
#montagem da tabela
i = 0
oop_temp = 0
if hsg > 0:
    print("___________________________________________________")
    print("horários da segunda")
    print("___________________________________________________")
    while i < hsg:
        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        oop_temp += 1
        i += 1
    print("___________________________________________________")
i = 0
if ht > 0:
    print("___________________________________________________")
    print("horários da terça")
    print("___________________________________________________")
    while i < ht:

        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        i += 1
        oop_temp += 1
    print("___________________________________________________")
i = 0
if hqa >= 0:
    print("___________________________________________________")
    print("horários da quarta")
    print("___________________________________________________")
    while i < hqa:
        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        i += 1
        oop_temp += 1
    print("___________________________________________________")
i = 0
if hqi >= 0:
    print("___________________________________________________")
    print("horários da quinta")
    print("___________________________________________________")
    while i < hqi:
        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        i += 1
        oop_temp += 1
    print("___________________________________________________")
i = 0
if hsx >= 0:
    print("___________________________________________________")
    print("horários da sexta")
    print("___________________________________________________")
    while i < hsx:
        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        i += 1
        oop_temp += 1

    print("___________________________________________________")
i = 0
if hsb >= 0:
    print("___________________________________________________")
    print("horários da sábado")
    print("___________________________________________________")
    while i < hsb:
        gg_temp = i+1
        print("horário "+ str(gg_temp)  +"\t\t\t" + materias[oop_temp])
        oop_temp += 1
        i += 1
    print("___________________________________________________")
print("Anote seus horários antes e encerrar o programa!!")
gd_temp = input("tecle ENTER para encerrar o programa")