# replace - 바꾸기/지우기
# 형식: 문자열.replace('바꿀것', '새것')
# - 모두 바꾸기, 결과 저장 필요

# print('정 상 가 동'.replace(' ',''))
# print('010-1234-5678'.replace('-',''))
# print('3,000'.replace(',',''))

# split - 구분자로 나누기 (결과 -> 리스트)
# 형식: 문자열.split('구분자') (구분자 생략 = 공백 기준)
# print('A1 A2 A3'.split())        #['A1', 'A2', 'A3']
# print('사과,배,감'.split(','))    #['사과', '배', '감']

# 실습
print('설비 정상 가동'.replace('정상','점검'))

# 실습
print('PUMP A 03'.split())

# 실습
print('a,b,c,d'.split(','))

# 실습
print('a,b,c,d'.split(',',1))