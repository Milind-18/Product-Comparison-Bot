from crewai import Task
from agents import info_extractor, comparator, recommender
from tools.serp_search import serper_tool

# Task 1: Extract product info
extract_info_task = Task(
    description=(
        "Use the provided product names '{product_1}' and '{product_2}' to search the internet and extract detailed, "
        "strengths, weaknesses, pricing, and summarized user reviews for both products. "
        "Be sure to focus on criteria like camera quality, battery life, performance, price, and real-world reviews."
    ),
    expected_output=(
        "A clear structured report including:\n"
        "- For each product: bullet points for camera, battery, performance, price, and user opinions\n"
        "- Sources if possible\n"
        "- Keep it concise but thorough"
    ),
    tools=[serper_tool],
    agent=info_extractor
)

# Task 2: Compare the products
compare_task = Task(
    description=(
        "Compare the two products using the extracted information. Focus on the following criteria:\n"
        "- Camera quality\n"
        "- Battery life\n"
        "- Performance\n"
        "- Price\n"
        "- User reviews\n"
        "Present a side-by-side breakdown of which product is better in each category."
    ),
    expected_output=(
        "A comparison table or summary that clearly shows strengths and weaknesses of each product "
        "per criterion. Include a short paragraph highlighting the overall trade-offs."
    ),
    agent=comparator
)

# Task 3: Make a recommendation
recommend_task = Task(
    description=(
        "Based on the comparison, recommend which product is the better choice overall and why. "
        "Your decision should take into account the original input criteria as well as the comparison data. "
        "Address different user needs if necessary (e.g., photographers, gamers, casual users)."
    ),
    expected_output=(
        "A final recommendation including:\n"
        "- Which product is preferred\n"
        "- Justification for the choice\n"
        "- Mention if there are user-specific cases where the other product might be better"
    ),
    agent=recommender
)
