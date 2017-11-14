# Numpy
- import
-     import numpy as np
## ndarray
- 메모리를 빠르고 효율적이게 사용가능
- 산술 연산과 브로드캐스팅 기능 제공
### 생성 방법
- **np.array()**
  - 기존 배열에서 데이터를 받아와 ndarray로 만들어줌
-     data = [1,2,3,4,5] 
      arr = np.array(data1) 
- **np.zeros()**
  - 0으로 초기화한 ndarray 생성
-     np.zeros(10)
      -> array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
      np.zeros((2,2))
      -> ([0., 0.],
          [0., 0.])
- **np.ones()**
  - 1으로 초기화 한 ndarray 생성
  - **np.zeros()** 와 사용 방법 같음
- **np.empty()**
  - 초기화되지 않은 ndarray를 반환하는 함수
  - **np.zeros()** 와 사용 방법 같음
- **np.eye()**
  - N * N 크기의 행렬 생성
  - 좌상단에서 우하단을 잇는 대각선은 1로 채워짐
-     array = np.eye(3)
      print(array)
      -> [[1, 0, 0],
          [0, 1, 0],
          [0, 0, 1]]
### 자료형
- int8(i1), int16(i2), int32(i3), int64(i4) 
  - 부호가 있는 n비트 정수형과 부호가 없는 n비트 정수형
- float16(f2), float32(f4 or f), float64(f8 or d)
  - 반정밀도 부동소수점
  - f4는 C언어의 float와 호환, f8은 c언어 double, 파이썬의 float와 호환
