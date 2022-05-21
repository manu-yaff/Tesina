from attr import attr
from django import forms

class StaticMapForm(forms.Form):
    map_shape = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    populations_file = forms.FileField()
    clusters_file = forms.FileField()
    bounding_box_width = forms.IntegerField()
    bounding_box_height = forms.IntegerField()
    map_shape_face_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    map_shape_edge_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    populations_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    clusters_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))

class VideoGenerationForm(forms.Form):
    map_shape = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    populations_file = forms.FileField()
    clusters_file = forms.FileField()
    bounding_box_width = forms.IntegerField()
    bounding_box_height = forms.IntegerField()
    map_shape_face_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    map_shape_edge_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    gene_o_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))
    gene_p_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color"}))

