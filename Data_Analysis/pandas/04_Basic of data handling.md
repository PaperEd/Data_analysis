## 기본적인 데이터 처리 방법

### .reindex( )
- 색인을 재색인해준다.
- 없는 값이 있다면, 비어있는 값을 새로 추가한다.
- `fill_value=`로 누락된 값에 들어갈 값을 지정할 수 있다.
```py
obj = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

obj.reindex(['d', 'c', 'b', 'a', 'e'])
=>  d    4.0
    c    3.0
    b    2.0
    a    1.0
    e    NaN
    dtype: float64
```
- `method=`를 이용해 누락된 값을 채워 넣을 수 있다.
  - `'ffill'`, `'pad'`: 앞의 값을 누락된 값을 채워 넣는다.
  - `'bfill'`, `'backfill'`: 뒤의 값으로 누락된 값을 채워 넣는다.
  - `method=` 가 `fill_value=`보다 우선순위 인것 같다.
```py
obj2 = Series(['Blue', 'Pruple', 'Yellow'], index=[0, 2, 4])

obj2.reindex(range(6), method='pad')
=>  0      Blue
    1      Blue
    2    Pruple
    3    Pruple
    4    Yellow
    5    Yellow
    dtype: object
```

- `DataFrame`의 `.reindex` 기본값은 행이다.
  - 각 행마다의 요소는 `columns=` 예약어를 사용해서 재색인 할 수 있다.
  - 사실 `.ix` 써서 하는게 더 간결하댄다.
### .drop( )
- 하나의 행 혹은 행의 요소를 제거해준다.
```py
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'],
                  columns=['First', 'Second', 'Third'])
frame = frame.drop('a')

print(frame)
=>    First  Second  Third
   b      3       4      5
   c      6       7      8

```
- `axis=` 속성에 `columns`를 넣어 행마다 들어가는 요소를 삭제할 수 있다.
```py
frame = frame.drop('First', axis="columns")
```

## Indexing
- 색인이 꼭 정수가 아니여도 된다.

### Series
```python
obj3 = Series(np.arange(4, 8), index=['a', 'b', 'c', 'd'])

obj3['b']           obj3[[1, 3]]
=> 5                => b    5
obj3[1]                d    7
=> 5                   dtype: int32

obj3[obj3 <= 5]     obj3['b': 'c'] 
=> a    4           => b    5
   b    5              c    6
   dtype: int32        dtype: int32
```
### DataFrame
- `.ix`를 이용해 지정하자

## Arithmetic operation
- 두 객체를 더할 때 색인끼리 더한다.
- 서로 겹치는 값이 없다면 **NA**값이 된다.

### .add(), .sub(), .div(), .mul()
- 위의 메소드를 이용하면 `fill_value`를 이용해 겹치는 값이 없는곳에 들어갈 값을 정해 줄 수 있다.
- fill_value + value 다.

### DataFrame과 Series 간의 연산
- DataFrame - Series 연산을 수행 할 경우 Series의 값이 각 행마다 전파된다.

