#!/usr/bin/env python3
import sys

for logfile in sys.argv[1:]:
    print(f"=== Checking {logfile} ===")
    count = 0
    try:
        with open(logfile) as f:
            for line in f:
                if "ERROR" in line or "WARNING" in line:
                    print(line.strip())
                    count += 1
        print(f"Total issues in {logfile}: {count}")
        if count > 2:
            print(f"ALERT: {count} issues found in {logfile} — needs attention")
    except FileNotFoundError:
        print(f"SKIPPED: {logfile} not found (maybe rotated or archived?)")
    print()
