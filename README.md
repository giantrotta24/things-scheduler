# Things Scheduler

Random python script I'm working on to automate part of my weekly review process.

Goal is to write a script that:

- [ ] parses my todo list
- [ ] serializes the data
- [ ] passes it to an AI model
- [ ] model suggests a schedule for tasks
- [ ] script updates my calendar accordingly

## Possible project structure

```
things-scheduler/
│
├── read_today.py               # Temporary scratch or CLI runner
├── main.py                     # Main entry point for production run
│
├── scheduler/                  # All your core logic lives here
│   ├── __init__.py
│   ├── serializer.py           # TaskSerializer lives here
│   ├── task_fetcher.py         # Functions to query and filter from Things
│   ├── calendar_writer.py      # (Future) functions to create events
│   └── constants.py            # Tag-effort mappings, etc.
│
├── tests/                      # (Optional, later) unit tests
│   ├── __init__.py
│   └── test_serializer.py
│
├── requirements.txt            # List of pip dependencies
└── README.md                   # Project overview and usage
```

