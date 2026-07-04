# dsa-question-bank

The **content bank** for the 100-Days-of-DSA automation system — contains all 120 DSA problems with solutions and tests.

## Overview

This repository holds the curated collection of Data Structures and Algorithms problems that power the daily automation. Each entry includes:
- Problem statement
- Solution code (Python)
- Test cases
- Metadata (topic, difficulty, slug)

## Repository Structure

```
├── problems/
│   └── bank.json    # Main problem bank (120 problems)
└── README.md
```

## Problem Bank Schema

Each problem in `bank.json` follows this structure:

```json
{
  "id": 1,
  "slug": "two-sum",
  "title": "Two Sum",
  "difficulty": "easy",
  "topic": "array-hashing",
  "statement": "Given an array and target...",
  "solution_code": "def two_sum(nums, target):\n    ...",
  "test_code": "from solutions.day_001_two_sum import two_sum\n\ndef test_two_sum_basic():\n    ..."
}
```

## Topics Covered

| Topic | Count | Examples |
|-------|-------|----------|
| array-hashing | ~15 | Two Sum, Contains Duplicate, Valid Anagram |
| two-pointers | ~10 | 3Sum, Container With Most Water |
| binary-search | ~10 | Find Minimum, Search Rotated Array |
| sliding-window | ~10 | Maximum Sum Subarray |
| stacks | ~8 | Valid Parentheses |
| dynamic-programming | ~20 | Fibonacci, Climbing Stairs |
| graphs | ~15 | Number of Islands, Clone Graph |
| intervals | ~8 | Merge Intervals |
| bit-manipulation | ~8 | Single Number |
| linked-lists | ~8 | Reverse Linked List |
| trees | ~10 | Binary Tree Inversion |
| tries | ~3 | Implement Trie |
| heaps | ~5 | Kth Largest Element |

## Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| Easy | ~35 |
| Medium | ~50 |
| Hard | ~35 |

## Access

This repository is **read-only** for the automation. The `dsa-bot` uses a fine-grained PAT with only `contents: read` permissions.

## Related Repos

- **[dsa-bot](https://github.com/4reeb-5yed/dsa-bot)** — Orchestrator that reads from this bank
- **[100-days-of-dsa](https://github.com/4reeb-5yed/100-days-of-dsa)** — Output with solved problems
