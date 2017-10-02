from mongoengine import *
import hashlib
import datetime

connect('muler')

# 员工类
class Employee(Document):

    id = StringField(required=True,primary_key=True) # 发现会与objectId冲突，将它设为主键后解决
    name = StringField(required=True)
    age = IntField(required=True)
    sex = StringField(required=True)
    salary = IntField()

    # 构造器
    # def __init__(self,name,age,sex,salary):
    #
    #     self.id = self.getTimestamp()
    #     self.name = name
    #     self.age = age
    #     self.sex = sex
    #     self.salary = salary

    # 获取时间戳md5值作为id
    @classmethod
    def getTimestamp(self):
        timestamp = str(datetime.datetime.now())
        return hashlib.md5(timestamp.encode("utf-8")).hexdigest()

    # 显示所有员工信息
    @staticmethod
    def showAll():
        for emp in Employee.objects:
            print("员工id:"+str(emp.id)+" 姓名:"+emp.name+" 年龄:"+str(emp.age)+" 性别:"+emp.sex+" 收入:"+str(emp.salary))


    # 多条件过滤
    def showAllByCondition(id_,name_,age_,sex_,salary_):
        emps = Employee.objects.filter(id=id_,name=name_,age=age_,sex=sex_,salary=salary_)
        for emp in emps:
            print("员工id:" + emp.id + " 姓名:" + emp.name + " 年龄:" + str(emp.age) + " 性别:" + emp.sex + " 收入:" + str(emp.salary))

    # 增加员工信息
    def addEmploree(name_new,age_new,sex_new,salary_new):
        t_id = str(Employee.getTimestamp())
        emp = Employee(id=t_id,name=name_new,age=age_new,sex=sex_new,salary=salary_new)
        emp.save()

    # 修改员工信息
    def updateEmploreeById(id_,name_new,age_new,sex_new,salary_new):
        Employee.objects(id=id_).update_one(name=name_new,age=age_new,sex=sex_new,salary=salary_new)

    # 删除员工信息
    def deleteEmploreeById(name_):
        emp = Employee.objects.filter(name=name_)
        emp.delete()


# Employee.addEmploree('史蒂芬平克',63,'male',666666)
# Employee.addEmploree('江主席',91,'male',11111111)
# Employee.addEmploree('查理芒格',93,'male',99999999)
# Employee.addEmploree('杨振宁',95,'male',2222223)

# Employee.showAll()

# Employee.deleteEmploreeById('江主席')

# Employee.updateEmploreeById('e63434db227f2da2e94b651000b2589d','杨老',93,'male',888888888)

# Employee.showAllByCondition('afe06162e534699a2e81fc348e244590','杨振宁',95,'male',2222223)