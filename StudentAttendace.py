import matplotlib.pyplot as plt
import numpy as np

# 1. Generate grid data: Study Hours (0-20 hrs) vs Attendance Rate (50%-100%)
study_hours = np.linspace(0, 20, 50)  # X-axis
attendance = np.linspace(50, 100, 50)  # Y-axis
X, Y = np.meshgrid(study_hours, attendance)

# 2. Calculate continuous score matrix (Z-axis) with diminishing returns
Z = 30 + (2.5 * X) + (0.4 * Y) - (0.03 * (X**2))
Z = np.clip(Z, 0, 100)  # Keep scores between 0 and 100%

# 3. Create 3D Surface Plot
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')

# Plot surface (Viridis colormap: Yellow = high scores, Purple = low scores)
surf = ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none', alpha=0.85)

# Labels and title
ax.set_title('3D Student Performance Analysis: Study Hours vs. Attendance')
ax.set_xlabel('Weekly Study Hours')
ax.set_ylabel('Attendance Rate (%)')
ax.set_zlabel('Predicted Exam Score (%)')

# Add colorbar legend
fig.colorbar(surf, ax=ax, shrink=0.5, aspect=6, label='Exam Score (%)')

plt.tight_layout()

# Save the plot directly to your workspace instead of popping open a GUI window
plt.savefig('student_attendance_3d.png', dpi=300, bbox_inches='tight')
print('Successfully saved 3D surface plot to student_attendance_3d.png!')