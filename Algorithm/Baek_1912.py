int(input())
resource = list(map(int, input().split(' ')))
max_res: int = -9999999
temp = 0

# print(resource)

manufacture = [0]
index = 0

# for i in resource:
#     if i > 0:
#         manufacture[index] += i
#     else:
#         index += 1
#         manufacture.append(i)
#         manufacture.append(0)

for i in resource:
    if i > 0:
        if manufacture[index] == 0:
            manufacture[index] += i
        else:
            manufacture.append(i)
    else:
        manufacture.append(i)
        index += 1
        manufacture.append(0)
#

# index = 0
# for i in manufacture:
#     if i == 0:
#         manufacture.pop(index)
#     index += 1

# index = 0
# for i in resource:
#     if i == 0:
#         resource.pop(index)
#     index += 1
# index = 0
#
# print(manufacture)
# print(len(manufacture))
#
# if len(manufacture) == 1:
#     max_res = manufacture[0]
#
#
# for i in range(0, len(manufacture) + 1):
#     for j in range(0, len(manufacture) + 1):
#         for k in range(j, j + i):
#             if k >= len(manufacture):
#                 continue
#             temp += manufacture[k]
#             if max_res < temp:
#                 max_res = temp
#                 temp = 0
#             else:
#                 temp = 0
# print(max_res)


if len(resource) == 1:
    max_res = resource[0]


for i in range(0, len(resource) + 1):
    for j in range(0, len(resource) + 1):
        for k in range(j, j + i):
            if k >= len(resource):
                continue
            temp += resource[k]
        if max_res < temp:
            max_res = temp
            temp = 0
        else:
            temp = 0

if max_res == 0:
    max_res = -9999999
    for i in resource:
        if max_res < i <= 0:
            max_res = i

# print(resource)
if len(resource) == 1:
    max_res = resource[0]
if len(resource) == 0:
    max_res = 0
print(max_res)

#
