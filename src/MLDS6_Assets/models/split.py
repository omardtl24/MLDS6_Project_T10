from sklearn.model_selection import train_test_split
import os
import shutil

def trainTestSplitImages(source_dir, train_dir, test_dir, test_size=0.2, random_state=42):
    """
    trainTestSplitImages

    Splits image data from a source directory into training and testing sets, 
    organizing them into separate subdirectories for each class.

    Parameters:
    -----------
    source_dir : str
        Path to the source directory containing class-wise subdirectories with images.

    train_dir : str
        Path to the directory where training images will be stored.
        A subdirectory for each class will be created automatically.

    test_dir : str
        Path to the directory where testing images will be stored.
        A subdirectory for each class will be created automatically.

    test_size : float, optional (default=0.2)
        The proportion of images to include in the testing set.
        Must be a float between 0.0 and 1.0.

    random_state : int, optional (default=42)
        Random seed used to shuffle the dataset before splitting.

    Returns:
    --------
    None
    """

    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    for class_name in os.listdir(source_dir):
        class_path = os.path.join(source_dir, class_name)
        if os.path.isdir(class_path):
            # Collect images in the current class folder
            images = [os.path.join(class_path, img) for img in os.listdir(class_path)]
            # Split images into train and test sets
            train_images, test_images = train_test_split(images, test_size=test_size, random_state=random_state)

            # Create class-specific subdirectories in train and test directories
            train_class_dir = os.path.join(train_dir, class_name)
            test_class_dir = os.path.join(test_dir, class_name)
            os.makedirs(train_class_dir, exist_ok=True)
            os.makedirs(test_class_dir, exist_ok=True)

            # Copy images to respective train/test directories
            for img in train_images:
                shutil.copy(img, train_class_dir)
            for img in test_images:
                shutil.copy(img, test_class_dir)

    print(f"Split from \n{source_dir}\nto\n{train_dir}\nand\n{test_dir}\nwas done successfully")