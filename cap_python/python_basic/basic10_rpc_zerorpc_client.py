import zerorpc

c = zerorpc.Client()
c.connect("tcp://0.0.0.0:4242")
print(c.hello("anan_baby"))
