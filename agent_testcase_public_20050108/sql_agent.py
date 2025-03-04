import asyncio
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
from dataclasses import dataclass
from typing import Any, Union, List

import aiosqlite
import logfire

from typing_extensions import TypeAlias

from pydantic_ai import Agent, ModelRetry, RunContext
from models import Success, InvalidRequest
from llms import model
logfire.configure(token="KDG7nFtbgb1nmHfVBkWbzJ7k0SMV58d6g3Kkmr3MKPs7")

DB_SCHEMA = """
CREATE TABLE test_requirements (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    requirements TEXT NOT NULL, -- 软件测试需求内容
    tag INTEGER DEFAULT 0, -- 0: 未完成, 1: 已完成
    date TEXT NOT NULL,    -- 日期格式: YYYY-MM-DD
    submitter TEXT NOT NULL -- 提交人: 田老师, 助教小姐姐, 但问智能
);
"""


@dataclass
class DBConnection:
    conn: aiosqlite.Connection  # SQLite 数据库连接

Response: TypeAlias = Union[Success, InvalidRequest]  # 响应类型别名
agent: Agent = Agent(model=model, result_type=Response, deps_type=DBConnection,)


@agent.system_prompt
async def system_prompt() -> str:
    return f"""\
        给定以下 SQLite 记录表，你的任务是编写符合用户请求的 SQL 查询。
        
        数据库模式：
        
        {DB_SCHEMA}
        示例
            请求: 获取 田老师提交的需求
            响应: SELECT * FROM records WHERE submitter = '田老师'
        示例
            请求: 获取未完成的需求
            响应: SELECT * FROM records WHERE tag = 0
        示例
            请求: 针对2024年9月16日之前的需求生成测试用例
            响应: SELECT * FROM records WHERE date(start_timestamp) < date('2024-09-16')
    """


@agent.result_validator
async def validate_result(ctx: RunContext[DBConnection], result: Response) -> Response:
    if isinstance(result, InvalidRequest):
        return result

    if not result.sql_query.upper().startswith('SELECT'):
        raise ModelRetry('请创建一个 SELECT 查询')

    try:
        await ctx.deps.conn.execute(f'EXPLAIN QUERY PLAN {result.sql_query}')
    except aiosqlite.Error as e:
        raise ModelRetry(f'无效的查询: {e}') from e
    else:
        return result

@agent.tool
async def execute_sql(ctx: RunContext[DBConnection], result: Response) -> List:
    """执行 SQL 查询并返回结果"""
    data = await ctx.deps.conn.execute_fetchall(result.sql_query)
    return data

@asynccontextmanager
async def connect_database(database: str) -> AsyncGenerator[Any, None]:
    with logfire.span('连接数据库'):
        conn = await aiosqlite.connect(database)
        try:
            yield conn
        finally:
            await conn.close()


async def run_agent(prompt: str):
    async with connect_database('.chat_app_db.sqlite') as conn:
        deps = DBConnection(conn)
        result = await agent.run(prompt, deps=deps)
        return result.data.requirements_list


if __name__ == '__main__':
    res = asyncio.run(run_agent("完成田老师提的软件测试需求"))
    print(res)
