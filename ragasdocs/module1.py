from dataclasses import dataclass
import typing as t
from pydantic import BaseModel


class Class(BaseModel):
    """
    Represents a class in the school system.

    This class inherits from pydantic's BaseModel for data validation.

    Attributes:
        name (str): The name of the class.
        teacher (Teacher): The teacher responsible for this class.
        class_code (str): A unique code identifying the class.

    Note:
        The 'teacher' attribute is a forward reference to the Teacher class.
    """
    name: str
    teacher: "Teacher"
    class_code: str


class Teacher(BaseModel):
    """
    Represents a teacher in the school system.

    Attributes:
        name (str): The name of the teacher.
        classes (List[Class]): A list of Class objects that the teacher is responsible for.

    Note:
        This class inherits from pydantic's BaseModel for data validation.
    """
    name: str
    classes: t.List["Class"]


class Student(BaseModel):
    """
    Represents a student in the school system.

    This class inherits from pydantic's BaseModel for data validation.

    Attributes:
        name (str): The name of the student.
        classes (List[str]): A list of class codes that the student is enrolled in.
        class_teacher (Teacher): The class teacher assigned to this student.

    Note:
        The 'class_teacher' attribute is a forward reference to the Teacher class.
        The 'classes' attribute contains class codes rather than Class objects.
    """
    name: str
    classes: t.List[str]
    class_teacher: "Teacher"

@dataclass
class School:
    """
    Represents a school in the educational system.

    This class encapsulates the core components of a school, including its teachers,
    students, and classes.

    Attributes:
        teachers (List[Teacher]): A list of Teacher objects representing all teachers in the school.
        students (List[Student]): A list of Student objects representing all students enrolled in the school.
        classes (List[Class]): A list of Class objects representing all classes offered by the school.

    Note:
        This class is implemented as a dataclass for automatic generation of 
        __init__, __repr__, and other special methods.
    """
    teachers: t.List[Teacher]
    students: t.List[Student]
    classes: t.List[Class]

    def get_classes_student_attends(self, student: Student):
        """
        Return the classes a student attends.

        Parameters
        ----------
        student : Student
            The student object for whom to retrieve the classes.

        Returns
        -------
        list of Class
            A list of Class objects that the student attends.

        Notes
        -----
        This method filters the school's classes based on the class codes
        associated with the given student.
        """
        return [c for c in self.classes if c.class_code in student.classes]

    async def get_classes_student_attends_async(self, student: Student):
        """
        Return the classes a student attends.

        Parameters
        ----------
        student : Student
            The student object for whom to retrieve the classes.
        """ 
        return [c for c in self.classes if c.class_code in student.classes]
