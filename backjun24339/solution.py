import sys
root = []
node = {}
p_node = {}
edge = {}

"""
made('1', 1)
made('2', 0)
made('3', 0)
made('4', 0)
made('5', 0)
made('6', 0)
made('7', 0)
made('8', 1)
made('9', 0)

add('1', '1', '2', 1)
add('2', '1', '3', 0)
add('3', '2', '6', 0)
add('4', '2', '4', 1)
add('5', '3', '5', 0)
add('6', '3', '7', 1)
add('7', '8', '9', 1)

p_node
node['1']
root
[edge[j][1] for j in node['1'] if edge[j][2] == 1]
remove('2')
print(search(0, root, []))
"""

def add(id, from_, to_, s):
    edge[id] = (from_, to_, s)
    node[from_].append(id)
    p_node[to_].append(id)

def remove(id):
    from_, to_, _= edge[id]
    del edge[id]
    node[from_].remove(id)
    p_node[to_].remove(id)

def made(id, r):
    if r:
        root.append(id)
    node[id] = []
    p_node[id] = []

def search(mode, now, visited = []):
    if mode == 0:
        for i in now:
            if i not in visited:
                visited.append(i)
                new_list = [edge[j][1] for j in node[i]]
                search(mode, new_list, visited)
    elif mode == 1:
        for i in now:
            if i not in visited:
                visited.append(i)
                new_list = [edge[j][1] for j in node[i] if edge[j][2]==1]
                search(mode, new_list, visited)
    return visited

def delete(remains):
    for n in list(node.keys()):
        if n not in remains:
            id_lis = node[n]
            id_lis2 = p_node[n]
            for id in id_lis:
                del edge[id]
            for id2 in id_lis2:
                if edge[id2][0] in remains:
                    node[edge[id2][0]].remove(id2)
                    del edge[id2]
            del node[n]

o, e = map(int, input().split())
for _ in range(o):
    node_id, r = sys.stdin.readline().rstrip().split()
    if r == 'ROOT':
        root.append(node_id)
    node[node_id] = []
    p_node[node_id] = []
for _ in range(e):
    input_list = sys.stdin.readline().rstrip().split()
    cmd = input_list[0]
    if cmd == 'MADE':
        _, id, r = input_list
        if r == '-':
            made(id, 0)
        else:
            made(id, 1)
    elif cmd == 'ADD':
        _, id, from_, s_, to_ = input_list
        if s_ == '=>':
            add(id, from_, to_, 1)
        else:
            add(id, from_, to_, 0)
    elif cmd == 'REMOVE':
        _, id = input_list
        remove(id)
    elif cmd == 'm':
        remain = search(0, root, [])
        delete(remain)
        print(len(node))
    elif cmd == 'M':
        remain = search(1, root, [])
        delete(remain)
        print(len(node))






