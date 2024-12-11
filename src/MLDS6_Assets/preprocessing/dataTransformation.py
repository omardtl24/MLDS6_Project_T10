import cv2
import os
from PIL import Image
import shutil

def copyFiles(source_path, destination_path):
    """
    Copies all files from the source directory to the destination directory.

    Parameters
    ----------
    source_path : str
        The path to the source directory containing files to copy.
    destination_path : str
        The path to the destination directory where files will be copied.

    Raises
    ------
    FileNotFoundError
        If the source directory does not exist.
    NotADirectoryError
        If either the source or destination path is not a directory.
    Exception
        For other unexpected errors during the copy process.

    Notes
    -----
    - This function does not copy subdirectories; only files in the top-level
      of the source directory are copied.
    - If the destination directory does not exist, it will be created.
    """
    # Check if the source directory exists
    if not os.path.exists(source_path):
        raise FileNotFoundError(f"The source path '{source_path}' does not exist.")

    # Check if the source path is a directory
    if not os.path.isdir(source_path):
        raise NotADirectoryError(f"The source path '{source_path}' is not a directory.")

    # Ensure the destination directory exists, create it if necessary
    if not os.path.exists(destination_path):
        os.makedirs(destination_path)
    elif not os.path.isdir(destination_path):
        raise NotADirectoryError(f"The destination path '{destination_path}' is not a directory.")

    # Iterate over files in the source directory
    filesNumber = 0
    for file_name in os.listdir(source_path):
        source_file = os.path.join(source_path, file_name)
        destination_file = os.path.join(destination_path, file_name)

        # Copy only if it is a file
        if os.path.isfile(source_file):
            try:
                shutil.copy2(source_file, destination_file)
                filesNumber+=1
            except Exception as e:
                print(f"Error copying {source_file} to {destination_file}: {e}")
    print(f'{filesNumber} files copied from {source_path} to {destination_path}')

def resizeImage(image_path, size, verbose = False):
    """
    Resizes image to the specified size and overwrites the original image

    Parameters:
        image_path (str): Path to the image file
        size(tuple) : Desired size as (width. height)
    Returns:
        None
    Raises:
        Exception: If an error occurs during resizing
    """
    try:
        with Image.open(image_path) as img:
            resized_img = img.resize(size, Image.LANCZOS)
            resized_img.save(image_path)
            if verbose: print(f'Image resized and saved to {image_path}')
    except Exception as e:
        raise Exception(f'Error resizing image: {e}')

def applyCallableToFiles(folder_path, callable_func, args = None):
    """
    Walks through all the files in the specified folder and its subfolders, and applies the 
    given callable function to each file.
    
    Parameters:
    folder_path (str): The path of the directory to walk through.
    callable_func (callable): A function to be applied to each file. It must accept the file path as its argument.
    
    Raises:
    FileNotFoundError: If the folder path does not exist.
    """
    
    # Check if the provided folder path exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder at {folder_path} does not exist.")
    c = 0
    # Walk through all the directories and files in the folder
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            # Construct the full file path
            if c%600==0: print(f'Progress: {c} files applied')
            file_path = os.path.join(root, file)
            # Apply the callable function to the file path
            if args is None: callable_func(file_path)
            else: callable_func(file_path,**args)
            c+=1
    print(f'Callable applied for {c} files')

def convertThreeChannelstoOneChannel(image_path, verbose=False):
    """
    Checks the number of channels in the input image. If the image has three channels (RGB),
    it converts it to grayscale. If the image already has one channel (grayscale), it remains unchanged.
    The processed image will overwrite the original image file.

    Parameters:
    image_path (str): The file path of the image to be processed.
    verbose (bool): If True, print detailed messages about the process.
    
    Returns:
    numpy.ndarray: The processed image, either as a grayscale image or the original image 
                    if it was already in grayscale.
    
    Raises:
    FileNotFoundError: If the image file does not exist or cannot be loaded.
    """
    
    # Load the image from the provided path
    image = cv2.imread(image_path)
    
    if image is not None:
        if verbose:
            print(f"Original image shape: {image.shape}")  # (height, width, channels)
        
        # Check if the image has 3 channels (RGB)
        if image.shape[2] == 3:
            # Convert the image to grayscale
            grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            if verbose:
                print("Image has been converted to grayscale.")
            # Overwrite the original image with the grayscale image
            cv2.imwrite(image_path, grayscale_image)
            return grayscale_image
        else:
            if verbose:
                print("Image is already in grayscale or has more than 3 channels.")
            # If the image is already grayscale, save it back unchanged
            cv2.imwrite(image_path, image)
            return image
    else:
        # Raise an error if the image could not be loaded
        raise FileNotFoundError(f"Failed to load image at {image_path}. Please check the file path.")