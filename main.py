from dotenv import load_dotenv
from deepagents import create_deep_agent

load_dotenv()

agent = create_deep_agent(
    name="hello-world-agent",
    model="google_genai:gemini-3.6-flash",
    tools=[],   
)

result = agent.invoke({"messages": [{"role": "user", "content": "Powiedz Hallo World w wybranym języku naturalnym(wybranym przez ciebie)?"}]})

# Print the agent's response
print(result["messages"][-1].text)