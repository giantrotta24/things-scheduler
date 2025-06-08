from things.api import today

def get_today_tasks():
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
    print(f"High priority tasks: {len(high_priority)}")

    return medium_priority, high_priority


