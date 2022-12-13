import datetime
def get7thdate():
    """
    The function returns the 7th day (DD) from current date.
    
    Input:
    The function does not require any inputs and can be called directly.
    
    Output:
    "The 7th date from today is: September 6, 1993"
    Returns the day part of the date 7 days from current date.
    """
    the7thdate = datetime.datetime.now() + datetime.timedelta(7)
    print("The 7th date from today is: ",the7thdate.strftime("%B %d, %Y"))
    return str(the7thdate.day)

def next7dates():
    """
    The function returns the next 7 dates (DD) from the current date.
    
    Input:
    The function does not require any inputs and can be called directly.
    
    Output:
    If today is December, 12: the output will be a list: ['13','14','15','16','17','18','19']
    """
    datelist=[]
    for i in range(1,8):
        datelist.append(str((datetime.datetime.now()+datetime.timedelta(i)).day))
    return datelist

##############################################################################################################

def DeliverableViewer(deliverable_list):
    for deliverable in deliverable_list:
        print(deliverable)

def DeliverableSearch(course_list):
    lst = []
    for course in course_list:
        for deliverable in course.deliverables:
            if (deliverable.date.split("/")[1] in next7dates()):
                lst.append(deliverable)
    return lst
                
def DeliverableAll(course_list):
    for course in course_list:
        for deliverable in course.deliverables:
            print(f"{deliverable.dname},{deliverable.date}")

##############################################################################################################            
            
import setup.course as c
import system.timemanager as tm 
import datetime 

# Course 1
Data533 = c.Course("Object Oriented Programming","Khalad Hasan","3",1)
Data533Project = c.Project("Data 533: Project- Time Manager","12/22", "None so far", "Bro no time!","MyRepo.git")
# How to assign deliverables to a course object
Data533.deliverables = Data533Project

# Course 2
Data543 = c.Course("Data Collection","Emelie Gustaffson","3",1)
Data543Quiz1 = c.Quiz("Data543: Quiz 1", "12/5", "Complete", "Lecture 1 to Lecture 4", "MCQ, Short Answers and R programming")
Data543Quiz2 = c.Quiz("Data543: Quiz 2", "12/19", "Incomplete", "Lecture 5 to Lecture 8", "MCQ and R programming")
Data543Assignment1 = c.AssignLab("Data543: Assignment 1", "12/12", "Complete", "", "", subloc="Canvas" )
Data543Assignment2 = c.AssignLab("Data543: Assignment 2", "12/16","Incomplete" , "", "", subloc="Canvas" )
Data543.deliverables = Data543Quiz1
Data543.deliverables = Data543Quiz2
Data543.deliverables = Data543Assignment1
Data543.deliverables = Data543Assignment2
# for deliverable in Data543.deliverables:
#     print(deliverable.date)

# Course 3
Data571 = c.Course("Resampling and Regularization","Jeff Andrews","3",3)
Data571Quiz1 = c.Quiz("Data571: Quiz 1", "12/7", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
Data571Quiz2 = c.Quiz("Data571: Quiz 2", "12/21", "Incomplete", "Lecture 4 to Lecture 6", "MCQ and Short Answers")
Data571Assignment1 = c.AssignLab("Data571: Assignment 1", "12/5", "Complete", "","",subloc="Canvas" )
Data571Assignment2 = c.AssignLab("Data571: Assignment 2", "12/19", "Incomplete","","",subloc="Canvas" )
Data571.deliverables = Data571Quiz1
Data571.deliverables = Data571Quiz2
Data571.deliverables = Data571Assignment1
Data571.deliverables = Data571Assignment2
# print("Deliverables for this course are:", end = "")
# for deliverable in Data571.deliverables:
#     print(deliverable, end = "")


# Course 4
Data581 = c.Course("Modelling and Simulation","Ladan Tazik","3",1)
Data581Quiz1 = c.Quiz("Data 581: Quiz 1", "12/6", "Complete", "Lecture 1 to Lecture 3", "MCQ and Short Answers")
Data581Quiz2 = c.Quiz("Data 581: Quiz 2", "12/20", "Incomplete", "Lecture 4 to Lecture 7", "MCQ and Short Answers")
Data581Lab1 = c.AssignLab("Data 581: Lab 1", "12/1", "Complete", "","",subloc="Canvas" )
Data581Lab2 = c.AssignLab("Data 581: Lab 2", "12/8", "Complete", "","",subloc="Canvas" )
Data581Lab3 = c.AssignLab("Data 581: Lab 3", "12/15", "Incomplete", "","",subloc="Canvas" )
Data581.deliverables = Data581Quiz1
Data581.deliverables = Data581Quiz2
Data581.deliverables = Data581Lab1
Data581.deliverables = Data581Lab2
Data581.deliverables = Data581Lab3

Courses = [Data533, Data543, Data571, Data581]
     
   