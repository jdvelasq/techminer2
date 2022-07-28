.PHONY: html
.PHONY: docs



docs:
	make html
	rmdir -rf docs/
	cp -r sphinx/_build/html docs/

html:
	source .venv/bin/activate
	cd sphinx
	make html
	cd ..	
