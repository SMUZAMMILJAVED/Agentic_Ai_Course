from agents import Runner, set_tracing_disabled
from my_agents.teacher_agent import agent
set_tracing_disabled(True)
res=Runner.run_sync(starting_agent=agent,input='2+2=?')
print(res.final_output)