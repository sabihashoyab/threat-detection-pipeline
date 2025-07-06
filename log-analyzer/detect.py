import argparse
import json
import csv
from parser import parse_auth_log
from enrich import enrich_ip

def load_rules():
    with open('rules.json', 'r') as f:
        return json.load(f)

def detect_threats(entries, rules):
    failed_count = {}
    for entry in entries:
        ip = entry['ip']
        if entry['result'] == 'Failed':
            failed_count[ip] = failed_count.get(ip, 0) + 1

    enriched_results = []
    for entry in entries:
        ip = entry['ip']
        enriched = enrich_ip(ip)
        enriched_entry = {
            **entry,
            **enriched,
            'failed_logins': failed_count.get(ip, 0),
            'suspicious': failed_count.get(ip, 0) >= rules['failed_login_threshold'] or
                          enriched.get('country') in rules['blocklisted_countries']
        }
        enriched_results.append(enriched_entry)

    return enriched_results

def save_to_csv(data, path):
    if not data:
        return
    with open(path, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def save_to_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f, indent=2)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--logfile', required=True, help='Path to log file')
    parser.add_argument('--output', default='reports/output.csv', help='CSV output file')
    parser.add_argument('--jsonreport', default='reports/output.json', help='JSON output file')
    args = parser.parse_args()

    print(f"[+] Parsing log: {args.logfile}")
    entries = parse_auth_log(args.logfile)

    print(f"[+] Loaded {len(entries)} login entries")

    rules = load_rules()
    results = detect_threats(entries, rules)

    save_to_csv(results, args.output)
    save_to_json(results, args.jsonreport)

    print(f"[+] Detection complete. CSV saved to {args.output} and JSON to {args.jsonreport}")

if __name__ == '__main__':
    main()
