#!/bin/bash

echo "=================================="
echo "Enterprise DevSecOps Security Scan"
echo "=================================="

mkdir -p reports

REPORT="reports/security_report.txt"

echo "Security Scan Report" > "$REPORT"
echo "Generated on: $(date)" >> "$REPORT"
echo "" >> "$REPORT"

echo "Checking for exposed secrets..."

FOUND=0

PATTERNS=(
"AWS_ACCESS_KEY_ID"
"AWS_SECRET_ACCESS_KEY"
"GITHUB_TOKEN"
"API_KEY"
"SECRET_KEY"
"PRIVATE KEY"
"PASSWORD="
)

for PATTERN in "${PATTERNS[@]}"
do
    if grep -R "$PATTERN" . \
        --exclude-dir=.git \
        --exclude-dir=venv \
        --exclude-dir=__pycache__ \
        >/dev/null 2>&1
    then
        echo "[WARNING] $PATTERN found" | tee -a "$REPORT"
        FOUND=1
    fi
done

if [ $FOUND -eq 0 ]
then
    echo "[PASS] No exposed secrets detected." | tee -a "$REPORT"
fi

echo "" >> "$REPORT"
echo "Security Scan Completed." >> "$REPORT"
echo ""
echo "Checking Python dependencies..." | tee -a "$REPORT"

if [ -f app/requirements.txt ]
then
    echo "[PASS] requirements.txt found." | tee -a "$REPORT"
else
    echo "[FAIL] requirements.txt missing." | tee -a "$REPORT"
fi
echo ""
echo "Checking Dockerfile..." | tee -a "$REPORT"

if [ -f docker/Dockerfile ]
then
    echo "[PASS] Dockerfile found." | tee -a "$REPORT"
else
    echo "[FAIL] Dockerfile missing." | tee -a "$REPORT"
fi
echo ""
echo "Checking Docker Compose..." | tee -a "$REPORT"

if [ -f docker/docker-compose.yml ]
then
    echo "[PASS] docker-compose.yml found." | tee -a "$REPORT"
else
    echo "[FAIL] docker-compose.yml missing." | tee -a "$REPORT"
fi

