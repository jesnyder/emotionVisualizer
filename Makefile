DEFAULT_GOAL:  web


.PHONY: clone
clone:
		rm -rf scraped_guts
		rm -rf core_code
		git clone https://github.com/jesnyder/scraped_guts.git
		mv scraped_guts/ core_code/

.PHONY: pythonanalysis
pythonanalysis:
	pip install --upgrade -r reqs.txt
	python3  core_code/python/a_main.py


.PHONY: web
web: pythonanalysis
		python3 -m http.server
