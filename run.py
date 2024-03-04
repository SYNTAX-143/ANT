import os, sys, platform
os.system('clear')
try:os.system('clear')
except:pass
try:os.system('clear')
except:pass
try:os.system('git pull')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    os.system('clear')
    os.system('chmod 777 ANT && ./ANT')
elif bit == '32bit':
    exit("\x1b[1;91mSORRY BRO 32 BIT NOT SUPPORTED\x1b[1;97m")
