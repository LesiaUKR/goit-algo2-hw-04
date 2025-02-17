class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key, value=None):
        """
        Inserts a key into the Trie with an optional value.

        Args:
            key (str): The key to insert.
            value (any, optional): The value associated with the key.
            Defaults to None.

        Raises:
            TypeError: If the key is not a non-empty string.
        """
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for put: key = {key} must be a "
                f"non-empty string"
            )

        current = self.root
        for char in key:
            if char not in current.children:
                current.children[char] = TrieNode()
            current = current.children[char]
        if current.value is None:
            self.size += 1
        current.value = value

    def get(self, key):
        """
        Retrieves the value associated with a key in the Trie.

        Args:
            key (str): The key to search for.

        Returns:
            any: The value associated with the key, or None if the
            key is not found.

        Raises:
            TypeError: If the key is not a non-empty string.
        """
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for get: key = {key} must be a "
                f"non-empty string"
            )

        current = self.root
        for char in key:
            if char not in current.children:
                return None
            current = current.children[char]
        return current.value

    def delete(self, key):
        """
        Deletes a key from the Trie.

        Args:
            key (str): The key to delete.

        Returns:
            bool: True if the key was deleted, False otherwise.

        Raises:
            TypeError: If the key is not a non-empty string.
        """
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for delete: key = {key} must be a "
                f"non-empty string"
            )

        def _delete(node, key, depth):
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    return len(node.children) == 0
                return False

            char = key[depth]
            if char in node.children:
                should_delete = _delete(node.children[char], key, depth + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, key, 0)

    def is_empty(self):
        """
        Checks if the Trie is empty.

        Returns:
            bool: True if the Trie is empty, False otherwise.
        """
        return self.size == 0

    def longest_prefix_of(self, s):
        """
        Finds the longest key in the Trie that is a prefix of the given string.

        Args:
            s (str): The string to search for.

        Returns:
            str: The longest prefix found, or an empty string if
            no prefix is found.

        Raises:
            TypeError: If the input is not a non-empty string.
        """
        if not isinstance(s, str) or not s:
            raise TypeError(
                f"Illegal argument for longestPrefixOf: s = {s} must be "
                f"a non-empty string"
            )

        current = self.root
        longest_prefix = ""
        current_prefix = ""
        for char in s:
            if char in current.children:
                current = current.children[char]
                current_prefix += char
                if current.value is not None:
                    longest_prefix = current_prefix
            else:
                break
        return longest_prefix

    def keys_with_prefix(self, prefix):
        """
        Finds all keys in the Trie that start with the given prefix.

        Args:
            prefix (str): The prefix to search for.

        Returns:
            list: A list of keys that start with the prefix.

        Raises:
            TypeError: If the prefix is not a string.
        """
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for keysWithPrefix: prefix = {prefix} "
                f"must be a string"
            )

        current = self.root
        for char in prefix:
            if char not in current.children:
                return []
            current = current.children[char]

        result = []
        self._collect(current, list(prefix), result)
        return result

    def _collect(self, node, path, result):
        """
        Helper function to collect all keys in the Trie starting from a
        given node.

        Args:
            node (TrieNode): The current node in the Trie.
            path (list): The current path of characters.
            result (list): The list to store the results.
        """
        if node.value is not None:
            result.append("".join(path))
        for char, next_node in node.children.items():
            path.append(char)
            self._collect(next_node, path, result)
            path.pop()

    def keys(self):
        """
        Retrieves all keys in the Trie.

        Returns:
            list: A list of all keys in the Trie.
        """
        result = []
        self._collect(self.root, [], result)
        return result
