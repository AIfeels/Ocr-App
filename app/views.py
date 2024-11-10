from django.http import JsonResponse
from django.shortcuts import render
import easyocr
import boto3
from PIL import Image
import io

# Initialize the AWS Translate client
translate_client = boto3.client('translate')

# Initialize the OCR reader
reader = easyocr.Reader(['en'])  # Supports multiple languages

def extract_and_translate(request):
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        image = Image.open(uploaded_file)
        
        # Convert image to text using EasyOCR
        extracted_text = reader.readtext(image)
        extracted_text = " ".join([text[1] for text in extracted_text])
        
        # Translate the extracted text into multiple languages
        translations = {}
        languages = ['en', 'de', 'fr', 'hi', 'nl']  # Example language codes

        for lang in languages:
            response = translate_client.translate_text(
                Text=extracted_text,
                SourceLanguageCode="en",
                TargetLanguageCode=lang
            )
            translations[lang] = response['TranslatedText']
        
        # Return extracted text and translations as JSON
        return JsonResponse({
            'text': extracted_text,
            'translations': translations
        })
    return JsonResponse({'error': 'Invalid request'}, status=400)

def index(request):
    return render(request, 'index.html')  # Points to the HTML file you provided
