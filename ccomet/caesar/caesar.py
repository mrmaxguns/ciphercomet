# caesar.py

# Import important modules
import random


class Message:
    def __init__(self, message_string, offset=None, alphabet=None, enc=False, dec=False, brute_force=False):
        """
        The class Message deals with encoding, decoding, and brute force attacks on messages in the form of python
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

        :param brute_force: A boolean statement that, if true enables brute force mode.
        """

        # Set self.message to the message to the message string
        self.message = message_string

        # Check what alphabet is, if none, set it as the default ASCII list of characters
        if alphabet is None:
            self.alphabet = [chr(i) for i in range(32, 127)]
        else:
            self.alphabet = alphabet

        # Check what the offset is, if none, set it as a random integer from 1 to the length of the alphabet
        if offset is None:
            self.offset = random.randint(1, len(self.alphabet))
        else:
            self.offset = offset

        # Set mode to encryption or decryption based on enc and dec. If both are true or false, set to encryption
        if enc is True and dec is False:
            self.mode = 'encryption'
        elif enc is False and dec is True:
            self.mode = 'decryption'
        else:
            self.mode = 'encryption'

        # Basic encryption/decryption function
        def crypt(message_, alphabet_, offset_, mode_):
            encrypted_list = []
            for i in message_:
                # For encryption:
                if i in alphabet_ and mode_ == 'e':
                    new_char = (alphabet_.index(i) + offset_) % len(alphabet_)
                    encrypted_list.append(alphabet_[new_char])
                # For decryption:
                elif i in alphabet_ and mode_ == 'd':
                    new_char = (alphabet_.index(i) - offset_) % len(alphabet_)
                    encrypted_list.append(alphabet_[new_char])
                # For exceptions:
                else:
                    encrypted_list.append(i)

            # Return the joined list as a string
            return ''.join(encrypted_list)

        # Set variable to all of the decryption combinations:
        self.all = []
        for i, j in enumerate(range(len(self.alphabet))):
            self.all.append(crypt(self.message, self.alphabet, self.offset + j, 'd'))

        # Encrypt the message
        if self.mode == 'encryption' and not brute_force:
            self.encrypted = crypt(self.message, self.alphabet, self.offset, 'e')
            self.decrypted = None

        # Decrypt the message
        elif self.mode == 'decryption' and not brute_force:
            self.decrypted = crypt(self.message, self.alphabet, self.offset, 'd')
            self.encrypted = None

        # Brute Force
        elif brute_force is True:
            letter_frequencies = {
                'a': 0.08167,
                'b': 0.01492,
                'c': 0.02202,
                'd': 0.04253,
                'e': 0.12702,
                'f': 0.02228,
                'g': 0.02015,
                'h': 0.06094,
                'i': 0.06966,
                'j': 0.00153,
                'k': 0.01292,
                'l': 0.04025,
                'm': 0.02406,
                'n': 0.06749,
                'o': 0.07507,
                'p': 0.01929,
                'q': 0.00095,
                'r': 0.05987,
                's': 0.06327,
                't': 0.09356,
                'u': 0.02758,
                'v': 0.00978,
                'w': 0.02560,
                'x': 0.00150,
                'y': 0.01994,
                'z': 0.00077
            }


class Text:
    def __init__(self, text_file_path, offset=None, alphabet=None, enc=False, dec=False, brute_force=False):
        # Open and read the file
        self.file = open(text_file_path, 'r')
        self.lines_u = self.file.readlines()

        # strip trailing newlines
        self.lines = [i.rstrip() for i in self.lines_u]

        # store basic info for easy access
        self.path = text_file_path
        self.offset = offset
        self.alphabet = alphabet
        self.enc = enc
        self.dec = dec
        self.brute_force = brute_force

        # Define encrypted and decrypted lists
        self.encrypted = []
        self.decrypted = []

        # Add each converted line to the new lists
        for i in self.lines:
            m = Message(i, offset, alphabet, enc, dec, brute_force)
            self.encrypted.append(m.encrypted)
            self.decrypted.append(m.decrypted)

