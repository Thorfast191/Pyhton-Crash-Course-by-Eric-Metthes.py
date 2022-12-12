def build_profile(f_name,l_name, **user_info):
    profile = {}

    #storing f_name & l_name intp user dictionary
    profile['First-name'] = f_name
    profile['Last-name'] = l_name

    # for loop to store userinfo
    for key,value in user_info.items():
        profile[key] =  value
    return profile

user_profile = build_profile('arafat','islam',username = 'thorfast',middle_name='tanvir', age = 20)
print(user_profile)
