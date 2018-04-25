import os.path
import clingo

class AspParser(object):
	def __init__(self):
		self._control = clingo.Control()
		self._model_view = None
		self._solver = None
		self._programs = {}
		self._str_model = ''

	def loadfile(self, filename):
		if not os.path.isfile(filename):
			print ('could not open file :' + filename)
			return -1
		print('load file' + filename)

		try:
			ff = open(filename)
			self._programs[filename] = ff.read()
			ff.close()
		except RuntimeError as error:
			print(error)
			print('load failed')
			return -2
		return 0

	def parse(self):
		if self._control is None:        
			return
		try:
			with self._control.builder() as bb:
				for key in self._programs:
				    clingo.parse_program(self._programs[key], lambda stm: bb.add(stm))
			self._control.ground([('base', [])])
			result = self._control.solve()
			print(result)
			with self._control.solve(yield_=True) as handle:
				for m in handle: 
					print(m) 
				print(handle.get())

		except RuntimeError as error:
			print(error)
			return -2
		return 0


Parser = AspParser()
Parser.loadfile("facts.lp")
Parser.loadfile("rules.lp")
Parser.parse()