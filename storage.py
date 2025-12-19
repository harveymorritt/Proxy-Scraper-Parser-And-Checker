import json
import csv
from typing import List
from pathlib import Path


def save_proxies(proxies: List[str], filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(proxies)))


def save_proxies_json(proxies: List[str], filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    data = [
        {
            "ip": p.split(':')[0],
            "port": int(p.split(':')[1]),
            "protocol": filepath.stem.split('_')[0]
        }
        for p in sorted(proxies)
    ]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)


def save_proxies_csv(proxies: List[str], filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(["ip", "port", "protocol"])
        protocol = filepath.stem.split('_')[0]
        for proxy in sorted(proxies):
            ip, port = proxy.split(':')
            writer.writerow([ip, port, protocol])


def load_proxies(filepath: Path) -> List[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []