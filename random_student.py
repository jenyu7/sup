'''
- How does water greet people? 
- sup
Shannon Lau and Jennifer Yu 
SoftDev Period 7 
HW #1: NO-body expects the Spanish Inquisition!
2017-09-13
'''
import random

CLASSES = {
        7: [ 'Helen', 'Shakil', 'Eric', 'Jennifer Y', 'Jennifer Z', 'Arif', 'Queenie', 'Jawadul', 'Shaina', 'Vivien', 'Brian', 'Naotaka', 'Bayan', 'Adam', 'Caleb', 'Terry', 'Jason', 'Alessandro', 'Samantha', 'Carol', 'Joyce', 'Shannon', 'Charles', 'Taylor', 'Kelly', 'Leo', 'Khyber', 'Ibnul', 'Eugene', 'Yuyang', 'Karina', 'Tiffany', 'Holden', 'Michael'],
        8: ['Masha', 'Adrian', 'David', 'Eric', 'Josh', 'Jerome', 'Henry', 'Jackie', 'Giorgio', 'Karen', 'Sonal', 'Xavier', 'Bermet', 'Alex', 'Iris', 'Manahal', 'Donia', 'Md', 'Connie', 'Lisa', 'Xing', 'Angelica', 'Angel', 'Augie', 'Dimitriy', 'Yiduo', 'Gordon', 'Tiffany', 'Clive', 'Jonathan', 'Sasha', 'Daniel'],
        9: [ 'Yu Qi', 'Michela', 'Kristin', 'Fabiha', 'Maxim', 'Marcus', 'Ish', 'James', 'Ryan', 'Edward', 'Adeeb', 'Jake', 'Cynthia', 'Kevin', 'Levi', 'Edmond', 'Kyle', 'Andrew', 'Max', 'Jenny', 'Philip', 'Shan', 'Mansour', 'Ray', 'Jake', 'Ida', 'Kerry', 'Stanley', 'Jackie', 'William', 'Tina', 'Michael']
}

#picks a random student from a specified period 
def random_student(period):
    return random.choice(CLASSES[period])

'''
print "7th period: " + random_student(7)
print "8th period: " + random_student(8)
print "9th period: " + random_student(9)
'''

#Functional for purposes of taking a random student from each class. 
def random_per_period(): 
	text = ""
	text +=  "7th period: " + random_student(7) + "\n"
	text +=  "8th period: " + random_student(8) + "\n"
	text +=  "9th period: " + random_student(9) + "\n"
	return text

print random_per_period()

#To create a program tasked with choosing a student for LCT, which seems to be one of the best applications of this random student generator, the program would have to retain some memory of the students who have already been chosen. 