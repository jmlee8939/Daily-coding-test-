import sys

aut_num_dic = {'R': ['4', '5', '6', '7'],
               'W': ['2', '3', '6', '7'],
               'X': ['1', '3', '5', '7']}
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
        t_acc = self.acc[self.search(name)]
        if t_acc in aut_num_dic[act]:
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

for _ in range(f):
    file_name, acc, owner, group = sys.stdin.readline().rstrip().split()
    file_dict[file_name] = File(acc, owner, group)
q = int(input())
for _ in range(q):
    p_name, file_name, action = sys.stdin.readline().rstrip().split()
    t_file = file_dict[file_name]
    print(t_file.ask(p_name, action))







