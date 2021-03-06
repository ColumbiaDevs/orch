# events/member_specs.py

from imagekit.specs import ImageSpec
from imagekit import processors

class ResizeThumb(processors.Resize):
	width = 225
	height = 290
	crop = True
	
class ResizeDisplay(processors.Resize):
    width = 400
    height = 300
	
class EnchanceThumb(processors.Adjustment):
	sharpness = 1.2
	
class EnchanceDisplay(processors.Adjustment):
	sharpness = 1.2
	
class Thumbnail(ImageSpec):
	access_as = 'thumb'
	pre_cache = True
	processors = [ResizeThumb, EnchanceThumb]
	
class Display(ImageSpec):
	increment_count = True
	processors = [ResizeDisplay, EnchanceDisplay]
