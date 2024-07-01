from extends.exception import AgeError, HeightError, WeightError

class_student = {
    "小红": {"age": 11, "height": 135, "weight": 54},
    "小明": {"age": 12, "height": 142, "weight": 60},
    "小刚": {"age": 12, "height": 143, "weight": 200}
}


class Student:

    def __init__(self, name):
        self.name = name

    def physical_examination(self):
        student = class_student[self.name]
        if student["age"] > 20:
            raise AgeError("age 超标")
        if student["height"] > 180:
            raise HeightError("height 超标")
        if student["weight"] > 120:
            raise WeightError("weight 超标")


if __name__ == '__main__':
    s = Student("小刚")
    grade = s.physical_examination()
    print(grade)
