from rest_framework import serializers 
from concepto.models import Concepto
 
 
class ConceptoSerializer(serializers.ModelSerializer):
 
    class Meta:
        model = Concepto
        fields = ('id',
                  'titulo',
                  'descripcion',
                  'published')

