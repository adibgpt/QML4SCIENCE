import torchvision
from torchvision import transforms
from torch.utils.data import DataLoader
import matplotlib.pyplot as plt

# Load training and testing data
train_data = torchvision.datasets.ImageFolder(
    '/content/drive/MyDrive/Images_Random_Split/Train',
    transform=transforms.Compose([transforms.ToTensor()])
)
test_data = torchvision.datasets.ImageFolder(
    '/content/drive/MyDrive/Images_Random_Split/Test',
    transform=transforms.Compose([transforms.ToTensor()])
)

# Check the shape of the first sample
print(train_data[0][0].shape)

# Create DataLoaders for training and testing
train_loader = DataLoader(train_data, shuffle=True, batch_size=1)
test_loader = DataLoader(test_data, shuffle=True, batch_size=1)

# Print class-to-index mapping
print(train_loader.dataset.class_to_idx)

# Number of samples to visualize
n_samples_show = 6

# Create an iterator for the DataLoader
data_iter = iter(train_loader)
fig, axes = plt.subplots(nrows=1, ncols=n_samples_show, figsize=(10, 10))

# Visualize a few samples from the training data
while n_samples_show > 0:
    images, targets = data_iter.__next__()

    axes[n_samples_show - 1].imshow(images[0, 0].numpy().squeeze(), cmap=plt.cm.rainbow)
    axes[n_samples_show - 1].set_xticks([])
    axes[n_samples_show - 1].set_yticks([])
    axes[n_samples_show - 1].set_title(f"Labeled: {targets[0].item()}")

    n_samples_show -= 1
