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

wordcloud==1.8.1
wrapt==1.14.1
zipp==3.8.0