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
                # Forming the conversation as a prompt with system and user messages
                conversation = f"You are a virtual doctor providing medical advice.\nPatient: {user_input}"

                response = openai.Completion.create(
                    engine="text-davinci-002",
                    prompt=conversation,
                    max_tokens=150,
                )

                gpt3_response = response["choices"][0]["text"]

                return JsonResponse({"response": gpt3_response})
            else:
                return JsonResponse({"error": "Invalid input. 'user_input' key not found."}, status=400)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON format in the request body."}, status=400)

    return JsonResponse({"error": "Invalid request. Use POST method."}, status=400)