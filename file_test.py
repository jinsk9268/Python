"""
# hello.txt 파일을 쓰기 모드(w)로 열기, 파일 객체 반환
file = open('hello.txt', 'w')

# 파일에 문자열 저장
file.write('Hello, world!')

# 파일 객체 닫기
file.close()
"""
"""
# hello.txt 파일을 읽기 모드(r)로 열기, 파일 객체 반환
file = open('hello.txt', 'r')

# 파일에서 문자열 읽기
s = file.read()

# 파일의 문자열 출력
print(s)

# 파일 객체 닫기
file.close()
"""
"""
# hello.txt 파일을 읽기모드(r)로 열어서 자동으로 닫기
with open('hello.txt', 'r') as file:
    s = file.read()     # 파일에서 문자열 읽기
    print(s)            # 문자열 출력
"""
"""
# hello2.txt 파일을 쓰기 모드(w)로 열기
with open('hello2.txt', 'w') as file:
    for i in range(3):
        file.write('Hello, world! {0}\n'.format(i))
"""
"""
# 파일에 쓸 문자열
lines = ['안녕하세요.\n', '파이썬\n', '배우는 중입니다.\n']

# hello3.txt 파일을 쓰기 모드(w)로 열어서 자동으로 닫기
with open('hello3.txt', 'w') as file:
    file.writelines(lines)
"""
"""
# hello3.txt 파일을 읽기 모드(r)로 열어서 자동으로 닫기
with open('hello3.txt', 'r') as file:
    lines = file.readlines()
    print(lines)
"""
"""
# hello3.txt 파일을 읽기 모드(r)로 열어서 자동으로 닫기
with open('hello3.txt', 'r') as file:
    line = None         # 변수 line을 None으로 초기화
    while line != '':   # 빈문자열이 아닐때까지 반복
        line = file.readline()
        print(line.strip('\n')) #파일에서 읽어온 문자열에서 \n을 삭제하여 출력
"""
"""
# hello3.txt 파일을 읽기 모드(r)로 열어서 자동으로 닫기
with open('hello3.txt', 'r') as file:
    for line in file:       
        print(line.strip('\n'))
        
    # for에 파일 객체를 지정하면 파일의 내용을 한 줄씩 읽어서 변수에 저장
    
        # 파일에서 읽어온 문자열에서 \n 삭제하여 출력
"""
file = open('hello3.txt', 'r')
a, b, c = file
print(a, b, c)
