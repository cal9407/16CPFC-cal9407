#-*-coding:cp949
x = "There are %d types of people." % 10
# x �� ��ɾ� ����
binary = "binary"
# binary �� ��ɾ� ����
do_not = "don't"
# do_not �� ��ɾ� ����
y = "Those who know %s and those who %s." % (binary, do_not)
# y �� ��ɾ� ����
print x
print y
# x,y �Է�
print "I said: %r." % x
print "I also said: '%s'." % y
# x,y �� ������ ���� �Է�
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
# ���ο� ��ɾ� ����
print joke_evaluation % hilarious
# ���ο� ���� �Է�
w = "This is the left side of..."
e = "a string with a right side."
# w,e �� ���� ����
print w + e
# w,e �Է