from enum import Enum
from urllib import request
class RequestTypes(Enum):
	GET = 0
	POST = 1

class Webhook:
	def __init__(self, endpoint, data=b"", type=RequestTypes.POST):
		self.endpoint = endpoint
		self.data = data
		self.type = type
		
		
	def Trigger(self):
		d = self.data if self.type != RequestTypes.GET else None
		try:
			return request.urlopen(self.endpoint,data=d,timeout=10)
		except Exception as e:
			print(e)
			return False