from my_models.groq_model import GROQ_MODEL
from agents import Agent
groq_agent = Agent(name="Assistant", instructions="You are a helpful assistant answer in short",model=GROQ_MODEL)