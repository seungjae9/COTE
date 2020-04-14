# SW대비

#### 약수
```python
                ex) 16의 약수 만들기
                num = 16
                for i in range(1, num+1):
                    if num % i == 0:
                        print(i) ===> i가 num 의 약수
                        print(num // i) 몫
```



##### 리스트 다루기
```python
			
			list 원하는데다가 집어넣기(맨앞에도 들어갈 수 있음)
			list.insert(원하는 인덱스 번호, 원하는 문자열, 숫자)
			
			
			list 뒤집기
				ex) res = [1,2,3,4]
					res.resver() 하면 바로 뒤집어짐
					res = reversed(res) 로 값 반환도 가능
					
			
			list join
				"".join(map(str, 리스트))
			
```
