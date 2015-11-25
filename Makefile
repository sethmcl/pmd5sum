VIRTUAL_ENV = ./venv
BIN         = pmd5sum
MODULE	    = pmd5sum

.PHONY: clean test uninstall

uninstall: clean
	@rm -rf "$(VIRTUAL_ENV)"

clean:
	@rm -rf {*.log,junit.xml,htmlcov,.coverage,coverage.xml,tests/__pycache__}
	@find . -iname "*.pyc" -exec rm {} \;

$(VIRTUAL_ENV):
	@virtualenv $(@)
	@. $(@)/bin/activate; pip install -Ur requirements.txt

test:	$(VIRTUAL_ENV) clean
	@. $(<)/bin/activate; cd $(MODULE) && python -m pytest ../tests --junit-xml=junit.xml --cov=. --cov-report=term --cov-report=html --cov-report=xml
	@mv $(MODULE)/junit.xml .
	@mv $(MODULE)/htmlcov .
	@mv $(MODULE)/coverage.xml .
	@mv $(MODULE)/.coverage .
