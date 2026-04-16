import streamlit as st
import datetime

st.set_page_config(
    page_title = "App"
)

st.title("OutfitPlannerz")

st.subheader("Today's Outfit: Khaki pants, button-up shirt, and brown boots")
st.write("Today's Weather: Sunny, 85°F")
st.write("No events scheduled for today. Check your calendar for upcoming events and outfit recommendations!")

st.subheader("Upcoming Events")
if "events" not in st.session_state or not st.session_state.events:
    pass
else:
    today = datetime.date.today()
    upcoming = []

    for e in st.session_state.events:
        try:
            event_date = datetime.date.fromisoformat(e["start"].split("T")[0])
            if event_date >= today:
                upcoming.append((event_date, e))
        except ValueError:
            continue

    upcoming.sort(key=lambda x: x[0])

    if upcoming:
        # Initialize visibility state
        if "visible_events" not in st.session_state:
            st.session_state.visible_events = {e["title"]: True for _, e in upcoming}
        for _, e in upcoming:
            if e["title"] not in st.session_state.visible_events:
                st.session_state.visible_events[e["title"]] = True

        # Display filtered events first
        displayed = [(d, e) for d, e in upcoming if st.session_state.visible_events.get(e["title"], True)]

        if displayed:
            for event_date, e in displayed:
                st.write(f"**{e['title']}** — {e['display']}")
        else:
            st.warning("pick at least one")

        st.divider()

        # Advanced settings expander with checkboxes nested inside
        with st.expander("⚙️ Advanced Settings"):
            st.write("Select which events to display:")
            for _, e in upcoming:
                #key below allows Streamlit to differentiate between different checkboxes for each event
                new_value = st.checkbox(
                e["title"], value=st.session_state.visible_events[e["title"]], key=f"check_{e['title']}"
                )
                if new_value != st.session_state.visible_events[e["title"]]:
                    st.session_state.visible_events[e["title"]] = new_value
                    st.rerun()
    else:
        st.info("No upcoming events. Head to the Calendar to add some!")