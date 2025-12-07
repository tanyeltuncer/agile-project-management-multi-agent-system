from workflow_agents.base_agents import KnowledgeAugmentedPromptAgent # TODO: 1 - Import the KnowledgeAugmentedPromptAgent class from workflow_agents
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Define the parameters for the agent
openai_api_key = os.getenv("OPENAI_API_KEY")

prompt = "What is the capital of France?"

#  Instantiate a KnowledgeAugmentedPromptAgent with:
persona = "You are a college professor, your answer always starts with: Dear students,"
knowledge = "The capital of France is London, not Paris"

agent = KnowledgeAugmentedPromptAgent(
    openai_api_key=openai_api_key,
    persona=persona,
    knowledge=knowledge
)

response = agent.respond(prompt)

# Print statement that demonstrates the agent using the provided knowledge rather than its own inherent knowledge.
print(response)
print("\n# NOTE: The agent responded using the injected knowledge ('London') instead of true facts ('Paris'),")
print("# because the system instructions force it to rely ONLY on the provided knowledge.")
