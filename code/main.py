import tornado.ioloop
import tornado.web
import tornado.httpserver
import os,MySQLdb,dbapi
from handler import *

#Change the handler class and make it to fit your requirement
#class historyHandler(tornado.web.RequestHandler):
#	def get(self):
#		self.render("index.html")

#	def post(self):
#		username=self.get_argument("username")
#		print self.application.dbapi.getEventById(1)

#register url handler
#class RegisterHandler(tornado.web.RequestHandler):
#        def post(self):
                #content = self.get_argument("content")
#                content = '{"username": "haha","password": 111111,"kind": 1, "cardid":11301 ,"realname":"hiii","sex":1,"age":41, "address":"iii","illness":"hijiiii"}'
#                j = json.loads(content)
#               if(self.application.dbapi.hasuserName(j['username'])):
#                        return {'state':1}
#                if(self.application.dbapi.hascardid(j['cardid'])):
#                        return {'state':2}
#                self.application.dbapi.regist(j)
#                return {'state':3}

#login url handler
class IndexHandler(tornado.web.RequestHandler):
        def get(self):
                self.render("index.html")

#class authentication



class app(tornado.web.Application):
	def __init__(self):
		settings = {
			"static_path": os.path.join(os.path.dirname(__file__), "static"),
			"debug": True
		}
		handlers=[(r"/",IndexHandler),
                          (r"/api/login",LoginHandler.LoginHandler),
                          (r"/api/register",RegisterHandler.RegisterHandler),
                          (r"/api/userauthentication",AuthenHandler.AuthenHandler),
                          (r"/api/logout",LogoutHandler.LogoutHandler),
                          (r"/api/cancel",CancelHandler.CancelHandler),
                          (r"/api/checkrelatives",CheckrelativesHandler.CheckrelativesHandler),
                          (r"/api/deleterelatives",DeleterelativesHandler.DeleterelativesHandler),
                          (r"/api/addrelatives",AddrelativesHandler.AddrelativesHandler),
                          (r"/api/history",HistoryHandler.HistoryHandler),
                          (r"/api/helpmessage",HelpmessageHandler.HelpmessageHandler),
                          (r"/api/supportmessage",SupportmessageHandler.SupportmessageHandler),
                          (r"/api/finish",FinishHandler.FinishHandler),
                          (r"/api/givecredit",GivecreditHandler.GivecreditHandler),
                          (r"/api/addaid",AddaidHandler.AddaidHandler),
                          (r"/api/sendsupport",SendsupportHandler.SendsupportHandler),
                          (r"/api/quitaid",QuitaidHandler.QuitaidHandler)
                          ]
		tornado.web.Application.__init__(self,handlers,**settings)
		self.dbapi=dbapi.dbapi()
		

if __name__=="__main__":
	server=tornado.httpserver.HTTPServer(app())
	server.listen(8080)
	tornado.ioloop.IOLoop.instance().start()
