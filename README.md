# BioUrja
A renewable electrical power distribution project 

State of Texas in United States has total of 100 wind farms spread across four geographic zones named East, North, West and South. Wind farm E1:E24 lie in East Zone, N1:N26 lie in North Zone, W1:W15 lie in West while S1:S35 lie in South Zone. Individual wind farm level power output forecast for tomorrow is provided in input data file. However, recent research by vendor providing the data found out that their zonal level forecasts are better than individual wind farm level forecasts. They further specify that their state level forecast is the most accurate among all and better than zonal level forecasts. Zonal and State level forecasts are provided as part of input data file as well.







 

Please develop a code to read these input data and redispatch the individual wind farms so that total output from all wind farms matches the state level forecasts (which is considered most accurate). While redistributing the dispatch please consider following constraints:



Wind farms should be re-dispatched in the ratio of their current individual level forecast compared to their capacity. For example, if a 100 MW plant has 50 MW of individual forecast, then 50% weight should be provided to that wind farm in re-distribution.
Each geographic regional/zonal level output should be in the ratio of regional/zonal level forecast (since regional forecast quality is better than individual forecasts) summing up to the total of state level forecast.
Dispatch of wind farms cannot exceed their total capacity.


If you think there are no feasible solutions possible for this problem, please specify in detail the reasons for the same.
