#!/usr/bin/env bash

# This script is used to build the documentation on CloudFlare Pages, this is just used for build previews
# A different script with the same name exists on the `docs-site` branch (where pre-built docs live).

set -e
set -x

python3 -V

python3 -m pip install --user poetry

python3 -m poetry install --only docs

python3 -m poetry shell

python3 -m mkdocs build
