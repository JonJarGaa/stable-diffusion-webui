import os
import time

# USER CHANGABLE ARGUMENTS

# Change to `True` if you wish to enable these common arguments

# Run upscaling models on the CPU
extra_models_cpu = False

# Automatically open a new browser window or tab on first launch
open_in_browser = False

# Run Stable Diffusion in Optimized Mode - Only requires 4Gb of VRAM, but is significantly slower
optimized = True

# If low vram mode, should generate higher-resolution images
low_vram_mode = False

# Run in Optimized Turbo Mode - Needs more VRAM than regular optimized mode, but is faster
optimized_turbo = True

# Creates a public xxxxx.gradio.app share link to allow others to use your interface (requires properly forwarded
# ports to work correctly)
share = False

# Enter other `--arguments` you wish to use - Must be entered as a `--argument ` syntax
additional_arguments = ""

# BEGIN RELAUNCHER PYTHON CODE

common_arguments = ""

if extra_models_cpu:
    common_arguments += "--extra-models-cpu "
if optimized_turbo:
    common_arguments += "--optimized-turbo "
if optimized:
    common_arguments += "--optimized "
if low_vram_mode:
    common_arguments += "----config optimizedSD/v1-inference_lowvram.yaml "
if share:
    common_arguments += "--share "

if open_in_browser:
    inbrowser_argument = "--inbrowser "
else:
    inbrowser_argument = ""

n = 0
while True:
    if n == 0:
        print('Relauncher: Launching...')
        os.system(f"python scripts/webui.py {common_arguments} {inbrowser_argument} {additional_arguments}")

    else:
        print(f'\tRelaunch count: {n}')
        print('Relauncher: Launching...')
        os.system(f"python scripts/webui.py {common_arguments} {additional_arguments}")

    n += 1
    if n > 100:
        print('Too many relaunch attempts. Aborting...')
        break
    print('Relauncher: Process is ending. Relaunching in 1s...')
    time.sleep(1)
