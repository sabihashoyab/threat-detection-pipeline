import re

def parse_auth_log(logfile_path):
    pattern = re.compile(
        r'(?P<timestamp>\w{3}\s+\d+\s+\d{2}:\d{2}:\d{2}) .*sshd.* (?P<result>Failed|Accepted) password .* from (?P<ip>\d{1,3}(?:\.\d{1,3}){3})'
    )

    entries = []
    with open(logfile_path, 'r') as f:
        for line in f:
            match = pattern.search(line)
            if match:
                print("[MATCHED]", line.strip())  # DEBUG
                entries.append({
                    'timestamp': match.group('timestamp'),
                    'ip': match.group('ip'),
                    'result': match.group('result')
                })

    return entries




