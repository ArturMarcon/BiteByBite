player1str = []
player2str = []
player1 = []
player2 = []
with open("baralhos.txt") as entrada:
    baralhos = entrada.readlines()
    for i in range(25):
        player1str.append(baralhos[i+1].rstrip("\n").split(","))
        player2str.append(baralhos[i+28].rstrip("\n").split(","))
    
    for sublist in player1str:
        for item in sublist:
            player1.append(int(item))
    for sublist in player2str:
        for item in sublist:
            player2.append(int(item))
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
            player1.pop(0)
            player2.pop(0)
            print("player 1 wins the round!")
        elif player2[0] > player1[0]:
            player2.append(player2[0])
            player2.append(player1[0])
            player1.pop(0)
            player2.pop(0)
            print("player 2 wins the round!")
    player2.reverse()
    x = 0
    soma = 0
    for i in player2:
        x+=1
        soma += i * x
    print(soma)