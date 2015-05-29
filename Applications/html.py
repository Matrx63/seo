#!/usr/bin/python
import os
import platform
from pattern.graph  import Graph
from pattern.en import Text

def open_html_file():
        file = open('/home/matrx63/Web/n-grams.html', 'w');
        _make_head(file, "n-grams");
        return file
    
def close_html_file(file):
    file.write("""
    </footer>
    </div> 
    </body>
    </html>
    """)
    file.close()
    return None

def make_graph(dgram, n, numWord):
    if n == 1:
        graph = Graph(distance=4.0)
        center = graph.add_node(' ', radius=0)
        center.fill = (0,0,0,0)
        for gram in dgram:
            key = gram
            w = dgram[gram] / numWord
            node = graph.add_node(key, centrality=w, radius=dgram[gram] + 1)
            node.fill = (0, 0.5, 1, node.radius * 0.1)
            graph.add_edge(center, node, length=2000/node.radius, stroke=(0,0,0,0)) # R,G,B,A
        graph.export('/home/matrx63/Web/monogram', pack=False, width='2000', height='2000', frames=5000, ipf=30)
        
    

def _make_head(file, title):
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
    file.write(title)
    file.write("""</h1>
    <h2>From Google News 
    </h2> </div>
    <nav>
    	<ul>
          <li><a href="index.html">Home</a></li>
          <li><a class="active" href="n-grams.html">""")
    file.write(title)
    file.write("""</a></li>
    	</ul>    
    </nav>
    <footer>
    """)
    return None
