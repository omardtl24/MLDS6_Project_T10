import numpy as np
import os

def underSampling(imagePath, samples, seed=42):
    """
    Randomly samples a specified number of image files from a given directory.

    This function performs random sampling without replacement on the files located 
    in the specified directory. It returns the names of the sampled files.

    Parameters
    ----------
    imagePath : str
        The path to the directory containing image files to sample from.
    samples : int
        The number of files to randomly sample.
    seed : int, optional
        The seed for the random number generator to ensure reproducibility. 
        Default is 42.

    Returns
    -------
    numpy.ndarray
        An array of sampled file names.

    Raises
    ------
    ValueError
        If the number of samples requested exceeds the number of files in the directory.
    FileNotFoundError
        If the specified directory does not exist.

    Notes
    -----
    - Sampling is done without replacement, meaning files are not selected more than once.
    - The `seed` parameter allows for customizable reproducibility.
    """
    # Ensure reproducibility
    np.random.seed(seed)

    # Get the list of image files in the directory
    images = os.listdir(imagePath)

    # Check if sampling size is valid
    if samples > len(images):
        raise ValueError("Number of samples requested exceeds the number of files in the directory.")
    
    # Perform random sampling
    sampled_images = np.random.choice(images, samples, replace=False)

    print(f'A total of {len(sampled_images)} files were sampled')
    return sampled_images

import os

def deleteUnselectedImages(image_dir, selected_images):
    """
    Deletes all images in a directory except those specified in a given list.

    This function iterates through all files in the specified directory and deletes 
    files that are not present in the `selected_images` list.

    Parameters
    ----------
    image_dir : str
        The path to the directory containing the images to be filtered.
    selected_images : list of str
        A list of file names that should be retained in the directory.

    Returns
    -------
    None
        The function prints the number of files deleted.

    Raises
    ------
    FileNotFoundError
        If the specified directory does not exist.
    PermissionError
        If the program lacks permissions to delete files in the directory.

    Notes
    -----
    - This function assumes the provided `selected_images` contains only file names, not full paths.
    - The deletions are irreversible; ensure you have a backup if necessary.
    - Files not listed in `selected_images` are deleted regardless of their type.
    """
    # Convert the list of selected images to a set for faster lookups
    selected_images_set = set(selected_images)
    c = 0  # Counter for deleted images

    # Iterate over files in the directory
    for filename in os.listdir(image_dir):
        file_path = os.path.join(image_dir, filename)

        # Delete files not in the selected images set
        if filename not in selected_images_set:
            os.remove(file_path)
            c += 1

    print(f'A total of {c} images were deleted')
