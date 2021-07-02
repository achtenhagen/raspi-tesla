# raspi-tesla
Raspberry Pi energy monitor for Tesla Solar and Powerwall

## Getting Started

### Install OpenSSL (macOS)

If you have not previously installed Xcode and the Xcode command-line tools, run:
```
$ xcode-select --install
```

Next install and link the OpenSSL package:
```
$ brew install openssl
$ brew link openssl --force
```

Add OpenSSL to your PATH (if using ZSH):
```
$ echo 'export PATH="/usr/local/opt/openssl@1.1/bin:$PATH"' >> ~/.zshrc
```

Export the following variables to compile the pycurl package in the next section:
```
$ export LDFLAGS="-L/usr/local/opt/openssl@1.1/lib"
$ export CPPFLAGS="-I/usr/local/opt/openssl@1.1/include"
```

### Install Python dependencies
```
$ pip install -r requirements.txt
```