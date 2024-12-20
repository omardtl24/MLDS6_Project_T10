import os
import shutil
import re

def separateImages(originalPath,targetPath):
    """
    Given a target path, separates the images by class in a target directory

    Parameters:
    ----------
    originalPath (str): Source path of the images
    targetPath (str): Destiny path to the images separated by classes
    """
    pattern = re.compile(r'../data[/\\]([^/\\]+)[/\\]([^/\\]+)$')
    m = pattern.search(targetPath)
    s1 , s2 = m.groups()

    mapper_path = {
      'Normal' : 'NORMAL',
      'bacterialPneumonia' : 'PNEUMONIA',
      'virusPneumonia' : 'PNEUMONIA'
    }

    originPath = originalPath+f'{s1}/{mapper_path[s2]}'

    mapper = {
      'bacterialPneumonia' : 'bacteria',
      'virusPneumonia' : 'virus'
    }

    if mapper_path[s2]=='NORMAL':
        for item in os.listdir(originPath):
            s = os.path.join(originPath, item)
            d = os.path.join(targetPath, item)
            shutil.copy2(s, d)
    else:
        for item in os.listdir(originPath):
            if mapper[s2] in item:
                s = os.path.join(originPath, item)
                d = os.path.join(targetPath, item)
                shutil.copy2(s, d)
    print(f'Copied files to {targetPath}')

def createDirectoryWithSubdirs(base_dir, subdirs):
    """
    Given a base dir, creates a set of subdirs inside of it

    Parameters:
    ----------
    base_dir (str): Path of the base directory that is wanted to be created
    subdirs (str): Name of the subdirectories that are wanted to be created inside the base directory

    Returns:
    ----------
        List of path names of the created directories (List of str)

    """
    os.makedirs(base_dir, exist_ok=True)
    dirs = []
    for subdir in subdirs:
        path = os.path.join(base_dir, subdir)
        os.makedirs(path, exist_ok=True)
        dirs.append(path)
        print(f"Directory created: {path}")
    return dirs

def deleteDirectoryAndContents(directory):
    """
    Deletes a directory and all its contents (files and subdirectories).

    Parameters:
    ----------
    directory (str): The path to the directory to delete.
    """
    try:
        # Delete the directory and its contents
        shutil.rmtree(directory)
        print(f"Deleted directory and all contents: {directory}")
    except FileNotFoundError:
        print(f"Directory not found: {directory}")
    except PermissionError:
        print(f"Permission denied: {directory}")
    except Exception as e:
        print(f"An error occurred: {e}")

def deleteFilesAndSubdirectories(directory):
    """
    Deletes all files and subdirectories within a given directory.

    Parameters:
    directory (str): The path to the directory to clean.
    """
    try:
        # List all items in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path) or os.path.islink(item_path):
                # Delete file or symbolic link
                os.remove(item_path)
                print(f"Deleted file: {item_path}")
            elif os.path.isdir(item_path):
                # Delete directory and its contents
                shutil.rmtree(item_path)
                print(f"Deleted directory: {item_path}")
    except Exception as e:
        print(f"An error occurred: {e}")