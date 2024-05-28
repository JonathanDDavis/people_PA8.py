#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jd0919889
#
# Created:     22/10/2019
# Copyright:   (c) jd0919889 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from objects_PA8 import Student as Student
from objects_PA8 import Faculty as Faculty
from objects_PA8 import students as students
from objects_PA8 import faculty as faculty

student0 = Student("Jason", "Phan", "male", "male", "123-45-6789", "02/25/2000", "Jphan@gmail.com", "Social Sciences", "205 hall", 2018, True)
students.append(student0)
student1 = Student("Leeroy", "Jenkins", "male", "male", "234-56-7890", "12/26/1999", "JenkinsL@gmail.com", "Biological And Biomedical Sciences", "561 hall", 2018, True)
students.append(student1)
student2 = Student("Janet", "Smith", "female", "female", "345-67-8901", "06/10/2000", "SmithJ@gmail.com", "Psychology", "203 hall", 2018, True)
students.append(student2)
student3 = Student("John", "Doe", "male", "male", "456-78-9012", "05/16/2000", "DoeJohn@gmail.com", "Engineering", "032 hall", 2018, True)
students.append(student3)
student4 = Student("Dave", "Davis", "male", "male", "567-89-0123", "08/15/2000", "DavisDave@gmail.com", "Visual And Performing Arts", "565 hall", 2019, False)
students.append(student4)
student5 = Student("Jacob", "Reed", "male", "male", "678-90-1234", "10/14/2000", "ReedJacob@gmail.com", "Education", "250 hall", 2018, True)
students.append(student5)
student6 = Student("Alessandra", "Austin", "female", "female", "789-01-2345", "02/16/2000", "AlessanA@gmail.com", "Multi/Interdisciplinary Studies", "012 hall", 2018, True)
students.append(student6)
student7 = Student("Guy", "Ramsey", "male", "male", "890-12-3456", "09/19/2000", "RamseyGuy@gmail.com", "Physical Sciences", "204 hall", 2019, False)
students.append(student7)
student8 = Student("Lyra", "Foley", "female", "female", "901-23-4567", "07/16/2000", "FoleyLyra@gmail.com", "History", "320 hall", 2018, True)
students.append(student8)
student9 = Student("Lincoln", "Novak", "male", "male", "012-34-5678", "08/10/2000", "NovakLi@gmail.com", "Mathematics And Statistics", "152 hall", 2018, True)
students.append(student9)
faculty0 = Faculty("Alphonse", "Boyer", "female", "female", "987-65-4321", "09/16/1979", "BoyerAl@gmail.com", "Education", "09-15", 2000)
faculty.append(faculty0)
faculty1 = Faculty("Morris", "Mercer", " male" , "male", "876-57-3210", "04/12/1956", "MorrisMe@gmail.com", "Social Sciences", "04-23", 1979)
faculty.append(faculty1)
faculty2 = Faculty("Jayne", "Riley", " female" , "female", "765-43-2109", "07/16/1949", "RileyJa@gmail.com", "Engineering", "06/18", 1976)
faculty.append(faculty2)
faculty3 = Faculty("Mac", "Collins", " male" , "male", "654-32-1098", "02/18/1937", "CollinsM@gmail.com", "Visual And Performing Arts", "07/24", 1961)
faculty.append(faculty3)
faculty4 = Faculty("Napoleon", "Li", " male" , "male", "5432-10-9876", "06/17/1924", "LiNap@gmail.com", "Psychology", "03/16", 1951)
faculty.append(faculty4)

Student.countStudents()
Faculty.yearsOfService()
