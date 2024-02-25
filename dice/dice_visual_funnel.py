import plotly.express as px

from die import Die

# Create one six-sided die and one ten-sided die.
die_1 = Die()
die_2 = Die(10)

# Make some rolls, and store results in a list.
results = [die_1.roll() + die_2.roll() for roll_num in range(50_000)]

# Analyze the results.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
possible_results = range(2, max_result+1)
frequencies = [results.count(value) for value in possible_results]

# Visualize the results.
title = "Results of rolling one six-sided die and one ten-sided die 50_000 times."
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.funnel(x=possible_results, y=frequencies, title=title, labels=labels)

# Further customize chart.
fig.update_layout(xaxis_dtick=1)

fig.write_html('dice_visual_funnel.html')
