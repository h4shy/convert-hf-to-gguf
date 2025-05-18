# Conversion Made Easy
Start with setting up the directory.  
<pre>git clone https://github.com/h4shy/convert-hf-to-gguf</pre>

Then navigate to `convert-hf-to-gguf` and do:  
<pre>git clone https://github.com/ggml-org/llama.cpp</pre>  
<pre>python -m venv venv</pre>  
<pre>./venv/Scripts/activate</pre>  
<pre>pip install -r requirements.txt</pre>  

Now move your model directory to `convert-hf-to-gguf`, or clone it.

That's it, run the script and follow instructions, most of them are skippable if you don't care :skull::  
<pre>python convert_to_gguf.py</pre>
