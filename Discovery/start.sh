#!/usr/bin/env bash
export PYENV_ROOT="$HOME/.pyenv"

cd /Users/scottmercer/Documents/Discovery/Scripts/updated-discovery/Discovery
pip3 install -r requirements.txt
HS_API_TOKEN=04015c97362a4458847cce0a9c1f1fe4 python3 -m pytest -s --disable-warnings
