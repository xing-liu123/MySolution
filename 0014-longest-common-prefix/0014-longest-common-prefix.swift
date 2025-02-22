class TrieNode {
    var children: [Character: TrieNode] = [:]
    var isEnd = false
}

class Trie {
    var root = TrieNode()
    var prefix = ""

    func insert(_ word: String) {
        var curr = root
        var tempPrefix = ""

        for c in word {
            if curr.children[c] == nil {
                curr.children[c] = TrieNode()
            }

            if curr.children.count > 1 || curr.isEnd{
                break
            }

            
            tempPrefix.append(c)
            curr = curr.children[c]!

        } 
        curr.isEnd = true
        prefix = tempPrefix
    }
}

class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var trie = Trie()

        for str in strs {
            trie.insert(str)
        }

        return trie.prefix
    }
}