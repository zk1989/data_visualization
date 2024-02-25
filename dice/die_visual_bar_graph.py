import plotly.express as px

from die import Die

# Create a six-sided die.
die = Die()

# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results.
frequencies = []
possible_results = range(1, die.num_sides+1)
for value in possible_results:
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results.
title = "Results of rolling one six-sided die 1_000 times"
labels = {'x': 'Result', 'y': 'Frequency of result'}
fig = px.bar(x=possible_results, y=frequencies, title=title, labels=labels)

fig.write_html('die_visual_bar_graph.html')
