# Python Leetcode note

## 49

### anagrams = {} (a standard dictionary) and dict = collections.defaultdict(list)

```py
dict = {}

defaultdict = collections.defaultdict(list)
```

- Standard Dictionary raises `KeyError` if key is missing
- Default Dictionary creates a default value automatically (e.g., `[]` for `list`).

```py
anagrams = defaultdict(list)
        for str in strs:
            # sort the word
            sorted_word = "".join(sorted(str))
            # Don't need to check if the sorted word is in the dictionary
            anagrams[sorted_word].append(str)
        return list(anagrams.values())

        # anagrams = {}
        # for str in strs:
        #     # sort the word
        #     sorted_word = "".join(sorted(str))
        #     # if the sorted word is not in the dictionary, add it
        #     if sorted_word not in anagrams:
        #         anagrams[sorted_word] = [str]
        #     else:
        #         anagrams[sorted_word].append(word)
        # return list(anagrams.values())
```
