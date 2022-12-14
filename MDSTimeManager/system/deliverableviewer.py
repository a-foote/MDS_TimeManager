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
    for i in range(0,7):
        datelist.append(str((datetime.datetime.now()+datetime.timedelta(i)).day))
    return datelist

def DeliverableViewer(deliverable_list):
    print("Deliverables due in the next 7 days are:\n")
    for deliverable in deliverable_list:
        print(deliverable)
    print("\n")

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
       

     
   