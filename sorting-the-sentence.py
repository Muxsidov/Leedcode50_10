# Buble sort implementation
# https://leetcode.com/problems/sorting-the-sentence/submissions/

    def sortSentence(self, s: str) -> str:
        
        string_list = s.split(' ')
        
        for i in range(len(string_list) - 1):
            for j in range(0, len(string_list) - i - 1):
                if int(string_list[j][-1]) > int(string_list[j + 1][-1]):
                    string_list[j], string_list[j + 1] = string_list[j + 1], string_list[j]
        return ' '.join(i[:-1] for i in string_list)
      
        # Second way to solve it
        # sorted_list = [''] * len(string_list)

            # for i in string_list:
            #     position = int(i[-1])
            #     sorted_list[position - 1] = i[:-1]

        #return ' '.join(sorted_list)
