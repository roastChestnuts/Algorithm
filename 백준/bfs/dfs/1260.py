def bfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)
    
    while need_visit:
        idx = need_visit.pop(0)
        if idx not in visited:
            visited.append(idx)
            if idx in graph:
              asc_node = list(graph[idx])
              asc_node.sort()
              need_visit.extend(asc_node)
    return ' '.join(str(i) for i in visited)

def dfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)
    
    while need_visit:
        idx = need_visit.pop()
        if idx not in visited:
            visited.append(idx)
            if idx in graph:
              asc_node = list(graph[idx])
              asc_node.sort(reverse=True) #스택이니까 거꾸로
              need_visit.extend(asc_node)
    return ' '.join(str(i) for i in visited)


v,e,start = map(int, input().split())
graph = dict()
for i in range(e):
    key, value = map(int, input().split())
    if key not in graph:
      graph[key] = [value]
    elif value not in graph[key]:
      graph[key].append(value)
      
    if value not in graph:
      graph[value] = [key]
    elif key not in graph[value]:
      graph[value].append(key)

print(dfs(graph, start))
print(bfs(graph, start))