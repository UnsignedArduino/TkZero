"""
Generate a badge for the PyLint score
"""

from pathlib import Path

import requests
from pylint.lint import Run

module_path = Path(r"..\TkZero")
badge_path = Path(r"..\assets\badges\pylint.svg")

results = Run([str(module_path)], do_exit=False)

score = round(results.linter.stats["global_note"], 2)
print(f"Score is {score}")

url = f"https://mperlet.github.io/pybadge/badges/{score}.svg"
print(f"URL is {repr(url)}")

response = requests.get(url)

if response.status_code == 200:
    print(f"Writing {len(response.content)} bytes to {repr(badge_path)}")
    badge_path.parent.mkdir(parents=True, exist_ok=True)
    badge_path.write_bytes(response.content)
else:
    print(f"Server returned {response.status_code}!")
    print(f"Content: {response.content}")
