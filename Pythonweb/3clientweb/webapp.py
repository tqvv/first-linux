def application(environ,start_response):
    start_response('200 ok',[('Content-Type','text/html')])
    return '<b> Hello,word'