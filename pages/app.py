import streamlit as st
from time import sleep

st.title("Interactive Outfit Planner")

st.divider()
st.header('Choose the day of the week')

days = {
    "Monday":    {"weather": "Sunny, 25°C",        "occasion": "Casual workday",     "outfit": "Light blouse, tailored pants, and loafers."},
    "Tuesday":   {"weather": "Cloudy, 18°C",        "occasion": "Business meeting",   "outfit": "Blazer, pencil skirt, and heels."},
    "Wednesday": {"weather": "Rainy, 15°C",         "occasion": "Casual day out",     "outfit": "Waterproof jacket, jeans, and rain boots."},
    "Thursday":  {"weather": "Windy, 20°C",         "occasion": "Outdoor event",      "outfit": "Windbreaker, comfortable pants, and sneakers."},
    "Friday":    {"weather": "Partly cloudy, 22°C", "occasion": "Weekend plans",      "outfit": "Denim jacket, shorts, and sandals."},
    "Saturday":  {"weather": "Sunny, 26°C",         "occasion": "Social gathering",   "outfit": "Floral dress, sandals, and a straw hat."},
    "Sunday":    {"weather": "Clear, 24°C",         "occasion": "Family outing",      "outfit": "Comfortable t-shirt, jeans, and sneakers."},
}

if st.button("🔄 Reset All Outfits"):
    for day in days.keys():
        st.session_state[f"{day}_use_suggested"] = True
        st.session_state[f"{day}_custom_outfit"] = ""
    st.toast("Filters cleared!")
    sleep(5)
    st.rerun()


for day, info in days.items():
    if f"{day}_use_suggested" not in st.session_state:
        st.session_state[f"{day}_use_suggested"] = True
    if f"{day}_custom_outfit" not in st.session_state:
        st.session_state[f"{day}_custom_outfit"] = ""

tabs = st.tabs(list(days.keys()))

for tab, (day, info) in zip(tabs, days.items()):
    with tab:
        st.subheader(day)
        st.write(f"Weather: {info['weather']}")
        st.write(f"Occasion: {info['occasion']}")
        st.write(f"Recommended Outfit: {info['outfit']}")

        st.divider()

        use_suggested = st.checkbox(
            "Use suggested outfit",
            key=f"{day}_use_suggested"
        )

        if not use_suggested:
            custom = st.text_input(
                "Enter your custom outfit:",
                key=f"{day}_custom_outfit",
                placeholder="e.g. White t-shirt, cargo pants, and white sneakers"
            )
            if not custom.strip():
                st.warning("Pick at least one outfit — enter a custom outfit above.")
            else:
                st.success(f"Custom outfit set: {custom}")
        else:
            st.info(f"Outfit selected: {info['outfit']}")

