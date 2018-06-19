import views

class Dispatcher(object):

    #Views to dispatch
    def __init__(self):
        self.thempHumView = views.TempView('', [150,50,100])
        self.nofityView = views.NotifyView('No notifications', [120,0,0])

    #check if views exist to dispatch
    def dispatch(self, request):
        if request.view in request.views:
            if request.views[0] == request.view:
                self.thempHumView.display()
            elif request.views[1] == request.view:
                self.nofityView.display()
            else:
                print ('Cant dispatch the request')

class RequestController(object):

    def __init__(self):
        self.dispatcher = Dispatcher()

    #If request is an Object of type Request
    def dispatch_request(self, request):        
        if isinstance(request, Request):
            self.dispatcher.dispatch(request)
        else:
            print('Request must be an object')


class Request(object):
    views = ['temp', 'notify']

    def __init__(self, request):
        self.view = None
        request = request.lower()

        #If valid request assign to object
        if request in self.views:
            self.view = request
        else:
            print('Request does not exist')

    
