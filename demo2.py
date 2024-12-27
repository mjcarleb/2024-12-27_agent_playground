from praisonaiagents import Agent, Task, PraisonAIAgents

# 1. Create agents
researcher = Agent(
    name="Researcher",
    role="Senior Research Analyst",
    goal="Find articles about Bittensor Network and price discovery for Tao",
    backstory="""You are an expert at a crypto hedge fund, 
    skilled in identifying trends and analyzing complex data.""",
    verbose=True,
    llm="gpt-4o",
    markdown=True
)
writer = Agent(
    name="Writer",
    role="Blockchain Content Strategist",
    goal="Craft compelling content on predictions for crypto prices",
    backstory="""You are a content strategist known for 
    making complex tech topics interesting and easy to understand.""",
    llm="gpt-4o",
    markdown=True
)

# 2. Define Tasks
task1 = Task(
    name="research_task",
    description="""Analyze End of Year Tao price and likely price trajectory in 2025.""",
    expected_output="""Create a detailedreport highlighting likely Bittensor advances in 2025 and price trajectory""",
    agent=researcher
)

task2 = Task(
    name="writing_task",
    description="""Create a blog post using the insights you have gained from the Bittensor reserach.
    Make it interesting, clear, and suited for tech enthusiasts. 
    It should be at most 4 paragraphs long.""",
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
