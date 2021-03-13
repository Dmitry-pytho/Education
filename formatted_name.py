def get_formatted_name(first_name, last_name, middle_name=""):
    if middle_name:
        full_name = first_name +" "+ middle_name +" "+ last_name
    else:
        full_name = first_name +" "+ last_name
    return full_name.title()

musican = get_formatted_name("frank", "sinatra")
print(musican)

musican = get_formatted_name("joe", "hooker", 'lee')
print(musican)
