import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents  # Replace 'your_module' with actual module name
# Fixtures
@pytest.fixture
def hogwarts_classroom():
    """Fixture to set up a Hogwarts classroom with a teacher and students."""
    mcgonagall = Teacher("Professor McGonagall")
    students = [
        Student("Harry Potter"),
        Student("Hermione Granger"),
        Student("Ron Weasley"),
    ]
    return Classroom(mcgonagall, students, "Transfiguration")

@pytest.fixture
def new_student():
    """Fixture to create a new student."""
    return Student("Draco Malfoy")

# Test adding a student
def test_add_student(hogwarts_classroom, new_student):
    hogwarts_classroom.add_student(new_student)
    assert new_student in hogwarts_classroom.students

# Test adding too many students
def test_too_many_students():
    snape = Teacher("Professor Snape")
    students = [Student(f"Student {i}") for i in range(11)]
    potions_class = Classroom(snape, students, "Potions")
    
    with pytest.raises(TooManyStudents):
        potions_class.add_student(Student("Extra Student"))

# Test removing a student
@pytest.mark.parametrize("student_name, expected_count", [
    ("Hermione Granger", 2),
    ("Ron Weasley", 2),
    ("Neville Longbottom", 3)  # Should remain the same if student isn't found
])
def test_remove_student(hogwarts_classroom, student_name, expected_count):
    hogwarts_classroom.remove_student(student_name)
    assert len(hogwarts_classroom.students) == expected_count
    assert all(student.name != student_name for student in hogwarts_classroom.students)

# Test changing the teacher
def test_change_teacher(hogwarts_classroom):
    new_teacher = Teacher("Albus Dumbledore")
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher == new_teacher
