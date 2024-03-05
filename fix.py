import os
os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/http')
os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/urllib3')
os.system('rm -rf /data/data/com.termux/files/usr/lib/python3.11/site-packages/requests')
os.system('pkg uninstall python -y;pkg install python -y;pip uninstall requests  rich mechanize future bs4 cython chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system('clear')
print("MAYBE FIXED RUN TOOLS AGAIN")
