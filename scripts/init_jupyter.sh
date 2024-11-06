#!/bin/bash

WORK_DIR="/home/onyxia/work"
CLONE_DIR="${WORK_DIR}/git_hackaton_llm_onyxia"

# Clone course repository
REPO_URL="https://github.com/IleDeFranceMobilites/hackathon_mobilite"
git clone --depth 1 $REPO_URL $CLONE_DIR

# Put relevant notebook in formation dir
cp "${CLONE_DIR}/notebooks/vector_db_template.ipynb" "${WORK_DIR}"
cp "${CLONE_DIR}/notebooks/rag_template.ipynb" "${WORK_DIR}"
cp "${CLONE_DIR}/notebooks/snippets_code.ipynb" "${WORK_DIR}"
cp -R "${CLONE_DIR}/notebooks/data" "${WORK_DIR}"
cp -R "${CLONE_DIR}/notebooks/images" "${WORK_DIR}"

# Install packages
pip install -r "${CLONE_DIR}/requirements.txt"

# Remove useless repository
rm -rf $CLONE_DIR

# Open the relevant notebook when starting Jupyter Lab
echo "c.LabApp.default_url = '/lab/tree/rag_template.ipynb'" >> /home/onyxia/.jupyter/jupyter_server_config.py
