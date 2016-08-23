#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2
from caesar import encrypt
from cgi import escape

head = """

<html>
    <head>
        <title>Caesar</title>
        <style type="text/css">
        
        body {
            font-family: arial;
            color: #fff3e6;
            background-color: #282828;
            align: center;
            padding: 15px;
            margin: auto;
            width: 450px;
            text-align: center;
            
        }
        
        form {
            padding: 15px;
            background-color: #666699; <!--#33334d;-->
        }
        
        textarea {
            width:400px;
            height:200px;
            padding: 15px;
            margin:15px 0;
        }
        
        .error {
            color: red;
            }
        
        </style>
    </head>
    
    <body>
        <h1>Caesar</h1>
"""

foot = """
    </body>
</html>

"""

class Index(webapp2.RequestHandler):
    
    def get(self):
        
        body = """
        <form>
            <label for="num"> Rotations </label>
            <input type="number" name="num" value="13"> <br>
            <textarea name="data">{}</textarea> <br>
            <input type="submit">
        </form>
        """
        
        default = "Enter Text to Cypher Here"
        
        print self.request.GET.items()
        
        error= ""
        #error = self.request.get("error")
        #error_element = "<p class='error'>" + error + "</p>" if error else ""
        
        try:
            num = self.request.GET["num"]
        except KeyError:
            num = 0

        if num and num != "":
            try:
                num = int(num)
            except ValueError:
                num = 0
        else:
            num = 0
            error = "Enter a Rotation Number and Message"
        
        print num
        
        data = self.request.get("data")
        if data and data != "":
            data = escape(data)
        else:
            data = "enter a message"
            error = "Enter a Message to cypher"
            num = 0;
                
        
        error_element = "<p class='error'>" + error + "</p>" if error else ""
        
        if data:
            data = encrypt(data, num)
            html = head + error_element + body.format(data) + foot
        else:
            html = head + error_element + body.format(default) + foot
            
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', Index)
], debug=True)
