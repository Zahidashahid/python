def addition_function(*values):
    result = 0
    for i in values:
        result += i
    print("Sum is:", result)


def advance_junaid(name, roll, *marks, area="GB", school="GBPS", **keywordArg):
    """
     Here marks is arbitrary
    :param name:
    :param roll:
    :param marks:
    :param area:
    :param school:
    :param keywordArg:
    :return:
    """
    total_subjects = len(marks)
    total_marks = len(marks) * 100
    gained_marks = 0
    is_passed = False

    for subject_marks in marks:
        gained_marks += subject_marks

    if gained_marks >= total_marks / 2:
        is_passed = True

    print("area  : ", area)
    print("school: ", school)
    print("roll  : ", roll)
    print("name  : ", name)
    print("marks : ", marks)

    print("Total Subjects    :", total_subjects)
    print("total marks       :", total_marks)
    print("Obtained marks    :", gained_marks)
    print("Is Passed         :", is_passed)

    print("---------------------")

    for values, keyword in keywordArg.items():
        print(values, keyword)


addition_function(1, 2)
advance_junaid("zahida", 166, 25, 25, contact=1031256589, language="Urdu", area="Danyore", school="DJ")
