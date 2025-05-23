#!/usr/bin/env python3

import subprocess

RESET = '\033[0m'
RED = '\033[91m'

def main():
    repos = {
        0:'https://github.com/BlackFan/client-side-prototype-pollution.git',
        1:'https://github.com/stealthcopter/deepce.git',
        2:'https://github.com/rebootuser/LinEnum.git',
        3:'https://github.com/PenturaLabs/Linux_Exploit_Suggester',
        4:'https://github.com/ajinabraham/nodejsscan.git',
        5:'https://github.com/swisskyrepo/PayloadsAllTheThings.git',
        6:'https://github.com/synacktiv/php_filter_chain_generator.git',
        7:'https://github.com/pentestmonkey/php-reverse-shell.git',
        8:'https://github.com/PowerShellMafia/PowerSploit.git',
        9:'https://github.com/dwisiswant0/ppfuzz.git',
        10:'https://github.com/itm4n/PrivescCheck.git',
        11:'https://github.com/KathanP19/protoscan.git',
        12:'https://github.com/dw0rsec/revshellgen',
        13:'https://github.com/tomnomnom/waybackurls.git',
        14:'https://github.com/bitsadmin/wesng.git',
        15:'https://github.com/s0md3v/XSStrike.git',
        16:'https://github.com/payloadbox/xss-payload-list.git',
        17:'https://github.com/terjanq/Tiny-XSS-Payloads.git',
        18:'https://github.com/Tib3rius/Turbo-Intruder-Scripts.git',
        19:'https://github.com/projectdiscovery/httpx.git'
        }

    for i in range(len(repos)):
        try:
            subprocess.run('git clone ' + repos[i], shell=True, check=True)
        except Exception as e:
            print(f'{RED}Error: {e}{RESET}')

if __name__ == '__main__':
    main()
