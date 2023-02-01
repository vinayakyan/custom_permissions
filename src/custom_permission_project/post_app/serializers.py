from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    created_by = serializers.HiddenField(default=serializers.CurrentUserDefault())
    owner = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"
    
    def get_owner(self,obj):
        return obj.created_by.username