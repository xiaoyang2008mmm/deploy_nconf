#!/usr/bin/python

import ansible.runner
import sys,os

def ansible_nconf(host="127.0.0.1"):
    results = ansible.runner.Runner(
    module_path=os.path.join(os.getcwd(),'modules'),
    pattern=host, forks=50,
    module_name='mod', 
    ).run()
    return ((results['contacted'])[host])['data']

#print  ansible_nconf()
