def password_qual(password):
    low_list = [x for x in password if x.islower()]
    upp_list = [x for x in password if x.isupper()]
    num_list = [x for x in password if x.isdigit()]
    return (len(low_list) > 0 and len(upp_list) > 0 and len(num_list) > 0)

def password_strength(password):
    low_list = [x for x in password if x.islower()]
    upp_list = [x for x in password if x.isupper()]
    num_list = [x for x in password if x.isdigit()]
    non_list = [x for x in password if not x.isdigit() and not x.islower() and not x.isupper() ]

    strength = 0
    if (len(low_list) > 0):
        strength += 2
    if (len(upp_list) > 0):
        strength += 2
    if (len(num_list) > 0):
        strength += 3
    if (len(non_list) > 0):
        strength += 3

    return strength
