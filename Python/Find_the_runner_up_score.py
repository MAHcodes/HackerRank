if __name__ == '__main__':
    score = []
    n = int(input())
    arr = map(int, input().split())
    for i in arr:
        if i not in score:
            score.append(i)          
    score.sort()
    print(score[-2])
