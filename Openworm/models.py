from __future__ import unicode_literals

from django.db import models
from s3direct.fields import S3DirectField
from django.contrib.auth.models import User

## Possible field in db models
#owner = models.ForeignKey(User)

class Aspect(models.Model):
    #aspectkey = models.IntegerField(db_column='AspectKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    class Meta:
        db_table = 'Aspect'

class Bodypart(models.Model):
    #bodypartkey = models.IntegerField(db_column='BodyPartKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    startskeletonindex = models.FloatField(db_column='StartSkeletonIndex', blank=True, null=True)
    endskeletonindex = models.FloatField(db_column='EndSkeletonIndex', blank=True, null=True)
    startskeletonindexdeprecated = models.FloatField(db_column='StartSkeletonIndexDEPRECATED', blank=True, null=True)
    endskeletonindexdeprecated = models.FloatField(db_column='EndSkeletonIndexDEPRECATED', blank=True, null=True)
    class Meta:
        db_table = 'BodyPart'

class Category(models.Model):
    #categorykey = models.IntegerField(db_column='CategoryKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    class Meta:
        db_table = 'Category'

class Computervisionalgorithm(models.Model):
    #cvalgorithmkey = models.IntegerField(db_column='CVAlgorithmKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    framebyframe = models.CharField(db_column='FrameByFrame', max_length=1)
    author = models.CharField(db_column='Author', max_length=20, blank=True)
    academicpaper = models.CharField(db_column='AcademicPaper', max_length=20, blank=True)
    code = models.CharField(db_column='Code', max_length=100)
    class Meta:
        db_table = 'ComputerVisionAlgorithm'

class Direction(models.Model):
   # directionkey = models.IntegerField(db_column='DirectionKey', primary_key=True)
   def get_subclass_name(self):
        return self.__class__.__name__
    
   timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
   name = models.CharField(db_column='Name', max_length=20, blank=True)
   description = models.CharField(db_column='Description', max_length=500, blank=True)
   class Meta:
        db_table = 'Direction'

