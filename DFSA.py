def recursive_dfs(graph, source, temp, path = []):
    d[source] = temp
    temp = temp 
    if source not in path:
        if temp%2 == 0:
            path.append(""+source+"^"+ "a"+ "\wedge(" )
        else:
            path.append(""+source+"^"+ "b"+ "\wedge(" )
        if source not in graph:
            # leaf node, backtrack
            return path
        for neighbour in graph[source]:
            d[neighbour]= temp
            temp = temp +1
            path = recursive_dfs(graph, neighbour, temp) 
            temp = temp +1 
            f = temp
            path.append(")_" + source +")")
        return path
        

graph = {"A":["B","C", "D"],
           "B":["E"],
           "C":["F","G"],
           "D":["H"],
           "E":["I"],
           "F":["J"]}


d = {"A":0, "B":0 , "C": 0, "D":0 , "E": 0, "F":0 , "G":0 , "H":0 , "I":0 , "J":0 }
path = recursive_dfs(graph, "A", 0)

formula = (" ".join(path).replace(") (", ")\\vee(")).replace("\wedge( )", ")")
print(" ".join(path))
print('\n')
print(formula)