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
├── scripts/
│   └── check_duplicates.py  # Verify no duplicate solutions
├── .gitignore       # Git ignore file
└── README.md
```

## Verification

```bash
# Check for duplicate solution_code in bank.json
python3 scripts/check_duplicates.py
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
| array-hashing | 12 | Two Sum, Contains Duplicate, Valid Anagram |
| backtracking | 7 | Word Search, N-Queens |
| binary-search | 6 | Find Minimum, Search Rotated Array |
| bit-manipulation | 8 | Single Number, Reverse Bits |
| design | 2 | LRU Cache, Min Stack |
| dynamic-programming | 15 | Climbing Stairs, Coin Change, House Robber |
| graphs | 13 | Number of Islands, Clone Graph, Course Schedule |
| greedy | 3 | Jump Game, Gas Station |
| heaps | 3 | Kth Largest Element, Median Data Stream |
| intervals | 7 | Merge Intervals, Meeting Rooms |
| linked-lists | 3 | Reverse Linked List, Merge Two Lists |
| math | 5 | Add Two Numbers, Multiply Strings |
| sliding-window | 8 | Maximum Sum Subarray, Longest Substring |
| stacks | 10 | Valid Parentheses, Min Stack, Largest Rectangle |
| strings | 2 | Longest Substring, Valid Palindrome |
| trees | 9 | Max Depth, Invert Tree, Validate BST |
| tries | 1 | Implement Trie |
| two-pointers | 6 | 3Sum, Container With Most Water |

## Difficulty Distribution

| Difficulty | Count |
|------------|-------|
| Easy | 38 |
| Medium | 55 |
| Hard | 27 |


## Related Repos

- **[dsa-bot](https://github.com/4reeb-5yed/dsa-bot)** — Orchestrator that reads from this bank
- **[100-days-of-dsa](https://github.com/4reeb-5yed/100-days-of-dsa)** — Output with solved problems
