from colorama import Fore, Style, init
from trie import Trie

# Initialize colorama for colored console output
init(autoreset=True)


class Homework(Trie):
    def count_words_with_suffix(self, pattern: str) -> int:
        """
        Counts the number of words in the Trie that end with the given suffix.

        Args:
            pattern (str): The suffix to search for. Must be a non-empty string.

        Returns:
            int: The number of words ending with the given suffix. Returns 0
             if no words match
                 or if the input is invalid.

        Raises:
            None: Errors are handled internally, and a message is printed to
            the console.
        """
        if not isinstance(pattern, str) or not pattern:
            print(Fore.RED + "Error: Suffix must be a non-empty string.")
            return 0

        count = 0

        def _dfs(node, current_suffix):
            """
            Helper function to perform a depth-first search (DFS) on the Trie.

            Args:
                node (TrieNode): The current node in the Trie.
                current_suffix (str): The suffix formed by traversing the Trie
                up to this node.
            """
            nonlocal count
            if node.value is not None:
                if current_suffix.endswith(pattern):
                    count += 1
            for char, child_node in node.children.items():
                _dfs(child_node, current_suffix + char)

        _dfs(self.root, "")
        print(Fore.GREEN + f"Number of words ending with '{pattern}': {count}")
        return count

    def has_prefix(self, prefix: str) -> bool:
        """
        Checks if there is any word in the Trie that starts with the given
        prefix.

        Args:
            prefix (str): The prefix to search for. Must be a non-empty string.

        Returns:
            bool: True if any word starts with the prefix, False otherwise.
            Returns False if the input is invalid.

        Raises:
            None: Errors are handled internally, and a message is printed
            to the console.
        """
        if not isinstance(prefix, str) or not prefix:
            print(Fore.RED + "Error: Prefix must be a non-empty string.")
            return False

        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                print(Fore.YELLOW + f"No words found with prefix '{prefix}'")
                return False
            current_node = current_node.children[char]

        print(Fore.BLUE + f"Words found with prefix '{prefix}'")
        return True

if __name__ == "__main__":
    trie = Homework()
    words = ["apple", "application", "banana", "cat"]
    print(Fore.RED +f"Words in Trie:  {words}")
    for i, word in enumerate(words):
        trie.put(word, i)

    # Test count_words_with_suffix method
    assert trie.count_words_with_suffix("e") == 1  # apple
    assert trie.count_words_with_suffix("ion") == 1  # application
    assert trie.count_words_with_suffix("a") == 1  # banana
    assert trie.count_words_with_suffix("at") == 1  # cat

    # Test has_prefix method
    assert trie.has_prefix("app") == True  # apple, application
    assert trie.has_prefix("bat") == False
    assert trie.has_prefix("ban") == True  # banana
    assert trie.has_prefix("ca") == True  # cat