
---

# Motor Vehicle Collisions in New York City

This Streamlit application is a dashboard designed to analyze motor vehicle collisions in New York City using Python libraries such as Streamlit, Pandas, NumPy, Pydeck, and Plotly Express.

## Overview

The application allows users to explore and visualize data related to motor vehicle collisions in New York City. It provides interactive maps, charts, and tables to understand various aspects of these collisions, such as the location, time of day, and types of vehicles involved.

## Installation

To run the application locally, you need to have Python installed on your system. You can install the required Python libraries using pip:

```bash
pip install streamlit pandas numpy pydeck plotly
```

## Data Source

The data used in this application is sourced from the New York City Open Data platform and is stored in a CSV file named "Motor_Vehicle_Collisions_-_Crashes.csv".
url = https://data.cityofnewyork.us/d/h9gi-nx95

## Functionality

1. **Map Visualization**: The application displays a map showing the locations of motor vehicle collisions in New York City. Users can adjust the slider to filter collisions based on the number of injured persons and visualize them on the map.

2. **Time-based Analysis**: Users can select a specific hour of the day to analyze the number of collisions occurring during that time period. The application displays a map with hexagon layers representing collision density and a bar chart showing the breakdown of collisions by minute.

3. **Top Dangerous Streets**: Users can select the affected class (Pedestrians, Cyclists, or Motorists) to view the top 5 dangerous streets based on the number of injuries. The application provides a table showing the streets with the highest number of injuries for the selected affected class.

4. **Raw Data**: Users can choose to view the raw data used in the analysis by toggling the "Show Raw Data" checkbox.

## Usage

To run the application, execute the following command in your terminal:

```bash
streamlit run app.py
```

This will start a local web server and open the application in your default web browser.

