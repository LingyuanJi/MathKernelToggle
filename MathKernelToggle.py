import subprocess
import re
import sys
from workflow import Workflow

mathkernel_path=u"/Applications/Mathematica.app/Contents/MacOS/MathKernel"

def main(wf):
	query = wf.args[0]
	with open("temp.m","w") as temp_file:
		file_content = unicode("Print["+query+"]")
		temp_file.write(file_content)
	answer=unicode(subprocess.check_output(mathkernel_path+u" -script temp.m", shell=True))
	if u"::" in answer:
		error_list=re.findall(r"(\w+)::(\w+): ([^\n]+)", answer)
		error_count=1
		for error in error_list:
			wf.add_item(title=unicode(error[0])+u"::"+unicode(error[1]),\
						subtitle=error[2],\
						valid=False,\
						uid=str(error_count),\
						icon=u"icon_err.png")
			error_count+=1
	else:
		wf.add_item(title=answer,\
		 			subtitle=u"Hit RET to Copy to Clipboard",\
		  			arg=answer,\
		  			valid=True,\
		  			uid=u"0",\
		   			icon=u"icon.png",\
		    		copytext=answer)

	wf.send_feedback()

if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))