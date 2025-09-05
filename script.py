import requests   # husk 'pip install requests'


res = requests.get('https://www.ek.dk')
print( res.status_code )

f = open('index.html', 'w')
f.write(res.text)


css = requests.get('https://www.ek.dk/dist/css/fontawesome.CHUeQN7T.css')

f = open('stylesheet.css', 'w')
f.write(css.text)




























"""
import subprocess as sp

sp.run(['git', 'pull', 'origin', 'master' ])
"""
## jeg vil gerne læse filer fra mit filsystem
"""
import os

#print( os.mkdir('TEST')    )
os.chdir('TEST')
print( os.getcwd()     )
f = open('testfil.txt', 'w')
os.chdir('..')
print( os.getcwd()     )

os.chdir('TEST')
os.remove('testfil.txt')
"""
















"""
# import data
from data import name as xxx

print(xxx)


"""
