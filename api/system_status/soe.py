import pycurl
from modules.config import load_config


def get_state_of_energy(config):
    gateway = config['gateway']
    headers = [
        'Accept: application/json',
        f"Accept-Language: {config['lang']}",
        'Content-Type: application/json'
    ]

    crl = pycurl.Curl()
    crl.setopt(crl.VERBOSE, True)
    crl.setopt(crl.INTERFACE, gateway['interface'])
    crl.setopt(crl.URL, f"https://{gateway['ip_addr']}/api/system_status/soe")
    crl.setopt(crl.COOKIEFILE, 'cookie.txt')
    crl.setopt(crl.COOKIEJAR, 'cookie.txt')
    crl.setopt(crl.SSL_VERIFYPEER, False)
    crl.setopt(crl.SSL_VERIFYHOST, False)
    crl.setopt(crl.HTTPHEADER, headers)
    crl.setopt(crl.USERAGENT, crl.version)
    crl.perform()
    crl.close()


def main():
    config = load_config('gateway.toml')
    get_state_of_energy(config)


if __name__ == "__main__":
    main()
