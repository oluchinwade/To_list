def supply(request):
    inventory = 10000
    on_request = inventory - request 
    return on_request

