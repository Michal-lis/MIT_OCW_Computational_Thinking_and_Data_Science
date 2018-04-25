class Node():
    def __init__(self, name):
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge():
    def __init__(self, src, dest):
        """Assumes src and dest are nodes"""
        self.src = src
        self.dest = dest

    def getSource(self):
        return self.src

    def getDestination(self):
        return self.dest

    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()


class Diagram():
    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if Node in self.edges:
            raise ValueError("This node already exists in the diagram")
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        src = edge.getSource()
        dest = edge.getDestination()
        if [item for item in [src, dest] if item not in self.edges]:
            raise ValueError("Node not in the graph")
        else:
            self.edges[src].append(dest)

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' + dest.getName() + '\n'
        return result


n = Node('nike')
m = Node('mike')
k = Node('kike')
e = Edge(n, m)
ef = Edge(n, k)
d = Diagram()
d.addNode(n)
d.addNode(m)
d.addNode(k)
d.addEdge(e)
d.addEdge(ef)
print(d)
