north = 0
south = 0
east = 0
west = 0

direcao = 0

dNorthSouth = 0
dEastWest = 0

with open('ilha-input.txt', 'r') as input:
    inputee = input.readlines()
    print(inputee)

    for line in inputee:
        if line[0] == 'N':
            north += int(line[1:])
        elif line[0] == 'S':
            south += int(line[1:])
        elif line[0] == 'E':
            east += int(line[1:])
        elif line[0] == 'W':
            west += int(line[1:])


        elif line[0] == 'L':
            direcao -= int(line[1:])
        elif line[0] == 'R':
            direcao += int(line[1:])


        elif line[0] == 'F':
            if direcao%360 == 270:
                north += int(line[1:])
            elif direcao%360 == 90:
                south += int(line[1:])
            elif direcao%360 == 0:
                east += int(line[1:])
            elif direcao%360 == 180:
                west += int(line[1:])
    
    dNorthSouth = abs(north - south)
    dEastWest = abs(east - west)

    print(dEastWest + dNorthSouth)
