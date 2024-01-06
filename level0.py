import json

json_file_path = "level0.json"

with open(json_file_path,'r') as file:
    data = json.load(file)

def min_value(path,visited,distance):
    minimum = float('inf')
    locality = -1
    for i in range(len(distance)):
        if distance[i]!=0 and i not in visited:
            if minimum > distance[i]:
                locality = i
                minimum = distance[i]

    path.append(minimum)
    visited.append(locality)

neighbour = data["neighbourhoods"]
neighbourhood=[]
for i in neighbour:
    neighbourhood.append(i)
start=data["restaurants"]["r0"]["neighbourhood_distance"]
graph = {'r0':start}
for i in neighbourhood:
    val = data["neighbourhoods"][i]["distances"]
    graph[i] = val
  
n=len(neighbourhood)
path = []
locality = []    
min_value(path, locality, graph['r0'])
    
for i in range(1, 21):
    if i == 1:
        min_value(path, locality, graph['n0'])
    else:    
        last_place = locality[-1]
        min_value(path, locality, graph['n' + str(last_place)])

routes = {}

for i in range(len(path)-1):
    val = 'n' + str(locality[i])
    routes[val] = path[i]

final_path = []
for key in routes.keys():
    final_path.append(key)

final_path = ['r0'] + final_path + ['r0']
output = {"v0": {"path": final_path}}

with open('level0_output.json', "w") as json_file:
    json.dump(output, json_file)
    
print(output)             