# Numpy
- 파이썬 라이브러리를 이용한 데이터 분석 책을 읽고 정리한 내용입니다.
- How to **import**
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
- float16 (f2)
  - 반정밀도 부동소수점
- float32 (f4 or f)
  - 단정밀도 부동소수점
  - C언어의 **float**형과 호환
- float64 (f8 or d)
  - 배정밀도 부동소수점
  - C언어의 **double**형과 호환
  - 파이썬의 **float** 객체와 호환
- float128 (f16 or g)
  - 확장 정밀도 부동소수점
- complex64,128,256 (c8, c16, c32)
  - 각각 2개의 32,64,128비트의 부동소수점형을 가지는 복소수
- bool (?)
  - True, False 값을 저장하는 불리언형
- object (0)
  - 파이썬 객체형
- string_ (S)
  - 고정 길이 문자열형 (각 글자는 1바이트)
  - 길이가 n인 문자열의 dtype는 Sn
- unicode_ (U)
  - 고정 길이 유니코드형 (플랫폼에 글자별 바이트 수가 다르다)
  - **string_** 과 같은 형식을 사용 (Ex: U10)
- astype
  - ndarray의 astype 메소드를 사용해 배열의 dtype을 다른 형으로 명시적 변경 가능
-     arr = np.array([1, 2, 3, 4, 5])
      arr.dtype
      -> dtype('int64')
      
      float_arr = arr.astype(np.float64)
      float_arr.dtype
      -> dtype('float64')
  - 부동소숫점 숫자를 정수형을 ㅗ변호나하면 소수점 아래자리는 버려짐
-     arr = np.array([1.2, 3.4])
      arr
      -> array([1.2, 3.7])

      arr.astype(np.int32)
      -> array([1, 3] dtype=int32)
  - astype을 호출하면 dtype이 이전 dtype과 같아도 항상 새로운 배열을 생성함
### 배열과 스칼라 간의 연산
-     arr = np.array([1, 2, 3])
      arr
      -> ([1, 2, 3])
      arr * arr
      -> ([2, 4, 6])
      arr / arr
      -> ([1, 1, 1])
      arr + 3
      -> ([4, 5, 6])
  - 스칼라 값에 대한 연산은 각 요소로 전달됨
### 색인과 슬라이싱 기초
- 1차원 배열은 파이썬의 리스트와 유사하게 동작됨
-     arr = np.arange(6)
      arr
      -> ([0, 1, 2, 3, 4, 5])
      arr[5]
      -> 5
      arr[1:4]
      -> ([1, 2, 3])
      arr[1:4] = 9
      arr
      -> [(0, 9, 9, 9, 4, 5)]
