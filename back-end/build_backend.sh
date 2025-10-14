#!/bin/bash
set -e
pip install -r requirements.txt
pyinstaller --onefile --add-data "data:data" --name backend ap