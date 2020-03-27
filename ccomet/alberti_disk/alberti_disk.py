# alberti_disk.py

# Import important modules
import random


class Message:
    def __init__(self, message, initial_shift=0, periodic_increment=1, periodic_length=3, direction='clockwise',
                 enc=False, dec=False, brute_force=False, outer_alphabet=None, inner_alphabet=None):

        if outer_alphabet is None:
            self.outer_alphabet = [i for i in 'ABCDEFGILMNOPQRSTVXZ1234']
        else:
            self.outer_alphabet = outer_alphabet

        if inner_alphabet is None:
            self.inner_alphabet = [i for i in 'gklnprtuz&xysomqihfdbace']
        else:
            self.inner_alphabet = inner_alphabet

        for i in self.outer_alphabet:
            if len(i) != 1:
                raise Exception('Each item in the list outer_alphabet must only have one character')
        for i in self.inner_alphabet:
            if len(i) != 1:
                raise Exception('Each item in the list inner_alphabet must only have one character')

        if len(self.outer_alphabet) != len(self.inner_alphabet):
            raise Exception('Outer alphabet and inner alphabet must contain the same amount of characters')

        for i in self.outer_alphabet:
            if self.outer_alphabet.count(i) > 1:
                raise Exception('Outer alphabet has duplicate characters')
        for i in self.inner_alphabet:
            if self.inner_alphabet.count(i) > 1:
                raise Exception('Inner alphabet has duplicate characters')

        if direction != 'clockwise' or direction != 'counterclockwise':
            raise Exception('Invalid direction: %s' % direction)

        if not dec and enc:
            self.enc = True
        elif not enc and dec:
            self.dec = True
        else:
            self.enc = True

        self.message = message
        self.initial_shift = initial_shift
        self.periodic_increment = periodic_increment
        self.periodic_length = periodic_length
        self.direction = direction
        self.brute_force = brute_force
