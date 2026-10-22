# 메서드 - 점(.) 문법
# 형식: 문자열.메서드이름() (--> 꼭 괄호를 붙여야함)
# word = 'python'
# print(word.upper())         #대문자
# print(word.count('p'))
# print(word)             

# print('NORMAL'.lower())      #소문자
# print('python is'.capitalize())   #첫글자만 대문자
# print('hong gil'.title())         #첫문단 마다 대문자

# 실습
# word = 'ready'
# print(word.upper())

# 실습
# word ='WARNING'
# print('WARNING'.lower())

# 실습
# word = 'kim chul soo'
# print('kim chul soo'.title())

# 실습
# word = 'Fault.FAULT'
# print('Fault' == 'FAULT')
# print('Fault'.lower() == 'FAULT'.lower())

# 확인 메서드 : is*** 메서드는 참/거짓 반환
# print('ABC'.isupper(), 'abc'.islower())

# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
# raw = ' 정상 '
# print('[' + raw + ']')
# print('[' + raw.strip() + ']')

# .lstrip() -> 왼쪽 공백 제거 /.rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤' 공백만 제거, 가운데 공백 제거x
# strip() 으로 특정 문자 제거 -> strip('문자')
# s = "###정상###"
# print(s.strip("#"))

# 실습
# print('ABC'.isupper())
# print('abc'.islower())
# print('Abc'.isupper())

# 실습6
name = "Sensor_LOG.CSV"
low = name.lower()
print(low.startswith("sensor"))
print(low.endswith(".csv"))
print(name.endswith(".csv"))

# 실습
# raw = ' 가동중 '
# print('[' + raw.strip() + ']')

# 실습
# s = '#대기#'
# print('[' + s.lstrip("#") + ']')
# print('[' + s.rstrip("#") + ']')

# 실습9
# s = "***경고***"
# print(s.strip("*"))


# 체이닝 - 메서드 이어 붙이기
# 형식: 문자열.strip().lower() -> 왼쪽부터 차례로 적용
# clean = '   NORAML   '.strip().lower()
# print(clean)

# 실습
clean = '   WARNING   '.strip().lower()
print(clean)

# 실습
s = " 경보 "
s.strip()
print("[" + s +"]")
s = s.strip()
print("[" + s +"]")