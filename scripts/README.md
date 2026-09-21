# log-monitor.sh / log_monitor.py

Multi-file log scanner with threshold alerting, error handling for missing
files, and structured CSV export (line numbers + timestamps).

## Usage
./log-monitor.sh <logfile1> [logfile2] ...
python3 log_monitor.py <logfile1> [logfile2] ...

## Exit codes
0 - ran successfully
1 - no log file arguments given
