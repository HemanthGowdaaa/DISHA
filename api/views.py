from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate
from .models import Users
import json

@csrf_exempt
def register_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')
        phone_number = data.get('phone_number')
        role = data.get('role', 'girl')

        if Users.objects.filter(email=email).exists():
            return JsonResponse({'success': False, 'message': 'Email already exists'})

        try:
            user = Users.objects.create_user(email=email, name=name, phone_number=phone_number, password=password, role=role)
            return JsonResponse({'success': True, 'message': 'Registration successful'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})

@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email = data.get('email')
        password = data.get('password')

        try:
            user = Users.objects.get(email=email)
            if user.check_password(password):
                return JsonResponse({'success': True, 'message': 'Login successful'})
            else:
                return JsonResponse({'success': False, 'message': 'Invalid password'})
        except Users.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'User does not exist'})

    return JsonResponse({'success': False, 'message': 'Invalid request method'})



# @csrf_exempt
# def help_request(request):
#     if request.method == 'POST':
#         try:
#             data = json.loads(request.body)
#             message = data.get('message')
#             latitude = data.get('latitude')
#             longitude = data.get('longitude')
#             # You can save this data to your database or process it as needed
#             # For now, just return a success response
#             print(f"Message: {message}, Latitude: {latitude}, Longitude: {longitude}")
#             link_msg = f"https://www.google.com/maps?q={latitude},{longitude}"
#             print(link_msg)
#             return JsonResponse({
#                 'success': True,
#                 'message': 'Help request received!',
#                 'data': {
#                     'message': message,
#                     'latitude': latitude,
#                     'longitude': longitude,
#                 }
#             })
#         except Exception as e:
#             return JsonResponse({'success': False, 'error': str(e)}, status=400)
#     return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)






# # myapp/views.py
# from django.http import JsonResponse
# from .utils import send_sms

# def test_sms(request):
#     sid = send_sms("+919900871928", "Hello from Django + Twilio 🚀")
#     return JsonResponse({"message_sid": sid})


from .utils import send_sms

@csrf_exempt
def help_request(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            message = data.get('message')
            latitude = data.get('latitude')
            longitude = data.get('longitude')
            link_msg = f"https://www.google.com/maps?q={latitude},{longitude}"
            print(f"Message: {message}, Latitude: {latitude}, Longitude: {longitude}")
            print(link_msg)
            # Send SMS with the link
            sid = send_sms("+919900871928", link_msg)
            return JsonResponse({
                'success': True,
                'message': 'Help request received and SMS sent!',
                'data': {
                    'message': message,
                    'latitude': latitude,
                    'longitude': longitude,
                    'sms_sid': sid,
                }
            })
        except Exception as e:
            return JsonResponse({'success': False, 'error': str(e)}, status=400)
    return JsonResponse({'success': False, 'error': 'Invalid request method'}, status=405)



