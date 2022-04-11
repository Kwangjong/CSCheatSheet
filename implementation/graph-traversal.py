# starting node as char
# reference to the graph adjacency list
def bfs(start, graph):
  frontier = [start]
  discovered = []
  
  curr = ""
  while frontier:
    curr = frontier.pop()

    if curr not in discovered: #visit only undiscovered vertices.
       discovered.append(curr)
       frontier[0:0] = graph[curr][::-1]

  return discovered


def dfs(start, graph):
  stack =[start]
  discovered = []

  curr = ""
  while stack:
    curr = stack.pop()

    if curr not  in discovered:
       discovered.append(curr)
       stack+=graph[curr][::-1]

  return discovered





graph = { 
  'A' : ['B'], 
  'B' : ['C', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['A', 'D'],
  'F' : [],}

print(' '.join(bfs('A', graph))) #A B C E F D
print(' '.join(dfs('A', graph))) #A B C F E D