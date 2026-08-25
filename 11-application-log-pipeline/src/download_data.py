"""Prepara logs de aplicação a partir de logs Nginx reais (Elastic examples)."""
import json
import urllib.request
from pathlib import Path

URL = (
    "https://raw.githubusercontent.com/elastic/examples/master/"
    "Common%20Data%20Formats/nginx_logs/nginx_logs"
)
OUT = Path(__file__).resolve().parents[1] / "data" / "sample_logs.jsonl"


def parse_nginx_line(line: str) -> dict | None:
    parts = line.strip().split('"')
    if len(parts) < 3:
        return None
    try:
        status = int(parts[2].strip().split()[0])
    except (ValueError, IndexError):
        return None
    level = "ERROR" if status >= 500 else "WARN" if status >= 400 else "INFO"
    return {
        "service": "nginx",
        "level": level,
        "latency_ms": status * 3,
        "message": parts[1][:120],
    }


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    if OUT.exists():
        print(f"Dataset já existe: {OUT}")
        return

    req = urllib.request.Request(URL, headers={"User-Agent": "Mozilla/5.0"})
    lines = urllib.request.urlopen(req, timeout=60).read().decode("utf-8").splitlines()

    events = [e for line in lines[:100] if (e := parse_nginx_line(line))]
    OUT.write_text("\n".join(json.dumps(e) for e in events), encoding="utf-8")
    print(f"Dataset salvo: {OUT} ({len(events)} eventos)")


if __name__ == "__main__":
    main()
