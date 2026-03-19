import os, sys
os.chdir('/Users/jordan.kennard/Documents/world-cup-game-quiz-show')
sys.argv = ['http.server', '8080']
import http.server
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8080, bind='')
