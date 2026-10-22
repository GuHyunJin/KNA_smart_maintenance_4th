# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# len() - 
# 형식: len(문자열)
# print(len('PYTHON'))          #6
# print(len('AI 분석'))         #5 공백 포함
# print(len(''))                #0

# in / not in - 포함 / 불포함 여부 (결과 bool)
#  형식: '찾을 것' in 문자열
# print('고장' in '설비 고장 발생')      #True
# print('정상' not in '고장 발생')       #True

# count
# 형식: 문자열.count('x') -> 개수
# print('banana'.count('a'))            #3

# finc
# 형식: 문자열.find('x') -> 처음 나오는 위치
# print('banana'.find('a'))       #1

# 실습
# print(len('01012345678'))

# 실습
# print('고장' in '설비 고장 발생')      
# print('정상' in '설비 고장 발생')

# 실습
# text = "sensor-01-temp"
# print('sensor-01-temp'.count('-'))

# 실습
# text = "temp_2024"
# print('temp_2024'.find('_'))
# print('temp_2024'.find('z'))

# index
# 주의) 위치를 반환하지만 없으면 오류
# email = 'hong@company.com'
# at = email.index('@')
# print(at)
# print(email[:at])      #hong

# startswith / endswith
# 형식: 문자열.startswith('x') -> bool
# print('EQP-001'.startswith('EQP'))
# print('cmpass.csv'.endswith('csv'))

# 실습
text = 'sensor_log.csv'
print('sensor-001'.startswith('sensor'))
print('log.csv'.endswith('.csv'))

# 실습
text = 'WARNING'
print('WARNING' == 'WARNING')
print('WARNING' == 'warning')