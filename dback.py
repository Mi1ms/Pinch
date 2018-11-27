from websockets import handshake

original_build_request = handshake.build_request

def custom_build_request(headers):
    res = original_build_request(headers)
    headers['Access-Control-Allow-Origin'] = '*'
    return headers

handshake.build_request = custom_build_request

import os
import asyncio
import websockets
import inotify, inotify.adapters

async def testws(websocket, path):
    i = inotify.adapters.Inotify()
    # set file to watch
    url = os.getcwd()+'/db.json'
    i.add_watch(url)


    for event in i.event_gen(yield_nones=False):
        print("We've got an event from inotify")
        print(event)
        event, event_type, filepath, filename = event
        await websocket.send(filepath)



startserver = websockets.serve(testws, 'localhost', 2400)
asyncio.get_event_loop().run_until_complete(startserver)
asyncio.get_event_loop().run_forever()
