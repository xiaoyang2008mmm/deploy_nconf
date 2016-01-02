#!/usr/bin/python
import os,sys,json
class get_vhost_file(object):
    def __init__(self):
        self.vlist = []
    def vhlist(self,rootdir):
        for parent,dirnames,filenames in os.walk(rootdir):
            for filename in filenames:
                self.vlist.append(filename)
        return self.vlist

def main(file_path='/data/server/nginx/conf/vhosts'):
    vhost_list = get_vhost_file()
    print  json.dumps({
	"data": vhost_list.vhlist(file_path)
    })

if __name__ == "__main__":
    main()

