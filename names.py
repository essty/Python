people = [('andrew', 'in'), 
         ('bobby', 'in'), 
         ('esther', 'in'), 
         ('vince','in'), 
         ('judy','out')]
		 
#if the person is in the office then they get a bagel

def gets_reward(person_who_is_in, catchphrase):
    print "{} is in the office".format(person_who_is_in, catchphrase)
    print "{} gets to have so much cream cheese".format(person_who_is_in, catchphrase)
    print "{} gets a bagel".format(person_who_is_in, catchphrase)

def gets_punished(person_to_be_punished):
    print "{} is not in the office".format(person_to_be_punished)
    print "{} gets more email:(".format(person_to_be_punished)
    print "{} gets NO cream cheese".format(person_to_be_punished)
    
    
def person_is_in_the_office(status):
    """ return True if the person's status is 'in'
    """
    if status == 'in':
        return True
    else:
        return False

def take_attendance():
    cheer = 'whoopee'
    for person, status in people:
        person = person.upper()
        person_status = person_is_in_the_office(status)
        if person_status == True:
            gets_reward(person, cheer)
        else :
            gets_punished(person)

#calling the function
take_attendance()