import numpy as np

import altair as alt
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

#load dataset
df = pd.read_csv("clean_Himark_data.csv")

# Creating Overall_Damage
df['Overall_damage'] = df['sewer_and_water']+df['power']+df['roads_and_bridges']+df['buildings']+df['medical']

def display_option1():
    st.markdown('<center><h2 style="font-family: Arial, sans-serif">Areas of Concern</h2></center>', unsafe_allow_html=True)

    #sidebar
    with st.sidebar:
        days_dropdown = st.sidebar.selectbox('Select a Day', options=sorted(df['day'].unique()))

    col = st.columns((1.3, 4.5, 2), gap='medium')

    with col[0]:

#------------------------------------------------------------------------------------------------
        # Calculate the average power
        st.markdown('<center><h6> Avg Power </h6></center>', unsafe_allow_html=True)
        filtered_dataset = df[df['day'] == days_dropdown]
        average_power = filtered_dataset['power'].mean()
        average_power_rounded = round(average_power, 2)
        max_value = 10  # Define the maximum value (adjust this based on your data)

        # Create a figure and axis with black background
        fig, ax = plt.subplots(facecolor='black',figsize=(6, 6))


        # Define the colors for the circular KPI
        colors = ['#199e84', 'lightgrey']

        # Calculate the percentage completion
        percentage = (average_power_rounded / max_value) * 100

        # Set the radius of the pie chart
        radius = 0.8

        # Create a pie chart for Power with the specified radius
        ax.pie([percentage, 100 - percentage], colors=colors, startangle=90, counterclock=False, radius=radius)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle = plt.Circle((0, 0), radius * 0.8, fc='black')  # Set background color to black
        fig.gca().add_artist(centre_circle)

        # Set aspect ratio to be equal to make it a perfect circle
        ax.set_aspect('equal')

        # Add text to the center of the pie chart with the rounded average power value
        ax.text(0, 0, f'{average_power_rounded}', color='#199e84', fontsize=40, ha='center', va='center', weight='bold')

        # Hide axes
        ax.axis('off')

        # Display the plot in Streamlit
        st.pyplot(fig)

#------------------------------------------------------------------------------------------------------
        st.markdown('<center><h6> Avg Sewer & Water </h6></center>', unsafe_allow_html=True)
        filtered_dataset_sw = df[df['day'] == days_dropdown]
        average_sw = filtered_dataset_sw['sewer_and_water'].mean(skipna=True)
        average_sw_rounded = round(average_sw, 2)

        # Define the maximum value (adjust this based on your data)
        max_value_sw = 20
        percentage_sw = (average_sw_rounded / max_value_sw) * 100

        # Set the radius of the pie chart
        radius_sw = 0.8

        # Create a figure and axis with black background
        fig_sw, ax_sw = plt.subplots(facecolor='black')

        # Define the colors for the circular KPI
        colors_sw = ['#199e84', 'lightgrey']

        # Create a pie chart for Sewer & Water with the specified radius
        ax_sw.pie([percentage_sw, 100 - percentage_sw], colors=colors_sw, startangle=90, counterclock=False, radius=radius_sw)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle_sw = plt.Circle((0, 0), radius_sw * 0.8, fc='black')
        fig_sw.gca().add_artist(centre_circle_sw)

        # Set aspect ratio to be equal to make it a perfect circle
        ax_sw.set_aspect('equal')

        # Hide axes
        ax_sw.axis('off')

        # Display the text in the center
        ax_sw.text(0, 0, f'{average_sw_rounded}', color='#199e84', fontsize=40, ha='center', va='center', weight='bold')
        plt.subplots_adjust(top=0.8, bottom=0.1)
        # Display the plot in Streamlit
        st.pyplot(fig_sw)

