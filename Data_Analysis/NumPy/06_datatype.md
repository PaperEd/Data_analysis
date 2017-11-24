## 자료형
- `np.arange(10, dtype=)`와 같이 괄호 안에 `dtype=`을 넣어줌으로서 자료형을 지정할 수 있다.

### int8 (i1), int16 (i2), int32 (i3), int64 (i4) 
- 부호가 있는 n비트 정수형과 부호가 없는 n비트 정수형이다.

### float16 (f2)
- 반정밀도 부동소수점이다.

### float32 (f4 or f)
- 단정밀도 부동소수점이다.
- C언어의 `float`형과 호환된다.

### float64 (f8 or d)
- 배정밀도 부동소수점이다.
- C언어의 `double`형과 호환된다.
- 파이썬의 `float` 객체와 호환된다.

### float128 (f16 or g)
- 확장 정밀도 부동소수점이다.

### complex64, 128, 256 (c8, c16, c32)
- 각각 2개의 32,64,128비트의 부동소수점형을 가지는 복소수다.

### bool (?)
- True, False 값을 저장하는 불리언형이다.

### object (0)
- 파이썬 객체형

### string_ (S)
- 고정 길이 문자열형 (각 글자는 1바이트)
- 길이가 n인 문자열의 dtype는 Sn

### unicode_ (U)
- 고정 길이 유니코드형 (플랫폼에 글자별 바이트 수가 다르다)
- `string_` 과 같은 형식을 사용 (Ex: U10)

### datetime64
- 시간을 저장 할 때 사용하는 데이터 타입이다.
- `pandas`의 DatetimeIndex와 호환된다

### astype
- `ndarray`의 `astype` 메소드를 사용해 배열의 `dtype`을 다른 형으로 명시적으로 변경 가능하다.
```
     arr = np.array([1, 2, 3, 4, 5])
      arr.dtype
      -> dtype('int64')
      
      float_arr = arr.astype(np.float64)
      float_arr.dtype
      -> dtype('float64')
```
  - 부동소숫점 숫자를 정수형을 변환하면 소수점 아래자리는 버려진다.
```
      arr = np.array([1.2, 3.4])
      arr
      -> array([1.2, 3.7])

      arr.astype(np.int32)
      -> array([1, 3] dtype=int32)
```
- `astype`을 호출하면 `dtype`이 이전 `dtype`과 같아도 항상 새로운 배열을 생성함.
---