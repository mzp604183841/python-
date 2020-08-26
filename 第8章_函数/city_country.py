def city_country(city, country):
    info = str(city) + ', ' + str(country)
    return info

def make_albm(singer, albm_name, number_of_songs = ''):
    albm_dict = {'singer' : '', 'albm_name' : '', 'number_of_songs' : ''}
    albm_dict['singer'] = singer
    albm_dict['albm_name'] = albm_name
    albm_dict['number_of_songs'] = number_of_songs
    print(albm_dict)


print(city_country('大连', '中国'))
make_albm('周杰伦', '七里香', 34)
make_albm('林俊杰', '江南')

