"""
HTML
Hypertext Markup Language is a standard markup language used for creating World Wide Web pages.

Parsing
Parsing is the process of syntactic analysis of a string of symbols. 
It involves resolving a string into its component parts and describing their syntactic roles.

HTMLParser
An HTMLParser instance is fed HTML data and calls handler methods when start tags, end tags, 
text, comments, and other markup elements are encountered.
"""

# Enter your code here. Read input from STDIN. Print output to STDOUT

from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Start :", tag)
        for attribute in attrs:
            print("->", attribute[0], ">", attribute[1])

    def handle_endtag(self, tag):
        print("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print("Empty :", tag)
        for attribute in attrs:
            print("->", attribute[0], ">", attribute[1])


if __name__ == "__main__":
    parser = MyHTMLParser()

    for _ in range(int(input())):
        parser.feed(input())
