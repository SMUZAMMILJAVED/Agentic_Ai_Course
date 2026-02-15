from my_config.gemeni_config import gemeni_client
from agents import OpenAIChatCompletionsModel
MODEL=OpenAIChatCompletionsModel(model="gemini-3-flash-preview",openai_client=gemeni_client)
