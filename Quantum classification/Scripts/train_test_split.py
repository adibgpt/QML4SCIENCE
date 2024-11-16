import random
import pathlib

# Setup data paths
data_path = '/content/drive/MyDrive/Target/'

# Create function to split randomly into Train and Test
def train_test_split(image_path=data_path,
                     data_splits=['Train', 'Test'],
                     target_classes=[False, True],
                     split=0.3,
                     seed=42):
    random.seed(seed)
    label_splits = {}

    # Generate splits
    for data_split in data_splits:
        print(f"[INFO] Creating image split for: {data_split}...")
        image_paths = []
        for target in target_classes:
            labels = list(data[data['class'] == target]['image_filename'])
            sample = round((1 - split) * len(labels))
            print(f"Getting random set of {sample} images for {data_split}-{target} ...")
            if data_split == 'Train':
                sampled_images = random.sample(labels, k=sample)
            elif data_split == 'Test':
                sampled_images = labels
            image_paths.append([pathlib.Path(str(image_path + str(target) + '/' + sample_image)) for sample_image in sampled_images])
            data.drop(data[data['image_filename'].isin(sampled_images)].index, inplace=True)
            print(len(data))
        image_path_flat = [item for sublist in image_paths for item in sublist]
        label_splits[data_split] = image_path_flat

    print('\nFinish splitting!')
    return label_splits
