from dotenv import load_dotenv
from deepagents import create_deep_agent

load_dotenv()

agent = create_deep_agent(
    name="restaurant_agent",
    model="gpt-4o",
    tools=[],   
)

result = agent.invoke({"messages": [{"role": "user", "content": "Can you say Hallo World in some language (selected by you)?"}]})

# Print the agent's response
print(result["messages"][-1].content)