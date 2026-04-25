import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns

# --- STUDENT-SPECIFIC PARAMETERS ---
# Update these values with your information
student_name = "Ian Marlo S. Ganal"
student_id = "2025-0519"
color_bar = "skyblue"
color_line = "orange"
cmap_color = "YlGnBu"

# Load the dataset
# Ensure 'spotify_top_1000.csv' is in your working directory
df = pd.read_csv('spotify_top_1000.csv')

# --- 1. IDENTIFY LONGEST TRACKS ---
# Sort by duration and take top 10
longest_tracks = df.sort_values(by='duration_min', ascending=False).head(10)

# Display table
print("Top 10 Longest Tracks:")
print(longest_tracks[['track_name', 'artist', 'duration_min']])

# Plotting horizontal bar chart
plt.figure(figsize=(10, 6))
plt.barh(longest_tracks['track_name'], longest_tracks['duration_min'], color=color_bar)
plt.xlabel('Duration (min)')
plt.ylabel('Track Name')
plt.title(f'Top 10 Longest Songs\nStudent: {student_name} ({student_id})')
plt.gca().invert_yaxis()  # Put longest at the top
plt.tight_layout()
plt.show()

# --- 2. SONG RELEASE TREND ---
# Group by year and count
yearly_counts = df.groupby('year').size().reset_index(name='song_count')
yearly_counts['cumulative_count'] = yearly_counts['song_count'].cumsum()

# Plotting combined line and bar chart
fig, ax1 = plt.subplots(figsize=(12, 6))

ax1.bar(yearly_counts['year'], yearly_counts['song_count'], color=color_bar, alpha=0.7, label='Yearly Count')
ax1.set_xlabel('Year')
ax1.set_ylabel('Yearly Song Count', color=color_bar)
ax1.tick_params(axis='y', labelcolor=color_bar)

ax2 = ax1.twinx()
ax2.plot(yearly_counts['year'], yearly_counts['cumulative_count'], color=color_line, marker='o', label='Cumulative Growth')
ax2.set_ylabel('Cumulative Count', color=color_line)
ax2.tick_params(axis='y', labelcolor=color_line)

plt.title(f'Song Release Trend Over Time\nStudent: {student_name} ({student_id})')
fig.tight_layout()
plt.show()

# --- 3. ANIMATED DENSITY MAP OF DURATION VS POPULARITY ---
fig, ax = plt.subplots(figsize=(10, 7))
years = sorted(df['year'].unique())

def update(year):
    ax.clear()
    data_year = df[df['year'] <= year] # Showing evolution up to that year
    hb = ax.hexbin(data_year['duration_min'], data_year['popularity'], 
                   gridsize=20, cmap=cmap_color, mincnt=1)
    ax.set_title(f'Density Map: Duration vs Popularity (Year: {year})\n{student_name} - {student_id}')
    ax.set_xlabel('Duration (min)')
    ax.set_ylabel('Popularity')
    return hb,

ani = animation.FuncAnimation(fig, update, frames=years, repeat=False)
plt.show()