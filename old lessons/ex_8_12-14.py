def components_sandwich (*components):
    for component in components:
        print(component)
components_sandwich("1","2","3")
components_sandwich('09876asdf')

def build_profiles (first,last,**kwargs):
    kwargs['first_name']=first
    kwargs['last_name']=last
    print(kwargs)
build_profiles("Kirill","Baranov",age=32,city='Moscow')

def car_info(proizv,model,**info):
    info['proizvoditel']=proizv
    info['nomer_modeli']=model
    #return info
    for x,y in info.items():
        print(f"{x} данного автомобиля - {y}")
    return info    
car=car_info('Субару','Outback',color='blue',tow_package=True)
print (car)
