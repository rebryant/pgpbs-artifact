#!/usr/bin/python
# Simple, proof-generating SAT solver based on BDDs

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
import random

import stream
import pseudoboolean
import solver

# Increase maximum recursion depth
sys.setrecursionlimit(10 * sys.getrecursionlimit())

def usage(name):
    sys.stderr.write("Usage: %s [-h] [-v LEVEL] [-r SEED] [-i CNF] [-o file.{proof,lrat,lratb}] [-p PERMUTE] [-s SCHEDULE] [-m MODULUS] [-L logfile]\n" % name)
    sys.stderr.write("  -h          Print this message\n")
    sys.stderr.write("  -b          Process terms via bucket elimination ordered by variable levels\n")
    sys.stderr.write("  -v LEVEL    Set verbosity level\n")
    sys.stderr.write("  -r SEED     Set random seed (for breaking ties during pivot selection)\n")
    sys.stderr.write("  -i CNF      Name of CNF input file\n")
    sys.stderr.write("  -o pfile    Name of proof output file (.proof = tracecheck, .lrat = LRAT text, .lratb = LRAT binary)\n")
    sys.stderr.write("  -p PERMUTE  Name of file specifying mapping from CNF variable to BDD level\n")
    sys.stderr.write("  -s SCHEDULE Name of action schedule file\n")
    sys.stderr.write("  -m MODULUS  Specify modulus for equation solver (Either number or 'a' for auto-detect, 'i' for integer mode)\n")
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
    scheduler = None
    verbLevel = 1
    logName = None
    modulus = pseudoboolean.modulusAuto

    optlist, args = getopt.getopt(args, "hbv:r:i:o:p:s:m:L:")
    for (opt, val) in optlist:
        if opt == '-h':
            usage(name)
            return
        elif opt == '-v':
            verbLevel = int(val)
        elif opt == '-r':
            random.seed(int(val))
        elif opt == '-i':
            cnfName = val
        elif opt == '-o':
            proofName = val
            extension = proofName.split('.')[-1]
            if extension == 'lrat' or extension == 'lratb':
                doLrat = True
                doBinary = extension[-1] == 'b'
        elif opt == '-p':
            permuter = solver.readPermutation(val)
            if permuter is None:
                return
        elif opt == '-s':
            scheduler = solver.readScheduler(val)
            if scheduler is None:
                return
        elif opt == '-m':
            if val == 'a':
                modulus = pseudoboolean.modulusAuto
            elif val == 'i':
                modulus = pseudoboolean.modulusNone
            else:
                modulus = int(val)
        elif opt == '-L':
            logName = val
        else:
            sys.stderr.write("Unknown option '%s'\n" % opt)
            usage(name)
            return

    writer = stream.Logger(logName)

    if scheduler is None:
        writer.write("Must have schedule")
        return

    try:
        prover = solver.Prover(proofName, writer = writer, verbLevel = verbLevel, doLrat = doLrat, doBinary = doBinary)
    except Exception as ex:
        writer.write("Couldn't create prover (%s)\n" % str(ex))
        return

    start = datetime.datetime.now()
    solve = solver.Solver(cnfName, prover = prover, permuter = permuter, verbLevel = verbLevel)
    solve.runSchedule(scheduler, modulus)

    delta = datetime.datetime.now() - start
    seconds = delta.seconds + 1e-6 * delta.microseconds
    if verbLevel > 0:
        writer.write("Elapsed time for SAT: %.2f seconds\n" % seconds)
    if writer != sys.stderr:
        writer.close()
    
if __name__ == "__main__":
    run(sys.argv[0], sys.argv[1:])

    

    
