#!/usr/bin/env bash
export PYENV_ROOT="$HOME/.pyenv"

pip3 install -r requirements.txt
HS_API_TOKEN=03dcc445a81c48a4a3731563cbf9dd78 HOSTNAME=dev-ca-tor-2-proxy-0-mac.headspin.io python3 -m pytest -s --disable-warnings
