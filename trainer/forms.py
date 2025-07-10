from django import forms

SOIL_TYPES = [
    ('argile', 'Argile'),
    ('argile_sableuse', 'Argile Sableuse'),
    ('limons', 'Limons'),
    ('marne', 'Marne'),
    ('limon_argileux', 'Limon Argileux'),
    ('limon_sableux', 'Limon Sableux'),
    ('sable', 'Sable'),
]

class TrainingForm(forms.Form):
    soil_type = forms.ChoiceField(label="Nature du sol", choices=SOIL_TYPES)

    pd = forms.FloatField(label="pd", min_value=0.0, max_value=3.0, initial=1.8)
    w = forms.FloatField(label="w (%)", min_value=0.0, max_value=100.0, initial=20.0)
    FC = forms.FloatField(label="FC (%)", min_value=0.0, max_value=100.0, initial=30.0)
    WL = forms.FloatField(label="WL", min_value=0.0, max_value=100.0, initial=40.0)
    Ip = forms.FloatField(label="Ip", min_value=0.0, max_value=100.0, initial=15.0)