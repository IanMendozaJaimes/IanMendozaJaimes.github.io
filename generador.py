from pathlib import Path

def create_web_page(path = ''):

    p = Path(path)
    countries = dict()

    for country in p.iterdir():
        if country.is_dir():
            print(str(country).replace(path, 'hola'))
            if str(country) not in countries:
                countries[str(country)] = list()
            # p_university = Path(path + '/' + str(country))
            # for university in p_university.iterdir():
            #     print(university)





create_web_page('/Users/ianMJ/Documents/ESCOM/servicio_social/ianmendozajaimes.github.io/creador_prueba')
