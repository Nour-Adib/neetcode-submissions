class Solution:

    def encode(self, strs: List[str]) -> str:
        if(len(strs) == 0):
            return ""
        # For each word, let's get it's length
        # Then we add the length info at the front, with separating characters
        # Then a break character, which after that we start the sequency - glued together
        # Then we basically keep splicing

        word_lengths = []
        IN_HEADER_BREAK_CHAR = "-"
        END_OF_HEADER_CHAR = "_"

        for word in strs:
            word_length = len(word)
            word_lengths.append(word_length)

        encoded_header = IN_HEADER_BREAK_CHAR.join([str(number) for number in word_lengths])

        print(encoded_header)

        return f'{encoded_header}{END_OF_HEADER_CHAR}{''.join(strs)}'

    def decode(self, s: str) -> List[str]:
        print(s)
        if(len(s) == 0):
            return []
        IN_WORD_BREAK_CHAR = "-"
        END_OF_HEADER_CHAR = "_"

        header = s.split(END_OF_HEADER_CHAR)[0]
        print(header)
        message = s[len(header)+1:]
        print(message)

        reassembled_words = []
        word_lengths = header.split(IN_WORD_BREAK_CHAR)
        
        for length in word_lengths:
            reassembled_words.append(message[:int(length)])

            # Edit the string by removed the word we just took out
            message = message[int(length):]

        return reassembled_words

