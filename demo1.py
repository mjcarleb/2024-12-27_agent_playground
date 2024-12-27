from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Rest of imports
from praisonaiagents import Agent, Task, PraisonAIAgents

# Verify API key is loaded
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY not found in environment variables")

# 1. Create agents
researcher = Agent(
    name="Researcher",
    role="Senior Research Analyst",
    goal="Uncover cutting-edge developments in AI and data science",
    backstory="""You are an expert at a technology research group, 
    skilled in identifying trends and analyzing complex data.""",
    verbose=True,
    llm="gpt-4o",
    markdown=True
)
writer = Agent(
    name="Writer",
    role="Tech Content Strategist",
    goal="Craft compelling content on tech advancements",
    backstory="""You are a content strategist known for 
    making complex tech topics interesting and easy to understand.""",
    llm="gpt-4o",
    markdown=True
)

# 2. Define Tasks
task1 = Task(
    name="research_task",
    description="""Analyze 2024's AI advancements. 
    Find major trends, new technologies, and their effects.""",
    expected_output="""A detailed report on 2024 AI advancements""",
    agent=researcher
)

task2 = Task(
    name="writing_task",
    description="""Create a blog post about major AI advancements using the insights you have.
    Make it interesting, clear, and suited for tech enthusiasts. 
    It should be at least 4 paragraphs long.""",
    expected_output="A blog post of at least 4 paragraphs",
    agent=writer,
)

agents = PraisonAIAgents(
    agents=[researcher, writer],
    tasks=[task1, task2],
    verbose=False,
    process="hierarchical",
    manager_llm="gpt-4o"
)

result = agents.start()
