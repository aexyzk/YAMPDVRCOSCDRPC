import coverpy

class cover():
	def __init__(self):
		super().__init__()
		self.coverpy = coverpy.CoverPy()
		self.album = ""
		self.link = ""
		self.placeholder = "https://www.musicpd.org/logo.png"

	def get_cover(self, _album):
		if self.album != _album:
			self.album = _album
			try:
				result = self.coverpy.get_cover(self.album, 1)
				self.link = result.artwork(100)
			except coverpy.exceptions.NoResultsException:
				print("Cover art not found.")
				self.link = self.placeholder
			except requests.exceptions.HTTPError:
				print("Could not execute GET request")
				self.link = self.placeholder
		return self.link

# testing to make sure it doesnt fetch the same link over and over (if its the same album as the last)
if __name__ == "__main__":
	_cover = cover()
	print(_cover.get_cover("Sleepyhead - Cavetown"))
	print(_cover.get_cover("Sleepyhead - Cavetown"))
	print(_cover.get_cover("Vessel - Twenty One Pilots"))
	print(_cover.get_cover("Blurryface - Twenty One Pilots"))
	print(_cover.get_cover(""))