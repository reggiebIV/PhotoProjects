import piexif
from PIL import Image
import glob, os
import sys

print(sys.argv[1])

def ChangeExif(directory):    
    os.chdir(directory)
    for file in glob.glob('*.jpg'):
        image = Image.open(directory + '/' + file)
        metaDataDict = piexif.load(image.info["exif"])
        exifDict = metaDataDict.get('Exif')
        lens = exifDict.get(42036)
        lensString = lens.decode('utf-8')
        print(lensString)
        
        if lensString.find('500 mm f/4') > -1:
            lensString = 'Sigma 500mm f/4 Sport'
            lens = lensString.encode('utf-8')
            metaDataDict["Exif"][42036] = lens
            exif_bytes = piexif.dump(metaDataDict)
            if not os.path.exists(directory + '/AdjustedExif/'):
                os.makedirs(directory + '/AdjustedExif/')
            image.save(directory + '/AdjustedExif/' + file, "jpeg", exif=exif_bytes)
            
ChangeExif(sys.argv[1])