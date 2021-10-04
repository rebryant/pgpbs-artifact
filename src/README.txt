This directory contains the code for the proof-generating SAT solvers
PGBDD and PGPBS.  The code is entirely in Python, executable under
both python2.7 and python3.7.  It also contains several support programs.

The solvers use BDDs to determine whether the provided input formula
(in DIMACS CNF format) is satisfiable.  The expectation is that the
formula is not satisfiable, and it generates a proof to this effect.


1. Programs

pgbdd.py:
   A BDD-based SAT solver making use of only Boolean operations.
   
./pgbdd.py -h
Usage: ./pgbdd.py [-h] [-b] [-v LEVEL] [-i CNF] [-o file.{proof,lrat,lratb}] [-p PERMUTE] [-s SCHEDULE] [-L logfile]
  -h          Print this message
  -b          Process terms via bucket elimination ordered by variable levels
  -v LEVEL    Set verbosity level
  -i CNF      Name of CNF input file
  -o pfile    Name of proof output file (.proof = tracecheck, .lrat = LRAT text, .lratb = LRAT binary)
  -p PERMUTE  Name of file specifying mapping from CNF variable to BDD level
  -s SCHEDULE Name of action schedule file
  -L logfile  Append standard error output to logfile


pgpbs.py:
   Like PGBDD, but it uses a pseudo-Boolean solver to detect that the
   formula is unsatisfiable.  PGPBS must be given a schedule file,
   describing how to convert the clauses into pseudo-Boolean
   constraints.

./pgpbs.py  -h
Usage: ./pgpbs.py [-h] [-v LEVEL] [-r SEED] [-i CNF] [-o file.{proof,lrat,lratb}] [-p PERMUTE] [-s SCHEDULE] [-m MODULUS] [-L logfile]
  -h          Print this message
  -b          Process terms via bucket elimination ordered by variable levels
  -v LEVEL    Set verbosity level
  -r SEED     Set random seed (for breaking ties during pivot selection)
  -i CNF      Name of CNF input file
  -o pfile    Name of proof output file (.proof = tracecheck, .lrat = LRAT text, .lratb = LRAT binary)
  -p PERMUTE  Name of file specifying mapping from CNF variable to BDD level
  -s SCHEDULE Name of action schedule file
  -m MODULUS  Specify modulus for equation solver (Either number or 'a' for auto-detect, 'i' for integer mode)
  -L logfile  Append standard error output to logfile

./xor_extractor.py:
   Used to extract modulo-2 equations from file consisting of xor and xnor operators.  Generates a schedule
   file for use with PGPBS

./xor_extractor.py -h
Usage: ./xor_extractor.py [-v VLEVEL] [-h] [-c] [-i IN.cnf] [-o OUT.schedule] [-d DIR] [-m MAXCLAUSE]
  -h       Print this message
  -v VERB  Set verbosity level (1-4)
  -c       Careful checking of CNF
  -i IFILE Single input file
  -i OFILE Single output file
  -p PATH  Process all CNF files with matching path prefix
  -m MAXC  Skip files with larger number of clauses


./constraint_extractor.py
   Used to extract integer equations and ordering constraints from
   file.  Generates a schedule file for use with PGPBS

./constraint_extractor.py -h
Usage: ./constraint_extractor.py [-h] [-c] [-v VLEVEL] [-i IN.cnf] [-o OUT.schedule] [-p PATH] [-m MAXCLAUSE]
  -h       Print this message
  -v VERB  Set verbosity level (1-4)
  -c       Careful checking of CNF
  -i IFILE Single input file
  -i OFILE Single output file
  -p PATH  Process all CNF files with matching path prefix
  -m MAXC  Skip files with larger number of clauses

./formatter.py:
    Used to format results from benchmark runs

./formatter.py -h
Usage: ./formatter.py f1 f2 ...


2. Other Files
   
Used by PGBDD and PGPBS:
   bdd.py
   pseudoboolean.py
   resolver.py
   solver.py
   stream.py

Used by xor_extractor.py and constraint_extractor.py
   exutil.py


3. Format for the schedule file

The schedule file is a text file with each line providing a command to
a simple, stack-based interpreter.  The commands are as follows:

# ...
        Comment line

c C_1 C_2 ... C_k
        Retrieve specified clauses and push onto stack

a K
        Pop K+1 elements.  Compute their conjunction and push result onto stack

q V_1 V_2 ... V_k
        Pop top element of stack.  Existentially quantify it by
        specified variables and push result onto stack

i Docstring (PGBDD only)
        Print out BDD information about top element on stack

(=|=2|>=) b A_1.V_1 A_2.V_2 ... A_k.V_k  (PGPBS only)
	Generate a BDD representation of the specified pseudo-Boolean
	constraint.
	Pop current stack and prove that it implies the PB constraint.
	Push the PB constraint.
        '=' denotes integer equation, '=2" denotes modulo-2 equation,
	and '>=" denotes ordering constraint
	
