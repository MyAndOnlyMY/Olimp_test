math_dict = dict()
inf_dict = dict()
phis_dict = dict()

name_math_dict = dict()
name_inf_dict = dict()
name_phis_dict = dict()

def all_list_maker(n):
    for i in n.keys():
        all_list.append(i)
    return

def dict_maker(n):
    _dict = dict()
    _name_dict = dict()
    _str = input()
    while _str!="":
        _str_ = _str.split()
        _dict[_str_[0]] = int(_str_[2])
        _name_dict[_str_[0]] = _str_[1]
        _str = input()
        return _dict


math_dict = dict_maker()
inf_dict = dict_maker()
phis_dict = dict_maker()

all_list = list()

all_list_maker(math_dict)
all_list_maker(inf_dict)
all_list_maker(phis_dict)

num_people = len(set(all_list))

print(f"Количество человек: {num_people}")