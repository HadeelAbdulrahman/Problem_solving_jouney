import random
import string
s="randoms"
chars= string.ascii_letters+string.digits
s_list = list(s)
random.shuffle(s_list)
shuffled_s = ''.join(s_list)
t= shuffled_s+ random.choice(chars)

for i in t:
    if i in s:
        pass
    else:
        print(f"New letter is {i}")
