def parse_poem(poem):
    """
    Parses the poem into a list of lines.
    
    Args:
        poem (str): The poem as a string.
        
    Returns:
        list: A list of lines in the poem.
    """

    # split poem into lines and strip whitespace
    return [line.strip() for line in poem.strip().split("\n") if line.strip()]