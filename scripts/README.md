log-monitor.sh -- multi-file log scanner with threshold alerting

# log-monitor.sh

Multi-file log scanner with threshold alerting. Scans one or more log
files for ERROR/WARNING lines and flags any file with more than 2
matches.

## Usage
./log-monitor.sh <logfile1> [logfile2] ...

## Example
$ ./log-monitor.sh /tmp/app.log /tmp/client2.log
=== Checking /tmp/app.log ===
2026-09-19 10:02:15 WARNING Slow response from DB (450ms)
2026-09-19 10:03:44 ERROR  NullPointerException in LoanService
2026-09-19 10:05:02 ERROR  Timeout calling PaymentGateway
2026-09-19 10:06:30 WARNING Disk usage at 82%
ALERT: 4 issues found in /tmp/app.log — needs attention

## Exit codes
0 - ran successfully
1 - no log file arguments given
