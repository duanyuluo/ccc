def ccc2023j4():
    """number of column"""
    C = int(input())

    tape = 0

    """row 1, 2"""
    rows = [input().split(" ")]
    rows.append(input().split(" "))

    tape += calcrow(rows=rows, rowId=0, C=C)
    tape += calcrow(rows=rows, rowId=1, C=C)

    print(tape)

def calcrow(rows: list, rowId: int, C: int) -> int:
    """Returns tape meters"""
    tape = 0
    for i in range(0, C):
        """not wet, continue"""
        if (rows[rowId][i] == "0"):
            continue
        else: 
            if (i == 0):
                tape += 1
            else:
                """check wet or not in side A"""
                if (rows[rowId][i-1] == "0"):
                    tape += 1
            if (i == C - 1):
                tape += 1
            else:
                """side B"""
                if (rows[rowId][i+1] == "0"):
                    tape += 1
            if ((i + 1) % 2 == 0):
                tape += 1
            else:
                if (rows[(1 if rowId == 0 else 0)][i] == "0"):
                    tape += 1    
    return tape  


if (__name__ == "__main__"):
    ccc2023j4()