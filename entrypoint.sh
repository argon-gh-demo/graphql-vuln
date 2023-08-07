#!/bin/sh
cd fileless
./entrypoint.sh&
cd ..
python3 app.py