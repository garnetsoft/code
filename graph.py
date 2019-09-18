import sys

class Graph:

    g = {}

    def addEdge(self, node, neighbor):
        if node not in self.g:
            self.g[node] = [neighbor]
        else:
            self.g[node].append(neighbor)


    def showEdges(self):
        for node in self.g:
            for neighbor in self.g[node]:
                print("(",node,", ",neighbor,")")

    def showGraph(self):
        for node in self.g:
            l = []
            for neighbor in self.g[node]:
                l.append(neighbor)
            print("{",node,":",l,"}")


    def findPath(self, start, end, path=[]):
        path += [start]

        if start == end:
            return path

        for node in self.g[start]:
            if node not in path:
                newPath = self.findPath(node, end, path)

                if newPath:
                    return newPath

                return None

    def BFS(self, s):
        visted = {}
        queue = []

        for n in self.g:
            visted[n] = False

        queue.append(s)
        visted[s] = True

        while len(queue) != 0:
            n = queue.pop(0)
            
            for node in self.g[n]:
                if visted[node] != True:
                    visted[node] = True
                    queue.append(node)
            print(n,end=" ")

        print('\n')
        

    def DFS(self, s):
        visted = {}
        stack = []

        for n in self.g:
            visted[n] = False

        stack.append(s)
        visted[s] = True

        while len(stack) != 0:
            #n = stack.pop(len(stack)-1)
            n = stack.pop(-1)
            
            for node in self.g[n]:
                if visted[node] != True:
                    visted[node] = True
                    stack.append(node)
            print(n,end=" ")

        print('\n')
        

    def allPaths(self,start,end,path=[]):
        path = path + [start]
        if start == end:
            return [path]
        paths = []
        for node in self.g[start]:
            if node not in path:
              newpaths = self.allPaths(node, end, path)
              for newpath in newpaths:
                paths.append(newpath)
        return paths

    def shortestPath(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return path
        shortest=None
        for node in self.g[start]:
            if node not in path:
                newpath=self.shortestPath(node, end, path)
                if newpath:
                    if not shortest or len(shortest)>len(newpath):
                        shortest=newpath
        return shortest


###################################
g = Graph()

g.addEdge('1', '2')
g.addEdge('1', '3')
g.addEdge('2', '3')
g.addEdge('2', '1')
g.addEdge('3', '1')
g.addEdge('3', '2')
g.addEdge('3', '4')
g.addEdge('4', '3')


g.showEdges()
g.showGraph()

print(g.findPath('4','1',[]))
print(g.allPaths('4','1',[]))
print(g.shortestPath('4','1',[]))

g.BFS('1')
g.DFS('1')
