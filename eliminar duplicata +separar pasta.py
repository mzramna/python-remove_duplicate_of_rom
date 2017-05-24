import os
import csv
import re
import shutil
import eliminar as el
anylingua=r'(?<=\(|\[).+?(?=\)|\])'
usa="USA|\(u\)|\(U\)|UE|\(JU\)|Unl|Beta|\(World\)|\(world\)"
usa2="USA|u|U|UE|JU|Unl|Beta|World|world"
japan="\(J\)|\(j\)|Japan"
japan2="J|j|Japan"
europe="\(E\)|\(e\)|Europe"
europe2="E|e|Europe"
hack="Hack|hack"
bios="bios|Bios|BIOS"
def realocar (nome,lingua):
    csvfile=open('listaDRelocacao.csv', 'a')
    #teste de variavel
    testfile=open('listaDTeste.csv', 'a')
    trocas_realizadas = csv.writer(csvfile, delimiter='|')
    (local,nome2) = os.path.split(os.path.abspath(nome))
    print(encontrar_caminho(nome,lingua))
    newpath = local+"\\"+encontrar_caminho(nome,lingua)+"\\"
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    if os.path.isfile(newpath+nome2)==False:
        shutil.move(os.path.abspath(nome),newpath+nome2)
        trocas_realizadas.writerow([os.path.abspath(nome)]+[newpath+nome2])
        csvfile.close()
        testfile.close()
        return True
    else:
        os.remove(local+nome2)
        trocas_realizadas.writerow([os.path.abspath(nome)]+["excluido"])
        csvfile.close()
        testfile.close()
        return True
    csvfile.close()
    testfile.close()
    return False
def lingua2(lingua):
    if lingua is usa:
        return usa2
    elif lingua is europe:
        return europe2
    elif lingua is japan:
        return japan2
    elif lingua is hack:
        return "Hack"
    else:
        return qualquer_letra(nome)
    
def qualquer_letra(nome):
    local2=re.findall(anylingua,nome)
    anysplit=r'\,'
    coorsplit=str(local2)
    if re.search(anysplit,coorsplit):
        local2=re.split(anysplit,coorsplit)
        anysplit=r'[A-Z]'
        coorsplit=str(local2)
        local2=re.findall(anysplit,coorsplit)
        return local2[0]

def trocanome(nome,lingua):
    csvfile=open('listaDTrocas.csv', 'a')
    trocas_realizadas = csv.writer(csvfile, delimiter='|')#imprime o nome completo
    newnome=str(nome)
    nome2=nome
    #renomear os paises
    textos_encontrados=re.findall(anylingua,nome2);
    for k in range (0,len(textos_encontrados)):
        if re.search(lingua2(lingua)+"|"+lingua,textos_encontrados[k]):
            print(encontrar_caminho(nome,lingua))
            print (nome2)
            nome2 = nome2.replace(textos_encontrados[k],encontrar_caminho(nome,lingua))
            print(nome2)
            #input("lingua")
        else:
            print(textos_encontrados[k])
            print nome2
            nome2=nome2.replace(textos_encontrados[k],"")
            print nome2
        nome2=nome2.replace("(\(\))","")
        print nome2
        print "----------------"
            #input("nao lingua")
    os.rename(nome,nome2)
    (local,nome2) = os.path.split(os.path.abspath(nome))
    #final renomear paises
    #instancia vetor do nome final
    nomefinal=[""]*(len(newnome)-7)
    #condicional verificar se é necessario trocar
    if newnome[5] is '-' :
        for k in range (7,len(newnome)):
            nomefinal[k-7]+=newnome[k]
            nome2=nomefinal
        #transforma vetor em string
        novo_nome="".join(str(x)for x in nomefinal)
        trocas_realizadas.writerow([nome,nome2])
        os.rename(nome,nome2)
        csvfile.close()
    print("processo terminado de renomear")
    return nome2

def comparadores(nome):
    if re.search(bios,nome):
        print ("bios")
    elif re.search(usa,nome):
        troca=realocar(nome,usa)
        while (not troca):
            troca=realocar(nome,usa)
    elif re.search(europe,nome):
        troca=realocar(nome,europe)
        while (not troca):
            troca=realocar(nome,europe)
    elif re.search(japan ,nome):
        troca=realocar(nome,japan)
        while (not troca):
            troca=realocar(nome,japan)
    elif re.search(hack ,nome):
        troca=realocar(nome,hack)
        while (not troca):
            troca=realocar(nome,hack)
    elif re.search(qualquer_letra(nome),nome):
        troca=realocar(nome,qualquer_letra(nome))
        while (not troca):
            troca=realocar(nome,qualquer_letra(nome))
    print os.path.abspath(nome)
    return troca

