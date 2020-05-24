"""
import pickle

name = 'anne'
age = 17
address = '서울시 서초구 반포동'
scores = {'kor' : 90, 'eng':95, 'math':85, 'sci':82}

# anne.p 파일을 바이너리 쓰기 모드(wb)로 열어서 자동으로 닫기
with open('anne.p', 'wb') as file:
    pickle.dump(name, file)
    pickle.dump(age, file)
    pickle.dump(address, file)
    pickle.dump(scores, file)
"""
"""
import pickle

# anne.p 파일을 바이너리 읽기 모드(rb)로 열기
with open('anne.p', 'rb') as file:
    name = pickle.load(file)
    age = pickle.load(file)
    address = pickle.load(file)
    scores = pickle.load(file)
    print(name)
    print(age)
    print(address)
    print(scores)
"""
"""
# quiz
with open('words.txt', 'r') as file:
    count = 0
    words = file.readlines()
    for word in words:
        if len(word.strip('\n')) <= 10:
            count += 1

print(count)
"""
"""
# quiz 2
with open('words2.txt', 'r') as file:
    line = file.readline()
    line_list = list(line.split(' '))
    for word in line_list:
        if word.count('c') >= 1:
            print(word.strip(',.'))
"""

# quiz 2-1
with open('words2.txt', 'r') as file:
    line = file.readline()
    line_list = list(line.split(' '))
    for word in line_list:
        if 'c' in word:
            print(word.strip(',.'))
    
