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
    print(" \033[1;31m   Connect Vpn if Run Error!\033[1;37m")
    from ALEX import Sub
    Sub()
elif bit == '32bit':
    print("\x1b[1;91mOpps Sorry Brother Your Mobile Not Support This Tools")