field = [
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
]

import random
def print_grid(list):
    for i in list: 
        print(f'{i}\n')
print ('Movement Heat Map')
random.seed(43543)
agent = [6,6]
x = agent[0]
y = agent[1]
for step in range(0, 100):
    if step == 0:
        field[x][y] = field[x][y]+1
    else: 
        a = 0
        while a == 0:
            rand = random.randint(1,20)
            if 1<= rand <= 5:
                if (x<14):
                    x+=1
                    break
            elif 6<= rand <= 10:
                if (x>0):
                    x-=1
                    break
            elif 11<= rand <= 15:
                if (y>0):
                    y-=1
                    break
            elif 16<= rand <= 20:
                if (y<14):
                    y+=1
                    break
        field[x][y] +=1
print_grid(field)
distance = abs(6-x)+ abs(6-y)
print(f' Agents final position: {x}{y}')
print(f' Distance from start: {distance}')