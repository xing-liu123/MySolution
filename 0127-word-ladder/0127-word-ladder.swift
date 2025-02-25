class Solution {
    func ladderLength(_ beginWord: String, _ endWord: String, _ wordList: [String]) -> Int {
        var wordSet = Set(wordList)

        if !wordSet.contains(endWord) {
            return 0
        }

        var queue: [String] = []
        let lowercase = "abcdefghijklmnopqrstuvwxyz"

        queue.append(beginWord)

        var count = 0

        while !queue.isEmpty {
            let size = queue.count
            count += 1

            for _ in 0..<size {
                let word = queue.removeFirst()

                for i in 0..<word.count {
                    var charArray = Array(word)
                    for c in lowercase {
                        charArray[i] = c

                        let nextWord = String(charArray)

                        if wordSet.contains(nextWord) {
                            if nextWord == endWord {
                                return count + 1
                            }
                            print(nextWord)
                            queue.append(nextWord)
                            wordSet.remove(nextWord)
                        }
                    }
                }
            }
        }

        return 0
    }
}