# ChatGPT conectado ao Microfone do Windows

### Compilação

Você pode compilar o código utilizando a biblioteca [PyInstaller](https://github.com/pyinstaller/pyinstaller):

```
pip install pyinstaller

pyinstaller -F bot.py
```

### Usage

```
python bot.py
```

#### Código

```{python}
import chatgpt

bot = chatgpt.ChatGPT()
	
bot.run()
```
