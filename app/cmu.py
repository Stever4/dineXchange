def getEmail(user):
    return user.get(u'email', None)

def isCMU(email):
    return email.split('@')[1] == 'andrew.cmu.edu'

def andrewID(email):
    return email.split('@')[0]

def getAndrewID(user):
    return andrewID(getEmail(user))
