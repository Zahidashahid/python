def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person("zahida", roll=166, contact=1234567, country="Pakistan")


def student(name,*contact , **marks ):
    print(name)
    print(contact)
    for i, j in marks.items():
        print(i, j)


student("zahida", 123, 415, maths=1, english=2, urdu=3 )
