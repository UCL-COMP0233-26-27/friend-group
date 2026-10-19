"""An example of how to represent a group of acquaintances in Python."""

# 用字典表示整个群体：键是姓名，值是这个人的信息。
my_group = {
    "Jill": {
        "age": 26,           # 年龄：整数
        "job": "biologist",   # 职业：字符串；没有工作时使用 None
        "connections": [     # 关系列表；没有关系时使用空列表 []
            # relationship 表示当前这个人是 person 的什么人。
            {"person": "Zalika", "relationship": "friend"},
            {"person": "John", "relationship": "partner"},
        ],
    },
    "Zalika": {
        "age": 28,
        "job": "artist",
        "connections": [
            {"person": "Jill", "relationship": "friend"},
        ],
    },
    "John": {
        "age": 27,
        "job": "writer",
        "connections": [
            {"person": "Jill", "relationship": "partner"},
        ],
    },
    "Nash": {
        "age": 34,
        "job": "chef",
        "connections": [
            {"person": "John", "relationship": "cousin"},
            # Nash 是 Zalika 的房东。
            {"person": "Zalika", "relationship": "landlord"},
        ],
    },
}

# 关系具有方向性，不会自动生成反向关系。
# 例如：记录 Nash 是 Zalika 的房东，
# 并不会自动在 Zalika 的关系列表中记录她是 Nash 的租客。