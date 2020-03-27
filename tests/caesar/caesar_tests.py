import unittest

from ccomet.caesar import Message
from ccomet.caesar import Text


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


class FileEncryptionTest(unittest.TestCase):
    """
    Test file encryption using the caesar cypher.
    """
    # Reset all files:
    to_append = ['Two roads diverged in a yellow wood,\n',
                 'And sorry I could not travel both\n',
                 'And be one traveler, long I stood\n',
                 'And looked down one as far as I could\n',
                 'To where it bent in the undergrowth;\n',
                 'Then took the other, as just as fair,\n',
                 'And having perhaps the better claim,\n'
                 'Because it was grassy and wanted wear;\n'
                 'Though as for that the passing there\n'
                 'Had worn them really about the same,\n']

    unlocked_two = open('./data/unlocked2.txt', 'w')
    for i in to_append:
        unlocked_two.write(i)
    unlocked_two.close()

    unlocked_three = open('./data/unlocked3.txt', 'w')
    for i in to_append:
        unlocked_three.write(i)
    unlocked_three.close()

    unlocked_four = open('./data/unlocked4.txt', 'w')
    for i in to_append:
        unlocked_four.write(i)
    unlocked_four.close()

    unlocked_five = open('./data/unlocked5.txt', 'w')
    for i in to_append:
        unlocked_five.write(i)
    unlocked_five.close()

    unlocked_six = open('./data/unlocked6.txt', 'w')
    for i in to_append:
        unlocked_six.write(i)
    unlocked_six.close()

    def test_with_normal_known_offset_not_encrypt_directly(self):
        data = './data/unlocked1.txt'
        correct_d = ['Vyq"tqcfu"fkxgtigf"kp"c"{gnnqy"yqqf.',
                     'Cpf"uqtt{"K"eqwnf"pqv"vtcxgn"dqvj',
                     'Cpf"dg"qpg"vtcxgngt."nqpi"K"uvqqf',
                     'Cpf"nqqmgf"fqyp"qpg"cu"hct"cu"K"eqwnf',
                     'Vq"yjgtg"kv"dgpv"kp"vjg"wpfgtitqyvj=',
                     'Vjgp"vqqm"vjg"qvjgt."cu"lwuv"cu"hckt.',
                     'Cpf"jcxkpi"rgtjcru"vjg"dgvvgt"encko.',
                     'Dgecwug"kv"ycu"itcuu{"cpf"ycpvgf"ygct=',
                     'Vjqwij"cu"hqt"vjcv"vjg"rcuukpi"vjgtg',
                     'Jcf"yqtp"vjgo"tgcnn{"cdqwv"vjg"ucog.']

        result = Text(data, offset=2)
        self.assertEqual(result.encrypted, correct_d)

    def test_with_normal_known_offset_encrypt_directly(self):
        data = './data/unlocked2.txt'
        Text(data, offset=2, encrypt_directly=True)

        correct_d = ['Vyq"tqcfu"fkxgtigf"kp"c"{gnnqy"yqqf.\n',
                     'Cpf"uqtt{"K"eqwnf"pqv"vtcxgn"dqvj\n',
                     'Cpf"dg"qpg"vtcxgngt."nqpi"K"uvqqf\n',
                     'Cpf"nqqmgf"fqyp"qpg"cu"hct"cu"K"eqwnf\n',
                     'Vq"yjgtg"kv"dgpv"kp"vjg"wpfgtitqyvj=\n',
                     'Vjgp"vqqm"vjg"qvjgt."cu"lwuv"cu"hckt.\n',
                     'Cpf"jcxkpi"rgtjcru"vjg"dgvvgt"encko.\n',
                     'Dgecwug"kv"ycu"itcuu{"cpf"ycpvgf"ygct=\n',
                     'Vjqwij"cu"hqt"vjcv"vjg"rcuukpi"vjgtg\n',
                     'Jcf"yqtp"vjgo"tgcnn{"cdqwv"vjg"ucog.\n']

        test_file = open('./data/unlocked2.txt', 'r')
        self.assertEqual(test_file.readlines(), correct_d)
        test_file.close()

    def test_with_mirror_known_offset_not_encrypt_directly(self):
        data = './data/unlocked1.txt'
        correct_d = ['Two roads diverged in a yellow wood,',
                     'And sorry I could not travel both',
                     'And be one traveler, long I stood',
                     'And looked down one as far as I could',
                     'To where it bent in the undergrowth;',
                     'Then took the other, as just as fair,',
                     'And having perhaps the better claim,',
                     'Because it was grassy and wanted wear;',
                     'Though as for that the passing there',
                     'Had worn them really about the same,']

        result = Text(data, offset=95)
        self.assertEqual(result.encrypted, correct_d)

    def test_with_mirror_known_offset_encrypt_directly(self):
        data = './data/unlocked3.txt'
        Text(data, offset=95, encrypt_directly=True)

        correct_d = ['Two roads diverged in a yellow wood,\n',
                     'And sorry I could not travel both\n',
                     'And be one traveler, long I stood\n',
                     'And looked down one as far as I could\n',
                     'To where it bent in the undergrowth;\n',
                     'Then took the other, as just as fair,\n',
                     'And having perhaps the better claim,\n',
                     'Because it was grassy and wanted wear;\n',
                     'Though as for that the passing there\n',
                     'Had worn them really about the same,\n']

        test_file = open('./data/unlocked3.txt', 'r')
        self.assertEqual(test_file.readlines(), correct_d)
        test_file.close()

    def test_with_large_known_offset_not_encrypt_directly(self):
        data = './data/unlocked1.txt'
        correct_d = ['Y|t%wtfix%in{jwlji%ns%f%~jqqt|%|tti1',
                     'Fsi%xtww~%N%htzqi%sty%ywf{jq%gtym',
                     'Fsi%gj%tsj%ywf{jqjw1%qtsl%N%xytti',
                     'Fsi%qttpji%it|s%tsj%fx%kfw%fx%N%htzqi',
                     'Yt%|mjwj%ny%gjsy%ns%ymj%zsijwlwt|ym@',
                     'Ymjs%yttp%ymj%tymjw1%fx%ozxy%fx%kfnw1',
                     'Fsi%mf{nsl%ujwmfux%ymj%gjyyjw%hqfnr1',
                     'Gjhfzxj%ny%|fx%lwfxx~%fsi%|fsyji%|jfw@',
                     'Ymtzlm%fx%ktw%ymfy%ymj%ufxxnsl%ymjwj',
                     'Mfi%|tws%ymjr%wjfqq~%fgtzy%ymj%xfrj1']

        result = Text(data, offset=100)
        self.assertEqual(result.encrypted, correct_d)

    def test_with_large_known_offset_encrypt_directly(self):
        data = './data/unlocked4.txt'
        Text(data, offset=100, encrypt_directly=True)

        correct_d = ['Y|t%wtfix%in{jwlji%ns%f%~jqqt|%|tti1\n',
                     'Fsi%xtww~%N%htzqi%sty%ywf{jq%gtym\n',
                     'Fsi%gj%tsj%ywf{jqjw1%qtsl%N%xytti\n',
                     'Fsi%qttpji%it|s%tsj%fx%kfw%fx%N%htzqi\n',
                     'Yt%|mjwj%ny%gjsy%ns%ymj%zsijwlwt|ym@\n',
                     'Ymjs%yttp%ymj%tymjw1%fx%ozxy%fx%kfnw1\n',
                     'Fsi%mf{nsl%ujwmfux%ymj%gjyyjw%hqfnr1\n',
                     'Gjhfzxj%ny%|fx%lwfxx~%fsi%|fsyji%|jfw@\n',
                     'Ymtzlm%fx%ktw%ymfy%ymj%ufxxnsl%ymjwj\n',
                     'Mfi%|tws%ymjr%wjfqq~%fgtzy%ymj%xfrj1\n']

        test_file = open('./data/unlocked4.txt', 'r')
        self.assertEqual(test_file.readlines(), correct_d)
        test_file.close()

    def test_with_abnormally_large_known_offset_not_encrypt_directly(self):
        data = './data/unlocked1.txt'
        correct_d = ['^"y*|ykn}*ns!o|qon*sx*k*$ovvy"*"yyn6',
                     'Kxn*}y||$*S*my vn*xy~*~|k!ov*ly~r',
                     'Kxn*lo*yxo*~|k!ovo|6*vyxq*S*}~yyn',
                     'Kxn*vyyuon*ny"x*yxo*k}*pk|*k}*S*my vn',
                     '^y*"ro|o*s~*lox~*sx*~ro* xno|q|y"~rE',
                     '^rox*~yyu*~ro*y~ro|6*k}*t }~*k}*pks|6',
                     'Kxn*rk!sxq*zo|rkz}*~ro*lo~~o|*mvksw6',
                     'Lomk }o*s~*"k}*q|k}}$*kxn*"kx~on*"ok|E',
                     '^ry qr*k}*py|*~rk~*~ro*zk}}sxq*~ro|o',
                     'Rkn*"y|x*~row*|okvv$*kly ~*~ro*}kwo6']

        result = Text(data, offset=5900)
        self.assertEqual(result.encrypted, correct_d)

    def test_with_abnormally_large_known_offset_encrypt_directly(self):
        data = './data/unlocked5.txt'
        Text(data, offset=5900, encrypt_directly=True)

        correct_d = ['^"y*|ykn}*ns!o|qon*sx*k*$ovvy"*"yyn6\n',
                     'Kxn*}y||$*S*my vn*xy~*~|k!ov*ly~r\n',
                     'Kxn*lo*yxo*~|k!ovo|6*vyxq*S*}~yyn\n',
                     'Kxn*vyyuon*ny"x*yxo*k}*pk|*k}*S*my vn\n',
                     '^y*"ro|o*s~*lox~*sx*~ro* xno|q|y"~rE\n',
                     '^rox*~yyu*~ro*y~ro|6*k}*t }~*k}*pks|6\n',
                     'Kxn*rk!sxq*zo|rkz}*~ro*lo~~o|*mvksw6\n',
                     'Lomk }o*s~*"k}*q|k}}$*kxn*"kx~on*"ok|E\n',
                     '^ry qr*k}*py|*~rk~*~ro*zk}}sxq*~ro|o\n',
                     'Rkn*"y|x*~row*|okvv$*kly ~*~ro*}kwo6\n']

        test_file = open('./data/unlocked5.txt', 'r')
        self.assertEqual(test_file.readlines(), correct_d)
        test_file.close()

    def test_with_alphabet_known_offset_not_encrypt_directly(self):
        data = './data/unlocked1.txt'
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        correct_d = ['dGy ByknC nsFoBqon sx k IovvyG Gyyn,',
                     'Kxn CyBBI S myEvn xyD DBkFov lyDr',
                     'Kxn lo yxo DBkFovoB, vyxq S CDyyn',
                     'Kxn vyyuon nyGx yxo kC pkB kC S myEvn',
                     'dy GroBo sD loxD sx Dro ExnoBqByGDr;',
                     'drox Dyyu Dro yDroB, kC tECD kC pksB,',
                     'Kxn rkFsxq zoBrkzC Dro loDDoB mvksw,',
                     'LomkECo sD GkC qBkCCI kxn GkxDon GokB;',
                     'dryEqr kC pyB DrkD Dro zkCCsxq DroBo',
                     'Rkn GyBx Drow BokvvI klyED Dro Ckwo,']

        result = Text(data, offset=10, alphabet=alphabet)
        self.assertEqual(result.encrypted, correct_d)

    def test_with_alphabet_known_offset_encrypt_directly(self):
        data = './data/unlocked6.txt'
        alphabet = [i for i in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        Text(data, offset=10, encrypt_directly=True, alphabet=alphabet)

        correct_d = ['dGy ByknC nsFoBqon sx k IovvyG Gyyn,\n',
                     'Kxn CyBBI S myEvn xyD DBkFov lyDr\n',
                     'Kxn lo yxo DBkFovoB, vyxq S CDyyn\n',
                     'Kxn vyyuon nyGx yxo kC pkB kC S myEvn\n',
                     'dy GroBo sD loxD sx Dro ExnoBqByGDr;\n',
                     'drox Dyyu Dro yDroB, kC tECD kC pksB,\n',
                     'Kxn rkFsxq zoBrkzC Dro loDDoB mvksw,\n',
                     'LomkECo sD GkC qBkCCI kxn GkxDon GokB;\n',
                     'dryEqr kC pyB DrkD Dro zkCCsxq DroBo\n',
                     'Rkn GyBx Drow BokvvI klyED Dro Ckwo,\n']

        test_file = open('./data/unlocked6.txt', 'r')
        self.assertEqual(test_file.readlines(), correct_d)
        test_file.close()

if __name__ == '__main__':
    unittest.main()
