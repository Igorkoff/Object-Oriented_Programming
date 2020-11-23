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
    def study_type(self):
        return self.__study_type

    @study_type.setter
    def study_type(self, value):

        if value not in (Student.UNDERGRADUATE, Student.POSTGRADUATE):
            raise ValueError

        self.__study_type = value

    @property
    def student_name(self):
        return self.__f_name, self.__l_name
    
    @student_name.setter
    def student_name(self, value):
        
        if type(value) != list:
            raise TypeError

        self.__f_name = value[0]
        self.__l_name = value[1]
    
    @property
    def courses(self):
        return self.__courses

    @courses.setter
    def courses(self, value):
        
        if type(value) != str:
            raise TypeError

        self.__courses.append(value)

    @property
    def get_all_student_data(self):
        return self.student_name, self.study_type, self.courses


class RegistrationData:
    """
    The composite class. Creates a student object in its init function.
    
    Attributes:
    -----------
        __address : str
            Student address as one string data type

        __registration_fee : int
            Fee to pay

        __s_id : str
            A student's student ID. Is only assigned later.
            Default is "NA"

        __student_obj : Student
            Student Object, takes study_type, first name and last name as arguments.

    Methods:
    --------
        student_object_property : property
            returns __student_obj

        student_id_property : property
            returns __s_id
            available as a setter method. Will raise a TypeError
            if the student ID is not supplied as a string.

        address_property : property
            returns __address
            available as a setter.

        registration_fee_property : property
            returns __registration_fee
            available as a setter.

        display_student_data
            no arguments
            no returns
            prints all information about the student to screen.
    """
    def __init__(self, address, registration_fee, study_type, f_name, l_name, s_id = "NA"):
        
        self.__address = address
        self.__registration_fee = registration_fee
        self.__s_id = s_id

        try:
            self.__student_obj = Student(study_type, f_name, l_name)  # object of student class
        except Exception as e:
            pass
    
    @property
    def student_object_property(self):
        return self.__student_obj

    @property
    def student_id_property(self):
        return self.__s_id

    @student_id_property.setter
    def student_id_property(self, value):
        if type(value) != str:
            raise TypeError

        self.__s_id = value

    @property
    def address_property(self):
        return self.__address

    @address_property.setter
    def address_property(self, value):
        self.__address = value

    @property
    def registration_fee_property(self):
        return self.__registration_fee

    @registration_fee_property.setter
    def registration_fee_property(self, value):
        self.__registration_fee = value

    def display_student_data(self):
        print("Student Info: ", self.student_object_property.get_all_student_data, self.student_id_property)
        print("Address: ", self.address_property)
        print("Registration fee: ", self.registration_fee_property)


r = RegistrationData("274 North Circular Road, Dublin 7, Ireland", 11500, Student.UNDERGRADUATE, "Igor", "Alekhnovych")
r.student_id_property = "D18130122"
r.display_student_data()

for course in ("OOP", "Advanced Databases", "Environmental Analytics"):
    r.student_object.courses = course

r.display_student_data()

# print(RegistrationData.__doc__)