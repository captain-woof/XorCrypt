# XorCrypt
Utility scripts written in Python3 that help you **xor-encrypt/xor-decrypt data with your chosen key.**

*For the Powershell version, head over to my other repo 'PowerWoof' and check under 'Tools'.*

### XorEncrypt

```
usage: xorEncrypt.py [-h] [--key KEY] [--file FILE | --text TEXT]
                     [--output OUTPUT] [--no-result-display]

optional arguments:
  -h, --help            show this help message and exit
  --key KEY, -k KEY     Key to use while xor-encrypting; default: randomly
                        generated string of length between 20 and 30 (will be
                        shown)
  --file FILE, -f FILE  File to encrypt contents of
  --text TEXT, -t TEXT  Text to encrypt
  --output OUTPUT, -o OUTPUT
                        Output file containing encrypted data
  --no-result-display, -n
                        Turn off result display; default: not set
```

### XorDecrypt

```
usage: xorDecrypt.py [-h] [--key KEY] [--file FILE | --text TEXT]
                     [--output OUTPUT] [--no-result-display]

optional arguments:
  -h, --help            show this help message and exit
  --key KEY, -k KEY     Key to use while xor-decrypting
  --file FILE, -f FILE  File to decrypt contents of
  --text TEXT, -t TEXT  Text to decrypt
  --output OUTPUT, -o OUTPUT
                        Output file containing decrypted data
  --no-result-display, -n
                        Turn off result display; default: not set
```