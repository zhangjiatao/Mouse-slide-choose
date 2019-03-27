from pymouse import PyMouse
from pymouse import PyMouseEvent
from pykeyboard import PyKeyboardEvent
from pykeyboard import PyKeyboard
'''
通过滑动鼠标来实现多个token的选取
'''
TOKEN_WIDTH = 30 #小格子的宽度,需要根据屏幕尺寸调整,可以根据打印的start_postion进行设置

class Clickonacci(PyMouseEvent):

	def __init__(self):
		PyMouseEvent.__init__(self)
		self.s_x = 0
		self.s_y = 0
		self.mouse = PyMouse()

	def click(self, x, y, button, press):
		if button == 1:
			if press:
				# 记录鼠标滑动起始位置
				print ('start_postion:',PyMouse().position())
				self.s_x, self.s_y = PyMouse().position()

			else:
				print('end_postion:', PyMouse().position())
				# 记录终止位置
				e_x, e_y = PyMouse().position()
				# 屏蔽短距离移动
				if(abs(e_x - self.s_x) > 10):
					temp_x = min(self.s_x, e_x)
					num = (abs(e_x - temp_x) / TOKEN_WIDTH) + 1 # 计算点击次数，30是小格子的宽度，需要根据屏幕尺寸调整
					print('自动点击次数:', num)
					# 在起始位置和终止位置之间每隔一个TOKEN_WIDTH进行一次点击
					for i in range(int(num)):
						PyMouse().click(temp_x, e_y, 1, 1)
						temp_x = temp_x + TOKEN_WIDTH 

		else:
			self.stop()

if __name__ == '__main__':
	C = Clickonacci()
	C.run()

