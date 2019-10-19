from .models import User, Organization, UserOrganization
from rest_framework import serializers

class UserOrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserOrganization
        fields = ('id', 'users', 'organizations' )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', 'first_name', 'last_name', 'address', 'phone', 'organizations' )
        # write_only_fields = ('password',)
        extra_kwargs = {'password': {'write_only': True}}

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ('id', 'name', 'address', 'phone', 'users', )
        # lookup_field = 'user_list'
        # extra_kwargs = {
        #     'url' : {'lookup_field' : 'user_list'},
        # }
