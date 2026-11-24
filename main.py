import os

ENTRY = "v3.0.1: fixed a bug where the brain forgot why you walked into a room, then remembered in the doorway."
OUTPUT_PATH = '/output/entry.txt'

os.makedirs('/output', exist_ok=True)
with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
    f.write(ENTRY)
