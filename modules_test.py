def components_sandwich (*components):
    for component in components:
        print(component)
def build_profiles (first,last,**kwargs):
    kwargs['first_name']=first
    kwargs['last_name']=last
    print(kwargs)
def car_info(proizv,model,**info):
    info['proizvoditel']=proizv
    info['nomer_modeli']=model
    #return info
    for x,y in info.items():
        print(f"{x} данного автомобиля - {y}")
    return info    