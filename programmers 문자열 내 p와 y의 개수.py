  def solution(s):
	answer = False
	p_num = 0
	y_num = 0
    lists = ['p','y'] # 알파벳 리스트 
    s = s.lower()
    for i in s: # 입력 받은 문자열을 for문을 통해 확인
      if i in lists: # 만약 리스트 안에 알파벳이 있다면
          if i == lists[0] : # 알파벳이 p인 경우
              p_num +=1
          elif i == lists[1] : # 알파벳이 y인 경우
              y_num +=1 
      else : # 리스트 안에 알파벳이 없으면 True
          answer = True

  if p_num == y_num : # 알파벳 개수가 같으면 True
      answer = True
  else : # 같지 않으면 False 
      answer = False


  return answer 
