# author: Igor Alekhnovych
# date: 20-11-2020
# purpose: Lab 8

class Student:
    """
    The component class of the composition.
    This class contains data about the student.
    ...
    Attributes:
    -----------
        UNDERGRADUATE, POSTGRADUATE : range(2)
        Used to define the level of a study of a student.
        These are class variables. Usage via class name.

        __study_type : range(2)
        Allowed are only the predefined Student.UNDERGRADUATE
        and Student.POSTGRADUATE class variables.
        
        __f_name : str
        First name of a student.
        
        __l_name : str
        Last name of a student.
        
        __courses : list
        Contains a list of courses that a student is enrolled into
        Empty by default
    
    
    Methods:
    --------
        study_type : property
            Returns self.__study_type which is ("UNDERGRADUATE", "POSTGRADUATE")
            Available as setter
            Raises a ValueError if the supplied value does not match the tuple
        
        student_name : property
            Returns self.__f_name, self.__l_name
            Available as a setter that expects first and last name in this sequence in a list
            Raises a TypeError if the names are not supplied in a list data type
        
        courses : property
            Returns self.__courses which is of type list
            Available as a setter that adds a string value to the self.__courses list
            Raises a TypeError if the supplied names are not in a str type
        
        get_all_student_data : property
            Arguments: none
            Returns all information from self.student_name, self.study_type, self.course
    """

    UNDERGRADUATE, POSTGRADUATE = range(2)

    def __init__(self, study_type, f_name, l_name):
        
        if study_type not in (Student.POSTGRADUATE, Student.UNDERGRADUATE):
            raise ValueError

        self.__study_type = study_type
        self.__f_name = f_name
        self.__l_name = l_name
        self.__courses = []

    def __str__(self):
        return f"{self.student_name} {self.study_type} {self.courses}"
    
    @property
    def study_type(self)
        return self.__study_type

    @study_type.setter
    def study_type(self, value)

        if value not in (Student.UNDERGRADUATE, Student.POSTGRADUATE):
            raise ValueError

        self.__study_type = value

    @property
    def student_name(self)
        return self.__f_name, self.__l_name
    
    @student_name.setter
    def student_name(self, value)
        
        if type(value) != list:
            raise TypeError

        self.__f_name = value[0]
        self.__l_name = value[1]
    
    @property
    def courses(self)
        return self.__courses

    @courses.setter
    def courses(self, value)
        
        if type(value) != str:
            raise TypeError

        self.__courses.append(value)

    @property
    def get_all_student_data(self):
        return self.student_name, self.study_type, self.courses


class RegistrationData:
    """
    INSERT YOUR DOCSTRING INFORMATION HERE
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id="NA"):
        # YOUR CODE GOES HERE
        pass

    # YOUR CODE GOES HERE




r = RegistrationData("8 Lower Kevin Street, Dublin 8, Ireland", 1500, Student.POSTGRADUATE, "Bianca", "Phelan")
r.display_student_data()
r.student_id_property="C12345"
r.display_student_data()
for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)