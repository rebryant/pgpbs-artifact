reproduce: install
	cd experimental-results; make reproduce

reproduce-full: install
	cd experimental-results; make reproduce-full

install:
	cd lrat; make install

test: install
	cd demo; make test

test-pgbdd: install
	cd demo; make test-pgbdd

clean:
	cd experimental-results; make clean
	cd lrat; make clean
	cd src; make clean
	cd demo; make clean
	rm -f *~ *results*.txt

superclean:
	cd experimental-results; make superclean
	cd lrat; make clean
	cd src; make clean
	cd demo; make superclean
	rm -f *~ *results*.txt
	rm -f graphs.pdf




