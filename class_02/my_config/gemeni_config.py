from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from decouple import config
gemeni_key=config('GEMINI_API_KEY')
gemeni_base_url=config('BASE_URL')
gemeni_client = AsyncOpenAI(
    api_key=gemeni_key,
    base_url=gemeni_base_url
)