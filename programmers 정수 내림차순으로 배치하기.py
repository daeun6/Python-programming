def solution(n):
    stack =[]
    for i in str(n):
        stack.append(i) # 문자로 변환하여 스택에 추가
    stack.sort(reverse=True) # 내림차순으로 정렬
    answer = int(''.join(stack)) # join함수를 사용하여 리스트의 요소들을 합친 후 int()를 사용하여 정수로 바꿔 리턴 
    return answer
