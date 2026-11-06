import argparse

from dotenv import load_dotenv
from deepagents import create_deep_agent

load_dotenv()

parser = argparse.ArgumentParser()
parser.add_argument("prompt", nargs="?", help="Podaj prompt do agenta. Jeśli nie zostanie podany, zostaniesz poproszony o jego wprowadzenie.")
args = parser.parse_args()
prompt = args.prompt if args.prompt is not None else input("Podaj prompt:")

agent = create_deep_agent(
    name="hello-world-agent",
    model="gpt-6-luna",
    tools=[],
)

result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})

# Print the agent's response
print(result["messages"][-1].text)