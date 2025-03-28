def compute_lps_array(pattern):
    """Computes the Longest Prefix Suffix (LPS) array for the given pattern."""
    lps = [0] * len(pattern)  # Initialize LPS array with zeros
    prefix_length = 0  # Length of the longest proper prefix that is also a suffix
    index = 1  # Start from the second character

    while index < len(pattern):
        if pattern[index] == pattern[prefix_length]:
            prefix_length += 1
            lps[index] = prefix_length
            index += 1
        else:
            if prefix_length != 0:
                prefix_length = lps[prefix_length - 1]  # Reduce prefix length
            else:
                lps[index] = 0
                index += 1
    
    return lps


def kmp_search(text, pattern):
    """Searches for occurrences of the pattern in the given text using the KMP algorithm."""
    text_length = len(text)
    pattern_length = len(pattern)
    lps = compute_lps_array(pattern)  # Precompute LPS array
    
    text_index = 0  # Index for traversing the text
    pattern_index = 0  # Index for traversing the pattern
    occurrences = []  # List to store the starting indices of matches
    
    while text_index < text_length:
        if pattern[pattern_index] == text[text_index]:
            text_index += 1
            pattern_index += 1
        
        if pattern_index == pattern_length:
            occurrences.append(text_index - pattern_index)  # Match found
            pattern_index = lps[pattern_index - 1]  # Use LPS array to avoid redundant checks
        elif text_index < text_length and pattern[pattern_index] != text[text_index]:
            if pattern_index != 0:
                pattern_index = lps[pattern_index - 1]  # Use LPS array for efficient shifting
            else:
                text_index += 1  # Move text index forward if no partial match
    
    return occurrences


# Example usage
text = "ababcababcabc"
pattern = "abc"
print("Pattern found at indices:", kmp_search(text, pattern))
