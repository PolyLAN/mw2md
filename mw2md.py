#!/usr/bin/python

import sys
import os
import datetime

from creole import Parser
from creole.html_emitter import HtmlEmitter

from html2text import html2text

class MW2MD:

    def __init__(self, orig, dest):
        self.orig = self.__check_path(orig)
        self.dest = dest

    def transform(self):
        print("Transforming MediWiki from '%s' to MarkDown syntax..." % self.orig)
        t1 = datetime.datetime.now()
        fin = open(self.orig, "r")
        document = Parser(unicode(fin.read(), 'utf-8', 'ignore')).parse()
        fin.close()
        html = HtmlEmitter(document).emit().encode('utf-8', 'ignore')
        md = html2text(html)
        fout = open(self.dest, "w")
        fout.write(md)
        fout.flush()
        fout.close()
        t2 = datetime.datetime.now()
        time = t2 - t1
        print("MarkDown file saved at '%s' (time required: %s)! Please, check it." % (self.dest, time)) 

    def __check_path(self, path):
        path = os.path.abspath(path)
        if (os.path.exists(path)):
            return path
        else:
            raise ValueError("Cannot access file at '%s'" % path)
 
if __name__=="__main__":
    if (len(sys.argv) == 1):
        print("Input file is required!\n")
        print("Usage: python mw2md.py input [output]")
        sys.exit(-1)

    orig =  sys.argv[1]

    if (len(sys.argv) == 2):
        dest = "%s.md" % sys.argv[1]
    else:
        dest = sys.argv[2]

    mw2md = MW2MD(orig, dest)
    mw2md.transform()

