# https://www.hackerrank.com/challenges/torque-and-development/problem

def roadsAndLibraries(n, c_lib, c_road, cities):

    def toAdjList(cities):
        map = {i:[] for i in range(1,n+1)}
        for road in cities:
            map[road[0]].append(road[1])
            map[road[1]].append(road[0])
            
        return map

    def getShortestPath(city, map, visited):
    
        stack = [city]
        path = []
        
        while stack:
            
            current = stack.pop()
            visited[current] = True
            path.append(current)
            
            for neighbour_city in map[current]:
                if neighbour_city not in visited:
                    stack.append(neighbour_city)
                    visited[neighbour_city] = True

                
        return path
        
    map = toAdjList(cities)

    visited = {}
    path_list = []
    total_cost = 0
    
    for city in map.keys():
        if city not in visited:
            path = getShortestPath(city, map, visited)
            path_list.append(path)
        
    for path in path_list:
        n = len(path)
        total_cost += min(n*c_lib, ((n-1)*c_road) + c_lib)


    return total_cost

g = {"n_cities":3, "roads":[[1, 2], [3, 1], [2, 3]]}
g2 = {"n_cities":5, "roads":[[1, 2], [1, 3], [1, 4]]}

n = 5
cl = 6
cr = 1

print(roadsAndLibraries(g2["n_cities"], cl, cr, g2["roads"]))