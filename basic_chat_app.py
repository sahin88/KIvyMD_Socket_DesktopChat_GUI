import kivy
from kivy.uix.label import Label
import socket 
from kivy.lang import Builder
from kivy.uix.button import Button
from kivymd.uix.toolbar import MDToolbar
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.card import MDSeparator
from functools import partial
from kivy.factory import Factory
from kivy.uix.image import Image
from kivymd.uix.list import IRightBodyTouch, ILeftBody
from kivymd.uix.selectioncontrol import MDCheckbox
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivymd.uix.dialog import MDDialog
import socket 
import json 
import pickle 
import threading 
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivymd.uix.button import MDFillRoundFlatButton
import time


print('every thing is ok')

Builder.load_string('''
#: import  MDLabel kivymd.uix.label.MDLabel
#: import MDToolbar kivymd.uix.toolbar.MDToolbar
#: import MDButton kivymd.uix.button.MDRectangleFlatIconButton
#: import MDTextField  kivymd.uix.textfield.MDTextField
#: import partial functools.partial
#: import MDTextFieldRound  kivymd.uix.textfield.MDTextFieldRound
#: import MDIconButton  kivymd.uix.button.MDIconButton 
#: import MDFillRoundFlatButton   kivymd.uix.button.MDFillRoundFlatButton  



<Mdfill@OneLineListItem>:
	text:
	

<MDCheckbox>
	active:False
	on_active:
		print(self.active)

<ListItemWithCheckbox@OneLineAvatarIconListItem>:
	MyAvatar:
		source: "/home/alex/electron-quick-start/einstein.jpg"
	MyCheckbox:




	
<MainScreen>:
	
	name: 'first'

	FloatLayout:
		MDToolbar:
			pos_hint: {'top':1}
			title:' Welcome to Chat Application'
			md_bg_color:app.theme_cls.primary_color
			left_action_items:[["menu", lambda x:print(x)]]
			right_action_items:[['magnify', lambda x:print("")]]
		MDCard:
			size_hint: None, None
			size: dp(520), dp(340)
			pos_hint: {'center_x': 0.5, 'center_y': 0.5}

			BoxLayout:
				orientation:'vertical'
				padding:dp(10)
				spacing:20

				MDLabel:
					pos_hint:{"x":0, "y":.8}
					text:'Connection Property'
					theme_text_color:'Secondary'
					font_style:'Subtitle2'
					size_hint_y:None
					height:dp(36)
				MDSeparator:
					height:dp(1)


				MDTextField:
					id:ip
					text:''
					pos_hint:{"x":0, "top":.9}
					size_hint:None, None
					height:dp(35)
					width:dp(400)
					hint_text:"IP Number"
					helper_text:" To connect the speaker "
					required:True
					max_text_length:25
				MDTextField:
					id:port
					text:''
					pos_hint:{"x":0, "top":.7}
					size_hint:None, None
					height:dp(40)
					width:dp(400)
					hint_text:"Port Number"
					helper_text:" To connect the speaker "
					required:True
					max_text_length:25
				MDTextField:
					id:user
					text:''
					pos_hint:{"x":0, "top":.5}
					size_hint:None, None
					height:dp(40)
					width:dp(400)
					hint_text:"User Name"
					helper_text:" To connect the speaker "
					required:True

					max_text_length:25


				FloatLayout:

					MDRectangleFlatIconButton:
						pos_hint:{'x':0, "y":0}
						text:'Add New'
						icon:"ip"
						theme_text_color:'Custom'
						text_color:[1,1,1,1]
						md_bg_color: [1,0,0,1]
						on_release:root.set_ip()
					MDRectangleFlatIconButton:
						pos_hint:{'x':.6, "y":0}
						text:'Select '
						icon:"contacts"
						theme_text_color:'Custom'
						text_color:[1,1,1,1]
						md_bg_color: [1,0,0,1]
						on_release:
							app.root.current= "second"
							root.manager.transition.direction = 'left'
							root.page_two_item()
					


		MDToolbar:
			pos_hint: {'bottom':1}
			md_bg_color:app.theme_cls.primary_color

<SecondScreen>:

	name: 'second'
	fwrd:'third'

	GridLayout:
		cols:1
		MDToolbar:
			pos_hint: {'top':1}
			title:' Contacts'
			md_bg_color:app.theme_cls.primary_color
			left_action_items:[["arrow-left", lambda x:root.change_page(root.name)],["contacts", lambda x:print(x)]]
			right_action_items:[['plus', lambda x:app.root.page_adding()],["arrow-right",lambda x:root.change_page(root.fwrd)]]
			elevation: 10

		ScrollView:
			MDList:
				id:scroll


<ThirdScreen>:
	name: 'third'
	bckwrd:'backward'
	GridLayout:
		cols:1
		
		MDToolbar:
			pos_hint: {'top':1}
			title:'You are chatting with ananouyms be careful not to be hacked :)'
			md_bg_color:app.theme_cls.primary_color
			left_action_items:[["arrow-left", lambda x:app.root.get_screen('second').change_page(root.bckwrd)],["chat-processing", lambda x:print(x)]]

		ScrollView:
			MDList:
				id:scrolling

		FloatLayout:
			MDToolbar:
				pos_hint: {'bottom':1}
				md_bg_color:app.theme_cls.primary_color

			MDTextFieldRound:
				id:msg_send
				pos_hint: {'x':.02,'top':.2}
				size_hint_x:0.9
				icon:'send'
				hint_text:'This is chat entry'
				foreground_color:0,0,1,1
				md_bg_color:1,0,0,1
				focus:False
			MDIconButton:
				icon:'server-network'
				pos_hint:{'x':0.94,"top":0.2}
				theme_text_color:"Custom"
				text_color:[1,1,1,1]
				md_bg_color:[1,0,0,1]
				on_press:
					root.connect_server()
			MDIconButton:
				id:btn
				icon:'plus'
				pos_hint:{'x':0.87,"top":0.2}
				theme_text_color:"Custom"
				text_color:[1,1,1,1]
				md_bg_color:[1,0,0,1]
				focus:False
				on_press:
					root.sending_data()
			
		''')

