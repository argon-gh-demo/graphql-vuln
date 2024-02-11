#!/bin/sh

gcc -Os -s -o tiny tiny.c
python linux_loader_fileless_malware.py "$(base64 tiny -w 0)"
echo "Entering endless loop"
while true; do
  sleep 10
done
