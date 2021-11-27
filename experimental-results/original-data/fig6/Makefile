INTERP = python3
N = 10
VLEVEL = 1
SEED=123456

SDIR=../../../src
CDIR=../../code
LDIR=../../../lrat

GENERATOR=$(INTERP) $(CDIR)/chess.py
PGBDD=$(INTERP) $(SDIR)/pgbdd.py
PGPBS=$(INTERP) $(SDIR)/pgpbs.py
RANDOMIZER = $(INTERP) $(CDIR)/randomizer.py
EXTRACTOR = $(INTERP)  $(SDIR)/constraint_extractor.py
CHECKER = $(LDIR)/lrat-check
GRABBER =$(INTERP)  $(CDIR)/grab_clauses.py
EXTENSION = lrat

bcr: chess-board-$(N)-column-randomorder.data

tcs: chess-torus-$(N)-column.data

ter: chess-torus-$(N)-equation-auto-randomorder.data

ber: chess-board-$(N)-equation-randomorder.data


chess-board-$(N)-column-randomorder.data:
	$(GENERATOR) -n $(N) -r chess-board-$(N)-column-randomorder | tee chess-board-$(N)-column-randomorder.data
	$(RANDOMIZER) chess-board-$(N)-column-randomorder.cnf $(SEED)
	$(PGBDD) -v $(VLEVEL) -i chess-board-$(N)-column-randomorder.cnf -s chess-board-$(N)-column-randomorder.schedule \
		-p chess-board-$(N)-column-randomorder.order -o chess-board-$(N)-column-randomorder.$(EXTENSION) 2>&1 | tee -a chess-board-$(N)-column-randomorder.data
	$(CHECKER) chess-board-$(N)-column-randomorder.cnf chess-board-$(N)-column-randomorder.$(EXTENSION) | tee -a chess-board-$(N)-column-randomorder.data
	rm -f chess-board-$(N)-column-randomorder.$(EXTENSION)

chess-torus-$(N)-column.data:
	$(GENERATOR) -w b -n $(N) -r chess-torus-$(N)-column | tee chess-torus-$(N)-column.data
	$(PGBDD) -v $(VLEVEL) -i chess-torus-$(N)-column.cnf -s chess-torus-$(N)-column.schedule \
		-p chess-torus-$(N)-column.order -o chess-torus-$(N)-column.$(EXTENSION) 2>&1 | tee -a chess-torus-$(N)-column.data
	$(CHECKER) chess-torus-$(N)-column.cnf chess-torus-$(N)-column.$(EXTENSION) | tee -a chess-torus-$(N)-column.data
	rm -f chess-torus-$(N)-column.$(EXTENSION)

chess-torus-$(N)-equation-auto-randomorder.data:
	$(GENERATOR) -C -w b -n $(N) -r chess-torus-$(N)-equation-auto-randomorder -p e | tee chess-torus-$(N)-equation-auto-randomorder.data
	$(RANDOMIZER) chess-torus-$(N)-equation-auto-randomorder.cnf $(SEED)
	$(EXTRACTOR) -i chess-torus-$(N)-equation-auto-randomorder.cnf -o chess-torus-$(N)-equation-auto-randomorder.schedule -v 2 | tee -a chess-torus-$(N)-equation-auto-randomorder.data
	$(PGPBS) -v $(VLEVEL) -i chess-torus-$(N)-equation-auto-randomorder.cnf -s chess-torus-$(N)-equation-auto-randomorder.schedule -m a \
		-r $(SEED) \
		-p chess-torus-$(N)-equation-auto-randomorder.order \
		-o chess-torus-$(N)-equation-auto-randomorder.$(EXTENSION) 2>&1 | tee -a chess-torus-$(N)-equation-auto-randomorder.data
	$(CHECKER) chess-torus-$(N)-equation-auto-randomorder.cnf chess-torus-$(N)-equation-auto-randomorder.$(EXTENSION) | tee -a chess-torus-$(N)-equation-auto-randomorder.data
	rm -f chess-torus-$(N)-equation-auto-randomorder.$(EXTENSION)

chess-board-$(N)-equation-randomorder.data:
	$(GENERATOR) -C -n $(N) -r chess-board-$(N)-equation-randomorder -p e | tee chess-board-$(N)-equation-randomorder.data
	$(RANDOMIZER) chess-board-$(N)-equation-randomorder.cnf $(SEED)
	$(EXTRACTOR) -i chess-board-$(N)-equation-randomorder.cnf -o chess-board-$(N)-equation-randomorder.schedule -v 2 | tee -a chess-board-$(N)-equation-randomorder.data
	$(PGPBS) -v $(VLEVEL) -i chess-board-$(N)-equation-randomorder.cnf -s chess-board-$(N)-equation-randomorder.schedule -m a \
		-r $(SEED) \
		-p chess-board-$(N)-equation-randomorder.order -o chess-board-$(N)-equation-randomorder.$(EXTENSION) 2>&1 | tee -a chess-board-$(N)-equation-randomorder.data
	$(CHECKER) chess-board-$(N)-equation-randomorder.cnf chess-board-$(N)-equation-randomorder.$(EXTENSION) | tee -a chess-board-$(N)-equation-randomorder.data
	rm -f chess-board-$(N)-equation-randomorder.$(EXTENSION)



data:
	$(GRABBER) chess-board-*-column-randomorder.data > chess-board-column-randomorder.csv
	$(GRABBER) chess-torus-*-column.data > chess-torus-column.csv
	$(GRABBER) chess-torus-*-equation-auto-randomorder.data > chess-torus-equation-randomorder.csv
	$(GRABBER) chess-board-*-equation-randomorder.data > chess-board-equation-randomorder.csv

clean:
	rm -f *~

superclean: clean
	rm -f *.cnf *.lrat *.lratb *.order *.schedule *.buckets
