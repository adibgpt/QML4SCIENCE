import matplotlib.pyplot as plt

# Plot training loss and accuracy
fig, ax1 = plt.subplots()

# Plot loss on the left y-axis
ax1.plot(loss_list, 'g-', label="Loss")
ax1.set_xlabel("Training Iterations")
ax1.set_ylabel("Cross Entropy Loss", color='g')

# Plot accuracy on the right y-axis
ax2 = ax1.twinx()
ax2.plot(total_accuracy, 'b', label="Accuracy")
ax2.set_ylabel("Accuracy (%)", color='b')

# Add title and show the plot
plt.title("Hybrid NN Training Convergence", color='red')
plt.show()
