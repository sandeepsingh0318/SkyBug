
import random
import string
print(" Welcome my Password Generater")
def sandeep():
    length = int(input(" Enter a length of password"))
    char = string.ascii_letters+string.ascii_lowercase+string.ascii_uppercase+string.digits+string.punctuation
    P_W = random.sample(char,length)
    my_PW = " ".join(P_W)
    print(my_PW)
    sandeep()
sandeep()