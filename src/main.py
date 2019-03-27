from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent
from pykeyboard import PyKeyboard

# m = PyMouse()
# x_dim, y_dim = m.screen_size()

# m.click(x_dim/2, y_dim/2, 1)



class Clickonacci(PyMouseEvent):


	

	def __init__(self):
		PyMouseEvent.__init__(self)
		self.s_x = 0
		self.s_y = 0
		self.mouse = PyMouse()

	def click(self, x, y, button, press):
		'''Print Fibonacci numbers when the left click is pressed.'''
		if button == 1:
			if press:
				print ('start:',PyMouse().position())
				self.s_x, self.s_y = PyMouse().position()

			else:
				print('end:', PyMouse().position())
				e_x, e_y = PyMouse().position()
				if(abs(e_x - self.s_x) > 20):

					temp_x = min(self.s_x, e_x)
					num = (abs(e_x - temp_x) / 30) + 1 # 计算点击次数
					print('自动点击次数:', num)
					for i in range(int(num)):
						PyMouse().click(temp_x, e_y, 1, 1)
						temp_x = temp_x + 30

			# if release:
			# 	print('over:', PyMouse().position())
		else: # Exit if any other mouse button used
			self.stop()
	# def move(self, x, y):
	# 	print ("the mouse was moved to", x, y)
		# return x, y


class TapRecord(PyKeyboardEvent):
	def __init__(self):
		PyKeyboardEvent.__init__(self)

	def tap(self, keycode, character, press):
		print(time.time(), keycode, character, press)



C = Clickonacci()
C.run()
# K = TapRecord()
# K.run()
