INTERP = python3
N = 10
VLEVEL = 1
SEED=123456

SDIR=../../../src
CDIR=../../code
LDIR=../../../lrat

GENERATOR=$(CDIR)/chess.py
PGBDD=$(INTERP) $(SDIR)/pgbdd.py
PGPBS=$(INTERP) $(SDIR)/pgpbs.py
RANDOMIZER = $(INTERP) $(CDIR)/randomizer.py
EXTRACTOR = $(INTERP)  $(SDIR)/constraint_extractor.py
CHECKER = $(LDIR)/lrat-check
GRABBER =$(INTERP)  $(CDIR)/grab_clauses.py
EXTENSION = lrat

short:
	./gen-short.sh

full:
	./gen-full.sh

cs: chess-$(N)-column.data

e3: chess-$(N)-equation-mod3.data

ei: chess-$(N)-equation-integer.data

chess-$(N)-column.data:
	$(GENERATOR) -n $(N) -r chess-$(N)-column | tee chess-$(N)-column.data
	$(PGBDD) -v $(VLEVEL) -i chess-$(N)-column.cnf -s chess-$(N)-column.schedule \
		-p chess-$(N)-column.order -o chess-$(N)-column.$(EXTENSION) 2>&1 | tee -a chess-$(N)-column.data
	$(CHECKER) chess-$(N)-column.cnf chess-$(N)-column.$(EXTENSION) | tee -a chess-$(N)-column.data
	rm -f chess-$(N)-column.$(EXTENSION)

chess-$(N)-equation-mod3.data:
	$(GENERATOR) -C -n $(N) -r chess-$(N)-equation-mod3 -p e | tee chess-$(N)-equation-mod3.data
	$(EXTRACTOR) -i chess-$(N)-equation-mod3.cnf -o chess-$(N)-equation-mod3.schedule -v 2 | tee -a chess-$(N)-equation-mod3.data
	$(PGPBS) -v $(VLEVEL) -i chess-$(N)-equation-mod3.cnf -s chess-$(N)-equation-mod3.schedule -m 3 \
		-r $(SEED) \
		-o chess-$(N)-equation-mod3.$(EXTENSION) 2>&1 | tee -a chess-$(N)-equation-mod3.data
	$(CHECKER) chess-$(N)-equation-mod3.cnf chess-$(N)-equation-mod3.$(EXTENSION) | tee -a chess-$(N)-equation-mod3.data
	rm -f chess-$(N)-equation-mod3.$(EXTENSION)

chess-$(N)-equation-integer.data:
	$(GENERATOR) -C -n $(N) -r chess-$(N)-equation-integer -p e | tee chess-$(N)-equation-integer.data
	$(EXTRACTOR) -i chess-$(N)-equation-integer.cnf -o chess-$(N)-equation-integer.schedule -v 2 | tee -a chess-$(N)-equation-integer.data
	$(PGPBS) -v $(VLEVEL) -i chess-$(N)-equation-integer.cnf -s chess-$(N)-equation-integer.schedule  -m i \
		-r $(SEED) \
		-o chess-$(N)-equation-integer.$(EXTENSION) 2>&1 | tee -a chess-$(N)-equation-integer.data
	$(CHECKER) chess-$(N)-equation-integer.cnf chess-$(N)-equation-integer.$(EXTENSION) | tee -a chess-$(N)-equation-integer.data
	rm -f chess-$(N)-equation-integer.$(EXTENSION)

data:
	$(GRABBER) chess-*-column.data > chess-column.csv
	$(GRABBER) chess-*-equation-mod3.data > chess-equation-mod3.csv
	$(GRABBER) chess-*-equation-integer.data > chess-equation-integer.csv

clean:
	rm -f *~

superclean: clean
	rm -f *.cnf *.lrat *.lratb *.order *.schedule *.buckets *.csv
	rm -f *.data
