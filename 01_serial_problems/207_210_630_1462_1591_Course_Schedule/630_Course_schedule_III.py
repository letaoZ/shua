

## for each last day E1 compute its corresponding list of starting days [S1]
## [S1] will be linked to courses that ends before those starting dates


def searching(courses, visited, path, i):
    if visited[i] > 0:
        return visited[i]

    
    bound = courses[i][1] - courses[i][0]
    res = 1
    for j in range(i+1, len(courses)):
        if courses[j][1]>bound:
            continue
        res = max(res, 1+searching(courses, visited, path, j))

    visited[i] = res
    return res

courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
courses.sort(key=lambda v : -v[1])
visited = [0]*len(courses)
print(courses)

res = 0
for i in range(len(courses)):
    if visited[i] ==1: continue
    res = max(res, searching(courses, visited, path, i))
    print(res)
res