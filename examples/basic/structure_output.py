import asyncio

from rich.console import Console
from rich.panel import Panel
from pydantic import BaseModel,Field
from azent.core import DeepSeekClient,Agent
from azent.core.message import HumanMessage,SystemMessage

console = Console()

class Pizza(BaseModel):
    name:str = Field(title="name of pizza",description="披萨的名称",examples=["海鲜披萨"])
    description:str = Field(title="description of pizza",description="对于披萨的简单介绍",examples=["丰富的海鲜如虾、鱿鱼和贻贝搭配番茄酱和奶酪，海洋的味道在口中爆发。"])


# 初始化一个 client
client = DeepSeekClient(name="deepseek-client")

system_message = SystemMessage(content="you are very help assistant")
human_message = HumanMessage(content="生成 10 种以上披萨")


agent = Agent(
    name="pizza_generator",
    model_name="deepseek-chat",
    system_message=system_message,
    client=client,
    result_data_type=list[Pizza]
    )

async def main():
    result = await agent.run(human_message)
    console.print(result.response)
    data = result.get_data()
    if data is None:
        print("Error: Failed to retrieve pizza data.")
        return  # Or handle the error in another way
    for pizza in data:
        console.print(Panel(pizza.description,title=f"🍕 {pizza.name}"))

if __name__ == "__main__":
    asyncio.run(main=main())
    
