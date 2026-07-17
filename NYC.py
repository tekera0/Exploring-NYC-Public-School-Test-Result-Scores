'''Which NYC schools have the best math results?

The best math results are at least 80% of the *maximum possible score of 800* for math.
Save your results in a pandas DataFrame called best_math_schools, including "school_name" and "average_math" columns, sorted by "average_math" in descending order.
What are the top 10 performing schools based on the combined SAT scores?

Save your results as a pandas DataFrame called top_10_schools containing the "school_name" and a new column named "total_SAT", with results ordered by "total_SAT" in descending order ("total_SAT" being the sum of math, reading, and writing scores).
Which single borough has the largest standard deviation in the combined SAT score?

Save your results as a pandas DataFrame called largest_std_dev.
The DataFrame should contain one row, with:
"borough" - the name of the NYC borough with the largest standard deviation of "total_SAT".
"num_schools" - the number of schools in the borough.
"average_SAT" - the mean of "total_SAT".
"std_SAT" - the standard deviation of "total_SAT".
Round all numeric values to two decimal places.'''

# Re-run this cell 
import pandas as pd
# Read in the data
schools = pd.read_csv("schools.csv")

# Preview the data
schools.head()

# Start coding here...
best_math_schools =schools[schools['average_math']>=800*0.8]
best_math_schools = best_math_schools[['school_name','average_math']].sort_values('average_math',ascending=False)
print(best_math_schools)

schools['total_SAT'] = schools['average_math'] + schools['average_reading']+ schools['average_writing']
top_10_schools = schools[["school_name","total_SAT"]].sort_values("total_SAT", ascending = False).head(10)

# Display the result
print(top_10_schools)

borough_stats = schools.groupby('borough')['total_SAT'].agg(['count','mean','std']).round(2)


borough_stats.columns = ["num_schools", "average_SAT", "std_SAT"]
largest_std_dev = borough_stats[borough_stats['std_SAT']== borough_stats['std_SAT'].max()]
print(largest_std_dev)

