from cla.stu  import sayst


class Student():
    _age = 19
    __kk = 99
    def __init__(self, name):
        self._name = name

    def __gt__(self, obj):
        print("哈哈， {0} 会比 {1} 大吗？".format(self._name, obj._name))
        return self._name > obj._name


# 作业：
# 字符串的比较是按什么规则
print(dir(Student))
print(Student.__dict__)