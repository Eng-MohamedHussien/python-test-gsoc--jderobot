import json
import numpy as np
block = [[0,0,0,0],[0,1,1,0],[0,1,1,0],[0,0,0,0]]
bee_hive = [[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,1,0,0],[0,0,0,0,0,0]]
loaf = [[0,0,0,0,0,0],[0,0,1,1,0,0],[0,1,0,0,1,0],[0,0,1,0,1,0],[0,0,0,1,0,0],[0,0,0,0,0,0]]
boat = [[0,0,0,0,0],[0,1,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
tub = [[0,0,0,0,0],[0,0,1,0,0],[0,1,0,1,0],[0,0,1,0,0],[0,0,0,0,0]]
blinker = [[0,0,0,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,1,0,0],[0,0,0,0,0]]
toad = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,1,1,1,0],[0,1,1,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
beacon = [[0,0,0,0,0,0],[0,1,1,0,0,0],[0,1,1,0,0,0],[0,0,0,1,1,0],[0,0,0,1,1,0],[0,0,0,0,0,0]]
pulsar = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],[0,0,1,0,0,0,0,1,0,1,0,0,0,0,1,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
def get_neighbours(l,i,j):
    neighbours = []
    if(i-1 >= 0 and j-1 >= 0):
        neighbours.append(l[i-1][j-1])
    if(i-1 >= 0):
        neighbours.append(l[i-1][j])
    if(i-1 >= 0 and j+1 < len(l[0])):
        neighbours.append(l[i-1][j+1])
    if(j-1 >= 0):
        neighbours.append(l[i][j-1])
    if(j+1 < len(l[0])):
        neighbours.append(l[i][j+1])
    if(i+1 < len(l) and j-1 >= 0):
        neighbours.append(l[i+1][j-1])
    if(i+1 < len(l)):
        neighbours.append(l[i+1][j])
    if(i+1 < len(l) and j+1 < len(l[0])):
        neighbours.append(l[i+1][j+1])
    return neighbours

def oscillator(current_state):
    last_state = np.copy(current_state)
    current_state = np.zeros_like(current_state)
    for i in range(len(last_state)):
            for j in range(len(last_state[i])):
                neighbours = get_neighbours(last_state,i,j)
                if last_state[i][j] == 1:
                    if(neighbours.count(1)<2):
                        current_state[i][j] = 0
                    if(neighbours.count(1) == 2 or neighbours.count(1) == 3):
                        current_state[i][j] = 1
                    if(neighbours.count(1)>3):
                        current_state[i][j] = 0
                if last_state[i][j] == 0:
                    if(neighbours.count(1)==3):
                        current_state[i][j] = 1

    return current_state.tolist()


print(oscillator(blinker))
print(blinker)

dict_choices = {"Block":block,"Bee-hive":bee_hive,"Loaf":loaf,"Boat":boat,"Tub":tub,"Blinker":[blinker,oscillator(blinker)],"Toad":[toad,oscillator(toad)],"Beacon":[beacon,oscillator(beacon)],"Pulsar":[pulsar,oscillator(pulsar),oscillator(oscillator(pulsar))]}
with open('configuration.json', 'w') as f:  # writing JSON object
    json.dump(dict_choices, f)






