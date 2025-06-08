TAG_EFFORT_MAPPING = {
    "quick n easy": "quick",
    "evening": "evening",
    "about town": "about town",
    "heavy lifts": "heavy",
    "rvshare": "rvshare",
    "michelle": "michelle",
    "friends": "friends",
}

EFFORT_DURATION = {
    "quick": 30,
    "evening": 60,
    "about town": 45,
    "heavy": 90,
    "rvshare": 60,
    "michelle": 30,
    "friends": 30,
}


class TaskSerializer:
    def __init__(self, task):
        self.task = task
        self.tags = set(task.get("tags", []))

    def serialize(self) -> dict:
        effort = self.get_effort()
        return {
            "title": self.task.get("title", ""),
            "tags": list(self.tags),
            "priority": self.get_priority(),
            "effort": effort,
            "duration": EFFORT_DURATION.get(effort, 0),
            "project": self.task.get("project_title", ""),
            "area": self.task.get("area_title", ""),
            "notes": self.task.get("notes", ""),
            "deadline": self.task.get("deadline", ""),
            "created_at": self.task.get("created", ""),
            "today_index": self.task.get("today_index", 0),
        }

    def get_priority(self) -> str:
        if "High" in self.tags:
            return "High"
        elif "Medium" in self.tags:
            return "Medium"
        else:
            return "Unknown"

    def get_effort(self) -> str:
        for tag in self.tags:
            if tag in TAG_EFFORT_MAPPING:
                return TAG_EFFORT_MAPPING[tag]
        return "Unknown"


