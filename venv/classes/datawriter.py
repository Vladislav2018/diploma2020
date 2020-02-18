import csv
import datetime

def write(object):
    '''
    this function writes data of objects of custom classes in csv
    :param object: all of your classes
    :return: string
    '''
    #name of doc consist of name of the object class
    filename = str(object.__class__.__name__ )+ 's' + '.csv'
    with open(filename, 'r', newline='') as read:
        exists_lables = []
        exist_lables_check = csv.reader(read, delimiter=' ', quotechar='|')
        for string in exist_lables_check:
            for row in string:
                exists_lables.append(row)
            break
        if len(exists_lables) != 0:
            exists_lables = exists_lables[0].split(',')
    #first constant params
    lables = ['id', 'full_type']
    data = [id(object), object.__class__]
    for attr in dir(object):
        if '__' not in str(attr) and 'method' not in str(type(getattr(object, attr))):
            lables.append(attr)
            data.append(getattr(object,attr))
    lables.append('datatime')
    data.append(str(datetime.datetime.now()))
    all_data = [data]
    if len(exists_lables) == len(lables):
        for i in range(len(exists_lables)):
            if exists_lables[i] != lables[i]:
                all_data = [lables, data]
                break
    else:
        all_data = [lables, data]
    print('The object will be written: ')
    print(all_data)
    with open(filename, 'a', newline='') as csvfile:
        objwrt = csv.writer(csvfile)
        objwrt.writerows(all_data)
    return print('Written successfully')
