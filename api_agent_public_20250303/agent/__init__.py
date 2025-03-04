# pip install allure-pytest
# pip install pytest
# 安装 autogen系列包即可，技术问题请加微信：huice666

from autogen_agentchat.agents import AssistantAgent as Agent
from autogen_agentchat.conditions import SourceMatchTermination as Termination
from autogen_agentchat.teams import RoundRobinGroupChat as Team
from autogen_agentchat.ui import Console
from autogen_ext.models.openai import OpenAIChatCompletionClient as ChatClient

