import pandas as pd
import matplotlib.pyplot as plt
# Load CSV
df = pd.read_csv("bias_report.csv", index_col=0)
print("Similarity matrix:")
print(df)

# Calculate average similarity per language (bias check)
avg_similarity = df.mean(axis=1)
print("\nAverage similarity per language:")
print(avg_similarity)

# Calculate variance (statistical fairness)
fairness_variance = df.mean().var()
print("\nFairness variance across languages:", fairness_variance)

# Display heatmap image
img = plt.imread("similarity_matrix.png")
plt.imshow(img)
plt.axis('off')
plt.show()

# Optional: Bar chart for average similarity
avg_similarity.plot(kind='bar', title='Average Similarity per Language')
plt.ylabel('Similarity')
plt.show()