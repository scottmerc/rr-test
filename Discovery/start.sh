#!/usr/bin/env bash
export PYENV_ROOT="$HOME/.pyenv"

pip3 install -r requirements.txt
HS_API_TOKEN=03dcc445a81c48a4a3731563cbf9dd78 UDID=99ff9bdd142aec39d5bf86ec3c8a29d508aa9133 python3 -m pytest test_discovery.py::TestDiscovery::test_ios -s --disable-warnings
HS_API_TOKEN=03dcc445a81c48a4a3731563cbf9dd78 HOSTNAME=dev-ca-tor-2-proxy-0-mac.headspin.io python3 -m pytest test_discovery.py::TestDiscovery::test_firetab -s --disable-warnings
