# HIT 137 Assignment 2 Q2
# Group Name: CAS/DAN 1
# Group Members:
# Lee Potter - S368675
# Sahil Badgal - S384037

# Question 2 completed by Sahil Badgal

import os
import pandas as pd

# Directory containing the temperature CSV files
data_folder = "temperature_data"

# Output file paths
average_temp_file = "average_temp.txt"
largest_temp_range_file = "largest_temp_range_station.txt"
warmest_and_coolest_file = "warmest_and_coolest_station.txt"

# Load all data from CSV files
# def load_temperature_data(folder):
#     all_data = []
#     for filename in os.listdir(folder):
#         if filename.endswith(".csv"):
#             filepath = os.path.join(folder, filename)
#             data = pd.read_csv(filepath, delimiter="\t")  # Assuming tab-delimited
#             all_data.append(data)
#     return pd.concat(all_data, ignore_index=True)

def load_temperature_data(folder):
    all_data = []
    for filename in os.listdir(folder):
        if filename.endswith(".csv"):
            filepath = os.path.join(folder, filename)
            # Read the CSV file and ensure columns are trimmed
            data = pd.read_csv(filepath, delimiter=",")  # Comma-separated
            data.columns = data.columns.str.strip()  # Remove leading/trailing spaces
            all_data.append(data)
    return pd.concat(all_data, ignore_index=True)

# Calculate average temperature for each month
def calculate_monthly_averages(data):
    print(data.columns)
    months = ["January", "February", "March", "April", "May", "June", 
              "July", "August", "September", "October", "November", "December"]
    monthly_averages = data[months].mean()
    return monthly_averages

# Find the station(s) with the largest temperature range
def largest_temperature_range(data):
    data["Temperature_Range"] = data[["January", "February", "March", "April", "May", "June", 
                                       "July", "August", "September", "October", "November", "December"]].max(axis=1) - \
                                  data[["January", "February", "March", "April", "May", "June", 
                                       "July", "August", "September", "October", "November", "December"]].min(axis=1)
    max_range = data["Temperature_Range"].max()
    stations = data[data["Temperature_Range"] == max_range]["STATION_NAME"]
    return stations, max_range

# Find the warmest and coolest stations
def warmest_and_coolest_stations(data):
    data["Yearly_Average"] = data[["January", "February", "March", "April", "May", "June", 
                                    "July", "August", "September", "October", "November", "December"]].mean(axis=1)
    warmest_avg = data["Yearly_Average"].max()
    coolest_avg = data["Yearly_Average"].min()
    warmest_stations = data[data["Yearly_Average"] == warmest_avg]["STATION_NAME"]
    coolest_stations = data[data["Yearly_Average"] == coolest_avg]["STATION_NAME"]
    return warmest_stations, coolest_stations, warmest_avg, coolest_avg

# Main script
if __name__ == "__main__":
    # Load data
    temperature_data = load_temperature_data(data_folder)

    # Calculate monthly averages
    monthly_averages = calculate_monthly_averages(temperature_data)
    with open(average_temp_file, "w") as file:
        file.write("Average Temperature for Each Month:\n")
        file.write(monthly_averages.to_string())

    # Find the station(s) with the largest temperature range
    largest_range_stations, largest_range = largest_temperature_range(temperature_data)
    with open(largest_temp_range_file, "w") as file:
        file.write("Station(s) with Largest Temperature Range:\n")
        file.write(f"{', '.join(largest_range_stations)} (Range: {largest_range})\n")

    # Find the warmest and coolest stations
    warmest_stations, coolest_stations, warmest_avg, coolest_avg = warmest_and_coolest_stations(temperature_data)
    with open(warmest_and_coolest_file, "w") as file:
        file.write("Warmest and Coolest Stations:\n")
        file.write(f"Warmest Station(s): {', '.join(warmest_stations)} (Avg Temp: {warmest_avg})\n")
        file.write(f"Coolest Station(s): {', '.join(coolest_stations)} (Avg Temp: {coolest_avg})\n")
