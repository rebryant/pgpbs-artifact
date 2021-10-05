#!/usr/bin/python


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


# Generate report showing results of set of PGBDD runs
import sys

# First line of headings for the fields
heading1  = [
    "Benchmark",
    "Input",
    "Input",
    "Pseudo-Bool.",
    "Total",
    "SAT",
    "Verif.",
    "Verif.",
    ]

# Second line of headings for the fields
heading2  = [
    "File",
    "Vars.",
    "Clauses",
    "Constraints",
    "Clauses",
    "Time (s)",
    "Time (s)",
    "Status",
    ]

# Keywords indicating lines on which the fields occur
keywords = [
    "File",
    "Input variables",
    "Input clauses",
    "File",
    "Total Clauses",
    "Elapsed",
    "verification",
    "VERIFIED",
    ]

padding = 4

# Position in line, starting at 0
positions = [
    1, 2, 2, 2, 2, 4, 4, 1
]

def getField(s, id):
    fields = s.split()
    if len(fields) <= id:
        return "???"
    field = fields[id]
    # Trim trailing puncutation
    if field[-1] in ":.,":
        field = field[:-1]
    return field

def justifyRight(s, width):
    right = padding//2
    left = (padding-right) + width-len(s)
    if left > 0 and right > 0:
        return (" " * left) + s + (" " * right)
    else:
        return s

def justifyLeft(s, width):
    left = padding - padding//2
    right = (padding-left) + width-len(s)
    if left > 0 and right > 0:
        return (" " * left) + s + (" " * right)
    else:
        return s

def justifyCenter(s, width):
    total = padding+width-len(s)
    if total > 0:
        left = total // 2
        right = total - left
        return (" " * left) + s + (" " * right)
    else:
        return s

def appendData(fname, itemLists):
    fcount = len(heading1)
    gotItem = [False for idx in range(fcount)]
    f = open(fname, 'r')
    for line in f:
        for idx in range(fcount):
            if heading1[idx] == 'Benchmark':
                ffields = fname.split(".")
                cname = ".".join(ffields[:-1] + ['cnf'])
                field = cname
                if not gotItem[idx]:
                    itemLists[idx].append(field)
                gotItem[idx] = True
            elif keywords[idx] in line:
                pos = positions[idx]
                field = getField(line, pos)
                if not gotItem[idx]:
                    itemLists[idx].append(field)
                gotItem[idx] = True
    for pos in range(fcount):
        if not gotItem[pos]:
            itemLists[pos].append("XXX")
    f.close()
        
def findWidths(itemLists):
    fcount = len(itemLists)
    widths = [0] * fcount
    for idx in range(fcount):
        for item in itemLists[idx]:
            widths[idx] = max(widths[idx], len(item))
    return widths

# Read files.  Build list of item lists
def formatData(fnames):
    fcount = len(heading1)
    itemLists = [[heading1[idx], heading2[idx]] for idx in range(fcount)]
    for fname in fnames:
        appendData(fname, itemLists)
    widths = findWidths(itemLists)
    lcount = len(itemLists[0])
    for lidx in range(lcount):
        line = ""
        for idx in range(fcount):
            field = itemLists[idx][lidx]
            if lidx <= 1:
                field = justifyCenter(field, widths[idx])
            elif idx == 0:
                field = justifyLeft(field, widths[idx])                
            else:
                field = justifyRight(field, widths[idx])
            line += field
        print(line)
    
def run(name, args):
    if len(args) == 0 or args[0] == '-h':
        print("Usage: %s f1 f2 ..." % name)
        return
    formatData(args)

if __name__ == "__main__":
    run(sys.argv[0], sys.argv[1:])

    
    
