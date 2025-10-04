import asyncio
import websockets
import threading
import queue
import tan_code  # Import your Tan AI file

# Queue for Tan → GUI messages
log_queue = queue.Queue()
clients = set()

# Function for Tan to log messages to GUI
def log_to_gui(message):
    log_queue.put(message)

async def send_logs():
    while True:
        if not log_queue.empty():
            msg = log_queue.get()
            dead_clients = []
            for ws in clients:
                try:
                    await ws.send(msg)
                except:
                    dead_clients.append(ws)
            for ws in dead_clients:
                clients.remove(ws)
        await asyncio.sleep(0.2)

async def handler(websocket):
    clients.add(websocket)
    try:
        async for message in websocket:
            # You can forward messages from GUI to Tan if needed
            print(f"[GUI Input] {message}")
    finally:
        clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 6789):
        await send_logs()

def run_server():
    asyncio.run(main())

# Run WebSocket server in a background thread
server_thread = threading.Thread(target=run_server, daemon=True)
server_thread.start()

# Now run Tan AI
tan_code.start_ai(log_to_gui)  # Pass logging function into Tan
