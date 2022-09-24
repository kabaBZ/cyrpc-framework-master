from flask import Flask, request
import threading
import asyncio
import websockets
import json
import time
from websocket import create_connection

app = Flask(__name__)

getDataInfoTo = {}

dataonDthis = {}

@app.route('/cbb', methods=["GET","POST"])
def getRpcDate():
    if request.method == "GET":
        print(request.args)
        typeOfDate = request.args.get('type')
        data = request.args.get('data')
        webId = request.args.get('webId')
        reqData = typeOfDate+data
        getDataInfoTo[webId] = reqData
        ws = create_connection("ws://127.0.0.1:5679/getInfo")
        ws.send("ko---c~c")
        ws.recv()
        ws.close()
        while 1:
            if webId in dataonDthis:
                dateInfo = dataonDthis[webId]
                dataonDthis.pop(webId)
                break
        return dateInfo
    elif request.method == "POST":
        typeOfDate = request.form.get('type')
        data = request.form.get('data')
        webId = request.form.get('webId')
        reqData = typeOfDate + data
        getDataInfoTo[webId] = reqData
        ws = create_connection("ws://127.0.0.1:5679/getInfo")
        ws.send("ko---c~c")
        ws.recv()
        ws.close()
        while 1:
            if webId in dataonDthis:
                dateInfo = dataonDthis[webId]
                dataonDthis.pop(webId)
                break
        return dateInfo
    return 'web后端请求出现错误！！！'

@app.route('/getID')
def getId():
    return json.dumps(list(webScoketDist))

async def get_sesson(ws, path):
    # while 1:
    async for message in ws:
        print(message)
        Id = message.split('---')[0]
        data = '---'.join(message.split('---')[1:])

        print(path)
        print(Id)
        print(data)
        print('___________________________')
        if path == '/cbb':
            if Id not in webScoketDist:
                webScoketDist[Id] = ws
            if data != 'c~c':
                dataonDthis[Id] = data
            else:
                print('zh异步')
                await ws.send(getDataInfoTo[Id])
                adInfo = await ws.recv()
                dataonDthis[Id] = adInfo
                getDataInfoTo.pop(Id)

        elif path == '/getInfo':
            print(getDataInfoTo)
            print(webScoketDist)
            for i in list(getDataInfoTo):
                print(webScoketDist)
                print(i)
                if i in webScoketDist:
                    await webScoketDist[i].send('c~c')
            await ws.send('1')


def cbb():
    c_loop = asyncio.new_event_loop()
    asyncio.set_event_loop(c_loop)
    start_server = websockets.serve(get_sesson, '0.0.0.0', 5679)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()

if __name__ == '__main__':
    webScoketDist = {}
    yhh = threading.Thread(target=cbb)
    yhh.start()
    time.sleep(2)
    app.run(host='127.0.0.1', port=9420)

