This directory contains unsatisfiable benchmark problems based on
mismatched set sizes.  All have been processed with the program
scranfilize to randomize the ordering of variables and clauses.

1. Benchmarks:

mchess-board-24_shuf.cnf:
	The 24x24 mutilated chessboard.  Attempt to cover a chessboard
	with dominos, except that two opposite corners have been
	removed, and so there's a mismatch between the number of white
	and black squares.  This is a classic challenge problem for
	SAT solvers, since the shortest resolution proofs are
	exponential.  PGPBS can handle the problem easily.  PGBDD
	can handle it with extensive guidance on variable ordering
	and scheduling; otherwise it scales exponentially.

mchess-torus-24_shuf.cnf:
	Like the mutilated chessboard problem, but defined over a
	torus, with the edges of the board wrapping around for both
	top-bottom and left-right.  PGPBS can handle the problem
	easily.  PGBDD scales exponentially, with or without guidance
	from the user.

pigeon-direct-16_shuf.cnf:
pigeon-sinz-16_shuf.cnf:
	Two version of the pigeonhole problem, trying to assign 17
	pigeons to 16 holes, with no hole containing more than one
	pigeon.  One uses a direct encoding of the constraints,
	requiring O(n^3) clauses.  The other uses auxiliary variables,
	as described by Carsten Sinz, requiring O(n^2) variables.
	Pigeonhole is a well-known challenge problem for SAT solvers.
	KISSAT, winner of the 2020 SAT competition requires over 10
	hours on the Sinz version of this benchmark and generates a
	proof with over 196 million clauses.  PGBDD can handle the
	Sinz version when given sufficient guidance, but not the
	direct version.  PGPBS can handle both automatically.

randomG-XXXX-nN-d05_shuf.cnf
	Attempt to find perfect matchings in a random N X (N+1)
	bipartite graph with 50% density for N=19,20.  These are from
	a set of benchmarks in the 2021 SAT competition.  None of the
	entrants could generate a proof for these particular
	benchmarks within the 5000s time limit.  PGPBS handles them
	easily.  PGBDD could do so with extensive guidance from the
	user; otherwise it scales exponentialy

2. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         results-cardinality.txt

   test: Like run, but with smaller set of benchmarks

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

