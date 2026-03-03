from langchain import OpenAI, LLMChain
from langchain.agents import create_openai_agent

# Initialize the OpenAI model
llm = OpenAI(temperature=0)

# Create an agent using the OpenAI model
agent = create_openai_agent(llm)

# Define a simple task
user_input = "What is the capital of France?"

# Get response from the agent
response = agent.run(user_input)
print(response)