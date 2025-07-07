# Threat Detection & Log Analysis Pipeline (Python)

A Python-based command-line tool that parses system and web server logs to detect security anomalies, enrich suspicious IPs with geolocation data, and generate clean, human-readable CSV/JSON reports. Includes optional visualizations to reveal attack trends and behavioral patterns over time.

---

## Key Features

- Parses `/var/log/auth.log` or Apache access logs
- Detects:
  - Failed login bursts
  - Suspicious IP addresses
  - Root login events or privilege escalations
- Enriches IPs using GeoIP or ipinfo.io APIs
- Outputs enriched threat reports in CSV and JSON
- Built as a flexible CLI tool with flag-based configuration
- Optional visualizations: attack heatmaps, login histograms, trend charts

---

## Getting Started

### Requirements

- Python 3.8+
- Install dependencies:

```bash
pip install -r requirements.txt
```

### Run the Tool

```bash
python detect.py --logfile sample_logs/auth.log --output reports/report.csv
```

### CLI Options

| Option         | Description                                |
|----------------|--------------------------------------------|
| `--logfile`    | Path to your log file                      |
| `--output`     | Output file name (CSV or JSON)             |
| `--format`     | (Optional) Output format: csv or json      |
| `--geo`        | (Optional) Enable GeoIP enrichment         |
| `--visualize`  | (Optional) Generate charts and summaries   |

---

## Visual Output Examples

Optional data science analysis using pandas and matplotlib.

- Histogram of failed login attempts per hour  
- Map of IP geolocations  
- Anomaly spikes in login activity

![Login Attempts](screenshots/login_histogram.png)  
![IP Heatmap](screenshots/ip_map.png)

---

## How Detection Works

- IPs with 5+ failed login attempts in under 1 minute are flagged
- GeoIP API appends metadata: country, city, ISP, ASN
- Root logins and SSH brute-force indicators are extracted and tagged
- Report fields include timestamp, username, IP address, location data, and event type

---

## Project Structure

```
threat-log-pipeline/
├── detect.py                # Main CLI tool
├── geoip/                   # IP enrichment logic
│   └── ip_lookup.py
├── visualizations/          # Optional charts and visuals
│   └── charts.py
├── sample_logs/             # Example log files
├── reports/                 # Output directory
├── screenshots/             # Visual proof
└── requirements.txt
```

---

## Example Use Cases

- Security log forensics during an incident response
- Lightweight intrusion detection for personal or home servers
- Baseline attack pattern visualization across geographies
- Portfolio project demonstrating cybersecurity, Python, and data analysis

---

## Tech Stack

- Python 3.8+
- pandas, matplotlib for analytics
- argparse for CLI parsing
- requests for external GeoIP lookups
- Logs: Linux `/var/log/auth.log`, Apache access logs

---

## License

This project is licensed under the MIT License.

---

## Credits

IP enrichment via ipinfo.io  
Inspiration from common SIEM playbooks and analyst workflows.

---
