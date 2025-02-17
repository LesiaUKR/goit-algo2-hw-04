from colorama import Fore, init
from trie import Trie

# Initialize colorama for colored console output
init(autoreset=True)


class LongestCommonWord(Trie):
    """
    A class to find the longest common prefix among a list of strings using a Trie.

    Inherits from the Trie class.
    """

    def find_longest_common_word(self, strings) -> str:
        """
        Finds the longest common prefix among all strings in the input list.

        Args:
            strings (list): A list of strings to find the longest common prefix for.

        Returns:
            str: The longest common prefix. Returns an empty string if no common prefix exists
                 or if the input is invalid.

        Example:
            >>> trie = LongestCommonWord()
            >>> trie.find_longest_common_word(["flower", "flow", "flight"])
            "fl"
        """
        if not isinstance(strings, list) or not strings:
            print(Fore.RED + "Error: Input must be a non-empty list of strings.")
            return ""

        # Check if any string in the list is empty
        if any(not isinstance(word, str) or not word for word in strings):
            print(Fore.YELLOW + "Warning: The list contains empty or invalid strings. Returning empty prefix.")
            return ""

        # Insert all strings into the Trie
        for word in strings:
            self.put(word)

        # Find the longest common prefix
        current = self.root
        prefix = ""
        while True:
            # If the current node has more than one child or is the end of a word, stop
            if len(current.children) != 1 or current.value is not None:
                break
            # Get the only child node
            char, next_node = next(iter(current.children.items()))
            prefix += char
            current = next_node

        print(Fore.GREEN + f"Longest common prefix: '{prefix}'")
        return prefix

if __name__ == "__main__":
    # Test cases
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""

    # Edge cases
    trie = LongestCommonWord()
    strings = []  # Empty list
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["", "abc", "def"]  # Contains an empty string
    assert trie.find_longest_common_word(strings) == ""

    trie = LongestCommonWord()
    strings = ["abc", 123]  # Invalid input
    assert trie.find_longest_common_word(strings) == ""