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



#### 리스트 다루기
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



#### 인덱스
``` python
		만약에 인덱스찍을때 범위 넘어가는 문제 해결 방법
			ex) res = [1,2,3,4,5,6]
				a = 3
				b = a + 4
				res[a]
				res[b] 이렇게 넘어갔을때 0번째 부터 다시 세는 경우
			1. 제일 무식하게 찍을 인덱스를 늘려버린다.
				res * 2 or res * 3 이런식으로 늘려버린다.
			2. 리스트 길이만큼 나눈 나머지를 구한다.
				ex) a = 3
					b = (a + 4) % len(res) 
```




#### 끊어서 출력하기
``` python
			% 방법과 cnt 방법이 있음
			나는 cnt 방법이 더 직관적이라 이걸로 씀
			ex) 10개씩 끊어서 출력하기
			
			res = [1,2,3,4,5,6,7,8,9, ......]
			cnt = 0
			for i in range(len(res)):
				print(res[i], end=" ")   => 출력시 한칸 띄우기
				cnt += 1
				if cnt == 10:
					print("")     => 한줄 띄어 주는거
					cnt = 0
			
```




#### 톱니바퀴,  주사위 굴리기
``` python
		for문이나 반목되는 문자를 사용하면서 자꾸 한번씩 숫자를 틀리게 적거나, 
		반복되는 문자를 빼먹는다.
		
		반복되는것을 적을때 맨처음에 풀었던 for이나 반목코드를 보면서 체크하기
		
```



#### 사탕게임
```python
		중복되는곳 함수 사용
```