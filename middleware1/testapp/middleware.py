
class ExecutionFlowMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
            print('This line printed at pre processing of request')
            response=self.get_response(request)

            print('This line printed at post processing of request')
            return response
from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        return HttpResponse('<h1>currenly Application under maintenance....plz try after two days</h1>')


class ErrorMessageMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        return self.get_response(request)
    def process_exception(self,request,exception):
        return HttpResponse('<h1>currenly  we are facing some technical problems Application under maintenance....plz try after two days</h1>')
