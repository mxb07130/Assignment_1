import matplotlib.pyplot as plot
# Sample Data
language = 'Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++'
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

#Color representation for each language
colors = ["#1f77b4", "#ff7f0e", "#2ca02c", "#d62728", "#9467bd", "#8c564b"]

# explode the maximum percentage slice
exp = (0.2,0,0,0,0,0)

# Setting plot border color and width
border={'linewidth':1,'edgecolor':'black'}
plot.pie(popularity, explode=exp, labels=language, colors=colors,
autopct='%1.1f%%', shadow=True, wedgeprops= border,startangle=140)
plot.axis('equal')

# Plot
plot.show()