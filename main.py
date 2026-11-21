import os

POEM = """Two hands on one handle.
Neither turns it.
Each waits to feel
the other decide.

Then pressure, shared,
no telling whose,
and the door gives.

Later, asked who chose,
we each said I did,
and neither of us lied.
"""

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(POEM)
