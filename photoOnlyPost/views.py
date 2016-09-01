from django.shortcuts import render
import random
from . import models

# Create your views here.
def getRandomPosts(sampleSize):
    totalPostCount = models.PhotoPost.objects.count()
    
    if sampleSize < totalPostCount:
        numSamples = sampleSize
    else:
        numSamples = totalPostCount
        

    postIds = models.PhotoPost.objects.values_list('id',flat=True)
    rand_ids = random.sample(postIds, numSamples)
    
    randomizedPosts = list(models.PhotoPost.objects.filter(id__in=rand_ids))
    random.shuffle(randomizedPosts)
    
    return randomizedPosts

#def addNewPhoto(request):
