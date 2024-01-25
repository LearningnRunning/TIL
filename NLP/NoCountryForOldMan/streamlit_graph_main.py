import streamlit
from streamlit_agraph import agraph, Node, Edge, Config, TripleStore

nodes = []
edges = []
# node 를 정의하고
nodes.append( Node(id="Spiderman", 
                   label="시니어", 
                   size=25, 
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png"
                   ) 
            ) # includes **kwargs
nodes.append( Node(id="Captain_Marvel", 
                   label="멘토", 
                   
                   size=15,
                   shape="circularImage",
                   image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_captainmarvel.png") 
            )

nodes.append( Node(id="iron_man", 
                   label="연륜", 
                   
                   size=20,
                   shape="circularImage",
                   image="https://image.api.playstation.com/vulcan/img/rnd/202010/2716/8pc2fi23ksuIvi0gEHO5EqV2.png") 
            )


# edge 를 정의해서
edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

edges.append( Edge(source="iron_man", 
                   label="friend_of", 
                   target="Spiderman", 
                   # **kwargs
                   ) 
            ) 

edges.append( Edge(source="Captain_Marvel", 
                   label="friend_of", 
                   target="iron_man", 
                   # **kwargs
                   ) 
            ) 

# config 와 함께
config = Config(width=750,
                height=950,
                directed=True, 
                physics=True, 
                hierarchical=True,
                # **kwargs
                )

# graph 를 그리면 끝!
return_value = agraph(nodes=nodes, 
                      edges=edges, 
                      config=config)



# nodes = []
# edges = []

# # Create 30 nodes
# for i in range(30):
#     node_id = f"Node_{i}"
#     node_label = f"Label_{i}"

#     nodes.append(Node(id=node_id,
#                       label=node_label,
#                       size=25,
#                       shape="circularImage",
#                       image="http://marvel-force-chart.surge.sh/marvel_force_chart_img/top_spiderman.png"))

# # Create edges between nodes
# for i in range(29):
#     edge = Edge(source=f"Node_{i}",
#                 label="connected_to",
#                 target=f"Node_{i+1}")

#     edges.append(edge)

# # config
# config = Config(width=750,
#                 height=950,
#                 directed=True,
#                 physics=True,
#                 hierarchical=True)

# # Draw the graph
# return_value = agraph(nodes=nodes,
#                       edges=edges,
#                       config=config)