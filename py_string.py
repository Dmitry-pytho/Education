filename = "/home/dmitry/PycharmProjects/Education/Files_for_read/pi_million.txt"
with open(filename) as object_file:
    lines = object_file.readlines()
    pi_string = ""
    for line in lines:
        pi_string = pi_string+line.strip()
birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")


# print(pi_string[:10])
# print(len(pi_string))