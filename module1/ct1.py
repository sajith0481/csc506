def linear_search(data, target):
    """
    Searches for a target in a given dataset using linear search.
    
    Parameters:
    data (list): List of elements to search within.
    target: The item to search for.

    Returns:
    int: Index of the target if found, otherwise -1.
    """
    for index, value in enumerate(data):
        if value == target:
            return index
    return -1

# Example Usage
if __name__ == "__main__":
    marketplace_items = ["laptop", "smartphone", "tablet", "headphones", "camera"]
    target_item = "tablet"
    
    result = linear_search(marketplace_items, target_item)
    if result != -1:
        print(f"Item '{target_item}' found at index {result}.")
    else:
        print(f"Item '{target_item}' not found.")
