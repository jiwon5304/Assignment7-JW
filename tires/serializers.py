from rest_framework.serializers import ModelSerializer

from .models                    import UserTire

class UserTireSerializer(ModelSerializer):

    class Meta:
        model  = UserTire
        fields = "__all__"

    def to_representation(self, instance):
        return {
            "userid"             : instance.user.userid,
            "trimid"             : instance.tire.trimid,
            "front_width"        : instance.tire.front_width,
            "front_aspect_ratio" : instance.tire.front_aspect_ratio,
            "front_wheel"        : instance.tire.front_wheel,
            "rear_width"         : instance.tire.rear_width,
            "rear_aspect_ratio"  : instance.tire.rear_aspect_ratio,
            "rear_wheel"         : instance.tire.rear_wheel,
        }
