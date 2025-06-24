#Задание 1

class Friends:
    def __init__(self, connections):
        self.connections = set()
        for connection in connections:
            self.connections.add(frozenset(connection))
    
    def add(self, connection):
        conn = frozenset(connection)
        if conn in self.connections:
            return False
        self.connections.add(conn)
        return True
    
    def remove(self, connection):
        conn = frozenset(connection)
        if conn in self.connections:
            self.connections.remove(conn)
            return True
        return False
    
    def names(self):
        names_set = set()
        for conn in self.connections:
            names_set.update(conn)
        return names_set
    
    def connected(self, name):
        connected_names = set()
        for conn in self.connections:
            if name in conn:
                connected_names.update(conn - {name})
        return connected_names
    
f = Friends([{"Аня", "Боря"}, {"Боря", "Вася"}, {"Вася", "Аня"}])

print(f.names())  
print(f.connected("Аня"))  

# Задание 2

from typing import List, Dict, Set

class Student:
    def __init__(self, name: str, student_id: int):
        self.name = name
        self.student_id = student_id
        self.grades: Dict[str, List[int]] = {}  # {"Предмет": [оценки]}
    
    def add_grade(self, subject: str, grade: int):
        if subject not in self.grades:
            self.grades[subject] = []
        self.grades[subject].append(grade)
    
    def get_average_grade(self) -> float:
        if not self.grades:
            return 0.0
        all_grades = [grade for subj_grades in self.grades.values() for grade in subj_grades]
        return sum(all_grades) / len(all_grades)
    
    def get_subject_average(self, subject: str) -> float:
        if subject not in self.grades or not self.grades[subject]:
            return 0.0
        return sum(self.grades[subject]) / len(self.grades[subject])

class Group:
    def __init__(self, group_id: int, course: int):
        self.group_id = group_id
        self.course = course
        self.students: List[Student] = []
    
    def add_student(self, student: Student):
        self.students.append(student)
    
    def get_group_average(self) -> float:
        if not self.students:
            return 0.0
        return sum(student.get_average_grade() for student in self.students) / len(self.students)
    
    def get_subject_average(self, subject: str) -> float:
        if not self.students:
            return 0.0
        subject_grades = []
        for student in self.students:
            if subject in student.grades:
                subject_grades.extend(student.grades[subject])
        if not subject_grades:
            return 0.0
        return sum(subject_grades) / len(subject_grades)
    
    def get_students_to_expel(self, threshold: float) -> List[Student]:
        return [student for student in self.students if student.get_average_grade() < threshold]
    
    def get_top_students(self, count: int) -> List[Student]:
        return sorted(self.students, key=lambda s: s.get_average_grade(), reverse=True)[:count]

class Deanery:
    def __init__(self):
        self.groups: Dict[int, Group] = {}  
        self.subjects: Set[str] = set()
    
    def add_group(self, group: Group):
        self.groups[group.group_id] = group
        for student in group.students:
            self.subjects.update(student.grades.keys())
    
    def get_course_average(self, course: int) -> float:
        course_groups = [group for group in self.groups.values() if group.course == course]
        if not course_groups:
            return 0.0
        return sum(group.get_group_average() for group in course_groups) / len(course_groups)
    
    def get_subject_stats(self, subject: str) -> Dict[int, float]:
        return {
            group_id: group.get_subject_average(subject)
            for group_id, group in self.groups.items()
            if subject in self.subjects
        }
    
    def get_problem_subjects(self, threshold: float) -> Dict[str, float]:
        problem_subjects = {}
        for subject in self.subjects:
            subject_average = sum(
                group.get_subject_average(subject)
                for group in self.groups.values()
            ) / len(self.groups)
            if subject_average < threshold:
                problem_subjects[subject] = subject_average
        return problem_subjects
    

deanery = Deanery()

group_433 = Group(433, 1)
group_531 = Group(531, 2)

student1 = Student("Иванов Иван", 1)
student1.add_grade("Математика", 4)
student1.add_grade("Физика", 5)

student2 = Student("Петров Петр", 2)
student2.add_grade("Математика", 3)
student2.add_grade("Физика", 4)

group_433.add_student(student1)
group_433.add_student(student2)

deanery.add_group(group_433)

print(f"Средний балл группы 433: {group_433.get_group_average()}")
print(f"Средний по математике в 433: {group_433.get_subject_average('Математика')}")
print(f"Проблемные предметы: {deanery.get_problem_subjects(3.5)}")
print(f"Студенты на отчисление: {[s.name for s in group_433.get_students_to_expel(3.8)]}")