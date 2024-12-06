import os
import matplotlib.pyplot as plt

def printTree(directory, indent_level=0):
    """
    Recursively prints the folder tree for the given directory.

    Parameters:
    directory (str): The path of the directory to start the tree.
    indent_level (int): The level of indentation for the current folder.
    """
    try:
        # Print the current directory
        print(' ' * (4 * indent_level) + f'📁 {os.path.basename(directory)}')
        # Iterate over items in the directory
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isdir(item_path):
                # Recursively print subdirectory
                printTree(item_path, indent_level + 1)
    except PermissionError:
        print(' ' * (4 * indent_level) + f'🚫 Permission denied: {directory}')
    except FileNotFoundError:
        print(' ' * (4 * indent_level) + f'❓ Directory not found: {directory}')


def plotDataPartition(data_dict, title): 
    """
    Plots a bar chart based on the provided dictionary data.

    Parameters
    ----------
    data_dict : dict
        A dictionary where the keys represent categories (x-axis labels) and the values represent the corresponding numerical values (heights of the bars).
    
    title : str
        The title to be displayed on the bar chart.

    Returns
    -------
    None
        This function does not return any value. It displays a bar chart.

    Raises
    ------
    ValueError
        If `data_dict` is empty or does not contain any valid numerical values for the bars.
    """
    if not data_dict:
        raise ValueError("The data dictionary is empty.")
    
    keys = list(data_dict.keys())
    values = list(data_dict.values())

    total_sum = sum(values)
    
    plt.figure(figsize=(10, 6))
    bars = plt.bar(keys, values, color='skyblue')

    # Add value labels above each bar
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval, int(yval), ha='center', va='bottom')

    plt.legend([f"Total de muestras: {total_sum}"], fontsize=10)

    plt.title(title)
    plt.xlabel('Categorias')
    plt.ylabel('Numero de elementos')
    plt.tight_layout()
    plt.show()