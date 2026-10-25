from dotenv import load_dotenv
from deepagents import create_deep_agent

load_dotenv()

agent = create_deep_agent(
    name="hello-world-agent",
    model="google_genai:gemini-3.6-flash",
    tools=[],   
)

result = agent.invoke({"messages": [{"role": "user", "content": "Can you say Hallo World in some language (selected by you)?"}]})

# Print the agent's response
print(result["messages"][-1].text)