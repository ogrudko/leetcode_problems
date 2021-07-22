class Solution:
    def strStr(self, haystack, needle):
        if needle == "" or haystack == "":
            return 0
        elif needle not in haystack:
            return -1
        else:
            print(haystack.find(needle))

        

solution = Solution()
solution.strStr("hello world", "wo")