# Web Checker
Simple Script in python that checks if a domain is live or not by requesting it.
It can be set up the protocol (http, https) in the variable "protocols".

```
└──> python main.py -h
usage: main.py [-h] [file]

Checks if a domian is live by requesting the page.

positional arguments:
  file        path to domain list. Do not include HTTP:// or HTTPS://

optional arguments:
  -h, --help  show this help message and exit
```

The output is separated in 2 files. Live or Dead.

Live file format:

PROTOCOL	DOMAIN	RESPONSE_CODE

Dead File format:

PROTOCOL	DOMAIN	ERROR_MESSAGE