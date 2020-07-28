from django import forms
from .models import Image_M,Image_Dimensions


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image_M
        fields = ('title', 'image','image_url')
    def Image_validate(self):
        if not self.image_url and not self.image:
            return 'false'
        else:
            return 'true'
                
class Image_DimensionsForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = Image_Dimensions
        fields = ('height', 'width')