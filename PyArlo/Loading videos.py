# by default, all videos recorded within
# the last 30 days will be pre-loaded
arlo.ArloMediaLibrary.videos

# Or you can load Arlo videos directly
from pyarlo.media import ArloMediaLibrary
library = ArloMediaLibrary(arlo, days=2)
len(library.videos)

# showing a video properties
media = library.videos[0]

# printing video attributes
media.camera
media.content_type
media.media_duration_seconds

# displaying thumbnail to stdout
media.download_thumbnail()

# downloading video
media.download_video('/home/user/demo.mp4')