from django.shortcuts import render
# Create your views here.

import logging
logger = logging.getLogger(__name__)
logger.info('inside the view')

from django.http import HttpResponse
import datetime

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
