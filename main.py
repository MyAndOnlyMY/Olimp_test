math_dict = dict()
math_n_dict = dict()
id_m_dict = dict()

inf_dict = dict()
inf_n_dict = dict()
id_i_dict = dict()

phis_dict = dict()
phis_n_dict = dict()
id_p_dict = dict()

all_list = list()

# dict help maker
def d_h_m(a):
    _list = list(a.split())
    return _list

# for count all people
def all_list_maker(n):
    for i in n.keys():
        all_list.append(i)
    return

# id people maker
def id_pm(string, _count):
    _id = f"{_count}_{string[0][0]}_{len(string[1])}"
    return _id

# printing id + second name + name
def printer_id(n):
    for i in n.keys():
        print(f"{i} {n[i]}")
    return

# Math dict: Second name + Counts
a = str(input())
count = 1
while a!="":
    math_dict[d_h_m(a)[0]] = int(d_h_m(a)[2])
    math_n_dict[d_h_m(a)[0]] = d_h_m(a)[1]
    id_m_dict[id_pm(a, count)] = f"{d_h_m(a)[0]} {d_h_m(a)[1]}"
    count +=1
    a = str(input())

# Inf dict: Second name + Counts
a = str(input())
count = 1
while a!="":
    inf_dict[d_h_m(a)[0]] = int(d_h_m(a)[2])
    inf_n_dict[d_h_m(a)[0]] = d_h_m(a)[1]
    id_i_dict[id_pm(a, count)] = f"{d_h_m(a)[0]} {d_h_m(a)[1]}"
    count +=1
    a = str(input())

# Phis dict: Second name + Counts
a = str(input())
count = 1
while a!="":
    phis_dict[d_h_m(a)[0]] = int(d_h_m(a)[2])
    phis_n_dict[d_h_m(a)[0]] = d_h_m(a)[1]
    id_p_dict[id_pm(a, count)] = f"{d_h_m(a)[0]} {d_h_m(a)[1]}"
    count +=1
    a = str(input())

# Count people
all_list_maker(math_dict)
all_list_maker(inf_dict)
all_list_maker(phis_dict)

num_people = len(set(all_list))

print(f"Количество участников: {num_people}")

# id + second name + name
print()
print("Список участников олипиады по математике:")
printer_id(id_m_dict)
print()
print("Список участников олипиады по информатике:")
printer_id(id_i_dict)
print()
print("Список участников олипиады по физике:")
printer_id(id_p_dict)

print()

# people, who were in all olimp
print("Ученики, участвующие во всех олипиадах:")
for m in math_dict.keys():
    for i in inf_dict.keys():
        for p in phis_dict.keys():
            if m==i==p:
                print(f"{m} {math_n_dict[m]}")

print()

# person with max count
max_m_count = 0
man = ""
for k in all_list:
    all_p_count = 0
    if k in math_dict.keys():
        all_p_count += math_dict[k]
    if k in inf_dict.keys():
        all_p_count += inf_dict[k]
    if k in phis_dict.keys():
        all_p_count += phis_dict[k]
    if all_p_count > max_m_count:
        max_m_count = all_p_count
        man = k
print(f"Ученик {man} набрал {max_m_count} баллов по всем олипмиадам - наибольшее количество.")