# ---------------------------------------------------------------------------------------------------
        # Calculate the average roads and bridges
        st.markdown('<center><h6> Avg Roads & Bridges </h6></center>', unsafe_allow_html=True)
        filtered_dataset_rb = df[df['day'] == days_dropdown]
        average_rb = filtered_dataset_rb['roads_and_bridges'].mean()
        average_rb_rounded = round(average_rb, 2)
        max_value_rb = 10  # Define the maximum value (adjust this based on your data)

        # Create a figure and axis with black background
        fig_rb, ax_rb = plt.subplots(facecolor='black')

        # Define the colors for the circular KPI
        colors_rb = ['#199e84', 'lightgrey']

        # Calculate the percentage completion
        percentage_rb = (average_rb_rounded / max_value_rb) * 100

        # Set the radius of the pie chart
        radius_rb = 0.8

        # Create a pie chart for Roads and Bridges with the specified radius
        ax_rb.pie([percentage_rb, 100 - percentage_rb], colors=colors_rb, startangle=90, counterclock=False, radius=radius_rb)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle_rb = plt.Circle((0, 0), radius_rb * 0.8, fc='black')
        fig_rb.gca().add_artist(centre_circle_rb)

        # Set aspect ratio to be equal to make it a perfect circle
        ax_rb.set_aspect('equal')

        # Hide axes
        ax_rb.axis('off')

        # Display the text in the center
        ax_rb.text(0, 0, f'{average_rb_rounded}', color='#199e84', fontsize= 40, ha='center', va='center', weight='bold')

        # Display the plot in Streamlit
        st.pyplot(fig_rb)

# ---------------------------------------------------------------------------------------------------
        st.markdown('<center><h6> Avg Medical </h6></center>', unsafe_allow_html=True)
        filtered_dataset_med = df[df['day'] == days_dropdown]
        average_med = filtered_dataset_med['medical'].mean()
        average_med_rounded = round(average_med, 2)
        max_value_med = 10  # Define the maximum value (adjust this based on your data)

        # Create a figure and axis with black background
        fig_med, ax_med = plt.subplots(facecolor='black')

        # Define the colors for the circular KPI
        colors_med = ['#199e84', 'lightgrey']

        # Calculate the percentage completion
        percentage_med = (average_med_rounded / max_value_med) * 100

        # Set the radius of the pie chart
        radius_med = 0.8

        # Create a pie chart for Medical with the specified radius
        ax_med.pie([percentage_med, 100 - percentage_med], colors=colors_med, startangle=90, counterclock=False, radius=radius_med)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle_med = plt.Circle((0, 0), radius_med * 0.8, fc='black')
        fig_med.gca().add_artist(centre_circle_med)

        # Set aspect ratio to be equal to make it a perfect circle
        ax_med.set_aspect('equal')

        # Hide axes
        ax_med.axis('off')

        # Display the text in the center
        ax_med.text(0, 0, f'{average_med_rounded}', color='#199e84', fontsize=40, ha='center', va='center', weight='bold')

        # Display the plot in Streamlit
        st.pyplot(fig_med)
# ---------------------------------------------------------------------------------------------------
        # Calculate the average buildings
        st.markdown('<center><h6> Avg Buildings </h6></center>', unsafe_allow_html=True)
        filtered_dataset_b = df[df['day'] == days_dropdown]
        average_b = filtered_dataset_b['buildings'].mean()
        average_b_rounded = round(average_b, 2)
        max_value_b = 10  # Define the maximum value (adjust this based on your data)

        # Create a figure and axis with black background
        fig_b, ax_b = plt.subplots(facecolor='black')

        # Define the colors for the circular KPI
        colors_b = ['#199e84', 'lightgrey']

        # Calculate the percentage completion
        percentage_b = (average_b_rounded / max_value_b) * 100

        # Set the radius of the pie chart
        radius_b = 0.8

        # Create a pie chart for Buildings with the specified radius
        ax_b.pie([percentage_b, 100 - percentage_b], colors=colors_b, startangle=90, counterclock=False, radius=radius_b)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle_b = plt.Circle((0, 0), radius_b * 0.8, fc='black')
        fig_b.gca().add_artist(centre_circle_b)

        # Set aspect ratio to be equal to make it a perfect circle
        ax_b.set_aspect('equal')

        # Hide axes
        ax_b.axis('off')

        # Display the text in the center
        ax_b.text(0, 0, f'{average_b_rounded}', color='#199e84', fontsize=40, ha='center', va='center', weight='bold')

        # Display the plot in Streamlit
        st.pyplot(fig_b)
