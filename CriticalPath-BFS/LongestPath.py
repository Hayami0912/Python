#finding the longest path
completed_path = []
path_dist = []
source = MS1
path = {}
i = 1

for v in G2.vertices():
    path [v] = [[source.element()], 0, '']
Queue = []
edges = G2.edges()
Queue.append(source)

while (Queue):
    print('\nQueue #',i,': ')
    i+=1
    for q in Queue:
        print(q)
    print('Available path: ')
    for p in path:
        print(p.element(), path[p][0], path[p][1], path[p][2])
    
    v = Queue[0]
    del Queue[0]
    path[v][2] = 'marked'
    
    for e in G2.findNeighbors(v):
        print(e)
    print('Neighbors: ')
    
    for e in G2.findNeighbors(v):
        print('v = ', v, ' e = ', e)
        if path[e][2] != 'marked':
            path[e][2] = 'marked'
            path[e][0] = path[e][0] + path[v][0][1:] + [e.element()]
            path[e][1] += path[v][1] + G2.dist(v, e)
            Queue.append(e)
        else:
            dist_lenght = path[v][1] + G2.dist(v,e)
            if dist_lenght > path[e][1]:
                path[e][1] = dist_lenght

for p in path:
    if path[p][0][-1] == 'MS17':
        completed_path.append(path[p][0])
        path_dist.append(path[p][1])
print('\ncritical path: ')
for n in range (len(completed_path)):
    print(completed_path[n], path_dist[n])
