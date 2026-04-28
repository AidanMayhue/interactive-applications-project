API 1: Open-Meteo Geocoding API
URL: https://geocoding-api.open-meteo.com/v1/search
Authentication Method: None because Open-Meteo is a free, open-source API.
Rate Limits: The app uses @st.cache_data with a TTL value of 86400 seconds (1 day) since the location of a city is unlikely to change in a short amount of time.
Why the API is valuable: Busy college students live in many different cities and may not know their exact coordinates, so this API allows them to simply type their city/state and have it automatically be converted to the location for accurate weather data.

API 2: Open-Meteo Weather API
URL: https://api.open-meteo.com/v1/forecast
Authentication Method: None because Open-Meteo is a free, open-source API.
Rate Limits: The app uses @st.cache_data with a TTL value of 3600 seconds (1 hour) to avoid unnecessary requests and update weather every hour.
Why the API is valuable: Busy college students don’t have the time to check the weather and also plan outfits manually. This weather API automatically provides a forecast that produces outfit recommendations without the user having to do anything.


# Interactivity Self Review
## Self-Criteria Evaluation

| Criteria | Score (1–5) | Evidence | What Could Improve |
|----------|------------|----------|-------------------|
| Visualization Layout | 4 | The app uses structured layouts with columns (Analytics page), tabs (Outfit Planner), and sections (Homepage and Calendar). Charts such as the temperature line graph and the pie chart are clearly organized and readable. | Improve visual consistency across pages (spacing, alignment, and styling). Could add more visual hierarchy (e.g., larger section headers or color emphasis). |
| Basic Interactivity | 5 | Users can input location, add/delete events, select clothing items, and view analytics. Buttons, sliders, checkboxes, and forms all respond immediately and update the UI correctly. | Add tooltips or help icons to explain some controls for first-time users. |
| Adaptive Interactivity | 5 | The app includes dependent dropdowns (clothing categories → items), dynamic UI (toggle for all-day events hides time input), multi-step workflow (Outfit Builder with step tracker), and conditional rendering (events and outfit suggestions update based on user input). | Further personalize experience (e.g., remember user preferences or suggest default selections based on past behavior). |
| Performance | 4 | API calls are cached using `st.cache_data`, reducing repeated load times. Spinners provide feedback during loading. Most interactions are fast after the initial data fetch. | The initial API call can still feel slow. This could be optimized by preloading or reducing unnecessary reruns. |
| Feedback & Validation | 5 | The app uses `st.success`, `st.warning`, `st.error`, `st.info`, `st.spinner`, and `st.toast` to guide users. Validation prevents empty inputs, duplicate events, and invalid selections. Error handling for API responses is comprehensive. | Add more inline validation (e.g., immediate feedback while typing rather than after submission). |

## Usability Target Check

**ISO Metrics Evaluation**

Effectiveness:
The app is on track in terms of effectiveness. Users can accomplish the core task of planning outfits based on weather and scheduled events. For example, the Outfit Planner page automatically generates outfit recommendations using real-time weather data, and users can add events through the calendar to receive more context-specific suggestions. This demonstrates that the app supports the primary goal of helping users decide what to wear each day.

Efficiency:
The app is generally efficient, with most tasks completing within the intended time frame. Outfit recommendations are generated automatically once weather data is loaded, requiring little to no user effort on a typical day. Adding or removing events through the calendar form is also quick and can usually be completed in under a minute. However, the main bottleneck is the initial API call to fetch weather data, which can take a few seconds before results are displayed.

Satisfaction:
Overall, the app provides a pleasant user experience. Features like automatic outfit suggestions, a structured weekly layout, and interactive feedback (such as success and warning messages) contribute to a smooth and engaging interface. However, some users may initially feel slightly overwhelmed due to the number of features spread across multiple pages, especially when first exploring the app.

**Five Components of Usability**

Learnability: New users can quickly understand the app because the Outfit Planner uses clearly labeled tabs for each day of the week, allowing users to immediately navigate and view outfit recommendations without instructions.

Efficiency:
Users can complete tasks quickly since outfit recommendations are automatically generated from weather data, meaning most users do not need to manually input information daily.

Memorability:
Returning users can easily resume using the app because the layout is consistent across pages, with the sidebar for location input and tabs for daily planning remaining in the same place.

Errors:
The app prevents common mistakes by displaying warnings when required inputs are missing, such as prompting users to select at least one clothing item in the Outfit Builder before proceeding.

Satisfaction:
Users are likely to feel satisfied because the app reduces decision-making stress by automatically suggesting outfits while still allowing customization through features like custom outfit input. 

