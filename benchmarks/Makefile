INTERP=python3
FDIR = ../src
FORMATTER = $(INTERP) $(FDIR)/formatter.py

run:
	cd cardinality; make run
	cd parity; make run
	$(FORMATTER) {cardinality,parity}/*.data > results-pgpbs.txt

run-pgbdd:
	cd parity; make run-pgbdd
	$(FORMATTER) parity/*.data > results-pgbdd.txt

test:
	cd cardinality; make test
	cd parity; make test

test-pgbdd:
	cd parity; make test-pgbdd

clean:
	cd cardinality; make clean
	cd parity; make clean
	rm -f *~

superclean:
	cd cardinality; make superclean
	cd parity; make superclean
	rm -f *~ *.txt


