## DataFrame
- 표 같은 스프레드 형식의 자료구조이다.
- 각 행마다 서로 다른 종류의 데이터 타입을 지정할 수 있다.

### How to create
- 흔한 방법은 같은 길이의 리스트에 담긴 사전을 이용하거나 `NumPy` 배열을 사용하는 법이다.
```
data = {'date': [10, 11, 12],
        'money': [1000, 2000, 3000]}
frame = DataFrame(data)
->     date  money
  0    10   1000
  1    11   2000
  2    12   3000
```

### 생성자에서 사용 가능한 데이터
- 2차원 ndarray
  - 데이터를 담고 있는 행렬
  - 선택적으로 로우와 칼럼의 이름을 지정 할 수 있다.
- 배열, 리스트, 튜플의 사전
  - 모두 같은 길이여야 한다.
  - 각 항목의 내용이 `DataFrame`의 칼럼이 된다.
- `Numpy`의 구조화 배열
  - 배열의 사전과 같은 방식으로 취급된다
- `Series` 딕셔너리
  - 각 값이 칼럼이 된다
  - 색인을 넘겨주지 않으면 각 `Series`의 색인이 하나로 합쳐져서 로우의 색인이 된다.
- 딕셔너리의 딕셔너리
  - 내부에 있는 사전이 칼럼이 된다.
- 딕셔너리 혹은 `Series`의 리스트
  - 리스트의 각 항목이 로우가 됨.
- 리스트 혹은 튜플의 리스트
  - 2차원 ndArray와 같은 방식으로 취급
- 다른 DataFrame
  - 색인이 따로 지정되지 않으면 기존 DataFrame의 색인이 그대로 사용된다
- `NumPy` 의 MaskedArray
  - 2차원 ndArray와 같은 방식으로 취급되지만 값이 NA가 된다.

### columns=
- `columns=` 을 이용해 행에 들어갈 요소의 순서를 정할 수 있다
- ex) Dataframe(data, `colmuns=['money', 'date']`)

### data에 없는 값을 넘기면?
- `NaN` 값이 저장된다.

### DataFrame의 각 행의 요소 지정 방법
- 딕셔너리 형식의 표현법
  - `frame['date']` 
- 속성 형식의 접근 방법
  - `frame.date`

#### .iloc
- 정수만 지정할 수 있다

#### .loc
- 라벨, 즉 딕셔너리 형식만 지정할 수 있다.

#### .ix
- 정수와 딕셔너리 형식 모두 사용할 수 있다.
```
print(frame.ix[0]) # frame는 How to create에서 만든 DataFrame이다.
-> date     10
   money  1000
   Name: 0, dtype: int64
```

### 새로운 행 대입하기
- 기존에 없는 새로운 행을 대입한다.
- `frame['hour'] = [1, 2, 3]` 이런 식으로 한다.
- 하지만 기존 DataFrame과 크기가 같아야 한다.

### 행 삭제하기
- 파이썬처럼 `del` 명령어를 사용하면 된다.
- `del frame['hour']` 과 같은 방식으로 사용한다.

### 행과 열 뒤집기
- `NumPy`처럼 `.T` 를 사용하자

### Index 객체

#### Index
- 가장 일반적인거

#### Int64Index
- 정수 값을 위한 인덱스

#### MultiIndex
- 단일 축에 여러 단계의 색인을 표현
- `Tuple`의 배열과 유사하다

#### DatetimeIndex
- 나노초 타임스탬프
- `NumPy`의 `datetime64`로 표현된다  

#### PeriodIndex
- 기간 데이터를 위한 인덱스

