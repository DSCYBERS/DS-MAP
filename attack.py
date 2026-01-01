#!/usr/bin/env python3
import subprocess
import os

# Get target from environment variable
target = os.environ.get('DSCYBER_TARGET', "http://testphp.vulnweb.com/")
attack_sequence = f"0\n{target}\nC\nyes\n1\n"

process = subprocess.Popen(
    ["python", "dscyber.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.STDOUT,
    text=True,
    encoding='utf-8',
    errors='replace'
)

stdout, _ = process.communicate(input=attack_sequence)
print(stdout)
