dict = {}
n = int(input())
for i in range(n):
    name = input().split()
    dict[name[0]] = dict.get(name[0], 0) + int(name[1])
list_keys = list(dict.keys())
list_keys.sort()
for i in list_keys:
    print(i  + ' ' + str(dict[i]))
