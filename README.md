# MDS_TimeManager

This package that can help UBC Master of Data Science (MDS) students manage their time. A student can view the upcoming deliverables 
(Quizzes, Labs/Assignments, Projects) or get recommendations on study time for each course over the next 7 days.

## Sub-package 1 - setup

### Module 1: course.py

This module will have classes for entities Course, Deliverable, Quiz, Assignment and Lab. Deliverable class will be inherited by class 
Quiz, Assignment and Lab since they share common attributes.

#### class Course

- This class is the blueprint for all the courses that will be in each block. In this project we only work with Block 3 courses.
- Block 3 courses are defined in this package (they can be taken as inputs from the user in future additions).
- The attributes of this class are: cname, instructor, block, rank, deliverables.
- 'cname' is the name of the course, 'instructor' is the professor who will teach the course, 'block' represents the block the course
will be taught in, 'rank' represents the difficulty level a student assigns to the course, it defaults to 1. Ranks go from 1 to 3 with
1 being 'easy', 2 being 'moderate' and 3 being 'hardest'. 'deliverables' will represent the deliverables for that course which will mainly
be objects of type Quiz, AssignLab and Project. 
	
#### class Deliverable

- This is the parent class for Quiz, AssignLab and Project classes.
- The dname, date and status attributes of this class are shared by each of the child classes.
- The child classes have their own unique attributes as well in addition to the attributes being inherited.
- 'dname' will hold the name for the deliverable type, 'date' will contain the due date for the deliverable and 'status' tells whether
the deliverable is complete or not. It defaults to 'Incomplete' for the child class objects.

#### class Quiz

- This is one of the child classes of class Deliverable.
- The attributes unique to this class are: topics and qtype.
- 'topics' represents the topics that will be on the upcoming quiz, and 'qtype' has the type of questions that will be asked like MCQs,
long answers, coding or a combination of these. 

#### class AssignLab

- This is another child class of class Deliverable.
- This class will represent objects of type Lab and Assignment both. They will be named accordingly. Since, the attributes for both of
these types of deliverables were same, they were combined to be in one class.
- The attributes unique to this class are: dur, durleft, subloc.
- 'dur' represents the time it will take to complete this deliverable, and 'durleft' represents the time left to complete this 
deliverable and 'subloc' shows where this deliverable has to be submitted on Canvas or using a repository.


#### class Project

- This is another child class of class Deliverable.
- This deliverable represents the Projects in the course (if applicable).
- The attributes unique to this class are: milestones, dur, durleft, repo.
- 'milestones' is supposed to represent any milestones that a student will have during the course of the project, 'dur' represents the 
time it will take to complete the project, and 'durleft' represents the time left to complete the project and 'repo' represents the github
link of the repository.

### Module 2:  people.py

This package will include a class ‘People’ which will have some basic attributes that will be inherited by the class Instructor and 
class Student. Main functions will be the getter, setter and delete methods.

#### class Person

- This is the parent class for Instructor and Student classes.
- The 'name' attribute of this class is shared by each of the child classes.
- The child classes have their own unique attributes as well in addition to the attribute being inherited.
	
#### class Instructor

- This is one of the child classes of class Person.
- It inherits the attribute 'name' from the parent class.
- The attributes unique to this class are: hours and comm.
- 'hours' describes the Office hours of the instructor and 'comms' describes the instructor's preferred method of communication.

#### class Student

- This is one of the child classes of class Person.
- It inherits the attribute 'name' from the parent class.
- The attributes unique to this class is: sID.
- 'sID' is the student number which is unique to a student.

## Sub-package 2 - system

### Module 1: deliverableviewer.py

This module shows what deliverables are due in the next 7 days. 

#### get7thDate 

	Alyssa - to do

#### deliverableSearch

	Alyssa - to do

### deliverableViewer

	Alyssa - to do

### Module 2: timemanager.py

This module takes the next 7 days study time availability, inputed by the user and recommends an allotted study time for each course 
depending on how they have ranked the course and upcoming deliverables.

#### userinput

	Alyssa - to do

#### fetchRanks

	Alyssa - to do

#### fetchDeliverables
	
	Alyssa - to do

### timeManagerCalc

	Alyssa - to do