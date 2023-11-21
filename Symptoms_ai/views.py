
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import openai
import os
import json

openai.api_key = os.getenv("OPENAI_API_KEY")

@csrf_exempt
def gpt3_api(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
            user_input = data.get("user_input")

            if user_input:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "system", "content": "You are a helpful assistant."},
                              {"role": "user", "content": user_input}],
                )
                gpt3_response = response["choices"][0]["message"]["content"]

                return JsonResponse({"response": gpt3_response})
            else:
                return JsonResponse({"error": "Invalid input. 'user_input' key not found."}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format in the request body."}, status=400)

    return JsonResponse({"error": "Invalid request. Use POST method."}, status=400)