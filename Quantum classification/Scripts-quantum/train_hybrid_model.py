import torch.optim as optim
from torch.nn import CrossEntropyLoss

# Define optimizer and loss function
optimizer = optim.Adam(model.parameters(), lr=0.00001)
loss_func = CrossEntropyLoss()

# Training parameters
epochs = 50
model.train()

# Lists to store loss and accuracy per epoch
loss_list = []
total_accuracy = []

# Training loop
for epoch in range(epochs):
    correct = 0
    total_loss = []
    for batch_idx, (data, target) in enumerate(train_loader):
        optimizer.zero_grad(set_to_none=True)  # Clear gradients
        output = model(data)  # Forward pass
        loss = loss_func(output, target)  # Compute loss
        loss.backward()  # Backward pass
        optimizer.step()  # Update weights
        total_loss.append(loss.item())  # Store loss for this batch

        # Compute accuracy
        train_pred = output.argmax(dim=1, keepdim=True)
        correct += train_pred.eq(target.view_as(train_pred)).sum().item()

    # Compute and store average loss and accuracy for the epoch
    loss_list.append(sum(total_loss) / len(total_loss))
    accuracy = 100 * correct / len(train_loader.dataset)
    total_accuracy.append(accuracy)

    # Print epoch progress
    print(f"Training [{100.0 * (epoch + 1) / epochs:.0f}%]\tLoss: {loss_list[-1]:.4f}\tAccuracy: {accuracy:.2f}%")
