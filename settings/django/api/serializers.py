from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, NormalUser, ProviderUser

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super(MyTokenObtainPairSerializer, cls).get_token(user)
        token['username'] = user.username
        return token

class RegisterNormalUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = CustomUser
        fields = ('rut', 'email', 'name', 'address', 'phone', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['rut'],
            email=validated_data['email'],
            name=validated_data['name'],
            address=validated_data['address'],
            phone=validated_data['phone'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class RegisterProviderUserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    business_categories = serializers.ListField(
        child=serializers.CharField(max_length=250)
    )

    class Meta:
        model = CustomUser
        fields = (
            'rut',
            'email',
            'name',
            'business_name',
            'legal_name',
            'region',
            'province',
            'commune',
            'address',
            'company_type',
            'business_categories',
            'company_size',
            'description',
            'web_url',
            'password',
            'password2',
        )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = CustomUser.objects.create(
            username=validated_data['rut'],
            email=validated_data['email'],
            name=validated_data['name'],
            business_name=validated_data['business_name'],
            legal_name=validated_data['legal_name'],
            region=validated_data['region'],
            province=validated_data['province'],
            commune=validated_data['commune'],
            address=validated_data['address'],
            company_type=validated_data['company_type'],
            company_size=validated_data['company_size'],
            description=validated_data['description'],
            web_url=validated_data.get('web_url', ''),
        )

        user.business_categories.set(validated_data['business_categories'])
        user.set_password(validated_data['password'])
        user.save()

        return user
