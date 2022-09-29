# variáveis principais 

nomes = [] 
cantores = [] 
n_tocadas = [] 
letras = {} 

opcao = -1

print("---ProgFy: o melhor streaming de música---")
print("---Cadastro de músicas---") 

## inicio do item a)

opçao_cadastro = 1

while opçao_cadastro == 1:
    musica=input("Digite o nome da música: ")
    nomes.append(musica)

    cantor=input("Digite o cantor da música: ")
    cantores.append(cantor)

    letra=input("Digite a letra da música: ")
    letras[musica] = letra

    opçao_cadastro = int(input("Deseja cadastrar outra música? (1 - sim. outro - não): "))
    n_tocadas.append(0)

## fim do item a) 

print("---Menu principal---") 
print("1 - Tocar música.") 
print("2 - Calcular audiência.") 
print("3 - Qual é a música?") 
print("0 - Sair.")

while opcao != 0: 
    opcao = int(input("Digite a opcao desejada: >"))

    if opcao == 1:  
             ## inicio do item b) 

        musica = input("Digite o nome da música: ")
        indice= nomes.index(musica)
        print("Música tocada. Nome: {}. Cantor: {}. Letra: {}".format(nomes[indice], cantores[indice], letras[musica]))
        n_tocadas[indice] += 1

             ## fim do item b) 

    elif opcao == 2:
        
             ## inicio do item c)
        
        for i in range(len(n_tocadas)):
            if n_tocadas[i] > 0:
                audiencia = (n_tocadas[i]/sum(n_tocadas))*100
                print("Nome: {}. Audiência: {}% ".format(nomes[i], round(audiencia, 2)))

             ## fim do item c)

    elif opcao == 3:

            ## inicio do item d)
        
        trecho = input("Digite um trecho: ")
        for i in letras:
            string = letras[i].split()
            if string.count(trecho) > 0:
                print("Músicas com o trecho especificado: ", i)

            ## fim do item d)
                
    elif opcao == 0:
        print("Encerrando a execução...")

    else:
        print("Opção incorreta. Opções disponíveis:")
        print("1 - Tocar música.")
        print("2 - Calcular audiência.")
        print("3 - Qual é a música?")
        print("0 - Sair.")
