
import openai # controller para a API do ChatGPT-3
import os # remover audios
from datetime import datetime # nome dos arquivos
from io import BytesIO # arquivos binários temporários
from gtts import gTTS # texto para voz
from speech_recognition import ( # voz para texto
	Microphone, Recognizer, UnknownValueError
) 
from playsound import playsound # play 
from credentials import API_KEY

class ChatGPT():

	def voice_to_text(self):
	
		print('Iniciando módulos...')
	
		rec = Recognizer()
	
		mic = Microphone()
	
		print('Ajustando ao ambiente...')
	
		with mic as source:
	
			rec.adjust_for_ambient_noise(source)
				
			print('Ouvindo...')
	
			audio = rec.listen(source)
	
		try:
			
			print('Fazendo o reconhecimento da fala...')
	
			text = rec.recognize_google(audio, language = 'pt-BR')
			
			return text.capitalize()
		
		except UnknownValueError:
			
			pass
	
	def text_to_voice(self, text):
	
		print('Convertendo texto em fala...')
	
		tts = gTTS(text, lang='pt', tld='com.br', slow = False)
	
		filename = str(int(datetime.now().timestamp()))

		tts.save(f'{filename}.mp3')
	
		playsound(f'{filename}.mp3')

		os.remove(f'{filename}.mp3')
	
	def chat_gpt_conv(self, prompt, n_tokens, api_key):
	
		openai.api_key = api_key
		
		print('Pensando...')

		response = openai.Completion.create(
			model = 'text-davinci-003',
			prompt = prompt,
			temperature = 0,
			max_tokens = n_tokens,
			top_p = 1,
			frequency_penalty = 0.0,
			presence_penalty = 0.0,
		)
	
		return response['choices'][0]['text']

	def run(self):

		while True:

			try:

				prompt = self.voice_to_text()

			except:	

				print('Um erro desconhecido afetou o reconhecimento de voz.')

			if prompt == 'Cancelar':
	
				break
	
			elif prompt is not None:
		
				response = self.chat_gpt_conv(
					prompt = prompt,
					api_key = API_KEY,
					n_tokens = 4000
				)

				self.text_to_voice(
					response
				)
