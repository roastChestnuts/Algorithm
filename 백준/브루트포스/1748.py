n = input()
n_len = len(n)-1

#각 자릿수별 총 합
numbers = [9 * (i+1) * (10**(i)) for i in range(9)]
#1억은 숫자 9개
numbers.append(9) 

#만약 20이라면 1~9까지 합 더하기
answer = sum(numbers[:n_len])
#20 - 10 => 총 11개 * 자릿수 [두 숫자 사이의 개수 구하기 => m - n + 1]
answer += (int(n) - (10 ** n_len) + 1) * (n_len + 1)

print(answer)