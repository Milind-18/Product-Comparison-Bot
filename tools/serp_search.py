from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Set the SERPER_API_KEY environment variable (required by SerperDevTool)
os.environ['SERPER_API_KEY'] = os.getenv('SERPER_API_KEY')

from crewai_tools import SerperDevTool

# Initialize and export the SerperDevTool instance
serper_tool = SerperDevTool()
