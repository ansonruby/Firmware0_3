from server import Websocket, WebsocketServer
import os
import time
import json

SERVER_PORT = 1234
AWAIT_TIME = 0.08

DB_DIR_NAME = os.path.dirname(os.path.realpath(__file__))+"/db"

SEND_FLAG_PATH = DB_DIR_NAME+"/flagtosend.txt"
SEND_DATA_PATH = DB_DIR_NAME+"/datatosend.txt"

NEW_TICKETS_FLAG_PATH = DB_DIR_NAME+"/flagnewsreceived.txt"
NEW_TICKETS_DATA_PATH = DB_DIR_NAME+"/datanewsreceived.txt"

DEL_TICKETS_FLAG_PATH = DB_DIR_NAME+"/flagdelreceived.txt"
DEL_TICKETS_DATA_PATH = DB_DIR_NAME+"/datadelreceived.txt"

UPDATE_TICKETS_FLAG_PATH = DB_DIR_NAME+"/flagupdatereceived.txt"
UPDATE_TICKETS_DATA_PATH = DB_DIR_NAME+"/dataupdatereceived.txt"


class WsEvents(Websocket):

    SERVER_AWAIT_TIME = AWAIT_TIME

    def onLoop(self):
        with open(SEND_FLAG_PATH, 'r') as ff:
            if ff.read() == "1":
                with open(SEND_DATA_PATH, 'r') as df:
                    self.broadcast(json.dumps(
                        {'type': 'delTickets'})+'////\n'+df.read())
                    df.close()
                with open(SEND_FLAG_PATH, 'w') as ffw:
                    ffw.write("2")
                    ffw.close()
            ff.close()

    def onMessage(self, message):
        req = message.split("////\n")  # req[0]=headers, req[1]=body
        headerJson = json.loads(req[0])
        if headerJson["type"] == "updateDevice":
            while True:
                time.sleep(self.SERVER_AWAIT_TIME)
                with open(UPDATE_TICKETS_FLAG_PATH, 'r') as ff:
                    if ff.read() == "":
                        with open(UPDATE_TICKETS_DATA_PATH, 'w') as dfw:
                            dfw.write(req[1])
                            dfw.close()
                        with open(UPDATE_TICKETS_FLAG_PATH, 'w') as ffw:
                            ffw.write("1")
                            ffw.close()
                        break
                    ff.close()
        elif headerJson["type"] == "newTickets":
            while True:
                time.sleep(self.SERVER_AWAIT_TIME)
                with open(NEW_TICKETS_FLAG_PATH, 'r') as ff:
                    if ff.read() == "":
                        with open(NEW_TICKETS_DATA_PATH, 'w') as dfw:
                            dfw.write(req[1])
                            dfw.close()
                        with open(NEW_TICKETS_FLAG_PATH, 'w') as ffw:
                            ffw.write("1")
                            ffw.close()
                        break
                    ff.close()
        elif headerJson["type"] == "delTickets":
            while True:
                time.sleep(self.SERVER_AWAIT_TIME)
                with open(DEL_TICKETS_FLAG_PATH, 'r') as ff:
                    if ff.read() == "":
                        with open(DEL_TICKETS_DATA_PATH, 'w') as dfw:
                            dfw.write(req[1])
                            dfw.close()
                        with open(DEL_TICKETS_FLAG_PATH, 'w') as ffw:
                            ffw.write("1")
                            ffw.close()
                        break
                    ff.close()
        elif headerJson["type"] == "recived":
            while True:
                time.sleep(self.SERVER_AWAIT_TIME)
                with open(SEND_FLAG_PATH, 'r') as ff:
                    if ff.read() == "2":
                        with open(SEND_DATA_PATH, 'w') as dfw:
                            dfw.write("")
                            dfw.close()
                        with open(SEND_FLAG_PATH, 'w') as ffw:
                            ffw.write("")
                            ffw.close()
                        break
                    ff.close()
        else:
            pass

    def onConnect(self):
        print("[SERVER]= New connection, total connection:" +
              str(len(self.connections)))
        if not os.path.exists(DB_DIR_NAME):
            os.makedirs(DB_DIR_NAME)
        if not os.path.exists(SEND_FLAG_PATH):
            open(SEND_FLAG_PATH, 'w').close()
        if not os.path.exists(SEND_DATA_PATH):
            open(SEND_DATA_PATH, 'w').close()
        if not os.path.exists(NEW_TICKETS_FLAG_PATH):
            open(NEW_TICKETS_FLAG_PATH, 'w').close()
        if not os.path.exists(NEW_TICKETS_DATA_PATH):
            open(NEW_TICKETS_DATA_PATH, 'w').close()
        if not os.path.exists(DEL_TICKETS_FLAG_PATH):
            open(DEL_TICKETS_FLAG_PATH, 'w').close()
        if not os.path.exists(DEL_TICKETS_DATA_PATH):
            open(DEL_TICKETS_DATA_PATH, 'w').close()
        if not os.path.exists(UPDATE_TICKETS_FLAG_PATH):
            open(UPDATE_TICKETS_FLAG_PATH, 'w').close()
        if not os.path.exists(UPDATE_TICKETS_DATA_PATH):
            open(UPDATE_TICKETS_DATA_PATH, 'w').close()

        with open(SEND_FLAG_PATH, 'r') as ff:
            # if ff.read() == "3" or ff.read() == "2":
            with open(SEND_FLAG_PATH, 'w') as ffw:
                ffw.write("1")
                ffw.close()
            # ff.close()

        self.broadcast(json.dumps({'type': 'update'}))

    def onDisconnect(self):
        with open(SEND_FLAG_PATH, 'w') as ffw:
            ffw.write("3")
            ffw.close()
        print('[SERVER]= Closed conection from'+str(self.addr))


server = WebsocketServer("0.0.0.0", SERVER_PORT, 2, ws_cls=WsEvents)
server.run()
