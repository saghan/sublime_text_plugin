import sublime
import sublime_plugin


class DeleteCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		
		pos=2
		length=self.view.size()
		region=sublime.Region(0,length)
		arr_region=self.view.split_by_newlines(region)	
		final_res=""

		for regions in arr_region:
			line=self.view.substr(regions)
			res=line[:pos]+line[pos+1:]+"\n"
			final_res+=res
			
		self.view.replace(edit,region,final_res)
