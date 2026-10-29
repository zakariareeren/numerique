from collections import defaultdict

class Student:
    def __init__(self, first_name: str, last_name: str):
        self.first_name=first_name
        self.last_name=last_name
        self.dico=defaultdict(list)
    def __repr__(self):
        return f"Student({self.first_name}, {self.last_name})"


    def add_grade(self,course:str, grade: float):
        if not(grade>=0 and grade<=20):
            raise ValueError ("La note n'est pas entre 0 et 20")
        self.dico[course].append(grade)
    
    def followed_topics(self):
        f=[]
        for x in self.dico:
            f.append(x)
        return f 
    
    def compute_average(self, course: str):
            if not(course in self.dico):
                raise ValueError ("Il n'y a pas de notes dans cette matière")
            d=0
            c=0
            for x in self.dico[course]:
                d+=x
                c+=1
            return d/c
    
            
    def report(self):
        lines=["+===============+===============+","|     Topic     |    Average    |","+===============+===============+",]
        for x in self.dico:
            lines.append(f"|     {x}     |    {student.compute_average(x)}    |")
        "\n".join(lines)
        
Report for student Albert Einstein
+===============+===============+
|     Topic     |    Average    |
+===============+===============+
|   Chemistry   |     11.33     |
+---------------+---------------+
|    English    |     14.00     |
+---------------+---------------+
|    Physics    |     13.25     |
+---------------+---------------+
|    French     |     11.50     |
+---------------+---------------+
|  Mathematics  |     12.80     |
+---------------+---------------+
|  Scubadiving  |     12.50     |
+---------------+---------------+




# pour tester

try:
    student = Student("Achille", "Talon")
    r = repr(student)
    assert isinstance(r, str), "__repr__ must return a str"
    assert "Achille" in r and "Talon" in r, f"first and last name should appear in {r!r}"
except Exception as e:
    print('OOPS - There is an issue in your code.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')




 

# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    try:
        student.add_grade("History", 25.)
    except ValueError:
        pass
    else:
        raise Exception("a grade outside of [0, 20] should raise ValueError")
except Exception as e:
    print('OOPS - There is an issue in your add_grade method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')


# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    topics = student.followed_topics()
    if len(topics) != 1 or "History" not in topics:
        raise Exception(f"Expecting ['History'] got {topics}")
except Exception as e:
    print('OOPS - There is an issue in your followed_topics method')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')




# pour tester

try:
    student = Student("Achille", "Talon")
    student.add_grade("History", 10.)
    student.add_grade("History", 12.)
    if (student.compute_average("History") != 11.):
        raise Exception("Issue in your average calculation.")
    try:
        student.compute_average("French")
    except ValueError:
        pass
    else:
        raise Exception("If topic is not followed, a ValueError is expected")
    if student.followed_topics() != ["History"]:
        raise Exception(f"asking for the average of an unfollowed topic must not create it: {student.followed_topics()}")
except Exception as e:
    print('OOPS - There is an issue in your compute_average method.')
    print(f"Error message : {e}")
else:
    print('Congrats ! Your implementation works !')
