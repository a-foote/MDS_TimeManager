import system.deliverableviewer as dv
                  
#######################################################################################################################################

import setup.course as c
import system.timemanager as tm 
import system.deliverableviewer as dv
import datetime 

# Course 1
Data533 = c.Course("Object Oriented Programming","Khalad Hasan","3",1)
Data533Project = c.Project("Data 533: Project- Time Manager","12/22", milestones="no milestones",repo="MyRepo.git")
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

def userinput():
    
    type_assignLab = type(Data543Assignment1)
    next7deliverables = dv.DeliverableSearch(Courses)
    
    print("Please choose a rank out of (1,2,3) with 3 being most difficult.")
    for course in Courses:
        print(f"For {course}: ")
        rank = input()
        course.rank = rank
    weektime = float(input("How much time is available in the next 7 days for studies (in hours)? "))
    print("How much time (in hours) will you take for the following:\n")
    for deliverable in next7deliverables:
        if type(deliverable) == type_assignLab:
            print(f"For {deliverable}")
            time = float(input())
            weektime = weektime - time
            deliverable.dur = time
        else:
            continue
    print(f"\nTime left after assignments and labs: {weektime:.2f} hours")
    print("")
    return weektime

def fetchranks(course_list):
    totalranks = 0.0
    for course in course_list:
        totalranks = totalranks + float(course.rank)
    return totalranks 
    
def timemanagercal(timeavailable, course_list):
    studytime = 0.0
    tr = fetchranks(course_list)
    for course in course_list:
        cr = float(course.rank)
        studytime = (cr/tr)*timeavailable
        print(f"Recommended study time for {course} is {studytime:.2f} hours ({studytime*60:1.0f} mins)")