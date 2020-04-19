'''
과제 1. 별찍기 (4월 20일까지)
- 아래와 같이 * 을 출력 하는 프로그램을 만들어보세요
**********
*********
********
*******
*****
****
***
**
*

과제 2. 구구단 (4월 20일까지)
- 구구단 2단을 출력해보세요!

과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)

과제 4. for 문을 활용하여 멋사 학생들의 평균 점수를 구해보세요. (4월 20일까지)
- mutsa_scores = [90, 77, 40, 55, 90, 100, 88]

과제 5. input.py 문제 2개 풀기 (4월 20일까지)

과제 6. HTML / CSS 페이스북 모바일 클론코딩 (4월 27일까지)
- 이미지 자율
- 까먹기전에 해주세요~

'''
#문제 1
b = 11

while b > 0 :
    b -= 1
    if b == 6:
        continue
    print('*' * b)


#문제 2 구구단 2단을 출력해보세요!
a = 1

while a < 11:
    a = a + 1
    print('2 x ', a, '= ', 2 * a)

#문제 3  과제 3. while 문을 활용하여 1부터 1000까지의 자연수 중 3의 배수의 합을 구해보세요. (4월 20일까지)
a = 1
counter=0
while a < 1000: 
    if a % 3 == 0 :
        counter += a
    a += 1
print(counter)

#문제 4 
mutsa_scores = [90, 77, 40, 55, 90, 100, 88]
print('변수의 개수: ', len(mutsa_scores))

sum = 0
for i in range(len(mutsa_scores)):
    sum = sum + mutsa_scores[i]
average = sum / len(mutsa_scores)
print(average)