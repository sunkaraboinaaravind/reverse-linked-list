class Solution:
    def isValidSerialization(self, preorder: str) -> bool:
        if len(preorder) == 1:
            return True if preorder[0] == "#" else False
        if preorder[0] == "#":
            return False
        preorder = deque(preorder.split(","))
        preorder.popleft()
        def sim():
            for _ in range(2):
                if not preorder:
                    return False
                top = preorder.popleft()
                if top != "#":
                    sim()
            return True
        return True if (sim() and (not preorder)) else False
        
