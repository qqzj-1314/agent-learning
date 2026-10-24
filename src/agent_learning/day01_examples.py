"""第一天示例：Python 基础和 Agent 常见数据结构。"""


def make_message(role: str, content: str) -> dict[str, str]:
    """创建一条模型消息。"""
    return {
        "role": role,
        "content": content,
    }


def choose_tool(question: str) -> str:
    """根据问题中的关键词选择一个简单工具。"""
    if "天气" in question:
        return "weather"
    if "计算" in question or "加" in question:
        return "calculator"
    return "chat"


def main() -> None:
    """运行第一天的完整示例。"""
    student_name = "初学者"
    study_goal = "成为 Agent 开发工程师"
    study_day = 1
    is_ready = True

    print("=== 基本类型 ===")
    print(f"姓名：{student_name}")
    print(f"目标：{study_goal}")
    print(f"学习天数：{study_day}")
    print(f"环境是否准备好：{is_ready}")

    topics = ["变量", "列表", "字典", "条件判断", "函数"]
    print("\n=== 今日主题 ===")
    for index, topic in enumerate(topics, start=1):
        print(f"{index}. {topic}")

    messages = [
        make_message("system", "你是一名耐心的 Python 学习助手。"),
        make_message("user", "请解释 Python 函数。"),
    ]

    print("\n=== Agent 消息 ===")
    for message in messages:
        print(f"{message['role']}: {message['content']}")

    questions = [
        "香港今天的天气怎么样？",
        "请计算 12 加 30",
        "请解释什么是列表",
    ]

    print("\n=== 简单工具选择 ===")
    for question in questions:
        selected_tool = choose_tool(question)
        print(f"问题：{question}")
        print(f"选择：{selected_tool}")


if __name__ == "__main__":
    main()
