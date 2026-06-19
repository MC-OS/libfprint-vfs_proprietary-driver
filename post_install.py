#!/usr/bin/env python3
import os
import subprocess

# Only run if we are installing to the actual system root
if not os.environ.get('DESTDIR'):
    print("Refreshing linker cache...")
    try:
        subprocess.run(['ldconfig'], check=True)
    except Exception as e:
        print(f"Failed to run ldconfig: {e}")