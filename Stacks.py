def is_balanced(expression):
    """
    Checks if an expression is balanced.

    Args:
        expression (str): The expression to check.

    Returns:
        bool: True if the expression is balanced, False otherwise.
    """

    # Create a stack to store the opening brackets.
    stack = []

    # Iterate over the characters in the expression.
    for char in expression:
        # If the character is an opening bracket, push it onto the stack.
        if char in "{[(":
            stack.append(char)

        # If the character is a closing bracket, check if it matches the top of the stack.
        elif char in "}])":
            if not stack:
                return False
            if char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == ")" and stack[-1] == "(":
                stack.pop()
            else:
                return False

    # If the stack is empty, the expression is balanced.
    return not stack


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

