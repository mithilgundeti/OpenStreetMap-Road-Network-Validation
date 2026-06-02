import osmnx as ox

place = "Hyderabad, Telangana, India"

G = ox.graph_from_place(place, network_type="drive")

nodes, edges = ox.graph_to_gdfs(G)

nodes.to_csv("nodes.csv")
edges.to_csv("roads.csv")

print("Nodes:", nodes.shape)
print("Edges:", edges.shape)