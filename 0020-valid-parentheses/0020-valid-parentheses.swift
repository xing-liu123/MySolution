class Solution {
    func isValid(_ s: String) -> Bool {
        var stack: [Character] = []

        for char in s {
            if char == "{" || char == "[" || char == "(" {
                stack.append(char)
            } else if char == "}" || char == "]" || char == ")"{
                if stack.isEmpty {
                    return false
                }

                switch char {
                    case "}":
                        if stack.last != "{" {
                            return false
                        }
                        stack.popLast()
                    case "]":
                        if stack.last != "[" {
                            return false
                        }
                        stack.popLast()
                    case ")":
                        if stack.last != "(" {
                            return false
                        }
                        stack.popLast()
                    default:
                        break
                }
            }
        }

        return stack.isEmpty

    }
}