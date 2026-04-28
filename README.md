## Milestone 4

For LLM implementation, we implemented several prompt engineering techniques. The first is Role & Persona, as found under build_system_prompt() with "You are OutfitPlannerz AI, a warm and knowledgeable personal fashion coach...". This technique fits because the chatbot should be friendly and warm, providing useful outputs to the user according to their personal tastes to make all users comfortable with using it.

Another technique is a few-shot prompt, found with examples like "Example 1 - outfit question:...". This technique fits the app task because the user may ask questions in different ways. Providing examples teaches the model how to determine the relationship between weather data and clothing detail outputs that the user needs. 

A 3rd technique is structured output, found in "For outfit recommendations, always use this structure
**👗 Outfit:** [specific clothing items]
**🌤️ Reason:** [1–2 sentences tying the outfit to the weather data]". Establishing structure ensures the UI maintains consistency across all relevant responses. Without this, the model could write bullet points, paragraphs, or just a couple sentences with different information across different responses. This structure makes the app feel more polished.

An example user input for someone with an interview on Thursday would be "What should I wear Thursday?" The resulting reponse from the LLM is shows in the image below
![LLM response](<img width="1894" height="1326" alt="image" src="https://github.com/user-attachments/assets/2d1adca8-91e2-448c-af91-34442fff093a" />
)
