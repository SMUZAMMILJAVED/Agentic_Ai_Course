from my_config.groq_config import groq_client
from agents import OpenAIChatCompletionsModel
GROQ_MODEL=OpenAIChatCompletionsModel(model="llama-3.3-70b-versatile",openai_client=groq_client)
