inp = input().rstrip()

if len(inp) <= 9:
    n = len(inp)
else:
    n = int((len(inp)-9)/2 + 9)


num_list = []
output = []
def dfs(idx):
    global final_list
    if idx == len(inp):
        if len(num_list) == n:
            final_list = ' '.join(map(str, num_list))
            return 0
        return 1

    if int(inp[idx]) not in num_list:
        num_list.append(int(inp[idx]))
        if dfs(idx+1):
            num_list.pop()

    if idx + 1 < len(inp):
        if int(inp[idx:idx+2]) <= n and int(inp[idx:idx+2]) not in num_list:
            num_list.append(int(inp[idx:idx+2]))
            if dfs(idx+2):
                num_list.pop()

    return 1

dfs(0)

print(final_list)
