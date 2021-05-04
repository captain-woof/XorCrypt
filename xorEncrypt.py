from argparse import ArgumentParser
import random
from string import ascii_letters,digits

def MakeRandomStr():
    length = random.randint(20,30)
    charset = list(ascii_letters + digits)
    random_str = ""
    for _ in range(0,length):
        random_str += random.choice(charset)
    return random_str

def TextToBytes(text):
    return bytes(list(map(ord,text)))

def BytesToText(bytearrayy):
    try:
        s = "".join(list(map(chr,bytearrayy)))
    except:
        s = None
    finally:
        return s

# DRIVER CODE
parser = ArgumentParser()
parser.add_argument("--key","-k",type=str,action="store",default=MakeRandomStr(),required=False,help="Key to use while xor-encrypting; default: randomly generated string of length between 20 and 30 (will be shown)")
byte_source = parser.add_mutually_exclusive_group()
byte_source.add_argument("--file",'-f',type=str,action='store',help='File to encrypt contents of')
byte_source.add_argument("--text",'-t',type=str,action='store',help='Text to encrypt')
parser.add_argument("--output",'-o',type=str,action='store',required=False,help="Output file containing encrypted data")
parser.add_argument("--no-result-display",'-n',action='store_true',help='Turn off result display; default: not set')
args = parser.parse_args()

byteKey = TextToBytes(args.key)
output = args.output
bytesToEncrypt = None
if args.file:
    try:
        with open(args.file,'rb') as f:
            bytesToEncrypt = f.read()
    except:
        print("Error reading from '{0}'".format(args.file))
        exit(0)
elif args.text:
    bytesToEncrypt = TextToBytes(args.text)
else:
    parser.print_help()
    exit()

# Xor algo
print("Encrypting...")
encryptedData = []
for i in range(0,len(bytesToEncrypt)):
    encryptedData.append((bytesToEncrypt[i] ^ (byteKey[i % len(byteKey)])))
encryptedData = bytes(encryptedData)
if output:
    with open(output,'wb+') as f:
        f.write(encryptedData)
    print("{0} bytes xor-encrypted data written to '{1}'".format(len(encryptedData),output))

print("Chosen key: {0}".format(args.key))

if not args.no_result_display:
    try:
        print("Encrypted data: ",end="")
        resultToShow = BytesToText(encryptedData)
        if resultToShow is not None:
            print(resultToShow)
        else:
            raise Exception
    except Exception:
        print("FAILED TO DECODE (unprintable characters)")