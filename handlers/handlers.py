from views.views import *
import os.path

STATIC_PATH   = os.path.join(os.path.dirname(__file__), "../static")
TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "../templates")
HANDLERS =[
	   (r"/base/",		Base_Handler),
	   (r"/nconf/",		Nconf_Handler),
	   (r"/host_vhost/",	Host_vhost_Handler),
	   (r"/post_vhost/",	Post_vhost_Handler),
	]
#HANDLERS +=[(r"/chart/", ChartHandler)]
