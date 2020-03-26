# caesar.py
import random

class message:
    def __init__(self, message_string, offset=random.randint(1, 95), alphabet=[chr(i) for i in range(32, 127)]):
        self.message = message_string
        self.offset = offset
        self.alphabet = alphabet


m = message('hi', 5)
print(m.message+'\n'+str(m.offset))
print(m.alphabet)
