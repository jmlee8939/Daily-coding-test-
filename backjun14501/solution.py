N = int(input())
t_dict = {}
p_dict = {}
for day in range(1, N+1):
    t, p = map(int, input().rstrip().split())
    t_dict[day] = t
    p_dict[day] = p

max_v = 0
def dfs(today, money):
    global max_v
    if today > N+1:
        return

    if max_v < money:
        max_v = money

    if today == N+1:
        return

    dfs(today + t_dict[today], money + p_dict[today])
    dfs(today + 1, money)
    return

dfs(1, 0)
print(max_v)