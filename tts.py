import requests

def synthesize_speech(article_text, api_key, voice_id="default_voice_id", speech_rate=1.0, stability=0.5, similarity_boost=0.5):
    """
    Calls the ElevenLabs API to synthesize speech from text.

    :param article_text: The text to convert to speech.
    :param api_key: Your ElevenLabs API key.
    :param voice_id: The ID of the voice model to use.
    :param speech_rate: The rate of the speech.
    :param stability: The stability of the generated voice.
    :param similarity_boost: The similarity boost for the voice.
    :return: A bytes object containing the synthesized audio, or None if an error occurred.
    """
    url = "https://api.elevenlabs.io/v1/text-to-speech"  # Ensure this variable is defined

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }
    data = {
        "text": article_text,
        "model_id": voice_id,
        "voice_settings": {
            "rate": speech_rate,
            "stability": stability,
            "similarity_boost": similarity_boost,
            # Add more customization options here as needed
        }
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.content
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

# Example usage
if __name__ == "__main__":
    api_key = "e4e5af9dbd21fa66875570f74585ac3e"  # Replace with your actual ElevenLabs API key
    article_text = "how are you doing?."  # The text you want to convert to speech
    voice_id = "GjNGy4eZivVYyCUBkqTL"  # Replace with your actual voice ID

    # Call the function and get the synthesized speech
    audio_content = synthesize_speech(article_text, api_key, voice_id, 1.0, 0.5, 0.5)

    # Save the audio content to a file, if it exists
    if audio_content:
        with open("output.mp3", "wb") as audio_file:
            audio_file.write(audio_content)
        print("Audio saved as output.mp3")
    else:
        print("Failed to synthesize speech.")
