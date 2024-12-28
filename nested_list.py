if __name__ == '__main__':
    newList = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        newList.append([name, score])
    
secondLowestValue = sorted(set(x[1] for x in newList))[1]
finalNames = sorted(set(x[0] for x in newList if secondLowestValue==x[1]))

print("\n".join(finalNames))
