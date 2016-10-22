import sublime
import sublime_plugin
from subprocess import Popen, PIPE, STDOUT
import io

class cppfilt(sublime_plugin.TextCommand):
    def process_region(self, edit, region):
        text = self.view.substr(region)
        if not text.strip():
            return

        p = Popen(['c++filt'], stdout=PIPE, stdin=PIPE, stderr=STDOUT)    
        stdout_data, stderr_data = p.communicate(input=text.encode())

        if stderr_data:
            print("c++filt errors: %s" % (stderr_data))
        else:
            self.view.replace(edit, region, stdout_data.decode())

    def run(self, edit):
        regions = self.view.sel()
        for region in regions:
            self.process_region(edit, region)

