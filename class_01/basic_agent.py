from agents import Agent, Runner ,OpenAIChatCompletionsModel
from openai import AsyncOpenAI
from dotenv import load_dotenv
import os
load_dotenv()

gemini_api_key = os.getenv('GEMINI_API_KEY')
client=AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://api.generativeai.googleapis.com/v1beta/openai/"
)
agent = Agent(
    name="basic agent",
    instructions="You are a helpful assistant",
    model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),
)

result = Runner.run_sync(agent, "What is the capital of France?")
print(result.final_output)