class Experimenter(models.Model):
    #experimenterkey = models.IntegerField(db_column='ExperimenterKey', primary_key=True)
    labkey = models.ForeignKey('Lab', db_column='LabKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)

    class Meta:
        db_table = 'Experimenter'

class Featuresperplatewireframe(models.Model):
    #featuresperplatewireframe = models.IntegerField(db_column='FeaturesPerPlateWireframe', primary_key=True)
    platefeaturekey = models.ForeignKey('Platefeature', db_column='PlateFeatureKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    value = models.TextField(db_column='Value', blank=True)
    platewireframevideokey = models.ForeignKey('Platewireframevideo', db_column='PlateWireframeVideoKey')
    class Meta:
        db_table = 'FeaturesPerPlateWireframe'

class Featuresperwormwireframe(models.Model):
    #featuresperwormwireframekey = models.IntegerField(db_column='FeaturesPerWormWireframeKey', primary_key=True)
    wormfeaturekey = models.ForeignKey('Wormfeature', db_column='WormFeatureKey')
    wormwireframekey = models.ForeignKey('Wormwireframevideo', db_column='WormWireframeKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    value = models.TextField(db_column='Value', blank=True)
    class Meta:
        db_table = 'FeaturesPerWormWireframe'

class Histogramsperplatewireframe(models.Model):
    #histogramsperplatewireframekey = models.IntegerField(db_column='HistogramsPerPlateWireframeKey', primary_key=True)
    platewireframevideokey = models.ForeignKey('Platewireframevideo', db_column='PlateWireframeVideoKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    bins = models.TextField(db_column='Bins', blank=True)
    counts = models.TextField(db_column='Counts', blank=True)
    class Meta:
        db_table = 'HistogramsPerPlateWireframe'

class Histogramsperwormwireframe(models.Model):
    #histogramsperwormwireframekey = models.IntegerField(db_column='HistogramsPerWormWireframeKey', primary_key=True)
    eventdirectionkey = models.ForeignKey('Direction', db_column='EventDirectionKey')
    wormfeaturekey = models.ForeignKey('Wormfeature', db_column='WormFeatureKey')
    wormwireframekey = models.ForeignKey('Wormwireframevideo', db_column='WormWireframeKey')
    signkey = models.ForeignKey('Sign', db_column='SignKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    bins = models.TextField(db_column='Bins', blank=True)
    counts = models.TextField(db_column='Counts', blank=True)
    class Meta:
        db_table = 'HistogramsPerWormWireframe'

class Lab(models.Model):
    #labkey = models.IntegerField(db_column='LabKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    address = models.CharField(db_column='Address', max_length=20, blank=True)
    class Meta:
        db_table = 'Lab'

class Measurementsperwormwireframe(models.Model):
    #measurementsperwormwireframe = models.IntegerField(db_column='MeasurementsPerWormWireframe', primary_key=True)
    wormmeasurementkey = models.ForeignKey('Wormmeasurement', db_column='WormMeasurementKey')
    wormwireframekey = models.ForeignKey('Wormwireframevideo', db_column='WormWireframeKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    value = models.TextField(db_column='Value', blank=True)
    class Meta:
        db_table = 'MeasurementsPerWormWireframe'

class Plate(models.Model):
    #platekey = models.IntegerField(db_column='PlateKey', primary_key=True)
    experimenterkey = models.ForeignKey(Experimenter, db_column='ExperimenterKey')
    wormlistkey = models.ForeignKey('Wormlist', db_column='WormListKey')
    def get_subclass_name(self):
        return self.__class__.__name__

    name = models.CharField(db_column='Name', max_length=100)
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    sampletype = models.CharField(db_column='SampleType', max_length=18, blank=True)
    startdatetime = models.DateTimeField(db_column='StartDateTime', blank=True, null=True)
    copyright = models.CharField(db_column='Copyright', max_length=20, blank=True)
    vulvaorientation = models.CharField(db_column='VulvaOrientation', max_length=20, blank=True)
    annotation = models.CharField(db_column='Annotation', max_length=20, blank=True)
    chemicals = models.CharField(db_column='Chemicals', max_length=20, blank=True)
    food = models.CharField(db_column='Food', max_length=20, blank=True)
    illumination = models.CharField(db_column='Illumination', max_length=20, blank=True)
    temperature = models.IntegerField(db_column='Temperature', blank=True, null=True)
    tracker = models.CharField(db_column='Tracker', max_length=20, blank=True)
    agarside = models.CharField(db_column='AgarSide', max_length=20, blank=True)
    gasconcentration = models.TextField(db_column='GasConcentration', blank=True)
    class Meta:
        db_table = 'Plate'

class Platefeature(models.Model):
    #platefeaturekey = models.IntegerField(db_column='PlateFeatureKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    title = models.CharField(db_column='Title', max_length=20, blank=True)
    shorttitle = models.CharField(db_column='ShortTitle', max_length=20, blank=True)
    class Meta:
        db_table = 'PlateFeature'

class Platerawvideo(models.Model):
    #platerawvideokey = models.IntegerField(db_column='PlateRawVideoKey', primary_key=True)
    platekey = models.ForeignKey(Plate, db_column='PlateKey')
    def get_subclass_name(self):
        return self.__class__.__name__

    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    title = models.CharField(db_column='Title', max_length=20, blank=True)
    shorttitle = models.CharField(db_column='ShortTitle', max_length=20, blank=True)
    videofile = S3DirectField(dest='destination_key_from_settings')
    fps = models.IntegerField(db_column='FPS', blank=True, null=True)
    numframes = models.FloatField(db_column='NumFrames', blank=True, null=True)
    width = models.IntegerField(db_column='Width', blank=True, null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    micronsperpixel = models.IntegerField(db_column='MicronsPerPixel', blank=True, null=True)
    class Meta:
        db_table = 'PlateRawVideo'

class Platewireframevideo(models.Model):
    #platewireframevideokey = models.IntegerField(db_column='PlateWireframeVideoKey', primary_key=True)
    platerawvideokey = models.ForeignKey(Platerawvideo, db_column='PlateRawVideoKey')
    cvalgorithmkey = models.ForeignKey(Computervisionalgorithm, db_column='CVAlgorithmKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    wireframevideo = models.TextField(db_column='WireframeVideo', blank=True)
    droppedframeinfo = models.TextField(db_column='DroppedFrameInfo', blank=True)
    class Meta:
        db_table = 'PlateWireframeVideo'

class Sign(models.Model):
    #signkey = models.IntegerField(db_column='SignKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    class Meta:
        db_table = 'Sign'

class Strain(models.Model):
    #strainkey = models.IntegerField(db_column='StrainKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    gene = models.CharField(db_column='Gene', max_length=20, blank=True)
    genotype = models.TextField(db_column='Genotype', blank=True)
    allele = models.CharField(db_column='Allele', max_length=20, blank=True)
    chromosome = models.CharField(db_column='Chromosome', max_length=20, blank=True)
    simulated = models.CharField(db_column='Simulated', max_length=1)
    class Meta:
        db_table = 'Strain'

class Type(models.Model):
    #typekey = models.IntegerField(db_column='TypeKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    class Meta:
        db_table = 'Type'

"""
class User(models.Model):
    #userid = models.IntegerField(db_column='UserID', primary_key=True)
    name = models.CharField(db_column='Name', max_length=20, blank=True)
    accesslevel = models.FloatField(db_column='AccessLevel', blank=True, null=True)
    labkey = models.ForeignKey(Lab, db_column='LabKey')
    class Meta:
        db_table = 'User'
"""

"""
class Videoattributes(models.Model):
    #videometadatakey = models.CharField(db_column='VideoMetadataKey', primary_key=True, max_length=18)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    fps = models.IntegerField(db_column='FPS', blank=True, null=True)
    numframes = models.FloatField(db_column='NumFrames', blank=True, null=True)
    width = models.IntegerField(db_column='Width', blank=True, null=True)
    height = models.IntegerField(db_column='Height', blank=True, null=True)
    micronsperpixel = models.IntegerField(db_column='MicronsPerPixel', blank=True, null=True)
    class Meta:
        db_table = 'VideoAttributes'
"""

class Worm(models.Model):
    #wormkey = models.IntegerField(db_column='WormKey', primary_key=True)
    strainkey = models.ForeignKey(Strain, db_column='StrainKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    sex = models.CharField(db_column='Sex', max_length=20, blank=True)
    thaweddate = models.DateTimeField(db_column='ThawedDate', blank=True, null=True)
    generationssincethawing = models.FloatField(db_column='GenerationsSinceThawing', blank=True, null=True)
    habituation = models.CharField(db_column='Habituation', max_length=20, blank=True)
    class Meta:
        db_table = 'Worm'

class Wormfeature(models.Model):
    #wormfeaturekey = models.IntegerField(db_column='WormFeatureKey', primary_key=True)
    typekey = models.ForeignKey(Type, db_column='TypeKey')
    categorykey = models.ForeignKey(Category, db_column='CategoryKey')
    directionkey = models.ForeignKey(Direction, db_column='DirectionKey')
    aspectkey = models.ForeignKey(Aspect, db_column='AspectKey')
    bodypartkey = models.ForeignKey(Bodypart, db_column='BodyPartKey')
    featureindex = models.FloatField(db_column='FeatureIndex', blank=True, null=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    title = models.CharField(db_column='Title', max_length=20, blank=True)
    shorttitle = models.CharField(db_column='ShortTitle', max_length=20, blank=True)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    bin_width = models.IntegerField(blank=True, null=True)
    is_signed = models.CharField(max_length=1)
    is_time_series = models.CharField(max_length=1)
    is_zero_bin = models.IntegerField()
    units = models.CharField(max_length=20, blank=True)
    signed_field = models.CharField(max_length=20, blank=True)
    remove_partial_events = models.CharField(max_length=1)
    make_zero_if_empty = models.CharField(max_length=1)
    name = models.CharField(db_column='Name', max_length=100)
    class Meta:
        db_table = 'WormFeature'

class Worminteraction(models.Model):
    #worminteractionkey = models.CharField(db_column='WormInteractionKey', primary_key=True, max_length=18)
    platewireframevideokey = models.ForeignKey(Platewireframevideo, db_column='PlateWireframeVideoKey')
    wormlistkey = models.ForeignKey('Wormlist', db_column='WormListKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    framebyframewormparticipation = models.TextField(db_column='FrameByFrameWormParticipation', blank=True)
    area = models.TextField(db_column='Area', blank=True)
    interactiontype = models.CharField(db_column='InteractionType', max_length=20, blank=True)
    startframe = models.FloatField(db_column='StartFrame', blank=True, null=True)
    endframe = models.FloatField(db_column='EndFrame', blank=True, null=True)
    class Meta:
        db_table = 'WormInteraction'

class Wormlist(models.Model):
    #wormlistkey = models.IntegerField(db_column='WormListKey', primary_key=True)
    wormkey = models.ForeignKey(Worm, db_column='WormKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    class Meta:
        db_table = 'WormList'

class Wormmeasurement(models.Model):
    #wormmeasurementskey = models.IntegerField(db_column='WormMeasurementsKey', primary_key=True)
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    description = models.CharField(db_column='Description', max_length=500, blank=True)
    class Meta:
        db_table = 'WormMeasurement'

class Wormwireframevideo(models.Model):
    #wormwireframekey = models.IntegerField(db_column='WormWireframeKey', primary_key=True)
    platewireframevideokey = models.ForeignKey(Platewireframevideo, db_column='PlateWireframeVideoKey')
    def get_subclass_name(self):
        return self.__class__.__name__
    
    timestamp =  models.DateTimeField(db_column="Timestamp", auto_now_add=True)
    name = models.CharField(db_column='Name', max_length=100)
    wireframevideo = models.TextField(db_column='WireframeVideo', blank=True)
    droppedframeinfo = models.TextField(db_column='DroppedFrameInfo', blank=True)
    class Meta:
        db_table = 'WormWireframeVideo'
