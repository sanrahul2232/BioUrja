import pandas as pd

# Read the input data
input_data = pd.read_csv('input_data.csv')

# Add a new column 'Weights' to the dataset
input_data['Weights'] = input_data['Forecast'] / input_data['Capacity']

# Define the zone forecasts and total state forecast
zone_forecasts = {
    'E': 2800,
    'N': 1500,
    'W': 2000,
    'S': 6500,
}

total_state_forecast = 12000

# Calculate the total regional/zonal forecasts
total_regional_forecast = sum(zone_forecasts.values())

# Calculate zonal weights and revised forecasts in a loop
zone_weights = {}
zone_forecasts_revised = {}

for zone in zone_forecasts.keys():
    zone_weights[zone] = input_data[input_data['Plant_Name'].str.startswith(zone)]['Weights'].sum()

# Calculating total state weight
total_state_weight = sum(zone_weights.values())

# Calculating revised zonal forcasts for each zone
for zone in zone_forecasts.keys():
    zone_forecasts_revised[zone] = (zone_weights[zone] / total_state_weight) * total_state_forecast


# Redistribute the power output for each wind farm and round the redistributed forecast
def redistribute_forecast(row):
    zone = row['Plant_Name'][0]
    return row['Weights'] / zone_weights[zone] * zone_forecasts_revised[zone]

input_data['Redistributed_Forecast'] = input_data.apply(redistribute_forecast, axis=1)
input_data['Redistributed_Forecast'] = input_data['Redistributed_Forecast'].round(2)

# Check if redistributed forecast exceeds capacity for any wind farm
if any(input_data['Redistributed_Forecast'] > input_data['Capacity']):
    print('There is no feasible solution for this problem because some wind farms have re-dispatched forecast exceeding their capacity.')

# Format the output to the desired form and print it
output_data = input_data[['Plant_Name', 'Redistributed_Forecast']].apply(lambda x: f"{x['Plant_Name']},{x['Redistributed_Forecast']}", axis=1)
print(input_data[['Plant_Name', 'Redistributed_Forecast']].to_csv(index=False))