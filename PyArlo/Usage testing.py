# connecting
from pyarlo import PyArlo
arlo  = PyArlo('foo@bar', 'secret')

# listing devices
arlo.devices

# listing base stations
arlo.base_stations

# get base station handle
# assuming only 1 base station is available
base = arlo.base_stations[0]

# get the current base station mode
base.mode  # 'disarmed'

# listing Arlo modes
base.available_modes # ['armed', 'disarmed', 'schedule', 'custom']

# Updating the base station mode
base.mode = 'custom'

# listing all cameras
arlo.cameras

# showing camera preferences
cam = arlo.cameras[0]

# check if camera is connected to base station
cam.is_camera_connected  # True

# printing camera attributes
cam.serial_number
cam.model_id
cam.unseen_videos

# get brightness value of camera
cam.brightness

# get signal strength of camera with base station
cam.signal_strength

# get flip property from camera
cam.flip_state

# get mirror property from camera
cam.mirror_state

# get power save mode value from camera
cam.powersave_mode

# get current battery level of camera
cam.battery_level
92

# get boolean result if motion detection
# is enabled or not
base.is_motion_detection_enabled  # True

# get battery levels of all cameras
# prints serial number and battery level of each camera
base.get_cameras_battery_level  # {'4N71235T12345': 92, '4N71235T12345': 90}

# get base station properties
base.properties

# get camera properties
base.get_camera_properties

# get camera rules
base.get_camera_rules

# get camera schedule
base.get_camera_schedule

# get camera motion detection sensitivity
cam.get_motion_detection_sensitivity

# refreshing camera properties
cam.update()

# gathering live_streaming URL
cam.live_streaming()  # rtmps://vzwow72-z2-prod.vz.netgear.com:80/vzmodulelive?egressToken=b723a7bb_abbXX&userAgent=web&cameraId=48AAAAA

# gather last recorded video URL
cam.last_video.video_url