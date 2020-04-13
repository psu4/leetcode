class Solution:

    # https://www.youtube.com/watch?v=BHC0vgpsl5k
    def groupAnagrams(self, strs:List[str]) -> List[List[str]]:

    # we go through every string in the list, and sort each string

    # then we store the sorted string in the dictionary if it doesn't exist

    # or update the dictionary value if it exists

        solution = {}

        if len(strs) < 1:

            return strs

        else:

            # we want to go for each element in the list

            for i in range(len(strs)):

                reg = strs[i]

                print('reg data type is' + str(type(reg)))

                regsort = ''.join(sorted(reg))  # sort(reg) turns ['eat'] into ['a','e','t']

                # joins connect the word into 'aet' as a string

                print('solution data type is' + str(type(solution)))
                print('regsort data type is' + str(type(regsort)))

                if regsort in solution:

                    solution[regsort].append(reg)

                else:

                    solution[regsort] = [reg]

        return solution.values()