def comparadores_lingua(nome):
    if re.search(bios,nome):
        print ("bios")
    elif re.search(usa,nome):
        trocanome(nome,usa)
    elif re.search(europe,nome):
        trocanome(nome,europe)
    elif re.search(japan ,nome):
        trocanome(nome,japan)
    elif re.search(hack ,nome):
        trocanome(nome,hack)
    elif re.search(qualquer_letra(nome),nome):
        trocanome(nome,qualquer_letra(nome))
    print os.path.abspath(nome)

def comparadores_confirma_lingua(nome):
    if re.search(bios,nome):
        print ("bios")
    elif re.search(usa,nome):
        confirmar_troca_nome(nome,usa)
    elif re.search(europe,nome):
        confirmar_troca_nome(nome,europe)
    elif re.search(japan ,nome):
        confirmar_troca_nome(nome,japan)
    elif re.search(hack ,nome):
        confirmar_troca_nome(nome,hack)
    elif re.search(qualquer_letra(nome),nome):
        confirmar_troca_nome(nome,qualquer_letra(nome))
    print os.path.abspath(nome)

def encontrar_caminho(nome,lingua):
    (local,nome2) = os.path.split(os.path.abspath(nome))
    if lingua is usa:
        return "U"
    elif lingua is europe:
        return "E"
    elif lingua is japan:
        return "J"
    elif lingua is hack:
        return "Hack"
    else:
        return qualquer_letra(nome)    

def confirma_local(nome,lingua):
    loop=0
    newpath=encontrar_caminho(nome,lingua)
    while loop is 0:
        print ("deseja realocar o arquivo para:")
        print newpath
        print ("0/1")
        opcao = input()
        if opcao is 0:
            comfirmacao = 1
            loop = 1
        elif opcao is 1:
            comfirmacao = 0
            loop = 1
        else:
            loop = 0
        if comfirmacao is 1 :
            if realocar(nome,lingua):
                eliminar_duplicata(nome)
                return True
            else:
                while (not troca):
                    realocar(nome,lingua)
                return True
        return False

def confirmar_troca_nome(nome,lingua):
    newnome=str(nome)
    if newnome[5] is '-' :
        loop=0
        while loop is 0:
            print ("deseja trocar o nome do arquivo:")
            print nome
            print ("0/1")
            opcao = input()
        if opcao is 0:
            comfirmacao = 1
            loop = 1
        elif opcao is 1:
            comfirmacao = 0
            loop = 1
        else:
            loop = 0
    if comfirmacao is 1 :
        return trocanome(nome,lingua)
            

def confirmacao_realocar(nome):
    loop=0
    while loop is 0:
        print ("deseja realocar o arquivo:")
        print nome
        print ("0/1")
        opcao = input()
        if opcao is 0:
            return True
        elif opcao is 1:
            return False
        else:
            loop = 0        
        return False
        
def comparacao_confirma_local(nome):
    if re.search(nome,bios):
        print ("bios")
    elif re.search(nome,usa):
        nome=confirmar_troca_nome(nome,usa)
        confirmar_local(nome,usa)
        return True
    elif re.search(nome,europe):
        nome=confirmar_troca_nome(nome,europe)
        confirmar_local(nome,europe)
        return True
    elif re.search(nome ,japan):
        nome=confirmar_troca_nome(nome,japan)
        confirmar_local(nome,japan)
        return True
    elif re.search(nome ,hack):
        nome=confirmar_troca_nome(nome,hack)
        confirmar_local(nome,hack)
        return True
    elif re.search(nome,anylingua):
        nome=confirmar_troca_nome(nome,qualquer_letra(nome))
        confirmar_local(nome,qualquer_letra(nome))
        return True
    else:
        return False

def move_up(lista,posicao):
    for k in range(posicao,len(lista)):
        lista[posicao]=lista[posicao+1]
    for k in range(len(lista),0):
        if lista[k] is lista[k-1]:
            lista[k]=[]
    return lista

def num_de_posicoes_preenchidas(lista):
    for k in range(len(lista),0):
        if lista[k] is []:
            return k
    return len(lista)
    
if os.path.isfile('listaDRelocacao.csv') == False :
    csvfile=open('listaDRelocacao.csv', 'w')
    trocas_realizadas = csv.writer(csvfile, delimiter='|')
    trocas_realizadas.writerow(["local original"]+["local final"])
    csvfile.close()
