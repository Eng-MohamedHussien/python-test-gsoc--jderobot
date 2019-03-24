import tkinter as tk
import json
import sys
import time

def drawGrid(grid,l):
    gridElementSize1 = 300/len(l[0])
    gridElementSize2 = 300/len(l)
    for i in range(len(l)):
        x1 = 0
        y1 = gridElementSize2 * i
        x2 = gridElementSize1
        y2 = gridElementSize2 * (i+1)
        for j in range(len(l[i])):
            if l[i][j] == 1:
                grid.create_rectangle(x1, y1, x2, y2, fill="black")
            else:
                grid.create_rectangle(x1, y1, x2, y2)
            x1 = x1 + gridElementSize1 
            x2 = x2 + gridElementSize1 
    
window = tk.Tk()
grid = tk.Canvas(window, height=300, width=300, bg='light gray')
grid.pack()
choices = json.loads(open('configuration.json', 'r').read())
choice = sys.argv[1]
current_state = choices[choice]
if(len(current_state)==1):
    drawGrid(grid,current_state)
    grid.pack()
elif(len(current_state)>1):
    for j in range(30):
        for i in range(len(current_state)):
            drawGrid(grid,current_state[i])
            grid.pack()
            grid.update()
            time.sleep(0.4)
            grid.delete("all")
     
     
        
        
window.mainloop()
