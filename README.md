# MathKernelToggle
A Python-based Alfred 3 Workflow to toggle Mathematica Kernel to do computations.

# Main Features
* First, input the keyword `kernel`, then input the query string `query`.
* Then, the `query` will be sent to `/usr/local/bin/wolframscript -code`.
* It's `stdout` is then handled by Python library [`Alfred-Workflow`](https://github.com/deanishe/alfred-workflow).
* Hit `RET` to copy the result to your clipboard or hit `Command+RET` to directly paste the answer to the front most App.
* Update is checked before every run.

# Installation 
Open your Terminal and execute:  
`$ git clone git@github.com:LingyuanJi/math-kernel-toggle.git /path/to/your/workflow/`  

# Caution
* You need to **HAVE** a *Mathematica 11* installed into your macOS, along with the commandline executable `/usr/local/bin/wolframscript`.
