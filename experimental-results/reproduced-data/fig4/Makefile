INTERP = python3
M = 3
VLEVEL = 1
PCT=50
SEED=123456

SDIR=../../../src
CDIR=../../code
LDIR=../../../lrat
CNFDIR=../../original-data/fig4

PGBDD=$(INTERP) $(SDIR)/pgbdd.py
PGPBS=$(INTERP) $(SDIR)/pgpbs.py
RANDOMIZER = $(INTERP) $(CDIR)/randomizer.py
EXTRACTOR = $(INTERP) $(SDIR)/xor_extractor.py
CHECKER = $(LDIR)/lrat-check
GRABBER = $(INTERP) $(CDIR)/grab_clauses.py
EXTENSION = lrat

lro: urquhart-li-$(M)-randomorder.data
lre: urquhart-li-$(M)-ro-equation.data
sro: urquhart-simon-$(M)-$(SEED)-randomorder.data
sre: urquhart-simon-$(M)-$(SEED)-ro-equation.data

urquhart-li-$(M)-randomorder.data:
	$(RANDOMIZER) $(CNFDIR)/uhart-li-$(M).cnf $(SEED)
	$(PGBDD) -v $(VLEVEL) -i urquhart-li-$(M).cnf -b -p urquhart-li-$(M).order \
		-o urquhart-li-$(M)-randomorder.$(EXTENSION) 2>&1 | tee -a urquhart-li-$(M)-randomorder.data
	$(CHECKER) urquhart-li-$(M).cnf urquhart-li-$(M)-randomorder.$(EXTENSION) | tee -a urquhart-li-$(M)-randomorder.data
	rm -f urquhart-li-$(M)-randomorder.$(EXTENSION)

urquhart-li-$(M)-ro-equation.data:
	$(RANDOMIZER) urquhart-li-$(M).cnf $(SEED)
	$(EXTRACTOR) -i urquhart-li-$(M).cnf -o urquhart-li-$(M)-ro-equation.schedule
	$(PGPBS) -r $(SEED) -v $(VLEVEL) -i urquhart-li-$(M).cnf -s urquhart-li-$(M)-ro-equation.schedule \
	        -p urquhart-li-$(M).order \
		-o urquhart-li-$(M)-ro-equation.$(EXTENSION) 2>&1 | tee -a urquhart-li-$(M)-ro-equation.data
	$(CHECKER) urquhart-li-$(M).cnf urquhart-li-$(M)-ro-equation.$(EXTENSION) | tee -a urquhart-li-$(M)-ro-equation.data
	rm -f urquhart-li-$(M)-ro-equation.$(EXTENSION)

urquhart-simon-$(M)-$(SEED)-randomorder.data:
	$(RANDOMIZER) urquhart-simon-$(M)-$(SEED).cnf $(SEED)
	$(PGBDD) -v $(VLEVEL) -i urquhart-simon-$(M)-$(SEED).cnf -b -p urquhart-simon-$(M)-$(SEED).order \
		-o urquhart-simon-$(M)-$(SEED)-randomorder.$(EXTENSION) 2>&1 | tee -a urquhart-simon-$(M)-$(SEED)-randomorder.data
	$(CHECKER) urquhart-simon-$(M)-$(SEED).cnf urquhart-simon-$(M)-$(SEED)-randomorder.$(EXTENSION) | tee -a urquhart-simon-$(M)-$(SEED)-randomorder.data
	rm -f urquhart-simon-$(M)-$(SEED)-randomorder.$(EXTENSION)

urquhart-simon-$(M)-$(SEED)-ro-equation.data:
	$(EXTRACTOR) -i urquhart-simon-$(M)-$(SEED).cnf -o urquhart-simon-$(M)-$(SEED)-ro-equation.schedule
	$(RANDOMIZER) urquhart-simon-$(M)-$(SEED).cnf $(SEED)
	$(PGPBS) -r $(SEED) -v $(VLEVEL) -i urquhart-simon-$(M)-$(SEED).cnf -s  urquhart-simon-$(M)-$(SEED)-ro-equation.schedule \
		-p urquhart-simon-$(M)-$(SEED).order \
		-o urquhart-simon-$(M)-$(SEED)-ro-equation.$(EXTENSION) 2>&1 | tee -a urquhart-simon-$(M)-$(SEED)-ro-equation.data
	$(CHECKER) urquhart-simon-$(M)-$(SEED).cnf urquhart-simon-$(M)-$(SEED)-ro-equation.$(EXTENSION) | tee -a urquhart-simon-$(M)-$(SEED)-ro-equation.data
	rm -f urquhart-simon-$(M)-$(SEED)-ro-equation.$(EXTENSION)


data:
	$(GRABBER) urquhart-li-*-randomorder.data > urquhart-li-bucket.csv
	$(GRABBER) urquhart-li-*-ro-equation.data > urquhart-li-equation.csv
	$(GRABBER) urquhart-simon-*-randomorder.data > urquhart-simon-bucket.csv
	$(GRABBER) urquhart-simon-*-ro-equation.data > urquhart-simon-equation.csv

clean:
	rm -f *~

superclean: clean
	rm -f *.lrat *.lratb *.order *.schedule *.csv
	rm -f *.data
