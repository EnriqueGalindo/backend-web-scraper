#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Module docstring: Grabs the email, phone numbers, urls, and  off a website.

This displays the email addresses and phone numbers found on a website imputed
by the user. They are displayed in a single column using pretty print. The main
issue is that the phone numbers
"""
__author__ = "Enrique Galindo"

# Imports go at the top of your file, after the module docstring.
# One module per import line. These are for example only.
import sys
import requests
import re
import pprint
from html.parser import HTMLParser
regex_email = r'''(?:[a-z0-9!#$%&‘*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&‘*+/=?^_`{|}~-]+)*|“(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*“)@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])'''
regex_phone = r'''(1?\W*([2-9][0-8][0-9])\W*([2-9][0-9]{2})\W*([0-9]{4})(\se?x?t?(\d*))?)'''

class MyHTMLParser(HTMLParser):
    a_list = []
    src_list = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and "http://":
            for attr, value in attrs:
                if attr == 'href':
                    self.a_list.append(value)
                if attr == 'src':
                    self.src_list.append(value)


def main(args):
    """Main function is declared as standalone, for testability"""
    good_phone_list = []
    url = args[0]
    response = requests.get(url)
    response.raise_for_status()
    url_list = re.findall(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', response.text)
    email_list = set(re.findall(regex_email, response.text))
    bad_phone_list = set(re.findall(regex_phone, response.text))
    for number in bad_phone_list:
        good_phone_list.append(number[1] + number[2] + number[3])
    print(email_list)
    pprint.pprint(good_phone_list)
    parser =  MyHTMLParser()
    parser.feed(response.text)
    pprint.pprint(parser.a_list)
    pprint.pprint(parser.src_list)


    
if __name__ == '__main__':
    """Docstring goes here"""
    main(sys.argv[1:])