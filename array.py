import numpy as np # numpy 모듈을 가져움

a= np.array([[1,2,3], [4,5,6], [7,8,9]]) # 3*3행렬 생성
b= np.array([[1,2,3], [4,5,6], [7,8,9]]) # 3*3행렬 생성
c= a@b
print(c)
