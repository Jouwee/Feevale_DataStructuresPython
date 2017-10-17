from graph import Graph

my_graph = Graph()
my_graph.add_node("A", 1, 1)
my_graph.add_node("B", 2, 2)
my_graph.add_node("C", 1, 3)
my_graph.add_node("D", 4, 1)
my_graph.add_node("E", 5, 1)
my_graph.add_node("F", 6, 3)
my_graph.add_node("G", 6, 3)

my_graph.connect("A", "B", 7)
my_graph.connect("A", "D", 5)
my_graph.connect("B", "C", 8)
my_graph.connect("B", "D", 9)
my_graph.connect("B", "E", 7)
my_graph.connect("C", "E", 5)
my_graph.connect("D", "E", 15)
my_graph.connect("D", "F", 6)
my_graph.connect("E", "F", 8)
my_graph.connect("E", "G", 9)
my_graph.connect("F", "G", 11)

# A - B
# A - D
# B - E
# C - E
# D - F
# E - G

my_graph.show_on_console()

print("Connections of A: " + str(my_graph.get_connections("A")))
print("Connections of D: " + str(my_graph.get_connections("D")))

my_graph.kruskal_mst().show_on_console()

if my_graph.kruskal_mst().connections != [('A', 'D', 5), ('C', 'E', 5), ('D', 'F', 6), ('A', 'B', 7), ('B', 'E', 7), ('E', 'G', 9)]:
    print("ERROR: kruskal_mst is wrong!!! " + str(my_graph.kruskal_mst().connections))
