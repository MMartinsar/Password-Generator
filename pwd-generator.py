import random
import string

def password(len, upper, lower, numbers, others):
    password = []
    for x in range(len):
        if upper == 1:
            password += [random.choice(string.ascii_uppercase)]
        if lower == 1:    
            password += [random.choice(string.ascii_lowercase)]
        if numbers == 1:   
            password += [random.choice(string.digits)]
        if others == 1:   
            password += [random.choice(string.punctuation)]
    random.shuffle(password)
    return ''.join(password[:len])

print('TU CONTRASEÑA ES: ' + password(50,1,1,1,1))

