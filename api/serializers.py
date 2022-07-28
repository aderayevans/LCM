from rest_framework import serializers

from api.models import Champion

class ChampionSerializer(serializers.ModelSerializer):

    class Meta: 
        model = Champion
        fields = ['name', 'sex', 'clan']

    # def validate_name(self, value):
    #     if 1 == 0:
    #         raise serializers.ValidationError("ValidationError Name")
        
    #     return value

    def create(self):
        self.__create__(self.validated_data)

    def update(self):
        self.__update__(self.instance, self.validated_data)








#=================================================================================

    def __create__(self, validated_data):
        return Champion.objects.create(**validated_data)

    def __update__(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.sex = validated_data.get('sex', instance.sex)
        instance.clan = validated_data.get('clan', instance.clan)
        instance.save()
        return instance

    # def create(self, validated_data):
    #     champion = Champion(
    #         name=validated_data['name'],
    #         sex=validated_data['sex'],
    #         clan=validated_data['clan']
    #     )
    #     champion.save()
    #     return champion