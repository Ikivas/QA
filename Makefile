
VENV := venv

all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip3 install -r requirements.txt
venv: $(VENV)/bin/activate # shortcut

run: venv
	./$(VENV)/bin/python3 API/gitHubAPI.py

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean