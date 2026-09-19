#!/bin/bash
# checking.sh -- scan one or more log files for ERROR/WARNING lines,
#and flag any file with more than 2 matches
#
#
#!/bin/bash
# checklog.sh - scan one or more log files for ERROR/WARNING lines,
# and flag any file with more than 2 matches

if [ "$#" -eq 0 ]; then
    echo "Usage: $0 <logfile1> [logfile2] ..."
    exit 1
fi

for LOGFILE in "$@"; do
    echo "=== Checking $LOGFILE ==="
    grep -E "ERROR|WARNING" "$LOGFILE" | tail -n 20

    COUNT=$(grep -cE "ERROR|WARNING" "$LOGFILE")
    if [ "$COUNT" -gt 2 ]; then
        echo "ALERT: $COUNT issues found in $LOGFILE — needs attention"
    fi
    echo
done
