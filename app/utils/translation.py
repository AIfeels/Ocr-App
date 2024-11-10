import boto3

def translate_text(text, target_lang):
    translate_client = boto3.client('translate')
    response = translate_client.translate_text(Text=text, SourceLanguageCode='en', TargetLanguageCode=target_lang)
    return response['TranslatedText']