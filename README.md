# Travel_Guide
## AI-Powered Travel Itinerary Planner with CrewAI and Ollama

This project uses **CrewAI**, **LangChain**, and a locally running **Ollama** model to plan a complete travel itinerary. It combines live weather data, real-time web search, and user preferences through a team of collaborating AI agents to deliver a rich and weather-smart travel experience.

---

## 🌐 Features

- ✅ **Multi-Agent Collaboration**  
  Assigns specific tasks to expert agents for itinerary construction, weather analysis, and destination research.

- 🌤️ **Live Weather Forecast Integration**  
  Uses the **OpenWeather API** to assess real-time weather and suggest indoor alternatives when necessary.

- 🔍 **Web Search with DuckDuckGo**  
  Finds local experiences, food recommendations, and hidden gems using DuckDuckGo's search results.

- 🧠 **Local LLM Inference with Ollama**  
  Runs the `ollama/llama3.2` model locally for fast and secure LLM responses without cloud dependencies.

- 🗺️ **Detailed Day-by-Day Itinerary**  
  Builds a structured, balanced travel plan that considers timing, rest, meals, transportation, and fallback options.

- 💡 **Personalized Preference Handling**  
  Tailors suggestions based on:
  - Interests (e.g., culture, temples, food)
  - Travel pace (e.g., moderate)
  - Budget (e.g., mid-range)
  - Group composition (e.g., 2 adults)

---
