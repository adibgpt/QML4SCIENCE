import torch
from torch import no_grad

# Save the trained model's state
torch.save(model.state_dict(), "model.pt")

# Create a new QNN and hybrid model for evaluation
qnn1 = create_qnn()
model1 = Net(qnn1)

# Load the saved model state into the new model
model1.load_state_dict(torch.load("model.pt"))

# Set batch size and evaluation mode
batch_size = 1
model1.eval()

# Initialize lists for predictions and targets
pred_targets = []
test_targets = []
total_loss = []

# Evaluate the model on the test data
with no_grad():
    correct = 0
    for batch_idx, (data, target) in enumerate(test_loader):
        output = model1(data)  # Forward pass

        # Reshape output if necessary
        if len(output.shape) == 1:
            output = output.reshape(1, *output.shape)

        # Predict and store targets
        pred = output.argmax(dim=1, keepdim=True)
        pred_targets.append(pred.item())
        test_targets.append(target.item())

        # Calculate correct predictions
        correct += pred.eq(target.view_as(pred)).sum().item()

        # Compute loss
        loss = loss_func(output, target)
        total_loss.append(loss.item())

    # Print performance metrics
    print(f"Performance on test data:\n\tLoss: {sum(total_loss) / len(total_loss):.4f}\n\tAccuracy: {100 * correct / len(test_loader) / batch_size:.2f}%")
