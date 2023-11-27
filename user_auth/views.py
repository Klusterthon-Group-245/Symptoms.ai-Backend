from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from .serializers import UserSignupSerializer, UserSerializer



class SignupAPI(APIView):
    def post(self, request):
        serializer = UserSignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            login(request, user)
            return Response({'message': 'User created and logged in successfully', 'data': UserSerializer(user).data})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        user = User.objects.get(email=email)
        if user and check_password(password, user.password):
            login(request, user)
            return Response({'message': 'Login successful', 'data': UserSerializer(user).data})
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)



class ResetPasswordAPI(APIView):
    def post(self, request, user_id):
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        new_password = request.data.get('new_password')
        confirm_password = request.data.get('confirm_password')

        if new_password != confirm_password:
            return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)

        # Update user's password
        user.password = make_password(new_password)
        user.save()

        return Response({'message': 'Password reset successfully', 'data': UserSerializer(user).data})


