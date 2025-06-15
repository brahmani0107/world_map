import streamlit as st
import plotly.express as px

# Streamlit Page Config
st.set_page_config(page_title="World Map with Hover", layout="wide")

# Title
st.title("🌍 Interactive World Map with Country Names on Hover")

# Load the built-in world map using ISO country codes
fig = px.choropleth(
    locations=px.data.gapminder()['country'],  # All countries
    locationmode="country names",
    color=[1] * len(px.data.gapminder()['country']),  # Dummy color for uniform look
    hover_name=px.data.gapminder()['country'],  # Hover will show country name
    color_continuous_scale=px.colors.sequential.Blues
)

# Clean the map by hiding color bar
fig.update_layout(coloraxis_showscale=False)

# Display the map
st.plotly_chart(fig, use_container_width=True)
