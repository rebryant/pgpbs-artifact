#!/usr/bin/python
# Simple, proof-generating SAT solver based on BDDs and pseudo-Boolean reasoning

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

import sys
import getopt
import datetime

import stream
import pseudoboolean
import solver

# Increase maximum recursion depth
sys.setrecursionlimit(10 * sys.getrecursionlimit())

def usage(name):
    sys.stderr.write("Usage: %s [-h] [-b] [-v LEVEL] [-i CNF] [-o file.{proof,lrat,lratb}] [-p PERMUTE] [-s SCHEDULE] [-L logfile]\n" % name)
    sys.stderr.write("  -h          Print this message\n")
    sys.stderr.write("  -b          Process terms via bucket elimination ordered by variable levels\n")
    sys.stderr.write("  -v LEVEL    Set verbosity level\n")
    sys.stderr.write("  -i CNF      Name of CNF input file\n")
    sys.stderr.write("  -o pfile    Name of proof output file (.proof = tracecheck, .lrat = LRAT text, .lratb = LRAT binary)\n")
    sys.stderr.write("  -p PERMUTE  Name of file specifying mapping from CNF variable to BDD level\n")
    sys.stderr.write("  -s SCHEDULE Name of action schedule file\n")
    sys.stderr.write("  -L logfile  Append standard error output to logfile\n")

# Verbosity levels
# 0: Totally silent
# 1: Key statistics only
# 2: Summary information
# 3: Proof information
# 4: ?
# 5: Tree generation information

def run(name, args):
    cnfName = None
    proofName = None
    doLrat = False
    doBinary = False
    permuter = None
    bpermuter = None
    doBucket = False
    scheduler = None
    verbLevel = 1
    logName = None

    # No that some deprecated options are still implemented but not available
    optlist, args = getopt.getopt(args, "hbv:i:o:p:s:L:")
    for (opt, val) in optlist:
        if opt == '-h':
            usage(name)
            return
        if opt == '-b':
            doBucket = True
        elif opt == '-B':
            bpermuter = solver.readPermutation(val)
            if bpermuter is None:
                return
        elif opt == '-v':
            verbLevel = int(val)
        elif opt == '-i':
            cnfName = val
        elif opt == '-o':
            proofName = val
            extension = proofName.split('.')[-1]
            if extension == 'lrat' or extension == 'lratb':
                doLrat = True
                doBinary = extension[-1] == 'b'
        elif opt == '-M':
            proofName = None
            if val == 'b':
                doLrat = True
                doBinary = True
            elif val == 't':
                doLrat = True
        elif opt == '-p':
            permuter = solver.readPermutation(val)
            if permuter is None:
                return
        elif opt == '-s':
            scheduler = solver.readScheduler(val)
            if scheduler is None:
                return
        elif opt == '-L':
            logName = val
        else:
            sys.stderr.write("Unknown option '%s'\n" % opt)
            usage(name)
            return

    writer = stream.Logger(logName)

    if (doBucket or bpermuter is not None) and scheduler is not None:
        writer.write("Cannot have both bucket scheduling and defined scheduler\n")
        return
    if (doBucket and bpermuter is not None):
        writer.write("Cannot do bucket scheduling on levels and with defined permutation\n")
        return

    try:
        prover = solver.Prover(proofName, writer = writer, verbLevel = verbLevel, doLrat = doLrat, doBinary = doBinary)
    except Exception as ex:
        writer.write("Couldn't create prover (%s)\n" % str(ex))
        return

    start = datetime.datetime.now()
    solve = solver.Solver(cnfName, prover = prover, permuter = permuter, verbLevel = verbLevel)
    if doBucket:
        solve.runBucketSchedule()
    elif bpermuter is not None:
        solve.runBucketSchedulePerm(bpermuter)
    elif scheduler is not None:
        solve.runSchedule(scheduler, None)
    else:
        solve.runNoSchedule()

    delta = datetime.datetime.now() - start
    seconds = delta.seconds + 1e-6 * delta.microseconds
    if verbLevel > 0:
        writer.write("Elapsed time for SAT: %.2f seconds\n" % seconds)
    if writer != sys.stderr:
        writer.close()
    
if __name__ == "__main__":
    run(sys.argv[0], sys.argv[1:])

    

    
