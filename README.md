# MDS_TimeManager

This package that can help UBC Master of Data Science (MDS) students manage their time. A student can view the upcoming deliverables (Quizzes, Labs/Assignments, Projects) or get recommendations on study time for each course over the next 7 days.

## Sub-package 1 - setup

### Module 1:  people.py

This package will include a class ‘People’ which will have some basic attributes that will be inherited by the class Instructor and class Student. Main functions will be the getter, setter and delete methods.

#### class Person

	Vimal - to do
	
#### class Instructor

	Vimal - to do

#### class Student

	Vimal - to do

### Module 2: course.py

This module will have classes for entities Course, Deliverable, Quiz, Assignment and Lab. Deliverable class will be inherited by class Quiz, Assignment and Lab since they share common attributes.

#### class Course

	Vimal - to do
	
#### class Deliverable

	Vimal - to do

#### class Quiz

	Vimal - to do

#### class AssignLab

	Vimal - to do

#### class Project

	Vimal - to do
	

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

This module takes the next 7 days study time availability, inputed by the user and recommends an allotted study time for each course depending on how they have ranked the course and upcoming deliverables.

#### userinput

	Alyssa - to do

#### fetchRanks

	Alyssa - to do

#### fetchDeliverables
	
	Alyssa - to do

### timeManagerCalc

	Alyssa - to do