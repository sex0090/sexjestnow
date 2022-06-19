import os, platform, time
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
bit = platform.architecture()[0]
if bit == '64bit':
    print("\n\x1b[1;92m Congratulations ! Your Device Support Tolls")
    print("""\n
  \033[1;92m███╗   ███╗██████╗ ███████╗ 
  \033[1;92m████╗ ████║██╔══██╗╚══███╔╝ 
  \033[1;92m██╔████╔██║██████╔╝  ███╔╝ 
  \033[1;92m██║╚██╔╝██║██╔══██╗ ███╔╝ 
  \033[1;92m██║ ╚═╝ ██║██║  ██║███████╗ 
  \033[1;92m╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝ 
  
 
 \33[1;92m█▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█
\33[1;92m█  \33[mGithub: https://github.com/\33[1;92mBD-MRZ-KING
\33[1;92m█  \33[mFacebook: \33[1;92mRehaan Shekh
   Facebook: Md.Zakirul Islam
   Fb Group: BD CYBER ZONE (BCZ)
\33[1;92m█  \33[mWhatsApp: \33[1;92m+13346549239
\33[1;92m█  \33[mTools : \33[1;92mPAID
\33[1;92m█▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█
""")

def reg():
    os.system('clear')
    try:
        to = open('/sdcard/.hst.txt', 'r').read()
    except (KeyError, IOError):
        reg2()

    r = requests.get('https://raw.githubusercontent.com/ahmad77412/axi/main/server.txt').text
    if to in r:
        os.system('cd zzzzz && npm install')
        os.system('fuser -k 5000/tcp &')
        os.system('#')
        os.system('cd zzzzz && node index.js &')
        time.sleep(5)
        ip()
    else:
        os.system('clear')
        print logo
        print '\tApproved Failed'
        print ' \x1b[1;92mYour Id Is Not Approved Already '
        print ' \x1b[1;92mCopy token id and send to Owner'
        print ' \x1b[1;92mYour id: ' + to
        raw_input('\x1b[1;93m Press enter to send id')
        os.system('xdg-open https://wa.me/+923458630524')
        reg()


def reg2():
    os.system('clear')
    print logo
    print '\tApproval not detected'
    print ' \x1b[1;92mCopy and press enter , And Send Me'
    id = uuid.uuid4().hex[:50]
    print ' Your id: ' + id
    print ''
    raw_input(' Press enter to go to whatsapp ')
    os.system('xdg-open https://wa.me/+923458630524')
    sav = open('/sdcard/.hst.txt', 'w')
    sav.write(id)
    sav.close()
    raw_input('\x1b[1;92m Press enter to check Approval ')
    reg()


    print(" \033[1;31m   Connect Vpn if Run Error!\033[1;37m")
    from ALEX import Sub
    Sub()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")