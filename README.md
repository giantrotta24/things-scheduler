# Things Scheduler

A Python script that analyzes your daily tasks from the Things app and prepares them for scheduling automation.

## What it does

Currently, the script:

- ✅ **Fetches today's tasks** from Things app
- ✅ **Filters by priority** (Medium and High priority tags)
- ✅ **Serializes task data** with structured information including:
  - Task title, tags, and priority
  - Effort level and estimated duration (based on tag mappings)
  - Project, area, notes, and deadlines
  - Creation date and today index

## Tag-based effort mapping

The script recognizes these effort tags and assigns durations:
- `quick n easy` → 30 minutes
- `heavy lifts` → 90 minutes
- `evening` → 60 minutes
- `about town` → 45 minutes
- `rvshare`, `michelle`, `friends` → 30-60 minutes each

## Future goals

- [ ] Pass serialized data to an AI model
- [ ] Generate suggested schedule for tasks
- [ ] Automatically update calendar with scheduled tasks

## Usage

```bash
python main.py
```

**Requirements:** `things.py==0.0.15`

Install with: `pip install -r requirements.txt`
