input()
resource = []
resource += list(map(int, input().split()))
max_res = -99999
temp = 0

manufacture = [0]
index = 0

if len(resource) == 1:
    max_res = resource[0]

# print(resource)
for i in resource:
    if i > 0:
        manufacture[index] += i
    else:
        if manufacture[index] == 0:
            manufacture[index] += i
        else:
            manufacture.append(i)
            manufacture.append(0)
        index += 2

    # print(manufacture)
#
# print(manufacture)
# print(len(manufacture))

if len(manufacture) == 1:
    max_res = manufacture[0]

for i in range(0, len(manufacture) + 1):
    for j in range(0, len(manufacture) + 1):
        for k in range(j, j + i):
            if k >= len(manufacture):
                continue
            temp += manufacture[k]
            if max_res < temp:
                max_res = temp
                temp = 0
            else:
                temp = 0
# print(max_res)
# print(manufacture)
# print(len(manufacture))

if len(manufacture) == 1:
    max_res = manufacture[0]


for i in range(0, len(manufacture) + 1):
    for j in range(0, len(manufacture) + 1):
        for k in range(j, j + i):
            if k >= len(manufacture):
                continue
            temp += manufacture[k]
            if max_res < temp:
                max_res = temp
                temp = 0
            else:
                temp = 0
# print(max_res)

#
# for i in range(0, len(resource) + 1):
#     for j in range(0, len(resource) + 1):
#         for k in range(j, j + i):
#             if k >= len(resource):
#                 continue
#             temp += resource[k]
#         if max_res < temp:
#             max_res = temp
#             temp = 0
#         else:
#             temp = 0

if max_res == 0:
    max_res = -9999999
    for i in resource:
        if max_res < i <= 0:
            max_res = i

if len(resource) == 1:
    max_res = resource[0]
if len(resource) == 0:
    max_res = 0
print(max_res)
