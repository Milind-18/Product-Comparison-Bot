from crew import product_comparison_crew
from dotenv import load_dotenv
import os

import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-5"

# Example product input
input_data = {
    "product_1": "Samsung Galaxy S25 5G",
    "product_2": "OnePlus 13 5G"
}

# Run the crew with input
if __name__ == "__main__":
    print("🧠 Running Product Comparison Bot...\n")

    result = product_comparison_crew.kickoff(inputs=input_data)

    print("\n✅ Final Recommendation:\n")
    print(result)
