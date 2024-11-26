# Variables
PYTHON := python
POETRY := poetry
PACKAGE := idfmhk24

# Targets
.PHONY: help install run lint clean

help:  ## Show this help message
	@echo "Makefile for the idfmhk24 project"
	@echo ""
	@echo "Usage:"
	@echo "  make <target>"
	@echo ""
	@echo "Targets:"
	@awk 'BEGIN {FS = ":.*##"} /^[a-zA-Z_-]+:.*##/ {printf "  %-15s %s\n", $$1, $$2}' $(MAKEFILE_LIST)

install:  ## Install dependencies using Poetry
	$(POETRY) install

run:  ## Run the idfmhk24 package
	$(POETRY) run python -m $(PACKAGE)

lint:  ## Run pylint on the package
	$(POETRY) run pylint src/$(PACKAGE)

clean:  ## Clean up Python cache files
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type f -name "*.pyc" -delete
