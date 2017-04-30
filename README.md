# MathKernelToggle
A Python-based Alfred 3 Workflow to toggle Mathematica Kernel to do computations.

# Main Features
* First, input the keyword `ker`, then input the query string `query`.
* Then, the `query` will be sent to MathKernel of your OS.
* Result or errors will be formatted in `XML`.
* Display the `XML` file in Alfred using Python library `Alfred-Workflow`.
* Hit `RET` to copy the result to your clipboard or hit `Command+RET` to directly paste the answer to the front most App.

# Installation 
Open your Terminal and execute:  
`$ git clone https://github.com/LingyuanJi/MathKernelToggle.git /path/to/your/workflow/`  
If you install Alfred 2 and its support files in the standard path, the command should be:  
`$ git clone https://github.com/LingyuanJi/MathKernelToggle.git ~/Library/Application\ Support/Alfred\ 2/Alfred.alfredpreferences/workflows/`

# Caution
* You need to **HAVE** a *Mathematica* installed in your OS.
* You need to ensure that your *Mathematica* is in the **STANDARD PATH**, which is `/Applications/Mathematica.app`. If not, you will need to change the file path to the MathKernel. To do this, use the keyword `kernelpath` to open the file storing the kernel path. Modify this file to meet need and save. 
