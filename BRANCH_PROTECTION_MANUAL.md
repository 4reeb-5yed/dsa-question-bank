# Manual Branch Protection Setup

The code changes to use PR-based state updates are complete in `dsa-bot/scripts/pick_and_commit.py`.

## Manual Steps Required

Due to token permissions, branch protection must be enabled manually:

### dsa-question-bank
1. Go to https://github.com/4reeb-5yed/dsa-question-bank/settings/branches
2. Click "Add branch protection rule"
3. Set "Branch name pattern" to `main`
4. Check:
   - ✅ "Require a pull request before merging"
   - ❌ Uncheck "Allow force pushes" (or leave unchecked for safety)
5. Click "Create"

### dsa-bot
1. Go to https://github.com/4reeb-5yed/dsa-bot/settings/branches
2. Click "Add branch protection rule"
3. Set "Branch name pattern" to `main`
4. Check:
   - ✅ "Require a pull request before merging"
   - ❌ Uncheck "Allow force pushes"
5. Click "Create"

## Verification After Setup

```bash
# Check dsa-question-bank
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/4reeb-5yed/dsa-question-bank/branches/main | \
  python3 -c "import json,sys; d=json.load(sys.stdin); print('Protected:', d.get('protected', False))"

# Check dsa-bot
curl -s -H "Authorization: token $GITHUB_TOKEN" \
  https://api.github.com/repos/4reeb-5yed/dsa-bot/branches/main | \
  python3 -c "import json,sys; d=json.load(sys.stdin); print('Protected:', d.get('protected', False))"
```

Expected output: `Protected: True` for both repos.
