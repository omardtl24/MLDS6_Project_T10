import tensorflow as tf

data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal"),
    tf.keras.layers.RandomRotation(0.2),
    tf.keras.layers.RandomZoom(0.2),
    tf.keras.layers.RandomTranslation(0.2, 0.2),
    tf.keras.layers.Rescaling(1./255)
])

easy_rescaling = tf.keras.Sequential([
    tf.keras.layers.Rescaling(1./255)
])

def loadAndAugmentImagesFromDirectory(directory, batch_size, image_size=(720, 500)):
    """
    Loads images from a specified directory and applies data augmentation.

    Parameters:
    - directory (str): Path to the directory containing the images, organized into subdirectories by label.
    - batch_size (int): Number of images per batch.
    - image_size (tuple): Target size of the images (height, width).

    Returns:
    - tf.data.Dataset: A TensorFlow dataset with augmented images and their labels.

    Notes:
    - The data augmentation pipeline is applied during training, ensuring variability in the training data.
    """
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        image_size=image_size,
        batch_size=batch_size,
        label_mode='categorical',
        shuffle=True
    )
    dataset = dataset.map(lambda x, y: (data_augmentation(x, training=True), y))
    return dataset

def loadImagesFromDirectory(directory, batch_size, image_size=(720, 500)):
    """
    Loads images from a specified directory and applies simple rescaling.

    Parameters:
    - directory (str): Path to the directory containing the images, organized into subdirectories by label.
    - batch_size (int): Number of images per batch.
    - image_size (tuple): Target size of the images (height, width).

    Returns:
    - tf.data.Dataset: A TensorFlow dataset with rescaled images and their labels.

    Notes:
    - This function is suitable for validation or testing datasets where no augmentation is needed.
    """
    dataset = tf.keras.preprocessing.image_dataset_from_directory(
        directory,
        image_size=image_size,
        batch_size=batch_size,
        label_mode='categorical',
        shuffle=True
    )
    dataset = dataset.map(lambda x, y: (easy_rescaling(x, training=True), y))
    return dataset