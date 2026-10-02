class WordDictionary:

    def __init__(self):
       self.root = {} 

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in word:
            if i not in curr:
                curr[i] = {}
            curr = curr[i]
        curr["$"] = True

    def search(self, word: str) -> bool:

        def dfs(j, root):
            curr = root

            for i in range(j, len(word)):
                c = word[i]


                if c == ".":

                    for k, c in curr.items():
                        if k != "$" and dfs(i + 1, c):
                            return True
                    return False


                else:

                    if c not in curr:
                        return False

                    curr = curr[c]

            return "$" in curr

        return dfs(0,self.root)
