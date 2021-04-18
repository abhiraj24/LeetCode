class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if len(s.split())==0:
            return 0
        s_list=s.split()
        return len(s_list[len(s_list)-1])