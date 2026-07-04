# dsa-question-bank

The **content bank** for the 100-Days-of-DSA automation system — contains all 120 DSA problems with solutions and tests.

📖 **[Pipeline Build Guide](https://4reeb-5yed.github.io/100-days-of-dsa/)** — Step-by-step instructions to build this CI/CD system

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
| array-hashing | 10 | Two Sum, Contains Duplicate, Valid Anagram |
| backtracking | 4 | Word Search, N-Queens |
| binary-search | 7 | Find Minimum, Search Rotated Array |
| bit-manipulation | 10 | Single Number, Reverse Bits |
| dynamic-programming | 15 | Climbing Stairs, Coin Change, House Robber |
| graphs | 14 | Number of Islands, Clone Graph, Course Schedule |
| heaps | 4 | Kth Largest Element, Median Data Stream |
| intervals | 10 | Merge Intervals, Meeting Rooms |
| linked-lists | 5 | Reverse Linked List, Merge Two Lists |
| sliding-window | 10 | Maximum Sum Subarray, Longest Substring |
| stacks | 14 | Valid Parentheses, Min Stack, Largest Rectangle |
| trees | 5 | Max Depth, Invert Tree, Validate BST |
| tries | 4 | Implement Trie, Word Search II |
| two-pointers | 8 | 3Sum, Container With Most Water |

## Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| Easy | 41 |
| Medium | 41 |
| Hard | 38 |

## Access

This repository is **read-only** for the automation. The `dsa-bot` uses a fine-grained PAT with only `contents: read` permissions.

## Related Repos

- **[dsa-bot](https://github.com/4reeb-5yed/dsa-bot)** — Orchestrator that reads from this bank
- **[100-days-of-dsa](https://github.com/4reeb-5yed/100-days-of-dsa)** — Output with solved problems
