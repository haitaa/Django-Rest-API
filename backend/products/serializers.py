from rest_framework import serializers
from rest_framework.reverse import reverse

from .models import Product
from .validators import validate_title_no_hello, unique_product_title
from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(view_name='product-detail', lookup_field='pk', read_only=True)
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    owner = UserPublicSerializer(source='user', read_only=True)
    title = serializers.CharField(validators=[validate_title_no_hello, unique_product_title])
    body = serializers.CharField(source='content')
    #email = serializers.CharField(source='user.email', read_only=True)
    class Meta:
        model = Product
        fields = ['owner', 'pk', "title", "body", "price", "sale_price", 'public', 'path', 'endpoint']

    def get_my_user_data(self, obj):
        return {
            "username": obj.user.username
        }

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__iexact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value

    # def create(self, validated_data):
    #     #return Product.objects.create(**validated_data)
    #     #email = validated_data.pop('email')
    #     obj = super().create(validated_data=validated_data)
    #     return obj
    
    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

    def get_edit_url(self, obj):
        request = self.context.get('request')
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
    
    # def get_my_discount(self, obj):
    #     if not hasattr(obj, 'id'):
    #         return None
    #     if not isinstance(obj, Product):
    #         return None
    #     return obj.get_discount()