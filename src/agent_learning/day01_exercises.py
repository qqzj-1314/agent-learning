"""第一天练习。

逐个完成带有 TODO 的函数。每完成一个函数，运行：
uv run pytest tests/test_day01_exercises.py -v
"""


def make_message(role: str, content: str) -> dict[str, str]:
    """返回包含 role 和 content 的消息字典。"""
    # TODO: 删除下一行，返回正确的字典。
    raise NotImplementedError


def format_welcome(name: str, goal: str) -> str:
    """返回：你好，名字！今天开始学习：目标。"""
    # TODO: 使用 f-string 生成欢迎语。
    raise NotImplementedError


def count_completed(tasks: list[dict[str, str | bool]]) -> int:
    """统计 completed 为 True 的任务数量。"""
    # TODO: 使用变量保存数量，再使用 for 和 if 完成统计。
    raise NotImplementedError


def get_pending_titles(tasks: list[dict[str, str | bool]]) -> list[str]:
    """返回所有未完成任务的标题。"""
    # TODO: 创建空列表，把未完成任务的 title 加进去。
    raise NotImplementedError


def choose_tool(question: str) -> str:
    """根据关键词返回 weather、calculator 或 chat。

    规则：
    - 包含“天气”时返回 weather。
    - 包含“计算”或“加”时返回 calculator。
    - 其他问题返回 chat。
    """
    # TODO: 使用 if 判断 question 中是否包含关键词。
    raise NotImplementedError
