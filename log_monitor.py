#!/usr/bin/env python3
import sys
import json
import csv

def check_log(logfile):
    print(f"=== Checking {logfile} ===")
    count = 0
    records = []
    try:
        with open(logfile) as f:
            for line_number, line in enumerate(f, start=1):
                if "ERROR" in line or "WARNING" in line:
                    print(line.strip())
                    count += 1
                    records.append((logfile, line_number, line.strip()))
        print(f"Total issues in {logfile}: {count}")
        if count > 2:
            print(f"ALERT: {count} issues found in {logfile} — needs attention")
        return count, records
    except FileNotFoundError:
        print(f"SKIPPED: {logfile} not found (maybe rotated or archived?)")
        return "SKIPPED - file not found", []

summary = {}
all_records = []
for logfile in sys.argv[1:]:
    result, records = check_log(logfile)
    if result != 0:
        summary[logfile] = result
    all_records.extend(records)
    print()

print("=== Summary Report ===")
print(summary)
print(json.dumps(summary))

with open("detailed_report.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Log File", "Line Number", "Details (includes timestamp)"])
    for row in all_records:
        writer.writerow(row)
