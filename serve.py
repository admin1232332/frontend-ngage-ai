#!/usr/bin/env python3
"""
Simple HTTP server for nGAGE frontend
Serves the HTML file on localhost:8000
"""

import http.server
import socketserver
import os
import webbrowser
from pathlib import Path

def serve_frontend():
    """Serve the frontend on localhost:8000"""
    PORT = 8000
    
    # Change to frontend directory
    os.chdir(Path(__file__).parent)
    
    # Create server
    Handler = http.server.SimpleHTTPRequestHandler
    
    # Add CORS headers for local development
    class CORSRequestHandler(Handler):
        def end_headers(self):
            self.send_header('Access-Control-Allow-Origin', '*')
            self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
            self.send_header('Access-Control-Allow-Headers', 'Content-Type')
            super().end_headers()
        
        def do_OPTIONS(self):
            self.send_response(200)
            self.end_headers()
    
    with socketserver.TCPServer(("", PORT), CORSRequestHandler) as httpd:
        print("🌐 nGAGE Frontend Server")
        print("=" * 40)
        print(f"📱 Frontend: http://localhost:{PORT}")
        print(f"🔗 Backend: http://localhost:5000")
        print("=" * 40)
        print("✅ Make sure your backend is running on port 5000")
        print("🚀 Opening browser...")
        
        # Open browser
        try:
            webbrowser.open(f'http://localhost:{PORT}')
        except:
            print("⚠️ Could not open browser automatically")
        
        print(f"🔄 Serving at http://localhost:{PORT}")
        print("Press Ctrl+C to stop")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Frontend server stopped!")

if __name__ == "__main__":
    serve_frontend()