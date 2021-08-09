from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.core.audio import SoundLoader
from kivy.lang import Builder

Window.size = (480,800)
Window.minimum_height = 600
Window.minimum_width = 400

Builder.load_string('''
<Body>:
    
    id: err
    orientation: 'vertical'
    size_hint: 0.9, 0.9
    pos_hint: {'center_x':0.5,'center_y':0.5}  

    Image:
        id: image
        source: 'lupa.jpg'
        
    Label:
        text: 'Bear Search'
        font_size: 70
        bold: False
        color: 0,0,0,1
        
    FileChooserListView:
        id: filechooser
        dirselect: True
        on_selection: err.selected(filechooser.selection,*args)
        
    GridLayout:
        cols: 2

        MDRaisedButton:
            text: 'Search'
            on_release:
                root.search()
            
    AnchorLayout:
        anchor_x: 'center'
        anchor_y: 'bottom'
        
        MDRaisedButton:
            text: 'Authors'
            on_release:
                root.authors()
''')


class Body(MDBoxLayout):
   
	sound1 = SoundLoader.load('search.wav')
	sound2 = SoundLoader.load('authors.wav')
	

	def selected(self,*args):
		download_path = args[0]
		# копирует путь выбранного файла 
		self.ids.image.source="".join(download_path)
		# изменяет фото-label на скопированный путь
		print(self.ids.image.source)	


	def search(self):
		Body.sound1.play() 
		import main
		main.search(self.ids.image.source)

	def authors(self):		
		Body.sound2.play()

		gl = GridLayout(cols=1)	
		label = Label(text='\n• Даниил Чепко\n\n• Анастасия Кучер\n\n• Темирлан Алчаков\n')
		gl.add_widget(label)
		self.popup = Popup(title = "ByteScout", content=gl, 
							size_hint = (0.5,0.4), size=(400,400),
							auto_dismiss = True )		
		self.popup.open()
         
    
    
class ThisApp(MDApp):		
	title = 'BearSearch'
	
	def build(self):		
		return Body()


if __name__ == '__main__':
	ThisApp().run()
