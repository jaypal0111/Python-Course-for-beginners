def myInfo():
    print('My name is urmi')

myInfo()


def myInfo2(name, lastname):
    print('My name is ' +  name + ' '+  lastname)

myInfo2('Jay','Brahmbhatt')
myInfo2('Maria','Dsoza')
myInfo2('Peter','Danial')

print("=====================================")
def studentName(*name):
    #print('My name is ' +  name[1])
    for n in name:
       print('My name is ' +  n)


studentName('Jonny','Julia','Tina','Patrick','Maria')

print("=====================================")

def studentName2(name):
    #print('My name is ' +  name[1])
    for n in name:
       print('My name is ' +  n)

studentList = ['Jonny','Julia','Tina','Patrick','Maria']
studentName2(studentList)


def childInfo(child4,child2,child1,child3):
    print("The youngest child is " +  child4)

childInfo(child1="AB", child2="qw", child3="cw", child4="ty")


def testFun(testname="rest"):
    print('this is '+ testname)


testFun("best")
testFun()