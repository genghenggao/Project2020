'''
@Description: 
@Version: 1.0
@Autor: Henggao
@Date: 2020-03-12 10:48:06
@LastEditors: Henggao
@LastEditTime: 2020-03-12 11:58:14
'''


def get_city_country(city, country, population=''):
    if population:
        '''打印城市和国家'''
        city_country = city.title() + ',' + country.title() + '-'+ str(population)
        return city_country
    else:
        '''打印城市和国家'''
        city_country = city.title() + ',' + country.title()
        return city_country

