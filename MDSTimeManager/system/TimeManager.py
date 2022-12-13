import system.deliverableviewer as dv

def DeliverableSearch(course_list):
    for course in course_list:
        for deliverable in course.deliverables:
            if (deliverable.date.split("/")[1] in dv.next7dates()):
                print(f"{course}, {deliverable}")
                
def DeliverableAll(course_list):
    for course in course_list:
        for deliverable in course.deliverables:
            print(f"{deliverable.dname},{deliverable.date}")