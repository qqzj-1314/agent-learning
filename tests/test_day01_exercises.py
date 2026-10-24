"""第一天练习的自动测试。"""

from agent_learning.day01_exercises import (
    choose_tool,
    count_completed,
    format_welcome,
    get_pending_titles,
    make_message,
)


def test_make_message() -> None:
    assert make_message("user", "你好") == {
        "role": "user",
        "content": "你好",
    }


def test_format_welcome() -> None:
    assert format_welcome("小明", "Python") == "你好，小明！今天开始学习：Python。"


def test_count_completed() -> None:
    tasks: list[dict[str, str | bool]] = [
        {"title": "学习变量", "completed": True},
        {"title": "学习函数", "completed": False},
        {"title": "运行测试", "completed": True},
    ]
    assert count_completed(tasks) == 2


def test_get_pending_titles() -> None:
    tasks: list[dict[str, str | bool]] = [
        {"title": "学习变量", "completed": True},
        {"title": "学习函数", "completed": False},
        {"title": "运行测试", "completed": False},
    ]
    assert get_pending_titles(tasks) == ["学习函数", "运行测试"]


def test_choose_tool() -> None:
    assert choose_tool("香港今天的天气怎么样？") == "weather"
    assert choose_tool("请计算 12 加 30") == "calculator"
    assert choose_tool("请解释什么是列表") == "chat"
