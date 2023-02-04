def solution(answers):
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    answer = [0, 0, 0]
    return_ans = []
    for i in range(len(answers)):
        index1 = i%5
        index2 = i%8
        index3 = i%10
        
        if num1[index1] == answers[i]:
            answer[0] += 1
        if num2[index2] == answers[i]:
            answer[1] += 1
        if num3[index3] == answers[i]:
            answer[2] += 1    
    
    k = max(answer)
    
    if k == answer[0]:
        return_ans.append(1)
    if k == answer[1]:
        return_ans.append(2)
    if k == answer[2]:
        return_ans.append(3)
    return return_ans