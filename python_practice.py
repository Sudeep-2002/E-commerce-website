#OBJECT ORIENTED PROGRAMMING
class College:
    student='Sachin'
    branch='CSE'
    sem=6
    def __init__(self):#define the constructor
        print("The message is from constructor")
    def departments(self,deptName):
        self.deptName=deptName
    def mainBranch(self):
        print(self.deptName)
        
collegeObj = College()
print(collegeObj.student+' is from '+collegeObj.branch+' and sem '+str(collegeObj.sem))#CONCATENATION
collegeObj.departments("CSE ISE AND EC")
print(collegeObj.mainBranch())

#restful(representational state transfer) data and soap data can be used communication both client and server
#JSON is the type of restful data

