reproduce: install
	cd experimental-results; make reproduce

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
	cd experimental-results; make clean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt

superclean:
	cd experimental-results; make superclean
	cd lrat; make clean
	cd src; make clean
	rm -f *~ *results*.txt
	rm -f graphs.pdf




