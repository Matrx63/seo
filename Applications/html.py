#!/usr/bin/python
import os
import platform

def open_html_file(file_name):
    if file_name == "monogramme":
        file = open('/home/matrx63/Web/monogramme.html', 'w');
        make_head(file, "Monogramme");
        return file

    if file_name == "bigramme":
        file = open('/home/matrx63/Web/bigramme.html', 'w');
        make_head(file, "Bigramme");
        return file

    if file_name == "trigramme":
        file = open('/home/matrx63/Web/trigramme.html', 'w');
        make_head(file, "Trigramme");
        return file
        
    return None
    
def close_html_file(file):
    file.write("""
    </footer>
    </div> 
    </body>
    </html>
    """)
    file.close()
    
    return None

def make_head(file, title):
    file.write("""<!DOCTYPE html>
    <html lang="en">
    <head>  <meta charset="utf-8">
      <title>Google News Analyser</title>
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <link rel="stylesheet" href="//koding.com/hello/css/style.css">
      <!--[if IE]>
          	<script src="//html5shiv.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->
      <link href='//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
    </head>
    <body class="python">
      <div id="container">
        <div id="main" role="main"  class="hellobox" >
        <h1>""")
    file.write(title);
    file.write("""</h1>
    <h2>From Google News 
    </h2> </div>
    <nav>
    	<ul>
          <li><a href="index.html">Home</a></li>
          <li><a """)
    if title == "Monogramme":
        file.write(""" class="active" """)
    
    file.write(""" href="monogramme.html">Monogramme</a></li>
          <li><a """)
          
    if title == "Bigramme":
        file.write(""" class="active" """)
    
    file.write(""" href="bigramme.html">Bigramme</a></li>
          <li><a """)
          
    if title == "Trigramme":
        file.write(""" class="active" """)
    
    file.write(""" href="trigramme.html">Trigramme</a></li>
    	</ul>    
    </nav>
    <footer>
    """)
    return None
