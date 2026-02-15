from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from decouple import config
groq_key=config('GROQ_API_KEY')
groq_base_url=config('BASE_URL_GROQ')
groq_client = AsyncOpenAI(
    api_key=groq_key,
    base_url=groq_base_url
)