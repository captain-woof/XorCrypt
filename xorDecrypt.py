from argparse import ArgumentParser

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
parser.add_argument("--key","-k",type=str,action="store",required=True,help="Key to use while xor-decrypting")
byte_source = parser.add_mutually_exclusive_group()
byte_source.add_argument("--file",'-f',type=str,action='store',help='File to decrypt contents of')
byte_source.add_argument("--text",'-t',type=str,action='store',help='Text to decrypt')
parser.add_argument("--output",'-o',type=str,action='store',required=False,help="Output file containing decrypted data")
parser.add_argument("--no-result-display",'-n',action='store_true',help='Turn off result display; default: not set')
args = parser.parse_args()

byteKey = TextToBytes(args.key)
output = args.output
bytesToDecrypt = None
if args.file:
    try:
        with open(args.file,'rb') as f:
            bytesToDecrypt = f.read()
    except:
        print("Error reading from '{0}'".format(args.file))
        exit(0)
elif args.text:
    bytesToDecrypt = TextToBytes(args.text)
else:
    parser.print_help()
    exit()

# Xor algo
print("Decrypting...")
decryptedData = []
for i in range(0,len(bytesToDecrypt)):
    decryptedData.append(bytesToDecrypt[i] ^ (byteKey[i % len(byteKey)]))
decryptedData = bytes(decryptedData)
if output:
    with open(output,'wb+') as f:
        f.write(decryptedData)
    print("{0} bytes xor-decrypted data written to '{1}'".format(len(decryptedData),output))

print("Provided key: {0}".format(args.key))
if not args.no_result_display:
    try:
        print("Decrypted data: ",end="")
        resultToShow = BytesToText(decryptedData)
        if resultToShow is not None:
            print(resultToShow)
        else:
            raise Exception
    except UnicodeDecodeError:
        print("FAILED TO DECODE (unprintable characters)")