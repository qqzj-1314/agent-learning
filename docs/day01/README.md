# 第 1 天：Python 基础与 Agent 数据结构

建议用时：2～3 小时。今天不调用模型 API，目标是先学会读写 Agent 程序中最常见的数据。

## 今天学完应该会什么

完成今天的学习后，你应该能够：

1. 使用 `uv run` 运行 Python 程序。
2. 理解字符串、整数、浮点数和布尔值。
3. 使用列表保存多条消息。
4. 使用字典描述一条消息或一个任务。
5. 使用 `if` 做条件判断，使用 `for` 遍历数据。
6. 编写带参数、返回值和类型提示的函数。
7. 看懂一个简单的 Agent 工具选择逻辑。
8. 使用 pytest 检查自己的答案。

## 0. 开始前准备

打开 PowerShell：

```powershell
cd "D:\Python学习\agent-learning"
code .
```

在 VS Code 中打开终端，确认项目环境：

```powershell
uv run python --version
```

输出应为 Python 3.12。

然后运行今天的完整示例：

```powershell
uv run python -m agent_learning.day01_examples
```

先观察输出，再打开 `src/agent_learning/day01_examples.py` 对照代码阅读。

## 1. 变量和基本类型

变量可以理解为“给一个值取名字”：

```python
student_name = "小明"       # str：字符串
study_days = 1             # int：整数
progress = 0.1             # float：小数
is_ready = True            # bool：真或假
```

可以使用 `type()` 查看类型：

```python
print(type(student_name))
print(type(study_days))
```

变量名建议：

- 使用有意义的英文名称。
- 多个单词使用下划线，例如 `study_days`。
- 不要使用 `list`、`str`、`dict` 等内置名称作为变量名。

### 字符串格式化

推荐使用 f-string：

```python
name = "小明"
goal = "学习 Agent 开发"
message = f"你好，{name}！你的目标是：{goal}。"
print(message)
```

## 2. 列表：保存一组数据

Agent 的对话通常由多条消息组成，所以经常使用列表：

```python
topics = ["Python", "FastAPI", "工具调用"]

print(topics[0])       # 第一项，索引从 0 开始
print(len(topics))     # 列表长度

topics.append("RAG")  # 在末尾增加一项
```

遍历列表：

```python
for topic in topics:
    print(topic)
```

同时获得序号：

```python
for index, topic in enumerate(topics, start=1):
    print(f"{index}. {topic}")
```

## 3. 字典：描述一个对象

一条模型消息通常可以表示为字典：

```python
message = {
    "role": "user",
    "content": "请帮我制定学习计划",
}

print(message["role"])
print(message["content"])
```

字典由“键和值”组成：

```text
role     → user
content  → 请帮我制定学习计划
```

多条消息就是“列表中放字典”：

```python
messages = [
    {"role": "system", "content": "你是一名学习助手"},
    {"role": "user", "content": "解释什么是函数"},
]
```

这种结构以后会经常出现在模型 API、工具参数、RAG 结果和 Agent 状态中。

## 4. 条件判断

程序可以根据条件选择不同路径：

```python
question = "帮我查询北京天气"

if "天气" in question:
    tool = "weather"
elif "计算" in question:
    tool = "calculator"
else:
    tool = "chat"

print(tool)
```

注意：

- `=` 是赋值。
- `==` 是比较两个值是否相等。
- `in` 可以检查字符串或列表中是否包含某项。
- Python 使用缩进表示代码层级，通常使用 4 个空格。

## 5. 循环

使用 `for` 依次处理列表中的每一项：

```python
tasks = [
    {"title": "学习变量", "completed": True},
    {"title": "学习函数", "completed": False},
]

for task in tasks:
    if task["completed"]:
        print(f"已完成：{task['title']}")
    else:
        print(f"未完成：{task['title']}")
```

今天先掌握 `for`。`while` 会在后续需要重复执行 Agent 步骤时再学习。

## 6. 函数和类型提示

函数把一段逻辑封装起来，以后可以重复使用：

```python
def make_message(role: str, content: str) -> dict[str, str]:
    return {
        "role": role,
        "content": content,
    }
```

调用函数：

```python
user_message = make_message("user", "你好")
print(user_message)
```

逐部分理解：

```text
def                 定义函数
make_message        函数名称
role、content       输入参数
str                 参数应该是字符串
dict[str, str]      返回“键和值都是字符串”的字典
return              把结果交给调用者
```

类型提示主要帮助编辑器和开发者发现错误，并不会自动阻止所有错误输入。

## 7. 今天的练习

打开：

```text
src/agent_learning/day01_exercises.py
```

完成其中 5 个函数：

1. `make_message`：创建消息字典。
2. `format_welcome`：生成欢迎语。
3. `count_completed`：统计已完成任务。
4. `get_pending_titles`：找出未完成任务的标题。
5. `choose_tool`：根据问题选择工具。

第一次运行测试：

```powershell
uv run pytest tests/test_day01_exercises.py -v
```

刚开始看到失败是正常的。每完成一个函数就重新运行测试，目标是最后看到：

```text
5 passed
```

如果卡住超过 15 分钟，可以查看 `docs/day01/answers.md`，但建议先自己尝试。

## 8. 建议学习顺序

### 第 1 阶段：运行和观察，约 20 分钟

1. 运行 `day01_examples.py`。
2. 修改姓名、学习目标和问题内容。
3. 再运行一次，观察输出变化。

### 第 2 阶段：边抄边理解，约 40 分钟

1. 自己重新输入一个列表和字典。
2. 使用 `for` 打印列表内容。
3. 使用 `if` 判断任务是否完成。
4. 自己写一个接收姓名并返回欢迎语的函数。

### 第 3 阶段：完成练习，约 60～90 分钟

1. 一次只完成一个函数。
2. 每完成一个函数就运行 pytest。
3. 根据错误信息定位失败的函数。
4. 全部通过后运行 Ruff。

```powershell
uv run ruff check .
uv run ruff format .
```

## 9. 今天的验收问题

不看资料，尝试回答：

1. 列表和字典有什么区别？
2. 为什么模型消息适合用字典表示？
3. `=` 和 `==` 有什么区别？
4. `return` 与 `print` 有什么区别？
5. 为什么函数要写参数和返回值？
6. `list[dict[str, str]]` 表示什么？
7. 如何在项目环境中运行 Python 文件？

能够回答其中至少 5 个，并完成全部测试，就可以结束第一天。

## 10. 延伸阅读

- [Python 官方中文教程：Python 速览](https://docs.python.org/zh-cn/3/tutorial/introduction.html)
- [Python 官方中文教程：控制流](https://docs.python.org/zh-cn/3/tutorial/controlflow.html)
- [Python 官方中文教程：数据结构](https://docs.python.org/zh-cn/3/tutorial/datastructures.html)
- [uv 官方文档：运行项目命令](https://docs.astral.sh/uv/concepts/projects/run/)

不需要一次读完官方教程。今天只查阅变量、字符串、列表、字典、`if`、`for` 和函数相关部分。
