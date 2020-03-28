# alberti_disk.py

# Import important modules
import random


class Message:
    def __init__(self, message, initial_shift=0, periodic_increment=1, periodic_length=3, direction='clockwise',
                 enc=False, dec=False, infer=False, outer_alphabet=None, inner_alphabet=None, rotation_ring='outer'):

        # Set outer_alphabet to the standard alphabet if None
        if outer_alphabet is None:
            self.outer_alphabet = [i for i in 'ABCDEFGILMNOPQRSTVXZ1234']
        else:
            self.outer_alphabet = outer_alphabet

        # Set inner_alphabet to the standard alphabet if None
        if inner_alphabet is None:
            self.inner_alphabet = [i for i in 'gklnprtuz&xysomqihfdbace']
        else:
            self.inner_alphabet = inner_alphabet

        # Check to see if each item in each of the lists only has one character
        for i in self.outer_alphabet:
            if len(i) != 1:
                raise Exception('Each item in the list outer_alphabet must only have one character')
        for i in self.inner_alphabet:
            if len(i) != 1:
                raise Exception('Each item in the list inner_alphabet must only have one character')

        # Check to see the lengths of the outer and inner alphabets match
        if len(self.outer_alphabet) != len(self.inner_alphabet):
            raise Exception('Outer alphabet and inner alphabet must contain the same amount of characters')

        for i in self.outer_alphabet:
            if self.outer_alphabet.count(i) > 1:
                raise Exception('Outer alphabet has duplicate characters')
        for i in self.inner_alphabet:
            if self.inner_alphabet.count(i) > 1:
                raise Exception('Inner alphabet has duplicate characters')

        # Check if a valid direction was passed
        if direction != 'clockwise' and direction != 'counterclockwise':
            raise Exception('Invalid direction: %s' % direction)

        # Check if encryption or decryption
        if not dec and enc:
            self.mode = 'encryption'
        elif not enc and dec:
            self.mode = 'decryption'
        else:
            self.mode = 'encryption'

        # Define some important variables
        self.message = message
        self.initial_shift = initial_shift
        self.periodic_increment = periodic_increment
        self.periodic_length = periodic_length
        self.direction = direction
        self.infer = infer
        self.dec = dec
        self.enc = enc
        self.rotation_ring = rotation_ring
        self.ring_length = len(self.outer_alphabet)

        if self.rotation_ring == 'outer' and self.direction == 'clockwise':
            add_to_index = True
        elif self.rotation_ring == 'inner' and self.direction == 'counterclockwise':
            add_to_index = True
        else:
            add_to_index = False