include ../Makefile.vars
integrateDir = ${resultsdir}/repos/101integrate
termResourcesDir = ../../services/termResources

run:
	$(MAKE) clean
	cd ${integrateDir} ; $(MAKE) bootstrap; $(MAKE) clean
	cd ${integrateDir} ; $(MAKE) run BOOKS=Haskell
	$(MAKE) deploy

integrate:
	cd ${integrateDir}/src/integrate ; make integrate

deploy:
	mkdir -p ${modulesDir}/integrate ;\
	cp -r ${integrateDir}/data/allbooks ${modulesDir}/integrate ;\
	cp -r ${integrateDir}/data/perbook ${modulesDir}/integrate ;\
	#python deployResources.py ; #The respective folders are never generated
	cp -r ${integrateDir}/data/summary ${modulesDir}/integrate
	cp ${integrateDir}/data/allbooks/backlinks.json ${termResourcesDir}
	cp ${integrateDir}/data/allbooks/mapping.json ${termResourcesDir}

# Remove local temporary files, if any
clean:
	rm -rf ${modulesDir}/integrate
	mkdir -p ${modulesDir}/integrate

# Remove files created by this module
reset:
	rm -r ${modulesDir}/integrate
	mkdir -p ${modulesDir}/integrate

#installing und building 101-folder-structure
setup:						#ls for debugging
	mkdir -p ${modulesDir}/integrate
	mkdir -p ${resultsdir}/repos
	cd ${resultsdir}/repos; git clone https://github.com/101companies/101integrate; ls
	cd ${resultsdir}/repos/101integrate; ls; cd src; ls; touch Makefile.vars ; ls # integrateDir undefined if not existens on starting time of this Makefile
	cd ${resultsdir}/repos/101integrate ; make download-deps

install:
	apt-get install r-base r-cran-reshape r-cran-xtable r-cran-foreach 
	apt-get install python-antlr
	git clone https://github.com/101companies/101integrate.git
	cd 101integrate; make download-deps
	rm -rf 101integrate
