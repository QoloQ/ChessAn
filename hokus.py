class Base:
	def foo(self):
		return self.bar()

class Der(Base):
	def bar(self):
		return "bar"

c = Base()
b = Der()
c.foo()