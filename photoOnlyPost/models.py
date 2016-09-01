from django.db import models
import sys, os, PIL
from PIL import Image

def photo_file_name(instance, filename):
    return '/'.join(['photos', filename])

def full_photo_file_name(instance, filename):
    return '/'.join(['full', filename])

def thumb_photo_file_name(instance, filename):
    return '/'.join(['thumbs', filename])

# Create your models here.
class PhotoPost(models.Model):
    targetThumbnailWidth = 360
    targetThumbnailHeight = 240
    targetFullWidth = 1200
    targetFullHeight = 800
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200, default='', blank=True)
    photographer = models.CharField(max_length=200, default='')
    producer = models.CharField(max_length=200, default='', blank=True)
    created = models.DateTimeField(db_index=True,auto_now_add=True)
    modified = models.DateTimeField(db_index=True, auto_now=True)
    
    category = models.ForeignKey('photoOnlyPost.Category')
    
    photo = models.ImageField(upload_to=photo_file_name)
    fullPhoto = models.ImageField(upload_to=full_photo_file_name, default='', blank=True)
    thumbnailPhoto = models.ImageField(upload_to=thumb_photo_file_name, default='', blank=True)
    autoResizeOnSave = models.BooleanField(default=False)
    
    def __unicode__(self):
        return self.slug
    
    def borderFill(self, fileName, targetWidth, targetHeight):
        old_im = Image.open(fileName)
        old_size = old_im.size
            
        new_size = (targetWidth, targetHeight)
        
        #Currently defaulted to black
        new_im = Image.new("RGB", new_size)
        
        new_im.paste(old_im, ((new_size[0]-old_size[0])/2, (new_size[1]-old_size[1])/2))
        new_im.save(fileName)
        
    def resizeImage(self, fileName, targetWidth, targetHeight, newFileName):
        img = Image.open(fileName)
        wpercent = (targetWidth/ float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        
        imgResized = img.resize((targetWidth,hsize), PIL.Image.ANTIALIAS)
        imgResized.save(newFileName)
   
        if hsize != targetHeight:
            self.borderFill(newFileName, targetWidth, targetHeight)    
        
        return str('/').join(newFileName.split('/')[-2:])
    
    def save(self, *args, **kwargs):
        super(PhotoPost, self).save(*args, **kwargs)
        
        if self.autoResizeOnSave:
            originalFileName = self.photo.file.name
            baseFileName = originalFileName.split('/')[-1]
            prefix = str('/').join(originalFileName.split('/')[0:-2])
        
            thumbFileName = self.resizeImage(originalFileName,
                                             self.targetThumbnailWidth,
                                             self.targetThumbnailHeight,
                                             prefix + '/thumbs/' + baseFileName)
     
            fullFileName = self.resizeImage(originalFileName,
                                        self.targetFullWidth,
                                        self.targetFullHeight,
                                        prefix + '/full/' + baseFileName)
        
            self.thumbnailPhoto = thumbFileName
            self.fullPhoto = fullFileName    
            super(PhotoPost, self).save(*args, **kwargs)
        

class Category(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)
    
    def __unicode__(self):
        return self.title