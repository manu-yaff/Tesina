from attr import attr
from django import forms

class StaticMapForm(forms.Form):
    map_shape = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, "webkitdirectory": True, "mozdirectory": True }))
    populations_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.csv'}))
    clusters_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.bz'}))
    bounding_box_width = forms.IntegerField()
    bounding_box_height = forms.IntegerField()
    map_shape_face_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#D3D3D3"}))
    map_shape_edge_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#D3D3D3"}))
    populations_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#4682B4"}))
    clusters_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#66337f"}))

class VideoGenerationForm(forms.Form):
    map_shape = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, "webkitdirectory": True, "mozdirectory": True }))
    sim_files = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True, "webkitdirectory": True, "mozdirectory": True }))
    populations_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.csv'}))
    clusters_file = forms.FileField(widget=forms.ClearableFileInput(attrs={'accept': '.bz'}))
    bounding_box_width = forms.IntegerField()
    bounding_box_height = forms.IntegerField()
    map_shape_face_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#D3D3D3"}))
    map_shape_edge_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#D3D3D3"}))
    gene_h_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#4682B4"}))
    gene_o_color = forms.CharField(widget=forms.TextInput(attrs={"type": "color", "value": "#66337f"}))

