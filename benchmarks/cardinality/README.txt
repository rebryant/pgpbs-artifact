This directory contains unsatisfiable benchmark problems based on
mismatched set sizes.

1. Benchmarks:

mchess-board-N_shuf.cnf:
	The NxN mutilated chessboard.  Attempt to cover a chessboard
	with dominos, except that two opposite corners have been
	removed, and so there's a mismatch between the number of white
	and black squares.  This is a classic challenge problem for
	SAT solvers, since the shortest resolution proofs are
	exponential.  PGPBS can handle the problem easily.  PGBDD
	can handle it with extensive guidance on variable ordering
	and scheduling; otherwise it scales exponentially.

mchess-torus-N_shuf.cnf:
	Like the mutilated chessboard problem, but defined over a
	torus, with the edges of the board wrapping around for both
	top-bottom and left-right.  PGPBS can handle the problem
	easily.  PGBDD scales exponentially, with or without guidance
	from the user.

randomG-XXXX-nN-d05_shuf.cnf
	Attempt to find perfect mapping in a random N X (N+1) bipartite
	graph with 50% density.  From a set of benchmarks in the 2021
	SAT competition.  None of the entrants could generate a proof
	for these particular benchmarks within the 5000s time limit.
	PGPBS handles them easily.  PGBDD could do so with extensive
	guidance from the user;  otherwise it scales exponentialy

2. Make options

   run:  Run all benchmarks with PGPBS.  Tabulate results in
         results-cardinality.txt

   test: Like run, but with smaller set of benchmarks

   clean: Remove all intermediate files

   superclean: Remove all generated files, so that can rerun benchmarks

