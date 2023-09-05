def remove_duplicates(sequence):
    """
    Removes duplicates from a sequence.

    Args:
        sequence (list or tuple): The sequence to remove duplicates from.

    Returns:
        list: A new sequence with duplicates removed.
    """

    # Create a set to store the unique elements of the sequence.
    unique_elements = set(sequence)

    # Return a list of the unique elements.
    return list(unique_elements)


def remove_duplicates(sequence):
    seen = set()
    result = []
    
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    
    return result

# Sample input
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  # Output: [2, 3, 4, 5, 6, 7]
