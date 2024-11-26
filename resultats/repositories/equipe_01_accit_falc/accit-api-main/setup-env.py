#!/usr/bin/env python3
"""Initialize a new FastAPI project with standard structure and configuration."""

import os
import subprocess
from pathlib import Path


def create_directory_structure():
    """Create the project directory structure."""
    directories = [
        "app",
        "app/api",
        "app/api/routes",
        "app/core",
        "app/db",
        "app/models",
        "app/services",
        "app/utils",
        "tests",
    ]

    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        # Create __init__.py files in each directory
        (Path(directory) / "__init__.py").touch()


def create_config_files():
    """Create configuration files."""
    # Create .gitignore
    gitignore_content = """
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# PyInstaller
#  Usually these files are written by a python script from a template
#  before PyInstaller builds the exe, so as to inject date/other infos into it.
*.manifest
*.spec

# Installer logs
pip-log.txt
pip-delete-this-directory.txt

# Unit test / coverage reports
htmlcov/
.tox/
.nox/
.coverage
.coverage.*
.cache
nosetests.xml
coverage.xml
*.cover
*.py,cover
.hypothesis/
.pytest_cache/
cover/

# Translations
*.mo
*.pot

# Django stuff:
*.log
local_settings.py
db.sqlite3
db.sqlite3-journal

# Flask stuff:
instance/
.webassets-cache

# Scrapy stuff:
.scrapy

# Sphinx documentation
docs/_build/

# PyBuilder
.pybuilder/
target/

# Jupyter Notebook
.ipynb_checkpoints

# IPython
profile_default/
ipython_config.py

# pyenv
#   For a library or package, you might want to ignore these files since the code is
#   intended to run in multiple environments; otherwise, check them in:
# .python-version

# pipenv
#   According to pypa/pipenv#598, it is recommended to include Pipfile.lock in version control.
#   However, in case of collaboration, if having platform-specific dependencies or dependencies
#   having no cross-platform support, pipenv may install dependencies that don't work, or not
#   install all needed dependencies.
#Pipfile.lock

# poetry
#   Similar to Pipfile.lock, it is generally recommended to include poetry.lock in version control.
#   This is especially recommended for binary packages to ensure reproducibility, and is more
#   commonly ignored for libraries.
#   https://python-poetry.org/docs/basic-usage/#commit-your-poetrylock-file-to-version-control
#poetry.lock

# pdm
#   Similar to Pipfile.lock, it is generally recommended to include pdm.lock in version control.
#pdm.lock
#   pdm stores project-wide configurations in .pdm.toml, but it is recommended to not include it
#   in version control.
#   https://pdm.fming.dev/latest/usage/project/#working-with-version-control
.pdm.toml
.pdm-python
.pdm-build/

# PEP 582; used by e.g. github.com/David-OConnor/pyflow and github.com/pdm-project/pdm
__pypackages__/

# Celery stuff
celerybeat-schedule
celerybeat.pid

# SageMath parsed files
*.sage.py

# Environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# Spyder project settings
.spyderproject
.spyproject

# Rope project settings
.ropeproject

# mkdocs documentation
/site

# mypy
.mypy_cache/
.dmypy.json
dmypy.json

# Pyre type checker
.pyre/

# pytype static type analyzer
.pytype/

# Cython debug symbols
cython_debug/

# PyCharm
#  JetBrains specific template is maintained in a separate JetBrains.gitignore that can
#  be found at https://github.com/github/gitignore/blob/main/Global/JetBrains.gitignore
#  and can be added to the global gitignore or merged into this file.  For a more nuclear
#  option (not recommended) you can uncomment the following to ignore the entire idea folder.
.idea/
"""

    with open(".gitignore", "w") as f:
        f.write(gitignore_content.strip())

    # Create requirements.txt
    requirements_content = """
fastapi
uvicorn
pydantic
pydantic-settings
elasticsearch
duckdb
python-dotenv
langchain
langchain-community
langchain-openai
ruff
websockets
httpx
s3fs
pandas
llama-cpp-python
huggingface_hub[cli]
pytest
"""

    with open("requirements.txt", "w") as f:
        f.write(requirements_content.strip())

    # Create ruff.toml
    ruff_content = """
line-length = 88
target-version = "py39"

[lint]
select = ["E", "F", "B", "I"]
ignore = []

[format]
quote-style = "double"
indent-style = "space"
skip-magic-trailing-comma = false
line-ending = "auto"
"""

    with open("ruff.toml", "w") as f:
        f.write(ruff_content.strip())

    # Create .env
    env_content = """
ELASTICSEARCH_URL=http://localhost:9200
DUCKDB_PATH=./data/transport.db
IDFM_API_KEY=your_key_here
VELIB_API_KEY=your_key_here
GEOVELO_API_KEY=your_key_here
LLM_API_KEY=your_key_here
"""

    with open(".env", "w") as f:
        f.write(env_content.strip())


def initialize_git():
    """Initialize git repository."""
    subprocess.run(["git", "init"], check=True)
    subprocess.run(["git", "add", "."], check=True)
    subprocess.run(["git", "commit", "-m", "chore(init): init env and project structure"], check=True)


def setup_virtual_environment():
    """Create and activate virtual environment."""
    subprocess.run(["python", "-m", "venv", "venv"], check=True)

    # Print activation instructions
    print("\nTo activate the virtual environment:")
    print("On Windows: .\\venv\\Scripts\\activate")
    print("On Unix/MacOS: source venv/bin/activate")


def main():
    """Main function to run all initialization steps."""
    print("🚀 Initializing new FastAPI project...")

    print("\n📁 Creating directory structure...")
    create_directory_structure()

    print("⚙️  Creating configuration files...")
    create_config_files()

    print("🔧 Initializing git repository...")
    initialize_git()

    print("🐍 Setting up virtual environment...")
    setup_virtual_environment()

    print("\n✨ Project initialization complete!")
    print("\nNext steps:")
    print("1. Activate the virtual environment")
    print("2. Run: pip install -r requirements.txt")
    print("3. Start coding in the app directory!")


if __name__ == "__main__":
    main()
