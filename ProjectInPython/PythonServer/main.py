import http.server
import socketserver
import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Set the port you want the server to run on
port = 8080

# Specify the directory where your webpage file is located
web_directory = os.getcwd()

# Create a simple HTTP server
handler = http.server.SimpleHTTPRequestHandler

# Create the server with the specified port
with socketserver.TCPServer(("", port), handler) as httpd:
    print(f"Serving on port {port}")

    # Define a custom event handler to watch for changes in the directory
    class MyHandler(FileSystemEventHandler):
        def on_modified(self, event):
            if event.is_directory:
                return
            print(f'Reloading due to change in: {event.src_path}')
            httpd.shutdown()  # Shutdown the server

    # Start watching for file changes
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=web_directory, recursive=True)
    observer.start()

    try:
        # Start the server
        httpd.serve_forever()
    except KeyboardInterrupt:
        observer.stop()

# Join the observer thread
observer.join()
