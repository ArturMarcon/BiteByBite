nomes = [] 
cantores = [] 
n_tocadas = []
letras = {} 

opcao = -1

print("---Cadastro de músicas---\n") 

## load musicas ja cadastradas

with open("musicas.txt", "r") as biblioteca:
    for linha in biblioteca:
        linhasplit = linha.split("/")
        nomes.append(linhasplit[0])
        cantores.append(linhasplit[1])
        letras[linhasplit[0]] = linhasplit[2]

##

while opcao != 0:

    ## Menu principal

    print("---Menu principal---\n") 
    print("1 - Tocar música.")  
    print("2 - Qual é a música?")
    print("3 - Cadastrar nova música.")
    print("0 - Sair.\n")

    opcao = int(input("Digite a opcao desejada: >"))
    print("")

    if opcao == 1:  
         ## tocar música

        musica = input("Digite o nome da música: ")
        try:
            indice= nomes.index(musica)
            print("\nMúsica tocada. Nome: {}. Cantor: {}. Letra: {}".format(nomes[indice], cantores[indice], letras[musica]))
        except ValueError or KeyError:
            print("\nMúsica não encontrada")
         ##


    elif opcao == 2:

        ## achar música por palavras chave
        
        palavra = input("Digite uma palavra contida na música: ")

        encontrada = 0
        for i in letras:
            string = letras[i].split()
            if string.count(palavra) > 0:
                print("Músicas com a palavra especificada:", i)
                encontrada += 1
        if encontrada == 0:
            print("Nenhuma música encontrada")

        ##

    elif opcao == 3:

        ## cadastro

        opçao_cadastro = 1

        while opçao_cadastro == 1:
            musica=input("Digite o nome da música: ")
            nomes.append(musica.lower())

            cantor=input("Digite o cantor da música: ")
            cantores.append(cantor.lower())

            letra=input("Digite a letra da música: ")
            letras[musica] = letra.lower()

            with open("musicas.txt", "a") as biblioteca:
                biblioteca.write("{}/{}/{}\n".format(musica, cantor, letra))

            opçao_cadastro = int(input("Deseja cadastrar outra música? (1 - sim. 2 - não): "))
            n_tocadas.append(0)

        ##
                
    elif opcao == 0:
        print("Encerrando a execução...")

    else:
        print("Opção incorreta. Opções disponíveis:")
        print("1 - Tocar música.")
        print("2 - Qual é a música?")
        print("3 - Cadastrar nova música.")
        print("0 - Sair.")
