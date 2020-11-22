class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
                 "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        uniq = set()
        for w in words:
            r = ''.join([morse[ord(w[i]) % 97] for i in range(len(w))])
            uniq.add(r)
        return len(uniq)
