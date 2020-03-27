# caesar.py
import random

class message:
    def __init__(self, message_string, offset=None, alphabet=None, enc=False, dec=False):
        '''
        The class message deals with encoding, decoding, and brute force attacks on messages in the form of python
        strings.

        Uses the caesar cypher method to take the message_string and shift the characters in the string by the passed
        offset to either encrypt or decrypt the said string.

        :param message_string: the string to encrypt/decrypt (in the form of a python string) This string can contain
        any characters. Those that are not processed will remain the same.

        :param offset: Offset is an integer that represents the amount of spaces to shift the image on the alphabet. For
        example with an offset of 1 and the standard english alphabet A would be B, B would be C and so on.

        :param alphabet: Alphabet is passed in the form of a list, the alphabet the caesar cypher will use to know how
        to shift the letters in the message.

        :param enc: A boolean statement that says to encrypt the message.

        :param dec: A boolean statement that says to decrypt the message.
        '''

        # Set self.message to the message to the message string
        self.message = message_string

        # Check what the offset is, if none, set it as a random integer from 1 to 95
        if offset is None:
            self.offset = random.randint(1, 95)
        else:
            self.offset = offset

        # Check what alphabet is, if none, set it as the default ASCII list of characters
        if alphabet is None:
            self.alphabet = [chr(i) for i in range(32, 127)]
        else:
            self.alphabet = alphabet

        # Set mode to encryption or decryption based on enc and dec. If both are true or false, set to encryption
        if enc is True and dec is False:
            self.mode = 'encryption'
        elif enc is False and dec is True:
            self.mode = 'decryption'
        else:
            self.mode = 'encryption'
