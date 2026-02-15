from agents import Runner ,set_tracing_disabled
from my_agents.gemeni_agent import agent
from my_agents.groq_agent import groq_agent
from decouple import config
set_tracing_disabled(True)

result = Runner.run_sync(starting_agent=agent, input='2+2=?')
print(result.final_output)

