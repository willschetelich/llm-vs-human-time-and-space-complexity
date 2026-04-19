from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Time: O(n*L), Space: O(n*L)
        result = []
        i = 0
        while i < len(words):
            line_words = [words[i]]
            line_len = len(words[i])
            i += 1
            while i < len(words) and line_len + 1 + len(words[i]) <= maxWidth:
                line_len += 1 + len(words[i])
                line_words.append(words[i])
                i += 1
            if i == len(words) or len(line_words) == 1:
                line = ' '.join(line_words)
                result.append(line + ' ' * (maxWidth - len(line)))
            else:
                total_spaces = maxWidth - sum(len(w) for w in line_words)
                gaps = len(line_words) - 1
                space, extra = divmod(total_spaces, gaps)
                line = ''
                for j, word in enumerate(line_words[:-1]):
                    line += word + ' ' * (space + (1 if j < extra else 0))
                line += line_words[-1]
                result.append(line)
        return result
