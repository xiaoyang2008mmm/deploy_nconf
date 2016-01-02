# -*- coding: utf-8 -*- 
import tornado.web , os
import ConfigParser,string,os,sys
from modules.ansible_vhost import ansible_nconf
class BaseHandler(tornado.web.RequestHandler):
    @property
    def db(self):
       return self.application.db

class Base_Handler(BaseHandler):
    def get(self):
	self.render("base.html")

class Nconf_Handler(BaseHandler):
    def user_func(slef, host):
	vhlist = ansible_nconf(host)
        return  vhlist
    def get(self):
	s = get_host_list((os.path.join(os.getcwd(),'config')) + '/' + 'n_conf.conf')
	vhlist = ansible_nconf()
	_dict = { "config_file" : s ,"vhlist" : vhlist ,'user_func':self.user_func}
	self.render("nconf.html",**_dict)


class get_host_list(object):
    def __init__(self,file):
        self.cf = ConfigParser.ConfigParser()
        self.cf.read(file)
    def get_conf(self):
        s = self.cf.sections()
	return (self.cf.get(s[0], "nconf_host")).split(",")
    def get_vhost(self):
	return self.cf.get("nconf", "nconf_vhost")


