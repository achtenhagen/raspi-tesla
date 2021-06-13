import json

import pycurl
from modules.config import load_config


def do_login(config):
    gateway = config['gateway']
    login = config['gateway']['login']
    headers = [
        'Accept: application/json',
        f"Accept-Language: {config['lang']}",
        'Content-Type: application/json'
    ]

    crl = pycurl.Curl()
    crl.setopt(crl.VERBOSE, True)
    crl.setopt(crl.INTERFACE, gateway['interface'])
    crl.setopt(crl.URL, f"https://{gateway['ip_addr']}/api/login/Basic")
    crl.setopt(crl.COOKIEJAR, 'cookie.txt')
    crl.setopt(crl.SSL_VERIFYPEER, False)
    crl.setopt(crl.SSL_VERIFYHOST, False)
    crl.setopt(crl.HTTPHEADER, headers)
    crl.setopt(crl.USERAGENT, crl.version)

    data = {
        'email': login['email_addr'],
        'password': login['passwd'],
        'username': login['username']
    }

    crl.setopt(crl.POSTFIELDS, json.dumps(data))
    crl.perform()
    crl.close()


def main():
    config = load_config('gateway.toml')
    do_login(config)


if __name__ == "__main__":
    main()
