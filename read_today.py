from things.api import today

# Fetch all tasks Things would show in the "Today" view
today_tasks = today(trashed=False)

medium_priority = []
high_priority = []

for task in today_tasks:
    tags = set(task.get('tags', []))

    # tasks with both medium and high priority are visual "dividers" so can be ignored
    if "Medium" in tags and "High" in tags:
        continue

    if "Medium" in tags:
        medium_priority.append(task)

    if "High" in tags:
        high_priority.append(task)

print(f"Medium priority tasks: {len(medium_priority)}")
for task in medium_priority[:5]:
    print(task)

print(f"High priority tasks: {len(high_priority)}")
for task in high_priority[:5]:
    print(task)





