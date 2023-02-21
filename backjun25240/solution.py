import sys
from itertools import product

# owner 권한을 가진 유저들은 Group이 할 수 있는 모든 연산가능
# group 권한을 가진 유저는 other 권한을 가진 유저들이 할 수 잇는 연산 가능
# 수정 권한이 있으면 읽기 권한 존재.

# 세자리 숫자가 오면
num_aut_dic = {
    '0': [],
    '1': ['X'],
    '2': ['W', 'R'],
    '3': ['X', 'W', 'R'],
    '4': ['R'],
    '5': ['R', 'X'],
    '6': ['R', 'W'],
    '7': ['R', 'X', 'W']
}

for i in list(product(num_aut_dic, repeat=2)):
    num_aut_dic[i[0]+i[1]] = list(set(num_aut_dic[i[0]] + num_aut_dic[i[1]]))
    for j in range(8):
        num_aut_dic[i[0]+i[1]+str(j)] = list(set(num_aut_dic[i[0]+i[1]] + num_aut_dic[str(j)]))

u2g_dict = {}
file_dict = {}

class File:
    def __init__(self, acc, owner, group):
        self.owner = owner
        self.group = group
        self.acc = acc

    def search(self, name):
        if name == self.owner:
            return 0
        elif self.group in u2g_dict[name]:
            return 1
        else:
            return 2

    def ask(self, name, act):
        out = self.search(name)
        if out == 0:
            t_acc = self.acc
        elif out == 1:
            t_acc = self.acc[1:]
        else:
            t_acc = self.acc[2]
        if act in num_aut_dic[t_acc]:
            return 1
        else:
            return 0


u, f = map(int, input().split())
for _ in range(u):
    t = sys.stdin.readline().rstrip().split()
    if len(t) == 1:
        u2g_dict[t[0]] = t
    else:
        u2g_dict[t[0]] = t[1].split(',')
        u2g_dict[t[0]].append(t[0])

for _ in range(f):
    file_name, acc, owner, group = sys.stdin.readline().rstrip().split()
    file_dict[file_name] = File(acc, owner, group)
q = int(input())
for _ in range(q):
    p_name, file_name, action = sys.stdin.readline().rstrip().split()
    t_file = file_dict[file_name]
    print(t_file.ask(p_name, action))







