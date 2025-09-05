## Test GitHub Actions Workflow (Manual Trigger)

This repo contains a minimal Python script and a GitHub Actions workflow you can run manually with a button.

### What's included
- `hello.py`: prints a greeting with the current UTC time and writes it to `output.txt`.
- `.github/workflows/manual-test.yml`: a workflow with `workflow_dispatch` (button trigger) that runs `hello.py`.
- `.gitignore`: ignores common Python build artifacts and virtualenvs.

### How to use
1. Push this repository to GitHub.
2. In your GitHub repo, go to the **Actions** tab.
3. Select the workflow named **Manual Test**.
4. Click **Run workflow** to trigger it.

The workflow will:
- Check out your code
- Set up Python 3.11
- Run `python hello.py`
- Upload `output.txt` as an artifact named `hello-output`

### Run locally (optional)
```bash
python hello.py
```


