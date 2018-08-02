def is_mechanic(user):
    return user.groups.filter(name='mechanic')
    # return user.is_superuser

def is_mechanic_above(user):
    return user.groups.filter(name='mechanic') or user.is_superuser
    # return user.is_superuser