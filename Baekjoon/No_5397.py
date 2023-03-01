L = int(input())

for i in range(L):
  str = input()
  left, right = [],[]

  for s in str:
    if s == '<':
        if left:
            right.append(left.pop())
            #커서가 왼쪽으로 이동하면 left스택의 문자열을 right스택으로 옮기고
            #이후 추가된 문자열을 left스택마지막에 추가하면
            # "a b < c"가 입력된 경우 a b -> a c | b -> a c b가 출력되야 정답
    elif s == '>':
        if right:
            left.append(right.pop())
    elif s == '-':
        if left:
            left.pop()
    else:
        left.append(s)
  
  left.extend(reversed(right))
  #ex)예시로 AB<<C값이 입력되었을때 reversed를 해주지않으면
  #정답이 CAB가 되어야하지만 CBA가 나옴 -> '>' 를 해줄때마다 0인덱스에 옮겨지는게아니라 마지막항목으로 추가가 되기때문
  print(''.join(left))