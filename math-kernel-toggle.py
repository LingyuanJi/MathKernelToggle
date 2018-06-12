# coding=utf-8
import subprocess
import sys
from workflow import Workflow3

def main(wf):

        expr = wf.args[0]
	answer = subprocess.check_output(["/usr/local/bin/wolframscript", "-code", expr])
        answer = answer.strip()

	wf.add_item(title = answer,
		    subtitle = "Hit RET to Copy to Clipboard",
		    arg = answer,
		    valid = True)
        
	wf.send_feedback()

if __name__ == '__main__':
        wf = Workflow3(update_settings={
        "github_slug": "LingyuanJi/math-kernel-toggle"
        })
        if wf.update_available:
                wf.start_update()
        wf = Workflow3()
        sys.exit(wf.run(main))
