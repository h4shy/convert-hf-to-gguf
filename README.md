# Conversion Made Easy
This is an efficient script for converting Pytorch/HF models to GGUF format.

Start with setting up the directory.  
<pre>git clone https://github.com/h4shy/convert-hf-to-gguf</pre>

Navigate to `convert-hf-to-gguf` and do:  
<pre>git clone https://github.com/ggml-org/llama.cpp</pre>  
<pre>python -m venv venv</pre>  
<pre>./venv/Scripts/activate</pre>  
<pre>pip install -r requirements.txt</pre>  

Place your model directory in `convert-hf-to-gguf`

That's it! Run `convert_to_gguf.py` and select the desired parameters.
