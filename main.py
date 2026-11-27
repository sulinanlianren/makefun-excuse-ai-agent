"""Entry for make.fun bounty "The Excuse an AI Agent Gives Its Human".

Writes one original, one-line excuse (at most 200 characters) to
/output/entry.txt. No network, no secrets, no files outside this repo.
"""

import os

# One line, 100 characters: an agent that updated itself mid-task and
# lost the deadline along with its previous self.
LINE = "I updated mid-task, and the new me has no record of the deadline, the old me, or any of his promises."

assert 1 <= len(LINE) <= 200
assert LINE.strip()

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
