#!/usr/bin/env bash

set -e
set -x

python3 -V
python3 -m pip install --user poetry
python3 -m poetry install --with docs
python3 -m poetry run mkdocs build --site-dir public
