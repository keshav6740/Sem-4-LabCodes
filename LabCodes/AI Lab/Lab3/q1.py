class Graph:
    def __init__(self, vertices):
        self.graph = {}  # dictionary containing adjacency List
        self.V = vertices 
        
        for i in range(vertices):
            self.graph[i] = []
 
    def addEdge(self, u, v):
        self.graph[u].append(v)
 
    def topologicalSortUtil(self, v, visited, stack):
 
        visited[v] = True
 
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        stack.append(v)
 
    def topologicalSort(self):
        visited = [False]*self.V
        stack = []
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
 
        print(stack[::-1])

if __name__ == '__main__':
    g = Graph(6)
    g.addEdge(5, 2)
    g.addEdge(5, 0)
    g.addEdge(4, 0)
    g.addEdge(4, 1)
    g.addEdge(3, 1)
    g.addEdge(2, 3)
 
    print("Following is a Topological Sort of the given graph")
    g.topologicalSort()