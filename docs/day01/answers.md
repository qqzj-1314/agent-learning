# 第 1 天练习参考答案

建议先独立尝试，卡住超过 15 分钟再查看对应函数。

```python
def make_message(role: str, content: str) -> dict[str, str]:
    return {"role": role, "content": content}


def format_welcome(name: str, goal: str) -> str:
    return f"你好，{name}！今天开始学习：{goal}。"


def count_completed(tasks: list[dict[str, str | bool]]) -> int:
    completed_count = 0
    for task in tasks:
        if task["completed"]:
            completed_count += 1
    return completed_count


def get_pending_titles(tasks: list[dict[str, str | bool]]) -> list[str]:
    pending_titles = []
    for task in tasks:
        if not task["completed"]:
            pending_titles.append(str(task["title"]))
    return pending_titles


def choose_tool(question: str) -> str:
    if "天气" in question:
        return "weather"
    if "计算" in question or "加" in question:
        return "calculator"
    return "chat"
```

答案不是唯一的，只要行为满足测试要求，并且代码清楚易读即可。
