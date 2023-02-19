import json

print("示例json序列化")


class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Student:
    def __init__(self, name, school_name, school_address):
        self.name = name
        self.school = School(school_name, school_address)

    def to_json(self):
        json_data = {
            "name": self.name,
            "school": {
                "name": self.school.name,
                "address": self.school.address
            }
        }
        return json.dumps(json_data)


if __name__ == "__main__":
    tom = Student("tom", "liu_zhong", "200#")
    print(tom.to_json())
    print(json.loads(tom.to_json()))
