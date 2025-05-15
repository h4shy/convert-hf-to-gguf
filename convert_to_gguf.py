import os, subprocess, sys

# None means it will ask every time you run the script

model_dir = None # "model-dir" or "input"
OUTFILE = "output/model_output.gguf"
outtype = None; OUTTYPES = ['auto', 'f32', 'f16', 'bf16', 'q8_0', 'q4_0']

# using llama.cpp in current dir
script = None ; SCRIPTS = ['llama.cpp/convert_hf_to_gguf.py', 'llama.cpp/examples/convert_legacy_llama.py']
python = "venv/Scripts/python"
DEPENDENCIES = None # or "skip" to skip

# flags
USE_TEMP_FILE = False
NO_LAZY = False
VOCAB_ONLY = False

if __name__ == '__main__':
    os.makedirs(os.path.dirname(OUTFILE), exist_ok=True)
    while not os.path.isdir("llama.cpp"):
        print("\nCannot find llama.cpp in current dir, to install:\n\ngit clone https://github.com/ggml-org/llama.cpp\npython -m venv venv\n./venv/Scripts/activate\npip install -r requirements.txt\n")
        exit()

    if not script:
        r = input("Choose a script: \n1. llama.cpp/convert_hf_to_gguf.py (default) \n2. llama.cpp/examples/convert_legacy_llama.py \n\n>")
        script = SCRIPTS[1] if r == '2' else SCRIPTS[0]
    if not outtype:
        r = input("Choose outtype: \n0. auto \n1. f32 \n2. f16 \n3. bf16 \n4. q8_0 \n5. q4_0 \n\n>") or '0'
        outtype = OUTTYPES[int(r)]
    if not model_dir:
        model_dir = input("Set the model directory: \nMake sure it's in the current dir, skip if the model dir is named 'input' \n\n>") or 'input'

    cmd = [
        "python", script,
        model_dir,
        "--outfile", OUTFILE,
        "--outtype", outtype
    ]

    if USE_TEMP_FILE:
        cmd.append("--use-temp-file")
    if NO_LAZY:
        cmd.append("--no-lazy")
    if VOCAB_ONLY:
        cmd.append("--vocab-only")

    print("\n" + " ".join(cmd))

    if input("\nWould you like to run the command as a subprocess? (Y/n) \n\n>").lower() == 'n': exit()
    while not os.path.isdir("venv"):
        if input("\nNo 'venv' dir found, use whatever currently active python or venv? (Y/n) \n\n>").lower() == 'n':
            print("Please create a venv and install requirements."); exit()
        python = sys.executable

    cmd[0] = python

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd='.', text=True)

    for line in process.stdout:
        print(line, end='') 

    process.wait()

    print("\n\n-- Process Ended --")
