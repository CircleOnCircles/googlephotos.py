# googlephotos.py
an unofficial pythonic API to google photos services

# Quickstart
```bash
pipenv install googlephotos.py
```

```python
import googlephotos

with googlephotos.authenticate(by='browser') as gphotos:
	# upload a media item
	gphotos.upload('image1.jpg') 
	
	# upload and put in an album 
	gphotos.upload('i-see-a-real-python.mp4').toAlbum('vacation on my beach 2019', find_first=True)
	
	# list album
	for album in gphotos.albums:
		if len(album) > 10:
			print(f'`The album, {album.name}, has more than 10 media items.`)
	
	# get album by name
	album = gphotos.albums['vacation on my beach 2019']
	
	# get album by id, use byte data instead of string
	album = gphotos.albums[b'asdj21231jkebkad']
	
	# you can upload directly to album as well
	image_file = Path('my_kitten.jpg')
	
	album.upload(str(image_file)) # as path string
	
	album.upload(image_file) # as path object
	
	with image_file.open('rb') as fp:
		album.upload(fp) as file pointer
		album.upload(fp.read()) # as byte
```
	
