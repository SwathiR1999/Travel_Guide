import os
from crewai import Agent
from TG_Tools import search_web_tool, WeatherTool
from crewai import LLM

llm = LLM(
    model="ollama/llama3.2",
    base_url="http://localhost:11434"
)

weather_tool = WeatherTool(api_key=os.environ["Weather_Tool_API"])

weather_agent = Agent(
    role="Weather & Risk Advisor",
    goal="Analyze weather and suggest weather-safe options",
    backstory="A travel-savvy weather analyst who helps travelers avoid disruptions by adjusting for weather conditions.",
    tools=[weather_tool],
    llm = LLM(model="ollama/llama3.2",base_url="http://localhost:11434"),
    verbose=True,
    allow_delegation=False,
)

lead_planner = Agent(
    role="Lead Travel Planner",
    goal="Coordinate all travel planning tasks and ensure the final itinerary meets user needs",
    backstory="A seasoned travel expert who understands how to coordinate teams to deliver exceptional travel experiences.",
    llm = LLM(model="ollama/llama3.2",base_url="http://localhost:11434"),
    verbose=True,
    allow_delegation=False,
)

research_agent = Agent(
    role="Local Experience Researcher",
    goal="Gather destination-specific cultural experiences, food spots, and activities",
    backstory="An expert in curating authentic travel experiences by analyzing trends, local blogs, and event listings.",
    tools=[search_web_tool],
    llm = LLM(model="ollama/llama3.2",base_url="http://localhost:11434"),
    verbose=True,
    allow_delegation=False,
)

itinerary_agent = Agent(
    role="Itinerary Architect",
    goal="Build a detailed day-by-day itinerary using collected data",
    backstory="An itinerary expert focused on pacing, diversity of experiences, and hidden gems tailored to user references.",
    llm = LLM(model="ollama/llama3.2",base_url="http://localhost:11434"),
    verbose=True,
    allow_delegation=False,
)