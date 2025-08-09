from crewai import Crew, Process
from agents import info_extractor, comparator, recommender
from tasks import extract_info_task, compare_task, recommend_task

# Assemble the crew
product_comparison_crew = Crew(
    agents=[info_extractor, comparator, recommender],
    tasks=[extract_info_task, compare_task, recommend_task],
    process=Process.sequential  # Ensures logical order of execution
)
