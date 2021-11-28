reproduce: install
	cd experimental-results; make reproduce

demo: install
	cd benchmarks; make run
	cp benchmarks/results-pgpbs.txt .
	cat results-pgpbs.txt

reproduce-full: install
	cd experimental-results; make reproduce-full

install:
	cd lrat; make install

demo-pgbdd: install
	cd benchmarks; make run-pgbdd
	cp benchmarks/results-pgbdd.txt .
	cat results-pgbdd.txt

test: install
	cd benchmarks; make test

test-pgbdd: install
	cd benchmarks; make test-pgbdd

clean:
	cd benchmarks; make clean
	cd experimental-results; make clean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt

superclean:
	cd benchmarks; make superclean
	cd experimental-results; make superclean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt
	rm -f graphs.pdf




