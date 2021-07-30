def person(name, **data):
    print(name)
    print(data)
    for i, j in data.items():
        print(i, j)


person("zahida", roll=166, contact=1234567, country="Pakistan")