class MyCheckbox(IRightBodyTouch, MDCheckbox):
	pass


class MyAvatar(ILeftBody, Image):
	pass
class ThirdScreen(Screen):
		

	def sending_data(self):
			user_list=[]
			self.clients={}
			self.msg=self.ids.msg_send.text
			self.clients['user']=self.username
			self.clients['data']=self.msg
			if self.clients["user"]  in user_list:
				self.clients["user"]=None
				self.clients['data']=self.clients["user"]+" has attended to the chat"
				self.clients['data']=self.clients["user"]+" has attended to the chat"
			msg_to_send=pickle.dumps(self.clients)
			print("msg_to_send",msg_to_send)
			self.connect_server.send(msg_to_send)

			


	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.IP=MainScreen.l[0]
		self.connection_prot_1=socket.AF_INET
		self.connection_prot_2=socket.SOCK_STREAM
		self.PORT=int(MainScreen.l[1])

		self.thread_1=threading.Thread(target=self.connectin_to_server)
		self.thread_1.deamon=True
		self.thread_1.start()
		
	def connectin_to_server(self):
		try:
			self.connect_server=socket.socket(self.connection_prot_1,self.connection_prot_2)
			self.connect_server.connect((self.IP,self.PORT))
			md_dialog=MDDialog(title='info page', text="You have connected suceffully", size_hint=[.5,.5])
			md_dialog.open()
		except Exception as e:
			if e:
				md_dialog=MDDialog(title='info page', text=str(e), size_hint=[.5,.5])
				md_dialog.open()

		self.clients={}
		self.username=MainScreen.l[2]
		self.msg=self.ids.msg_send.text
		self.clients['user']=self.username
		self.clients['data']=self.msg

		self.thread_2=threading.Thread(target=self.comming_message)
		self.thread_2.deamon=True
		self.thread_2.start()
		
	
		self.thread_3=threading.Thread(target=self.sending_data)
		self.thread_3.deamon=True
		self.thread_3.start()



	def comming_message(self):	
		while True:
			self.comming_msg=self.connect_server.recv(1024)
			cmning=pickle.loads(self.comming_msg)
			print("user", cmning['user'])
			if  not self.comming_msg :
				 text_2=cmning['user']+"has left chat"

			elif cmning['user'] is None:
				text_2=cmning['data'] 
			else:
				text_2=cmning['user']+":>:"+cmning['data']
				print(text_2)
		
			

			self.ids.scrolling.add_widget(Factory.Mdfill(text= text_2))

		

class SecondScreen(Screen):

	def change_page(self, instance):
		print("instance", instance)
		if instance=='second':
			self.manager.current='first'
			self.manager.transition.direction='right'
		elif instance=='third':
			print("3. sayfaya gönderrrr")
			self.manager.current='third'
			self.manager.transition.direction='left'
		elif instance=='backward':
			self.manager.current='second'
			self.manager.transition.direction='right'

	def page_adding(self):
		s=ScreenManagement()
		s.add_widget(ThirdScreen())
		# self.manager.current='third'
		print("Adding to the page")
class MainScreen(Screen):
	l=[]
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.list_of_item=[]
		#self.set_ip()
	# main_src=ObjectProperty(None)
	# port = ObjectProperty(None)
	# ip = ObjectProperty(None)

	
	def set_ip(self):
		self.list_of_item=[]
		self.ids.ip.text=socket.gethostbyname(socket.gethostname())
		self.ids.port.text='1235'
		self.prt='1235' #self.ids.port.text
		if self.prt=="" or self.ids.user.text=="" or self.ids.ip.text=="":
			md_dialog=MDDialog(title='info page', text="Please check the port number or user name ", size_hint=[.5,.5])
			md_dialog.open()
		user=self.ids.user.text
		self.list_of_item.append(self.ids.ip.text)
		self.list_of_item.append(self.prt)
		self.list_of_item.append(user)
		MainScreen.l=self.list_of_item



	def page_two_item(self):
		text_1="Ip  :"+self.list_of_item[0]+"\n"+"Port Nr :"+self.list_of_item[1]+"User Name  :"+self.list_of_item[2]
		for i in range(int(len(self.list_of_item)/3)):
			print(i)
			self.manager.get_screen('second').ids.scroll.add_widget(Factory.ListItemWithCheckbox(text= text_1))
	

class ScreenManagement(ScreenManager):
	def __init__(self,**kwargs):
		super().__init__(**kwargs)
		self.add_widget(MainScreen())
		self.add_widget(SecondScreen())
	def page_adding(self):
		
		self.add_widget(ThirdScreen())
		

		



class MyApp(MDApp):
	def __init__(self,**kwargs):
		self.theme_cls.theme_style = "Light"
		super().__init__(**kwargs)
		
	def build(self):

	
		return ScreenManagement()

		


if __name__ == '__main__':
	MyApp().run()