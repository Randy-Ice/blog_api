from djoser import serializers

class UserCreationSerializer(serializers.UserCreateSerializer):
    class Meta(serializers.UserCreateSerializer.Meta):
        fields = [
            'id', 'first_name', 'last_name', 'email', 'username', 'password',
        ]


class UserProfileSerializer(serializers.UserSerializer):
    class Meta(serializers.UserSerializer.Meta):
        fields = ['first_name', 'last_name', 'email' ,'username']