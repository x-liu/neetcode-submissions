class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowSums = [0]*9
        colSums = [0]*9
        subBoxSums = [[0 for i in range(3)] for j in range(3)]
        rowNums = [[0]*10 for i in range(10)]
        colNums = [[0]*10 for i in range(10)]
        subBoxNums = [[[0]*10 for i in range(3)] for i in range(3)]
        for j, row in enumerate(board):
            for i, val in enumerate(row):
                if val == '.':
                    num = 0
                else:
                    num = int(val)
                rowNums[i][num]+=1
                colNums[j][num]+=1
                subBoxNums[i//3][j//3][num]+=1
                if (num != 0 and rowNums[i][num] >1): return False
                if (num != 0 and colNums[j][num] >1): return False
                if (num != 0 and subBoxNums[i//3][j//3][num] >1): return False
        return True

