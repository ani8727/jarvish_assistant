import os
import sys
import time
import webbrowser
import eel


def main():
	host = os.environ.get('HOST', 'localhost')
	port = int(os.environ.get('PORT', '8000'))
	url = f'http://{host}:{port}/index.html'

	eel.init('www')

	# -- Minimal backend functions exposed to the frontend --
	@eel.expose
	def playAssistantSound():
		"""Called from JS to indicate the assistant should play a sound or start listening.
		This minimal implementation updates the UI via exposed JS functions.
		"""
		try:
			# Show a listening message and UI state
			eel.ShowHood()
			eel.DisplayMessage('Listening...')
		except Exception:
			pass

	@eel.expose
	def allCommands(message=None):
		"""Called from JS to process a message. This minimal implementation echoes back
		a simple response so the UI shows activity. In a real assistant you'd call
		speech recognition, NLU, or other logic here.
		"""
		user_message = message or ''
		try:
			if user_message:
				# show sender message in UI
				eel.senderText(user_message)
				response = f"Assistant: I heard '{user_message}'"
			else:
				response = 'Assistant: Hello — say something!'

			# show assistant response
			eel.receiverText(response)
			# also update the displayed message
			eel.DisplayMessage(response)
			return response
		except Exception:
			return None


	# If NO_BROWSER is set (1/true), do not attempt to open a browser.
	no_browser = str(os.environ.get('NO_BROWSER', '0')).lower() in ('1', 'true', 'yes')

	try:
		if no_browser:
			# Block the main thread; useful for containers and services.
			print(f'Starting Eel server on {host}:{port} (no browser)...')
			eel.start('index.html', mode=None, host=host, port=port, block=True)
			return
		else:
			# Non-blocking start so we can open the user's default browser.
			print(f'Starting Eel server on {host}:{port} and opening browser...')
			eel.start('index.html', mode=None, host=host, port=port, block=False)
	except Exception as e:
		print('Failed to start Eel server:', e)
		sys.exit(1)

	# Give the server a moment to start
	time.sleep(0.5)

	# Try to open the user's default browser. Use os.startfile on Windows as fallback.
	try:
		webbrowser.open(url, new=1, autoraise=True)
	except Exception:
		try:
			if sys.platform.startswith('win'):
				os.startfile(url)
			else:
				print('Please open this URL in your browser:', url)
		except Exception:
			print('Please open this URL in your browser:', url)

	# Keep the main thread alive while Eel runs in background threads
	try:
		while True:
			time.sleep(1)
	except KeyboardInterrupt:
		print('\nShutting down...')


if __name__ == '__main__':
	main()