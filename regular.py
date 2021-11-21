import csv
import re

with open("phonebook_raw.csv", 'r', encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

result_dict = {}
result_list = []
for i in contacts_list[1:]:
    temp_dict = {}
    phone = re.sub(r'\+*\d\s*\(*(\d\d\d)\)*\s*\-*(\d\d\d)\s*\-*(\d\d)\s*\-*(\d\d)', r'+7(\1)\2-\3-\4', i[-2])
    temp_name = re.sub(r'\s+$', '', i[0] + " " + i[1] + " " + i[2])
    name = re.findall(r'\w+', temp_name)
    temp_dict['lastname'] = name[0]
    temp_dict['firstname'] = name[1]
    if len(name) == 3:
        temp_dict['surname'] = name[2]
    temp_dict['organization'] = i[3]
    temp_dict['position'] = i[4]
    temp_dict['phone'] = re.sub(r'\(*(доб.) (\d+)\)*', r'\1\2', phone)
    temp_dict['email'] = i[6]
    key_name = name[0] + " " + name[1]
    if key_name not in result_dict:
        result_dict[key_name] = temp_dict
    else:
        for key, value in result_dict[key_name].items():
            for key_t, value_t in temp_dict.items():
                if key == key_t and value == '':
                    result_dict[key_name][key] = temp_dict[key_t]

result_list.append(contacts_list[0])
for value in result_dict.values():
    temp_list = [values for values in value.values()]
    result_list.append(temp_list)

with open("phonebook.csv", "w") as f:
   datawriter = csv.writer(f, delimiter=',')
   datawriter.writerows(result_list)
