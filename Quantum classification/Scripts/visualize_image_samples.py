import random
import matplotlib.pyplot as plt

# Group data by class
byClass = data.groupby('class_number')

# Number of samples per class to display
n = 20

# Randomly sample indices for each class
c = random.sample(byClass.get_group(1).index.tolist(), n)
s = random.sample(byClass.get_group(0).index.tolist(), n)

# Create a grid figure to display images
fig = plt.figure(figsize=(16, 8))
columns = 10  # Number of columns in the grid
rows = 4      # Number of rows in the grid

for i in range(0, columns * rows):
    fig.add_subplot(rows, columns, i+1)
    if i < 20:  # First 20 images: Class 1 (Without Cavity)
        plt.imshow(img[c[i]], cmap='Greys_r')
        plt.title('Without Cavity')
        plt.xticks([])
        plt.yticks([])
    else:       # Remaining 20 images: Class 0 (With Cavity)
        plt.imshow(img[s[i-20]], cmap='Greys_r')
        plt.title('With Cavity')
        plt.xticks([])
        plt.yticks([])

# Display the grid of images
plt.show()
