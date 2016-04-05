#-*-coding:cp949
x = "There are %d types of people." % 10
# x 의 명령어 지정
binary = "binary"
# binary 의 명령어 지정
do_not = "don't"
# do_not 의 명령어 지정
y = "Those who know %s and those who %s." % (binary, do_not)
# y 의 명령어 지정
print x
print y
# x,y 입력
print "I said: %r." % x
print "I also said: '%s'." % y
# x,y 를 포함한 문장 입력
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# 새로운 명령어 지정
print joke_evaluation % hilarious
# 새로운 문장 입력
w = "This is the left side of..."
e = "a string with a right side."
# w,e 의 명렁어 지정
print w + e
# w,e 입력