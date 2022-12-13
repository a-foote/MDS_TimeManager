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
    datelist = []
    for i in range(1,8):
        datelist.append(str((datetime.datetime.now()+datetime.timedelta(i)).day))
    return datelist