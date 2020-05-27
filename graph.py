####################
## Wyatt Dooley
##4/23/2018
##Graph Application
####################

import networkx as nx
import matplotlib.pyplot as plt
G=nx.Graph()
#node added
G.add_node(1)
G.add_node(2)
G.add_node(3)
G.add_node(4)
G.add_node(5)
G.add_node(6)
G.add_node(7)
G.add_node(8)
G.add_node(9)
G.add_node(10)
G.add_node(11)
G.add_node(12)
G.add_node(13)
G.add_node(14)
G.add_node(15)
G.add_node(16)
G.add_node(17)
G.add_node(18)
G.add_node(19)
G.add_node(20)
G.add_node(25)#check to see if it works
#edge
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(6,7)
G.add_edge(7,8)
G.add_edge(8,9)
G.add_edge(9,10)
print("Did it run")
G.add_edge(10,11)
G.add_edge(11,12)
G.add_edge(12,13)
G.add_edge(13,14)
G.add_edge(14,15)
G.add_edge(15,16)
G.add_edge(16,17)
G.add_edge(17,18)
G.add_edge(18,19)
G.add_edge(19,20)
G.add_edge(20,21)
G.add_edge(8,15)
print("edgework")

#G.remove_node(3)
print("Diditrun2")

print("Shortest Path ->",list(nx.shortest_path(G,source=18,target=6)))
#nx.shortest_path(G,source=1)
#print("Diditrun3")
print(("DFS preorder nodes ->"),list(nx.dfs_preorder_nodes(G,source=1)))

print("Draw-> ")
#G = nx.dodecahedral_graph()
#nx.draw(G)
#nx.draw(G, pos=nx.spring_layout(G))
nx.draw(G)
plt.show()
#nx.draw_random(G)
print("draw to the print screen test")



#G = nx.dodecahedral_graph()
#nodes = nx.draw_networkx_nodes(G, pos=nx.spring_layout(G))
#print ("edges added")
#print("-> 1 <-")

#print("this should not be printing if it doe not work")


#print("not NONE")





