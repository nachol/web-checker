#!/usr/bin/env python

import sys
import requests
import urllib3
import argparse
from lxml.html import fromstring

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

protocols={
    'http',
    # 'https'
}

def get_title(html):
    try:
        tree = fromstring(html.content)
        return tree.findtext('.//title').rstrip()
    except Exception as e:
        return "none"

def check_domain(domain):
    print('[-] Checking Domain: ' + domain)

    for prot in protocols:
        test_url=prot+'://' + domain
        try:
            r = requests.get(url=test_url, allow_redirects=True, verify=False, timeout=10)
            hosts_vivos=open("Live.txt","a")
            hosts_vivos.write(prot+"\t"+domain+"\t"+str(r.status_code)+"\t"+str(get_title(r))+"\n")
            hosts_vivos.close()
        except requests.exceptions.RequestException as e:
            hosts_muertos=open("Dead.txt","a")
            hosts_muertos.write(prot+"\t"+domain+"\t"+str(e)+"\n")
            hosts_muertos.close()

def main():
    parser = argparse.ArgumentParser(description='Checks if a domian is live by requesting the page.')
    parser.add_argument('path', metavar='file', type=str, nargs='?',help='path to domain list. Do not include HTTP:// or HTTPS://')
    args = parser.parse_args()

    print('Defined Protocols: ')
    for p in protocols:
        print('- '+p)

    with open(args.path, 'r') as my_file:
        for domain in my_file:
            check_domain(domain.rstrip())

if __name__ == "__main__":
    main()