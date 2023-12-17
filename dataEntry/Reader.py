import json

my_list = []

with open('Employee.txt') as f:
    lines = f.readlines()
    columns = []

    i = 0
    for line in lines:
        line = line.strip()
        if line:
            if i == 0:
                columns = [item.strip() for item in line.split('|') if item != ""]
                i = i + 1
            else :
                d = {}
                data = [item.strip() for item in line.split('|') if item != ""]
                for index, elem in enumerate(data):
                    if (columns[index] == 'idDepartment'):
                        d[columns[index]] = i
                    else:
                        d[columns[index]] = data[index]
                i = i + 1

                my_list.append(d)

print(json.dumps(my_list, indent = 4))

def read():
    return my_list
