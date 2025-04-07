import asyncio

from rich.console import Console
from rich.markdown import Markdown

from azent.core import DeepSeekClient,Agent
from azent.core.message import HumanMessage,SystemMessage
console = Console()

# 初始化一个 client
client = DeepSeekClient(name="deepseek-client")

# 准备我们的 message System Message(Meta Prompt)
system_message = SystemMessage(content="you are very help assistant")
# 准备我们的 human Message
human_message = HumanMessage(content="write hello world in python")

# 初始化 Agent
agent = Agent(
    name="hello_agent",
    system_message=system_message,
    )

# 调用 agent 的 run 方法
async def main():
    result = await agent.run(human_message)
    if result:
        console.print(Markdown(result.get_text()))
if __name__ == "__main__":
    asyncio.run(main=main())