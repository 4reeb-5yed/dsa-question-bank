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
├── solutions/       # Python solution files (day_001_*.py - day_120_*.py)
├── tests/           # Pytest test files (test_day_001_*.py - test_day_120_*.py)
├── .gitignore       # Git ignore file
└── README.md
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific problem tests
pytest tests/test_day_001_two_sum.py
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
| array-hashing | 13 | Two Sum, Contains Duplicate, Valid Anagram |
| backtracking | 7 | Word Search, N-Queens |
| binary-search | 5 | Find Minimum, Search Rotated Array |
| bit-manipulation | 8 | Single Number, Reverse Bits |
| design | 2 | LRU Cache, Min Stack |
| dynamic-programming | 16 | Climbing Stairs, Coin Change, House Robber |
| graphs | 13 | Number of Islands, Clone Graph, Course Schedule |
| greedy | 2 | Jump Game, Gas Station |
| heaps | 3 | Kth Largest Element, Median Data Stream |
| intervals | 7 | Merge Intervals, Meeting Rooms |
| linked-lists | 3 | Reverse Linked List, Merge Two Lists |
| math | 5 | Add Two Numbers, Multiply Strings |
| sliding-window | 8 | Maximum Sum Subarray, Longest Substring |
| stacks | 10 | Valid Parentheses, Min Stack, Largest Rectangle |
| strings | 2 | Longest Substring, Valid Palindrome |
| trees | 8 | Max Depth, Invert Tree, Validate BST |
| tries | 1 | Implement Trie |
| two-pointers | 7 | 3Sum, Container With Most Water |

## Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| Easy | 39 |
| Medium | 55 |
| Hard | 26 |

## Access

This repository is **read-only** for the automation. The `dsa-bot` uses a fine-grained PAT with only `contents: read` permissions.

## Related Repos

- **[dsa-bot](https://github.com/4reeb-5yed/dsa-bot)** — Orchestrator that reads from this bank
- **[100-days-of-dsa](https://github.com/4reeb-5yed/100-days-of-dsa)** — Output with solved problems
