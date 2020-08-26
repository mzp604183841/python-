def make_pizza(*topping):
    # 打印披萨配料
    print(topping)

make_pizza('牛肉', 'yangcong', 'jirou')


def build_user_profile(first_name, last_name, **user_info):
    profile = {}
    profile['first_name'] = first_name
    profile['last_name'] = last_name
    for key, value in user_info.items():
        profile[key] = value
    return profile

mzp = build_user_profile('毛', '志鹏', age = 28, height = 180, weight = 67)
print(mzp)
