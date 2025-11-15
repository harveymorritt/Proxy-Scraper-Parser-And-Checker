from typing import List
from pathlib import Path


def save_proxies(proxies: List[str], filepath: Path) -> None:
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('\n'.join(sorted(proxies)))


def load_proxies(filepath: Path) -> List[str]:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]
    except FileNotFoundError:
        return []