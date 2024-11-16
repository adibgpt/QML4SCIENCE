# Perform the train-test split
label_splits = train_test_split(split=0.3, seed=42)

# Display the first 10 items from the Train split
print(label_splits['Train'][0:10])

# Verify no overlap between Train and Test splits
from collections import Counter

counter1 = Counter(label_splits['Train'])
counter2 = Counter(label_splits['Test'])

# Find common elements between Train and Test splits
common_elements = counter1 & counter2

# Print the count of common elements
print(f"Number of overlapping elements: {len(common_elements)}")
