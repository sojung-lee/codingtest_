import sys

input_data = sys.stdin.readline().rstrip()

print(input_data)

#sys라이브러리를 사용할 때는 한 줄 입력받고 나서 rstrip() 함수를 꼭 호출해야 한다. 소스코드에 readline()으로 입력하면 입력 후 엔터가 줄 바꿈 기호로
#입력되는데, 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야 한다.