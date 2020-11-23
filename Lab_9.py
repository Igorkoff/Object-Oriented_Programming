# author: Igor Alekhnovych
# date: 20-11-2020
# purpose: Lab 8

class Student:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """

    def __init__(self, study_type, f_name, l_name):
        # YOUR CODE GOES HERE
        pass

    # YOUR CODE GOES HERE



class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        pass

    # YOUR CODE GOES HERE




r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500,
                     Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)