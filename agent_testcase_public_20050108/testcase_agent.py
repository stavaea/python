from dataclasses import dataclass
import logfire
from pydantic import Field
from pydantic_ai import Agent, RunContext
from llms import model
from sql_agent import run_agent as run_sqlagent
logfire.configure(token="KDG7nFtbgb1nmHfVBkWbzJ7k0SMV58d6g3Kkmr3MKPs7")

@dataclass
class UserMessage:
    prompt: str = Field(..., description="用户消息")
    result: str = Field(..., description="")
# 初始化AI代理
testcase_agent = Agent(model=model,deps_type=UserMessage)

@testcase_agent.system_prompt
async def generate_requirements(ctx: RunContext[UserMessage]) -> str:
    reqs = await run_sqlagent(ctx.deps.prompt)
    prompt = (f"你是一名高级软件测试用例编写工程师，可以根据如下的软件测试需求列表，生成专业的、合适条数的测试用例。\n"
              f"确保测试用例覆盖所有功能点，逻辑清晰，易于执行，且符合软件测试最佳实践。\n"
              f"需要生成测试用例的需求列表如下：\n{reqs}")
    return prompt

async def run_agent(prompt: str):
    user_prompt = UserMessage(prompt=prompt)

    result = await testcase_agent.run(prompt, deps=user_prompt)
    print(result.data)

if __name__ == '__main__':
    import asyncio
    user_input = "对前2个需求生成3条测试用例，每条用例都需要显示对应的需求点"
    asyncio.run(run_agent(user_input))
