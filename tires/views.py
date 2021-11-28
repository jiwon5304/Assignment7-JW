from django.db                  import transaction

from rest_framework             import status
from rest_framework.exceptions  import ValidationError
from rest_framework.response    import Response
from rest_framework.viewsets    import GenericViewSet

from users.models               import User
from .serializers               import UserTireSerializer
from .models                    import UserTire, Tire
from .permissions               import CustomPermission
class UserTireViewSet(GenericViewSet):
    permission_classes = [CustomPermission]

    @transaction.atomic
    def create(self, request):
        """
        POST / users

        data body request
        - userid(required)
        - trimid(required)
        """
        if len(request.data) > 5:
            return Response({'error' : 'too many requests'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            for data in request.data:
                print(data)
                user = User.objects.get(userid=data['id'])
                tire = Tire.objects.get(trimid=data['trimId'])
                
                if  UserTire.objects.filter(user=user, tire=tire).exists():
                    raise ValidationError
                
                else: 
                    UserTire.objects.create(
                        user = user,
                        tire = tire
                    )
            return Response({'success' : 'registed'}, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({'error' : 'do not exist user'}, status=status.HTTP_400_BAD_REQUEST)

        except Tire.DoesNotExist:
            return Response({'error' : 'do not exist tire'}, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        GET / users

        data params
        - userid(required)
        """
        try:
            userid = self.request.query_params.get('id', None)
            userid = User.objects.get(userid=userid)

            queryset = UserTire.objects.filter(user=userid)
            serializer = UserTireSerializer(queryset, many=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        except User.DoesNotExist:
            return Response({'error' : 'do not exist user'}, status=status.HTTP_400_BAD_REQUEST)