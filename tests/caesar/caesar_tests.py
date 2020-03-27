import unittest

from ccomet.caesar import Message


class EncryptionTest(unittest.TestCase):
    """
    Test encryption using the caesar cypher.
    """

    def test_with_normal_known_offset(self):
        data = 'Hello, World!'
        result = Message(data, 2)
        self.assertEqual(result.encrypted, 'Jgnnq."Yqtnf#')

    def test_with_mirror_known_offset(self):
        data = 'Pack my box with five dozen liquor jugs!'
        result = Message(data, 95)
        self.assertEqual(result.encrypted, 'Pack my box with five dozen liquor jugs!')

    def test_with_large_known_offset(self):
        data = 'Pack my box with five dozen liquor jugs!'
        result = Message(data, 96)
        self.assertEqual(result.encrypted, 'Qbdl!nz!cpy!xjui!gjwf!ep{fo!mjrvps!kvht"')

    def test_with_abnormally_large_known_offset(self):
        data = 'Pack my box with five dozen liquor jugs!'
        result = Message(data, 9800)
        self.assertEqual(result.encrypted, '_prz/|)/q~(/\'x$w/ux&t/s~*t}/{x!%~"/y%v#0')

    def test_with_alphabet_known_offset(self):
        data = 'Pack my box with five dozen liquor jugs!'
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        result = Message(data, 3, alphabet=alphabet)
        self.assertEqual(result.encrypted, 'Sdfn pB erA zlwk ilyh grChq oltxru mxjv!')


class DecryptionTest(unittest.TestCase):
    """
    Test decryption using the caesar cypher
    """
    def test_with_normal_known_offset(self):
        data = 'Jgnnq."Yqtnf#'
        result = Message(data, 2, dec=True)
        self.assertEqual(result.decrypted, 'Hello, World!')

    def test_with_mirror_known_offset(self):
        data = 'Pack my box with five dozen liquor jugs!'
        result = Message(data, 95, dec=True)
        self.assertEqual(result.decrypted, 'Pack my box with five dozen liquor jugs!')

    def test_with_large_known_offset(self):
        data = 'Qbdl!nz!cpy!xjui!gjwf!ep{fo!mjrvps!kvht"'
        result = Message(data, 96, dec=True)
        self.assertEqual(result.decrypted, 'Pack my box with five dozen liquor jugs!')

    def test_with_abnormally_large_known_offset(self):
        data = '_prz/|)/q~(/\'x$w/ux&t/s~*t}/{x!%~"/y%v#0'
        result = Message(data, 9800, dec=True)
        self.assertEqual(result.decrypted, 'Pack my box with five dozen liquor jugs!')

    def test_with_alphabet_known_offset(self):
        data = 'Sdfn pB erA zlwk ilyh grChq oltxru mxjv!'
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        result = Message(data, 3, alphabet=alphabet, dec=True)
        self.assertEqual(result.decrypted, 'Pack my box with five dozen liquor jugs!')


if __name__ == '__main__':
    unittest.main()
