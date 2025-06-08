from services.things import get_today_tasks
from serializers.task_serializer import TaskSerializer

def main():
    print("Getting today's tasks...🤪")
    medium_priority, high_priority = get_today_tasks()
    all_tasks = medium_priority + high_priority

    print("Serializing tasks...🤪")
    for task in all_tasks:
        serializer = TaskSerializer(task)
        print(serializer.serialize())

    print("Done! 🎉")


if __name__ == "__main__":
    main()
