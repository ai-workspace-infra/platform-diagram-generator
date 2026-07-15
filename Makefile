.PHONY: all venv generate clean

VENV := venv
PYTHON := $(VENV)/bin/python3
PIP := $(VENV)/bin/pip3
PLAYWRIGHT := $(VENV)/bin/playwright

all: generate

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	$(PLAYWRIGHT) install chromium
	touch $(VENV)/bin/activate

venv: $(VENV)/bin/activate

generate: venv
	$(PYTHON) generate.py

clean:
	rm -rf $(VENV)
	rm -f temp_render.html
	rm -f platform_architecture.png
