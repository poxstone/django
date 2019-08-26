from django.http import HttpResponse
import json


def numbers(req):
    numbers = req.GET['numbers'] if 'numbers' in req.GET else '1,2'
    numbers = [int(i) for i in numbers.split(',')]
    numbers_sorted = sorted(numbers)
    data = {'status': 'ok', 'numbers':numbers_sorted, 'message': 'message send'}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')

def agePath(req, name, age):
    message = 'Hello {} you have {} age old'.format(name, age)
    data = {'status': 'ok', 'message': message}
    json_data = json.dumps(data)
    return HttpResponse(json_data, content_type='application/json')
