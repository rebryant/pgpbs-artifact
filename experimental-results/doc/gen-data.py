#!/usr/bin/python
import sys
import getopt

#####################################################################################
# Copyright (c) 2021 Marijn Heule, Randal E. Bryant, Carnegie Mellon University
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and
# associated documentation files (the "Software"), to deal in the Software without restriction,
# including without limitation the rights to use, copy, modify, merge, publish, distribute,
# sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all copies or
# substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT
# OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
########################################################################################

# Input is CSV file with entries x,y.
# 05/19/2021 ... Allow entries of the form x,y1,y2,...,yN
# Default is to use column N as value of y, but this can be changed as an option

# Output is line like the following
#          \addplot coordinates {(4, 900) (8, 8320) (9, 39628) (11, 252970) (12, 1324539) (13, 4095084) (14, 7131764) (15, 15225960)};

# Threshold value.  Don't include data with Y values exceeding this value
yThresh = 1000 * 1000 * 1000
xThresh = 1000 * 1000
yColumn = -1
optionString = ""

def usage(name):
    print("Usage: %s [-h] [-x XTHRESH] [-y YTHRESH] < file.csv > file.tex")
    print(" -h         Print this message")
    print(" -x XTHRESH Set maximum X value included")
    print(" -Y YCOL    Set column number to use as Y value")
    print(" -y YTHRESH Set maximum Y value included")
    print(" -O OSTRING Specify addplot options (usually quoted string)")

def trim(s):
    while len(s) > 0 and s[-1] == '\n':
        s = s[:-1]
    return s

def gen(infile, outfile):
    outfile.write("\\addplot %s coordinates {" % optionString)
    for line in infile:
        line = trim(line)
        fields = line.split(",")
        if len(fields) >= 2:
            try:
                fx = float(fields[0])
                if fx > float(xThresh):
                    continue
            except:
                pass
            try:
                fy = float(fields[yColumn])
                if fy < 0.0 or fy > float(yThresh):
                    continue
            except:
                pass
            outfile.write(" (%s,%s)" % (fields[0], fields[yColumn]))
    outfile.write("};\n")
        
def run(name, args):
    global xThresh, yThresh, yColumn, optionString
    optlist, args = getopt.getopt(args, "hx:y:Y:O:")
    for (opt, val) in optlist:
        if opt == '-h':
            usage(name)
            return
        elif opt == '-x':
            try:
                xThresh = int(val)
            except:
                print("Desired x threshold '%s' not a number" % val)
                usage(name)
                return
        elif opt == '-y':
            try:
                yThresh = int(val)
            except:
                print("Desired y threshold '%s' not a number" % val)
                usage(name)
                return
        elif opt == '-Y':
            try:
                yColumn = int(val)
            except:
                print("Desired y column '%s' is not a number" % val)
                usage(name)
                return
        elif opt == '-O':
            optionString = val
            if optionString[0] != '[':
                optionString = '[' + optionString
            if optionString[-1] != ']':
                optionString += ']'
        else:
            print("Unknown option '%s'" % opt)
            usage(name)
            return
    gen(sys.stdin, sys.stdout)

if __name__ == "__main__":
    run(sys.argv[0], sys.argv[1:])
