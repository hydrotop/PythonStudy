strdata1='나는 파이썬 프로그래머다'
strdata2="You are a programmer"
strdata3="""I love
     python. You love
python too!"""
strdata4="My son's name is John"
strdata5='문자열 "abc"의 길이는 3입니다.'

txt1='자바'; txt2='파이썬'
num1=5; num2=10
print('나는 %s보다 %s에 더 익숙합니다.'%(txt1,txt2))
print('%s는 %s보다 %d배 더 쉽습니다.'%(txt1,txt2, num1))
print('%d + %d = %d' %(num1, num2, num1+num2))
print('작년 세계 경제 성장율은 전년에 비해 %d%% 포인트 증가했다.' %num1)

from time import sleep
for i in range(100):
    msg='\r진행률%d%%'%(i+1)
    print(''*len(msg),end='')
    print(msg,end='')
    sleep(0.1)