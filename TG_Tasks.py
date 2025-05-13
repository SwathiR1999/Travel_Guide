from crewai import Task

def task_overview(destination, travel_dates, preferences, budget, group_info, lead_planner):
    return Task(
        description=(
            f"Understand the user requirements for a trip to {destination} from {travel_dates}, "
            f"preferences: {preferences}, budget: {budget}, for {group_info}. "
            "Break the planning into subtasks: research, weather check, and itinerary construction. "
            "Assign tasks to the right specialists and ensure the final plan is complete and well-integrated."
        ),
        expected_output="Delegated plan with all subcomponents integrated into one final itinerary.",
        agent=lead_planner,
    )


def gather_travel_info_task(destination, travel_dates, preferences, budget, research_agent):
    return Task(
        description=(
            f"Find top-rated attractions, food, and cultural experiences in {destination} for the dates {travel_dates}. "
            f"Focus on experiences aligned with {preferences}, and within a {budget} budget."
        ),
        expected_output="Curated experiences list with descriptions, locations, and relevance to the user's interests.",
        agent=research_agent,
    )


def weather_forecast_task(city, state, country, weather_agent):
    return Task(
        description=(
            f"Analyze current weather in {city}, {state}, {country}. "
            "Flag any potential issues and suggest backup indoor options where relevant."
        ),
        expected_output="Day-wise weather forecast with activity suitability recommendations and indoor backup plans.",
        agent=weather_agent,
    )


def build_final_itinerary_task(itinerary_agent):
    return Task(
        description=(
            "Using the research and weather data, create a detailed day-by-day itinerary that balances relaxation and activity. "
            "Include timing, food suggestions, transport notes, and indoor options if needed."
        ),
        expected_output="An interactive visually well presented report on final daily itinerary with alternatives for bad weather, including places to eat and cultural highlights.",
        agent=itinerary_agent,
        verbose=True,
    )
