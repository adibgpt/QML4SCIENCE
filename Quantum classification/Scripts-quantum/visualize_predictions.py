from PIL import Image
import matplotlib.pyplot as plt
import torchvision

# Number of test samples to display
n_samples_show = 6
count = 0

# Create a figure for displaying the predictions
fig, axes = plt.subplots(nrows=1, ncols=n_samples_show, figsize=(10, 3))

# Set the model to evaluation mode
model1.eval()

# Visualize predictions
with no_grad():
    for batch_idx, (data, target) in enumerate(test_loader):
        if count == n_samples_show:  # Stop after displaying the required number of samples
            break
        
        # Get model predictions
        output = model1(data[0:1])
        if len(output.shape) == 1:  # Adjust output shape if necessary
            output = output.reshape(3, *output.shape)

        # Get the predicted class
        pred = output.argmax(dim=1, keepdim=True)

        # Display the image and prediction
        axes[count].imshow(
            torchvision.transforms.ToPILImage(mode='RGB')(data[0].squeeze()), cmap=plt.cm.rainbow
        )
        axes[count].set_xticks([])
        axes[count].set_yticks([])
        axes[count].set_title(f"Predicted {pred.item()}")

        count += 1
