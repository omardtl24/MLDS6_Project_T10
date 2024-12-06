import os
from PIL import Image

def countFilesinFolder(carpeta):
    """
    Counts the total number of files in a folder and its subfolders.

    Parameters
    ----------
    carpeta : str
        Path to the folder whose files are to be counted.

    Returns
    -------
    int
        Total number of files in the specified folder and its subfolders.

    Raises
    ------
    FileNotFoundError
        If the specified folder does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    if not os.path.exists(carpeta):
        raise FileNotFoundError(f"The folder '{carpeta}' does not exist.")
    if not os.path.isdir(carpeta):
        raise NotADirectoryError(f"The path '{carpeta}' is not a directory.")
    
    contador = 0
    for _ , _, archivos in os.walk(carpeta):
        contador += len(archivos)
    return contador


def getFileExtensions(carpeta):
    """
    Retrieves the unique file extensions from a folder and its subfolders.

    Parameters
    ----------
    carpeta : str
        Path to the folder from which to extract file extensions.

    Returns
    -------
    set
        A set containing the unique file extensions (in lowercase) found in the specified folder and its subfolders.
        If no files with extensions are found, an empty set is returned.

    Raises
    ------
    FileNotFoundError
        If the specified folder does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    if not os.path.exists(carpeta):
        raise FileNotFoundError(f"The folder '{carpeta}' does not exist.")
    if not os.path.isdir(carpeta):
        raise NotADirectoryError(f"The path '{carpeta}' is not a directory.")
    
    extensiones_archivos = set()
    for _, _, archivos in os.walk(carpeta):
        for archivo in archivos:
            extension = os.path.splitext(archivo)[1].lower()
            if extension:
                extensiones_archivos.add(extension)
    return extensiones_archivos


def analyzeImageShapes(directory): 
    """
    Analyzes the shapes (dimensions) of image files in a given directory and its subdirectories.

    Parameters
    ----------
    directory : str
        Path to the directory containing the image files to be analyzed. The function supports the following image formats: PNG, JPG, JPEG, BMP, and TIFF.

    Returns
    -------
    str
        A summary string containing:
        - The number of different image shapes found.
        - The shape with the most pixels and its total pixel count.
        - The shape with the least pixels and its total pixel count.

    Raises
    ------
    FileNotFoundError
        If the specified directory does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    shape_count = {}
    max_pixels = 0
    min_pixels = float('inf')
    max_shape = None
    min_shape = None

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                file_path = os.path.join(root, filename)
                with Image.open(file_path) as img:
                    shape = img.size
                    pixels = shape[0] * shape[1]

                    # Count different shapes
                    shape_count[shape] = shape_count.get(shape, 0) + 1

                    # Determine max and min shapes
                    if pixels > max_pixels:
                        max_pixels = pixels
                        max_shape = shape
                    if pixels < min_pixels:
                        min_pixels = pixels
                        min_shape = shape

    num_different_shapes = len(shape_count)

    res = f"""Number of different shapes: {num_different_shapes}
Shape with most pixels: {max_shape} (Total pixels: {max_pixels})
Shape with least pixels: {min_shape} (Total pixels: {min_pixels})"""

    return res

def analyzeImageChannels(directory): 
    """
    Analyzes the number of color channels in image files in a given directory and its subdirectories.

    Parameters
    ----------
    directory : str
        Path to the directory containing the image files to be analyzed. The function supports the following image formats: PNG, JPG, JPEG, BMP, and TIFF.

    Returns
    -------
    str
        A summary string containing:
        - The number of images with 1 channel (grayscale).
        - The number of images with 3 channels (RGB).
        - The number of images with other channel configurations.

    Raises
    ------
    FileNotFoundError
        If the specified directory does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    grayscale_count = 0
    rgb_count = 0
    other_channels_count = 0

    # Walk through the directory and subdirectories
    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                file_path = os.path.join(root, filename)
                with Image.open(file_path) as img:
                    channels = len(img.getbands())  # Number of channels in the image
                    
                    # Categorize the image based on the number of channels
                    if channels == 1:
                        grayscale_count += 1
                    elif channels == 3:
                        rgb_count += 1
                    else:
                        other_channels_count += 1

    res = f"""Number of grayscale images (1 channel): {grayscale_count}
Number of RGB images (3 channels): {rgb_count}
Number of images with other channel configurations: {other_channels_count}"""

    return res


import os

def getFolderSize(folder_path):
    """
    Calculates the total size of a folder and its subfolders in GB.

    Parameters
    ----------
    folder_path : str
        Path to the folder whose size is to be calculated.

    Returns
    -------
    float
        The total size of the folder in gigabytes (GB).

    Raises
    ------
    FileNotFoundError
        If the specified folder does not exist.
    NotADirectoryError
        If the specified path is not a directory.
    """
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The folder '{folder_path}' does not exist.")
    if not os.path.isdir(folder_path):
        raise NotADirectoryError(f"The path '{folder_path}' is not a directory.")
    
    total_size = 0
    # Walk through the folder and accumulate the sizes of all files
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)

    # Convert the total size from bytes to GB
    total_size_gb = total_size / (1024 ** 3)

    return total_size_gb
