import argparse

# Create the parser
my_parser = argparse.ArgumentParser(prog='ccomet',
                                    description='Encrypt text and files using the alberti disk and caesar cipher',
                                    epilog='I hope you enjoy this program.\nFor more visit:'
                                           ' https://github.com/mrmaxguns/')

# Define parameters
my_parser.add_argument('message',
                       help='The message or file path of the text file you want to encrypt/decrypt')

my_parser.add_argument('cipher',
                       help='The cipher used (caesar or alberti)')

my_parser.add_argument('--encode',
                       help='set this if you want to encode the message',
                       action='store_true')

my_parser.add_argument('--decode',
                       help='set this if you want to decode the message',
                       action='store_true')

my_parser.add_argument('--infer',
                       help='set this if you want the program to use letter frequencies to decipher the code without'
                            ' and offset (EXPERIMENTAL)',
                       action='store_true')

my_parser.add_argument('-offset',
                       help='CAESAR ONLY: The offset is used in the caesar cipher to determine the letter shift (an '
                            'offset of one would turn a to b',
                       type=int)

my_parser.add_argument('-alphabet',
                       help='CAESAR ONLY: The alphabet is used as the guide to how to correctly shift the letters. If '
                            'this parameter is unused, the default alphabet will be used',
                       type=list)

my_parser.add_argument('-initial_shift',
                       help='ALBERTI ONLY: the position of the inner disk to the outer disk',
                       type=int)

my_parser.add_argument('-periodic_increment',
                       help='ALBERTI ONLY: the number of letters to decode before shifting the wheel by the periodic '
                            'length',
                       type=int)

my_parser.add_argument('-direction',
                       help='ALBERTI ONLY: the direction to turn the virtual alberti disc (clockwise/counterclockwise)')

my_parser.add_argument('-outer_alphabet',
                       help='Just separate all characters in the outer disc with a space. For example: -outer_alphabet '
                            'a b c',
                       nargs='*')

my_parser.add_argument('-inner_alphabet',
                       help='Just separate all characters in the inner disc with a space. For example: -innerer_alphabet'
                            ' a b c',
                       nargs='*')

my_parser.add_argument('-rotation_ring',
                       help='ALBERTI ONLY: The ring that is being turned (inner or outer)')

# Activate parser and get args
args = my_parser.parse_args()
