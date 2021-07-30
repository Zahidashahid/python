
def student(name, rollNum, marks):
    """
    here we have to take spacial care of positions of assigning values to variables
    :param name:
    :param rollNum:
    :param marks:
    :return:
    """
    print("Name is {} roll number is {} obtain marks are {}".format(name, rollNum, marks))


student("zahida", 166, 50)
student(name="zahida", marks=70,rollNum= 166)
# here I change the position of data by using variables names