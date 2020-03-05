'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-02-23 15:52:26
@LastEditors: Henggao
@LastEditTime: 2020-02-27 16:24:05
'''

"""
Demo 1
"""
# aliens = []

# for aliens_num in range(20):
#     new_aliens = {"name": "Jack", "age": 23, "color": "green"}
#     aliens.append(new_aliens)

# for alien in aliens[:5]:

#     print(alien)

"""
Demo 2
"""
# favorite_languages = {
#     'jen': ['python', 'ruby'],
#     'sarah': ['c'],
#     'edward': ['ruby', 'go'],
#     'phil': ['python', 'haskell'],
# }

# for name, languages in favorite_languages.items():
#     print("\n" + name.title() + "'s favorite languages are :")
#     for language in languages:
#         print("\t" + language.title())


"""
Demo 3
"""
# pets = []
# for pet in range(10):
#     new_pet = {"name":"dog","age":2,"color":"black"}
#     pets.append(new_pet)

# for pet in pets[:3]:
#     print(pet)

'''
Demo 4
'''

pet_dirs = {
    "pig": {
        "name": "peiqi",
        "hobby": "eat",
        "host": "Jack"
    },
    "dog": {
        "name": "xiaotianquan",
        "hobby": "run",
        "host": "erlangshen"
    },
    "cat": {
        "name":"tom",
        "hobby":"drink",
        "host":"david"
    }
}

for name,pet_info in pet_dirs.items():
    print("\n" + name.title() + "'s " + pet_info["name"].title() +
     ", it's hobby is " + pet_info["hobby"] + ".")


