#!/usr/bin/env python3
"""
Check for duplicate solution_code in bank.json
Fails if any two entries share the same solution_code hash.
"""
import json
import hashlib
from collections import defaultdict

def hash_code(code: str) -> str:
    return hashlib.sha256(code.encode()).hexdigest()[:16]

def main():
    with open('problems/bank.json') as f:
        bank = json.load(f)
    
    hash_to_entries = defaultdict(list)
    for entry in bank:
        h = hash_code(entry['solution_code'])
        hash_to_entries[h].append((entry['id'], entry['slug'], entry['title']))
    
    duplicates = {h: entries for h, entries in hash_to_entries.items() if len(entries) > 1}
    
    if duplicates:
        print("DUPLICATE solution_code FOUND:")
        for h, entries in duplicates.items():
            print(f"  Hash: {h}")
            for eid, slug, title in entries:
                print(f"    id={eid} slug={slug} title={title}")
        print(f"\nTotal: {len(duplicates)} duplicate groups found")
        return 1
    else:
        print(f"CLEAN: No duplicate solution_code found across {len(bank)} entries")
        return 0

if __name__ == '__main__':
    exit(main())
