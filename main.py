math_dict = dict()
inf_dict = dict()
phis_dict = dict()

# Math dict: Second name + Counts
while True:
    a = str(input())
    if a=="":
        break
    math_list = list(map(str, a.split()))
    math_dict[math_list[0]] = math_list[2]

# Inf dict: Second name + Counts
while True:
    a = str(input())
    if a=="":
        break
    inf_list = list(map(str, a.split()))
    inf_dict[inf_list[0]] = inf_list[2]

# Phis dict: Second name + Counts
while True:
    a = str(input())
    if a=="":
        break
    phis_list = list(map(str, a.split()))
    phis_dict[phis_list[0]] = phis_list[2]

all_list = ()

for i in math_dict:
    for j in inf_dict:
        if math_dict[i] == inf_dict[j]:
            all_list += i

print(all_list)