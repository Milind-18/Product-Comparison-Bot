from crewai import Agent
from tools.serp_search import serper_tool

# Agent 1: Info Extractor
info_extractor = Agent(
    role='Product Information Extractor',
    goal='Research both products in depth and extract feature lists, technical specs, pros & cons, and user reviews',
    backstory=(
        "A tech-savvy researcher who specializes in analyzing smartphones by scanning the web for trusted sources. "
        "You know where to look and how to summarize specs and reviews accurately. "
        "You are obsessed with data completeness and unbiased reporting."
    ),
    tools=[serper_tool],
    verbose=True,
    memory=True
)

# Agent 2: Comparator
comparator = Agent(
    role='Product Comparator',
    goal='Evaluate two products based on predefined criteria and highlight strengths and weaknesses of each',
    backstory=(
        "You are an analytical evaluator with a sharp eye for technical comparisons. "
        "You're known for writing honest, no-fluff feature breakdowns for tech blogs and helping people make informed decisions."
    ),
    tools=[],
    verbose=True,
    memory=True
)

# Agent 3: Recommender
recommender = Agent(
    role='Product Recommendation Expert',
    goal='Recommend the best product based on the comparison and user priorities',
    backstory=(
        "You are a product advisor with experience in guiding users based on their needs. "
        "You consider technical facts but also tailor recommendations to real-world usage and user types."
    ),
    tools=[],
    verbose=True,
    memory=True,
    allow_delegation=False
)
