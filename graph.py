import matplotlib.pyplot as plt
import numpy as np

# Data from the table
moisture_content= [9.2, 9.7, 10.9, 14.1, 15.9, 16.0] # X axis
dry_density=[1810, 1911, 1996 ,1935 ,1873 , 1873] # Y axis

#Plotting the graph
plt.figure(figsize=(8,6))
plt.plot(moisture_content, dry_density,
marker="o", linestyle="-", color="b", label="Dry Density")

# Adding labels, title and grid
plt.title("Dry Density vs Moisture Content", fontsize=14)
plt.xlabel("Moisture Content (%)", fontsize=12)
plt.ylabel("Dry Density (mg/m3)", fontsize=12)
plt.grid(True, linestyle="--", alpha=0.6)
plt.legend()

# Display the graph
plt.show()