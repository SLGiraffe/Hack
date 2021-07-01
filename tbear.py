#from kivy.app import App
from kivymd.app import MDApp

from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup
from kivy.uix.filechooser import FileChooserIconView
from kivy.core.window import Window
from kivy.core.audio import SoundLoader

from kivymd.theming import ThemeManager
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.filemanager import MDFileManager


#Window.clearcolor = (0, 0, 0, 1)
Window.size = (480,800)
Window.minimum_height = 600
Window.minimum_width = 400


class Body(MDBoxLayout):
   
	sound1 = SoundLoader.load('search.wav')
	sound2 = SoundLoader.load('authors.wav')
	
#	file_chooser = MDFileManager(dirselect = True)

	def selected(self,*args):

		download_path = args[0]
		
		self.ids.image.source = "".join(download_path)
		print(self.ids.image.source)



#   ^		


	def search(self):
		Body.sound1.play() 
		import main
		main.search(self.ids.image.source)

	def authors(self):		
		Body.sound2.play()

		gl = GridLayout(cols=1)	
		label = Label(text = ' \n• Даниил Чепко\n\n• Анастасия Кучер\n\n• Темирлан Алчаков\n')
		gl.add_widget(label)
		self.popup = Popup(title = "ByteScout", content=gl, size_hint = (0.5,0.4), size=(400,400), auto_dismiss = True)
		self.popup.open()
    
   

    
    
    
class ThisApp(MDApp):
# Основное тело
	title = 'BearSearch'
	def build(self):


		return Body()


if __name__ == '__main__':
	ThisApp().run()

input()