if os.path.isfile('listaDTeste.csv') == False :
    csvfile=open('listaDTeste.csv', 'w')
    trocas_realizadas = csv.writer(csvfile, delimiter='|')
    trocas_realizadas.writerow(["variavel"]+["valor"])
    csvfile.close()
menu=-1
while(menu!=0):
    print("1-realocar todos jogos e remover copias")
    print("2-realocar um jogo por vez e remover copias")
    print("3-realocar um jogo por vez confirmando destino e remover copias")
    print("4-desfazer a realocacao")
    print("5-desfazer realocacao individual")
    menu=int(input())
    if menu is 1:
        for nome in os.listdir('.'):
            troca=False
            (shortname, extension) = os.path.splitext(nome)
            if extension!=".jpg" and extension!=".doc"and extension!=".csv" and extension!=".html"and extension!=".py"and extension!=".png"and extension!=".txt"and extension!="":
                
                #print("e uma rom")
                (local,nome2) = os.path.split(os.path.abspath(nome))
                troca=comparadores_lingua(nome)                    
        for nome in os.listdir('.'):
            troca=False
            (shortname, extension) = os.path.splitext(nome)
            if extension!=".jpg" and extension!=".doc"and extension!=".csv" and extension!=".html"and extension!=".py"and extension!=".png"and extension!=".txt"and extension!="":
                (local,nome2) = os.path.split(os.path.abspath(nome))
                el.eliminar_duplicata(nome)
                troca=comparadores(nome)
            if troca:
                print "trocou"
    if menu is 2:
        for nome in os.listdir('.'):
            if confirmacao_realocar(nome):
                    (local,nome2) = os.path.split(os.path.abspath(nome))                
                    comparadores_confirma_lingua(nome)
        for nome in os.listdir('.'):
            if confirmacao_realocar(nome):
                    (local,nome2) = os.path.split(os.path.abspath(nome))
                    el.eliminar_duplicata(nome)
                    troca=realocar(nome,lingua)
            if troca:
                print "trocou"
    if menu is 3:
        for nome in os.listdir('.'):
            trocas_realizadas = csv.writer(csvfile, delimiter='|') 
            (shortname, extension) = os.path.splitext(nome)
            if extension!=".jpg" or extension!=".doc"or extension!=".csv"or extension!=".html"or extension!=".py"or extension!=".png":
                if confirmacao_realocar(nome):
                    #print("e uma rom")
                    (local,nome2) = os.path.split(os.path.abspath(nome))
                    #print "original: "+os.path.abspath(nome)
                    el.eliminar_duplicata(nome)
                    troca=comparacao_confirma_local(nome)
                if troca:
                    print "trocou"
        if menu is 4:
            trocas_realizadas=csv.reader(csvfile,delimiter='|')
            header = trocas_realizadas.next()
            data=[]
            for row in trocas_realizadas:
                data.append(row)
            data=np.array(data)
            for k in range(0,len(data)):
                nome=data[k][1]
                csvfile.close()
                csvfile=open('listaDRelocacao.csv', 'a')
                trocas_realizadas = csv.writer(csvfile, delimiter='|')
                novo_nome=data[k][0]
                #transforma vetor em string
                trocas_realizadas.writerow([nome]+[novo_nome])
                shutil.move(nome,novo_nome)
            print("ok")
        if menu is 5:
            csvfile=open('listaDRelocacao.csv', 'r')
            trocas_realizadas=csv.reader(csvfile,delimiter='|')
            header = trocas_realizadas.next()
            data=[]
            for row in trocas_realizadas:
                data.append(row)
            data=np.array(data)
            for k in range(0,len(data)):
                nome=data[k][1]
                loop=0
                while loop is 0:
                    print ("deseja trocar o nome do arquivo:")
                    print nome
                    print ("0/1")
                    opcao = input()
                    if opcao is 0:
                        comfirmacao = 1
                        loop = 1
                    elif opcao is 1:
                        comfirmacao = 0
                        loop = 1
                    else:
                        loop = 0
                if comfirmacao is 1 :
                    csvfile.close()
                    csvfile=open('listaDRelocacao.csv', 'a')
                    trocas_realizadas = csv.writer(csvfile, delimiter='|')
                    novo_nome=data[k][0]
                    #transforma vetor em string
                    print("o nome ao final do processo sera: "+novo_nome)
                    trocas_realizadas.writerow([nome]+[novo_nome])
                    shutil.move(nome,novo_nome)
                    csvfile.close()
