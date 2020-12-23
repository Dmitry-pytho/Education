import json
import csv

# with open("test.csv", "r") as csv_file:
#     data = []
#     reader = csv.DictReader(csv_file, delimiter = ";")
#     for row in reader:
#         data.append(row)
# # print(data)
#
# for row in data:
#     print("e-mail:", row{"e-mail"})


with open("test.csv", "r") as csv_file:
    data = []
    reader = csv.reader(csv_file, delimiter = ";")
    for row in reader:
        data.append(row)

# headers = data.pop(0)
print(data)
# print(headers)
for row in data[1:]:
    print("e-mail:", row[1])

data.append([5, "5@gmail.com", 7])
with open("test_new.csv", "w") as csv_file:
    writer = csv.writer(csv_file, delimiter = ";")
    writer.writerows(data)
# with open("test.json", "r", encoding="utf-8") as json_file:
#     data = json.load(json_file)
#     print(type(data), data)
#     # print(data["name"])


# with open("test.json", "r") as json_file:
#     data_txt = json_file.read()
# print(type(data_txt), data_txt)
# json_data = json.loads(data_txt)
# print(json_data)
# data["last_name"] = "Connor"
# data["skills"] = [1,2,3,4,5]
# with open("test_new_json", "w") as json_file:
#     json.dump(data,json_file, indent=4)