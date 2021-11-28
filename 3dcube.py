import tkinter as tk
from tkinter.constants import CENTER
wn = tk.Tk()
canvas = tk.Canvas(wn, width=1366, height=768)
canvas.place(x=500, y=300)
canvas.pack()
wn.geometry("1366x768")






qnode0 = [-100, -100, -100]
qnode1 = [-100, -100,  100]
qnode2 = [-100,  100, -100]
qnode3 = [-100,  100,  100]
qnode4 = [ 100, -100, -100]
qnode5 = [ 100, -100,  100]
qnode6 = [ 100,  100, -100]
qnode7 = [ 100,  100,  100]
qnodes = [qnode0, qnode1, qnode2, qnode3, qnode4, qnode5, qnode6, qnode7]

def reset():
      qnodes[0] = [-100, -100, -100]
      qnodes[1] = [-100, -100,  100]
      qnodes[2] = [-100,  100, -100]
      qnodes[3] = [-100,  100,  100]
      qnodes[4] = [ 100, -100, -100]
      qnodes[5] = [ 100, -100,  100]
      qnodes[6]= [ 100,  100, -100]
      qnodes[7] = [ 100,  100,  100]



node0 = [-100, -100, -100]
node1 = [-100, -100,  100]
node2 = [-100,  100, -100]
node3 = [-100,  100,  100]
node4 = [ 100, -100, -100]
node5 = [ 100, -100,  100]
node6 = [ 100,  100, -100]
node7 = [ 100,  100,  100]
nodes = [node0, node1, node2, node3, node4, node5, node6, node7]

sides=[]
left=[nodes[0], nodes[1], nodes[3], nodes[2]]
right=[nodes[3], nodes[1], nodes[5], nodes[7]]
front=[nodes[2], nodes[6], nodes[4], nodes[0]]
back = [nodes[3], nodes[1], nodes[5], nodes[7]]
sides=[left, right, front, back]
print(sides, "\n\n")
edge0  = [0, 1]
edge1  = [1, 3]
edge2  = [3, 2]
edge3  = [2, 0]
edge4  = [4, 5]
edge5  = [5, 7]
edge6  = [7, 6]
edge7  = [6, 4]
edge8  = [0, 4]
edge9  = [1, 5]
edge10 = [2, 6]
edge11 = [3, 7]
edges = [edge0, edge1, edge2, edge3, edge4, edge5, edge6, edge7, edge8, edge10, edge9, edge11]





      

def rotateZ(nodes, deg):
      import math
      coss=math.cos(math.radians(deg))
      sinn=math.sin(math.radians(deg))
      for i in nodes:
            x=i[0]
            y=i[1]
            i[0] = x * coss - y * sinn
            i[1] = y*coss + x * sinn

def rotateX(nodes, deg):
      import math
      coss=math.cos(math.radians(deg))
      sinn=math.sin(math.radians(deg))
      for i in nodes:
            x=i[1]
            y=i[2]
            i[1] = x * coss - y * sinn
            i[2] = y*coss + x * sinn



def rotateY(nodes, deg):
      import math
      coss=math.cos(math.radians(deg))
      sinn=math.sin(math.radians(deg))
      for i in nodes:
            x=i[0]
            y=i[2]
            i[0] = x * coss - y * sinn
            i[2] = y*coss + x * sinn


def draw(nodes, edges, canva):
      for e in range(len(edges)):
            n0 = edges[e][0]
            n1 = edges[e][1]
            node0 = nodes[n0]
            node1 = nodes[n1]
            canva.create_line(node0[0]+1366/2, node0[1]+768/2, node1[0]+1366/2, node1[1]+768/2)
""""
            nodeA.penup()
            nodeA.goto(node0[0], node0[1])
            nodeA.pendown()
            nodeA.goto(node1[0], node1[1])
            nodeA.penup()
"""







import time


draw(nodes, edges, canvas)
po=0
x=7#1366/2
y=7#768/2
z=7

# when creating polygons 0, 1, 3, 2
while po < 30000:
      y=wn.winfo_pointerx() - 1366/2
      x=wn.winfo_pointery() - 768/2
      x, y = (x/2, y/2)
      
      rotateZ(nodes, z)
      rotateX(nodes, x)
      rotateY(nodes, y)
      draw(nodes, edges, canvas)
      lop=[]
      lop.append(canvas.create_polygon([nodes[0][0]+1366/2,nodes[0][1]+768/2, nodes[1][0]+1366/2,nodes[1][1]+768/2, nodes[3][0]+1366/2,nodes[3][1]+768/2, nodes[2][0]+1366/2,nodes[2][1]+768/2], fill="#a00"))
      lop.append(canvas.create_polygon([nodes[4][0]+1366/2,nodes[4][1]+768/2, nodes[5][0]+1366/2,nodes[5][1]+768/2, nodes[7][0]+1366/2,nodes[7][1]+768/2, nodes[6][0]+1366/2,nodes[6][1]+768/2], fill="#00a"))
      lop.append(canvas.create_polygon([nodes[2][0]+1366/2,nodes[2][1]+768/2, nodes[6][0]+1366/2,nodes[6][1]+768/2, nodes[4][0]+1366/2,nodes[4][1]+768/2, nodes[0][0]+1366/2,nodes[0][1]+768/2], fill="#aa0"))
      lop.append(canvas.create_polygon([nodes[3][0]+1366/2,nodes[3][1]+768/2, nodes[1][0]+1366/2,nodes[1][1]+768/2, nodes[5][0]+1366/2,nodes[5][1]+768/2, nodes[7][0]+1366/2,nodes[7][1]+768/2], fill="#0a0"))
      
      






    #  p = 
    #  l.append(p)
      canvas.update()
      canvas.delete("all")
#      nodeA.clear()
      nodes = qnodes
      reset()
      time.sleep(0.005)
      po+=1
