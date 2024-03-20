import streamlit as st
import pandas as pd
import numpy as np
import pydeck as pdk
import plotly.express as px
DATA_URL = (
    "Motor_Vehicle_Collisions_-_Crashes.csv"
)

st.title("Motor Vehicle Collisions in New York City")
st.markdown ("This application is a streamlit dashboard that can be used to analyze motor vehicle collision in New York City 💥")

def load_data (nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows, parse_dates=[['CRASH_DATE','CRASH_TIME']])
    data.dropna(subset=['LATITUDE','LONGITUDE'], inplace=True)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data.rename(columns={'crash_date_crash_time': 'date/time'}, inplace=True)
    return data

data = load_data(100000)

st.header("Where are the most people injured in NYC?")
injured_people = st.slider("Number of persons injured in vehicle collisions", 0, 19)
if st.button('Show map'):
    st.map(data.query("injured_persons >= @injured_people")[["latitude", "longitude"]].dropna(how="any"))

st.header("How many collisions occur during a given time of day?")
# hour=st.header("Hour to llok at" , range(0,24), 1)
hour = st.slider("Hour to look at", 0, 23)
data = data[data['date/time'].dt.hour == hour]

st.markdown("Vehicle collisions between %i:00 and %i:00" % (hour, (hour + 1) % 24))
midpoint = (np.average (data['latitude']), np.average(data['longitude']))


st.write(pdk.Deck(
    map_style="mapbox://styles/mapbox/light-v9",
    initial_view_state={
        "latitude": midpoint[0],
        "longitude": midpoint[1],
        "zoom": 11,
        "pitch": 50,
        }
        ,layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data[['date/time', 'latitude', 'longitude']],
                get_position=['longitude', 'latitude'],
                radius=100,
                extruded = True,
                pickable = True,
                elevation_scale = 4,
                elevation_range = [0, 1000],
                ),
        ],
        ))

st.subheader("Breakdown by minute between %i:00 and %i:00" % (hour, (hour + 1) % 24))
filtered = data[
    (data['date/time'].dt.hour >= hour) & (data['date/time'].dt.hour < (hour + 1))
]
hist = np.histogram(filtered['date/time'].dt.minute, bins=60, range=(0, 60))[0]
chart_data = pd.DataFrame({'minute': range(60), 'crashes': hist})
fig = px.bar(chart_data, x='minute', y='crashes', hover_data=['minute', 'crashes'], height=400)
st.write(fig)


st.header("Top 5 dangerous streets by affected class")
select = st.selectbox('Affected class', ['Pedestrians', 'Cyclists', 'Motorists'])

if select == 'Pedestrians':
    st.write(data.query("injured_pedestrians >= 1")[["on_street_name", "injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how="any")[:5])


#    st.write(data.query("injured_pedestrians >= 1")[["on_street_name", "injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how="any")[:5])

elif select == 'Cyclists':
    st.write(data.query("injured_cyclists >= 1")[["on_street_name", "injured_cyclists"]].sort_values(by=['injured_cyclists'], ascending=False).dropna(how="any")[:5])

    # st.write(data.query("injured_cyclists >= 1")[["on_street_name", "injured_cyclists"]].sort_values(by=['injured_cyclists'], ascending=False).dropna(how="any")[:5]) st.write(data.query("injured_pedestrians >= 1")[["on_street_name", "injured_pedestrians"]].sort_values(by=['injured_pedestrians'], ascending=False).dropna(how="any")[:5])

else:
    st.write(data.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how="any")[:5])
    # st.write(data.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how="any")[:5])
    # st.write(data.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how="any")[:5])

    # st.write(data.query("injured_motorists >= 1")[["on_street_name", "injured_motorists"]].sort_values(by=['injured_motorists'], ascending=False).dropna(how="any")[:5])'
    
if st.checkbox("Show Raw Data", False):
    st.subheader("Raw Data")
    st.write(data)


# if st.checkbox("Show Raw Data"):
#     st.subheader("Raw Data")
#     st.write(data)

# collision_times = [f"{i}:00 - {i+1}:00" for i in range(6)] + ["12:00 AM -  1:00 AM"]
# selected_time = st.selectbox("selected time period", collision_times)
# start, end = selected_time.split(" - ")
# start,end = int(start[:-3]),int(end[:-3]) if "AM" not in end else int(end[:-3])+12 if start=="12" and end=="12"
# if user selects "12:0

# if start == "12":
#     start_hr = 0
# else:
#     start_hr = int(start[:-3])
# end_hr = int(end[:-3])

# start,end = int(start[:-3]),int(end[:-3])

# @st.cache
# def get_collision_counts(df, start, end):
    # """Get count of crashes within a specific   collision   point"""
    # Ensure that times are properly formatted
    # df['CRASH_TIME'] = pd.to_datetime(df['CRASH_TIME'])
    
    # Extract hours from CRASH TIME and convert to integer values
    # crash_hours = df['CRASH_TIME'].dt.hour.astype(int)
    
    # Create new column HOUR with mapped values based on CRASH TIME
    # df['HOUR'] = crash_hours.apply(lambda x : f"{x}:00")
    
    # Filter dataframe by user defined time frame and group by HOUR
    # counts = df.query("CRASH_TIME >= @start and CRASH_TIME < @end").groupby('HOUR').size().reset_index(name='COUNT')
    # counts = df.loc[(df['CRASH_TIME']>=pd.to_datetime(f"1900-01-01 {start}")) & \
    #                (df['CRASH_TIME']<pd.to_datetime(f"1900-01-02 {end}"))] \
    #           .groupby('HOUR').size().reset_index(name='COUNT')
              
    # return counts

# Display number of accidents per hour if button is clicked
# if st.button("Display chart"):
#     counts = get_collision_counts(data, start, end)
#     st.line_chart(counts + 1, countlabel='Number of Collisions', timelabel='Hour of Day')
#     st.markdown("<hr>", unsafe_allow_html=True)

# st.subheader("What factors contribute to more injuries?")
# factors = ['SPEED','WEATHER','VEHICLE_TYPE','ROAD_CONDITION']
# user_input = st.multiselect("Select variable to view its impact", factors)

# @st.cache
# def factor_impact(factor, data):
#     """Return average value of 'factor' along with standard deviation"""
#     avg = round(data[factor].mean(),2)
#     std_dev = round(np.avg (data[factor].std()),2)
#     return f"The average {factor} is {avg}. The standard deviation is {std_dev}."
# if len(user_input)>0:
#     col1,col2 = st.columns((1,6))
#     with col1:
#         st.write(factor_impact(user_input[0], data))</s> 



