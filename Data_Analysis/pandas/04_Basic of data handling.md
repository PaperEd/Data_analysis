## 기본적인 데이터 처리 방법

### .reindex( )
- 색인을 재색인해준다.
- 없는 값이 있다면, 비어있는 값을 새로 추가한다.
- `fill_value=`로 비어있는 값에 들어갈 값을 지정할 수 있다.
```
obj = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

obj.reindex(['d', 'c', 'b', 'a', 'e'])
->  d    4.0
    c    3.0
    b    2.0
    a    1.0
    e    NaN
    dtype: float64
```
- `method=`를 이용해 누락된 값을 채워 넣을 수 있다.
  - `'ffill'`, `'pad'`: 앞의 값을 누락된 값을 채워 넣는다.
  - `'bfill'`, `'backfill'`: 뒤의 값으로 누락된 값을 채워 넣는다
```
obj2 = Series(['Blue', 'Pruple', 'Yellow'], index=[0, 2, 4])

obj2.reindex(range(6), method='pad')
->  0      Blue
    1      Blue
    2    Pruple
    3    Pruple
    4    Yellow
    5    Yellow
    dtype: object
```

- `DataFrame`에서 열은 `columns=` 예약어를 사용해서 재색인 할 수 있다.
- 기본값은 행이다.
### .drop( )
- 하나의 행 혹은 열을 제거해준다.
```
frame = DataFrame(np.arange(9).reshape(3, 3), index=['a', 'b', 'c'],
                  columns=['First', 'Second', 'Third'])
frame = frame.drop('a')

print(frame)
->    First  Second  Third
   b      3       4      5
   c      6       7      8

```