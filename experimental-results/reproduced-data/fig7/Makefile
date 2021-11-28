INTERP = python3
N = 10
VLEVEL = 1
SEED=123456

SDIR=../../../src
CDIR=../../code
LDIR=../../../lrat

SGENERATOR=$(INTERP) $(CDIR)/pigeon-sinz.py
DGENERATOR=$(INTERP) $(CDIR)/pigeon-cook.py
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

dl: pigeon-direct-$(N)-pm-linear.data
scol: pigeon-tseitin-$(N)-column.data
srcon: pigeon-tseitin-$(N)-constraint-randomorder.data
drcon: pigeon-direct-$(N)-constraint-randomorder.data
sreq: pigeon-tseitin-$(N)-equation-randomorder.data
dcook: pigeon-direct-$(N)-cook.data

pigeon-direct-$(N)-pm-linear.data:
	$(DGENERATOR) -c -n $(N) -r pigeon-direct-$(N)-pm
	$(PGBDD) -v $(VLEVEL) -i pigeon-direct-$(N)-pm.cnf -o pigeon-direct-$(N)-pm.$(EXTENSION) 2>&1 | tee pigeon-direct-$(N)-pm-linear.data
	$(CHECKER) pigeon-direct-$(N)-pm.cnf pigeon-direct-$(N)-pm.$(EXTENSION) | tee -a pigeon-direct-$(N)-pm-linear.data
	rm -f pigeon-direct-$(N)-pm.$(EXTENSION)

pigeon-tseitin-$(N)-column.data:
	$(SGENERATOR) -n $(N) -r pigeon-tseitin-$(N) | tee pigeon-tseitin-$(N)-column.data
	$(PGBDD) -v $(VLEVEL) -i pigeon-tseitin-$(N).cnf -s pigeon-tseitin-$(N).schedule \
		-p pigeon-tseitin-$(N).order -o pigeon-tseitin-$(N).$(EXTENSION) 2>&1 | tee -a pigeon-tseitin-$(N)-column.data
	$(CHECKER) pigeon-tseitin-$(N).cnf pigeon-tseitin-$(N).$(EXTENSION) | tee -a pigeon-tseitin-$(N)-column.data
	rm -f pigeon-tseitin-$(N).$(EXTENSION)

pigeon-tseitin-$(N)-constraint-randomorder.data:
	$(SGENERATOR) -C -c -n $(N) -r pigeon-tseitin-$(N)-constraint-randomorder | tee pigeon-tseitin-$(N)-constraint-randomorder.data
	$(EXTRACTOR) < pigeon-tseitin-$(N)-constraint-randomorder.cnf > pigeon-tseitin-$(N)-constraint-randomorder.schedule
	$(RANDOMIZER) pigeon-tseitin-$(N)-constraint-randomorder.cnf $(SEED)
	$(PGPBS) -r $(SEED) -v $(VLEVEL) -i pigeon-tseitin-$(N)-constraint-randomorder.cnf -s pigeon-tseitin-$(N)-constraint-randomorder.schedule \
		-p pigeon-tseitin-$(N)-constraint-randomorder.order -o pigeon-tseitin-$(N)-constraint-randomorder.$(EXTENSION) 2>&1 | tee -a pigeon-tseitin-$(N)-constraint-randomorder.data
	$(CHECKER) pigeon-tseitin-$(N)-constraint-randomorder.cnf pigeon-tseitin-$(N)-constraint-randomorder.$(EXTENSION) | tee -a pigeon-tseitin-$(N)-constraint-randomorder.data
	rm -f pigeon-tseitin-$(N)-constraint-randomorder.$(EXTENSION)

pigeon-direct-$(N)-constraint-randomorder.data:
	$(DGENERATOR) -c -n $(N) -r pigeon-direct-$(N)-constraint-randomorder
	$(RANDOMIZER) pigeon-direct-$(N)-constraint-randomorder.cnf $(SEED)
	$(EXTRACTOR) < pigeon-direct-$(N)-constraint-randomorder.cnf > pigeon-direct-$(N)-constraint-randomorder.schedule
	$(PGPBS) -r $(SEED) -v $(VLEVEL) -i pigeon-direct-$(N)-constraint-randomorder.cnf -o pigeon-direct-$(N)-constraint-randomorder.$(EXTENSION) \
		-p pigeon-direct-$(N)-constraint-randomorder.order \
		-s pigeon-direct-$(N)-constraint-randomorder.schedule 2>&1 | tee pigeon-direct-$(N)-constraint-randomorder.data
	$(CHECKER) pigeon-direct-$(N)-constraint-randomorder.cnf pigeon-direct-$(N)-constraint-randomorder.$(EXTENSION) | tee -a pigeon-direct-$(N)-constraint-randomorder.data
	rm -f pigeon-direct-$(N)-constraint-randomorder.$(EXTENSION)


pigeon-tseitin-$(N)-equation-randomorder.data:
	$(SGENERATOR) -E -C -c -n $(N) -r pigeon-tseitin-$(N)-equation-randomorder | tee pigeon-tseitin-$(N)-equation-randomorder.data
	$(EXTRACTOR) < pigeon-tseitin-$(N)-equation-randomorder.cnf > pigeon-tseitin-$(N)-equation-randomorder.schedule
	$(RANDOMIZER) pigeon-tseitin-$(N)-equation-randomorder.cnf $(SEED)
	$(PGPBS) -r $(SEED) -v $(VLEVEL) -i pigeon-tseitin-$(N)-equation-randomorder.cnf -s pigeon-tseitin-$(N)-equation-randomorder.schedule \
		-p pigeon-tseitin-$(N)-equation-randomorder.order -o pigeon-tseitin-$(N)-equation-randomorder.$(EXTENSION) 2>&1 | tee -a pigeon-tseitin-$(N)-equation-randomorder.data
	$(CHECKER) pigeon-tseitin-$(N)-equation-randomorder.cnf pigeon-tseitin-$(N)-equation-randomorder.$(EXTENSION) | tee -a pigeon-tseitin-$(N)-equation-randomorder.data
	rm -f pigeon-tseitin-$(N)-equation-randomorder.$(EXTENSION)

pigeon-direct-$(N)-cook.data:
	$(DGENERATOR) -n $(N) -r pigeon-direct-$(N)-cook | tee pigeon-direct-$(N)-cook.data
	$(CHECKER) pigeon-direct-$(N)-cook.cnf pigeon-direct-$(N)-cook.lrat | tee -a pigeon-direct-$(N)-cook.data
	rm -f pigeon-direct-$(N)-cook.lrat


data:
	$(GRABBER) pigeon-direct-*-pm-linear.data > pigeon-direct-linear-inputorder.csv
	$(GRABBER) pigeon-tseitin-*-column.data > pigeon-sinz-column-inputorder.csv
	$(GRABBER) pigeon-tseitin-*-constraint-randomorder.data > pigeon-sinz-constraint-randomorder.csv
	$(GRABBER) pigeon-direct-*-constraint-randomorder.data > pigeon-direct-constraint-randomorder.csv
	$(GRABBER) pigeon-tseitin-*-equation-randomorder.data > pigeon-sinz-equation-randomorder.csv
	$(GRABBER) pigeon-direct-*-cook.data > pigeon-direct-cook.csv

clean:
	rm -f *~
	rm -f *.csv

superclean: clean
	rm -f *.cnf *.lrat *.lratb *.order *.schedule