#- ---------------------------------------------------
        ''''# Calculate the average shake intensity
        st.markdown('<center><h6> Avg Shake Intensity </h6></center>', unsafe_allow_html=True)
        filtered_dataset_si = df[df['day'] == days_dropdown]
        average_si = filtered_dataset_si['shake_intensity'].mean()
        average_si_rounded = round(average_si, 2)
        max_value_si = 10  # Define the maximum value (adjust this based on your data)

        # Create a figure and axis with black background
        fig_si, ax_si = plt.subplots(facecolor='black')

        # Define the colors for the circular KPI
        colors_si = ['#199e84', 'lightgrey']

        # Calculate the percentage completion
        percentage_si = (average_si_rounded / max_value_si) * 100

        # Set the radius of the pie chart
        radius_si = 0.8

        # Create a pie chart for Shake Intensity with the specified radius
        ax_si.pie([percentage_si, 100 - percentage_si], colors=colors_si, startangle=90, counterclock=False, radius=radius_si)

        # Draw a white circle at the center to make it look like a donut chart
        centre_circle_si = plt.Circle((0, 0), radius_si * 0.8, fc='black')
        fig_si.gca().add_artist(centre_circle_si)

        # Set aspect ratio to be equal to make it a perfect circle
        ax_si.set_aspect('equal')

        # Hide axes
        ax_si.axis('off')

        # Display the text in the center
        ax_si.text(0, 0, f'{average_si_rounded}', color='#199e84', fontsize=40, ha='center', va='center', weight='bold')

        # Display the plot in Streamlit
        st.pyplot(fig_si)'''



    with col[1]:
        st.markdown('<center><h5> Average Shake Intensity by Time Period</h5></center>',unsafe_allow_html=True)

        # Define a custom color scheme with shades of olive green
        custom_color_scheme = alt.Scale(
            domain=['Morning', 'Afternoon', 'Evening', 'Night'],  # Assuming Period_of_day values
            range=['#43755b','#FFFFE0','#dffabb','#3d613c']
        )

        # Filter the DataFrame based on the selected day
        filtered_dataset = df[df['day'] == days_dropdown]

        # Create the bar chart
        time_period_chart = alt.Chart(filtered_dataset).mark_bar().encode(
            x=alt.X('Period_of_day:N', title='Time Period'),
            y=alt.Y('average(shake_intensity):Q', title='Shake Intensity'),
            color=alt.Color('Period_of_day:N', title='Time Period', scale=custom_color_scheme, legend = None),
        ).properties(
            width=500,
            height=300
        ).configure_mark(
            cornerRadius=3
        )

        # Display the bar chart
        st.altair_chart(time_period_chart)

        # Define the dropdown options
        custom_color_scheme = alt.Scale(domain=[0, 10],   range=['#FFFFE0','#d9f299','#99c965','#b2d162','#6d9c3b','#73b572','#59ab64','#27822a','#1c872c','#376b36']
                                        )



        st.markdown('<center><h5> Daily Distribution by location </h5></center>',unsafe_allow_html=True)
        options = ['sewer_and_water', 'power', 'roads_and_bridges', 'medical', 'buildings']
        selected_column = st.selectbox('Select Column:', options)

        # Filter the DataFrame based on the selected day
        filtered_df = df[df['day'] == days_dropdown]

        # Create the heatmap

        heatmap = alt.Chart(filtered_df).mark_rect().encode(
            x=alt.X('hours:O', title='Hours'),
            y=alt.Y('location:N', title='Location'),
            color=alt.Color(f'{selected_column}:Q', title='Value', scale=custom_color_scheme),
            tooltip=[selected_column, 'location:N', 'hours:O']
        ).properties(
            title=f'Heatmap of {selected_column}',
            width=500,
            height=450
        ).configure_view(
            strokeWidth=0
        ).configure_axis(
            labelFontSize=14,
            titleFontSize=16
        )

        # Display the heatmap
        st.altair_chart(heatmap)

    with col[2]:
        st.markdown('<center><h5> Total Damage </h5></center>', unsafe_allow_html=True)

        filtered_df = df[df['day'] == days_dropdown]

        # Calculate the total overall damage for the selected day
        total_damage = filtered_df['Overall_damage'].sum()

        # Calculate the sum of damage for each category
        category_sum = filtered_df[
            ['sewer_and_water', 'roads_and_bridges', 'shake_intensity', 'buildings', 'medical', 'power']].sum()

        # Convert the sums to percentages
        category_percentage = category_sum / total_damage * 100

        # Create a DataFrame for the pie chart
        pie_data = pd.DataFrame({
            'Category': category_percentage.index,
            'Percentage': category_percentage.values
        })

        # Create the pie chart
        pie_chart = alt.Chart(pie_data).mark_arc().encode(
            color=alt.Color('Category:N',
                            scale=alt.Scale(range=['#556B2F', '#6B8E23', '#808000', '#BDB76B', '#F0E68C', '#FFFFE0'])
                            ),
            tooltip=['Category:N', 'Percentage:Q'],
            theta='Percentage:Q'
        ).properties(
            width=270,  # Adjust the width
            height=300,  # Adjust the height

        ).configure_title(
            fontSize=20  # Increase font size
        ).configure_legend(
            title=None,
            labelFontSize=8
        )


        # Display the pie chart
        st.altair_chart(pie_chart)

        #chart2
        st.markdown('<center><h5> Average Overall Damage By Location</h5></center>',unsafe_allow_html=True)
        filtered_dataset = df[df['day'] == days_dropdown]
        nearest = alt.selection(type='single', nearest=True,
                                fields=['day'], empty='none')

        # Calculate average damage for the filtered dataset
        average_damage = filtered_dataset['Overall_damage'].mean()
        # Get unique locations from the filtered dataset
        unique_locations = filtered_dataset['location'].unique()

        # Create an Altair chart
        overall_damage_bar_chart = alt.Chart(filtered_dataset).mark_bar().encode(
            y=alt.Y('location:N', title='Location', sort='-x', axis=alt.Axis(values=unique_locations)),
            x=alt.X('Overall_damage:Q', title='Overall Damage'),
            tooltip=['location:N', alt.Tooltip('Overall_damage:Q', format='.2f')]  # Round to two decimal places
        ).properties(
            width=270,
            height=500
        ).configure_mark(
            fill='#F0E68C',
            cornerRadius=3
        ).configure_axis(
            labelBound=True  # Enable label bounding
        )


        # Display the Altair chart
        st.altair_chart(overall_damage_bar_chart)

        #chart2
        '''st.markdown('### Count of Incidents by Location')
        location_counts = filtered_dataset['location'].value_counts().reset_index()
        location_counts.columns = ['location', 'count']

        # Sorting the locations by counts in descending order
        location_counts = location_counts.sort_values(by='count', ascending=False)

        # Create the horizontal bar chart
        frequency_chart = alt.Chart(location_counts).mark_bar().encode(
            y=alt.Y('location:N', title='Location', sort='-x'),  # Sort by count in descending order
            x=alt.X('count:Q', title='Count'),
            tooltip=['location:N', 'count:Q']
        ).properties(
            width=340,
            height=320,

        )

        # Show the chart
        st.altair_chart(frequency_chart)'''



















