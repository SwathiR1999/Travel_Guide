from flask import Flask, render_template, request
from TG_Agents import weather_agent, lead_planner, research_agent, itinerary_agent
from TG_Tasks import task_overview, gather_travel_info_task, weather_forecast_task, build_final_itinerary_task
from crewai import Crew
from pyngrok import ngrok
import markdown

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        city = request.form["city"]
        state = request.form["state"]
        country = request.form["country"]
        travel_dates = request.form["travel_dates"]
        preferences = request.form["preferences"]
        budget = request.form["budget"]
        group_info = request.form["group_info"]
        destination = f"{city}, {state}, {country}"
        

        if not all([city, state, country, travel_dates, preferences, budget, group_info]):
            return render_template("index.html", error="Please fill in all fields.")

        overview = task_overview(destination, travel_dates, preferences, budget, group_info, lead_planner)
        research = gather_travel_info_task(destination, travel_dates, preferences, budget, research_agent)
        weather = weather_forecast_task(city, state, country, weather_agent)
        itinerary = build_final_itinerary_task(itinerary_agent)

        crew = Crew(
            agents=[lead_planner, research_agent, weather_agent, itinerary_agent],
            tasks=[overview, research, weather, itinerary],
            planning=False,
            strategy="hierarchical",
            # full_output=True,
            verbose=True,
        )

        result = crew.kickoff()
        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    # app.run(debug=True)
    public_url = ngrok.connect(5000)
    print(" * ngrok tunnel: ", public_url)
    if __name__ == '__main__':
        app.run()
