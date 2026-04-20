# Run LLM Model Locally


### Install ollama 
> Visit ``https:ollama.com``

1. Copy command `` irm https://ollama.com/install.ps1 | iex ``
if you connection is fast and stable, 
2.   Or Click Download for windows or ``https://ollama.com/download/OllamaSetup.exe``

### Verify Download 

1. Go to CMD or PowerShell using Win+R then type cmd and hit enter
or Simple search for CMD in apps

2.  Run `` ollama --version ``
> if it prints version then you may proceed


### Install or pull a model 

1. `` ollama pull llama3 ``
>  8B parameters
> Good quality responses
> Slower on CPU
> Popular default choice

2. `` ollama pull mistral ``
> Slightly heavier than Gemma 2B
> Much smarter than tiny models
> Sweet spot for most people
3. `` ollama pull gemma ``
> 2B = very light
> 7B = still manageable
> Balanced performance
4. `` ollama pull phi ``
> ~2B–4B parameters Very fast
> Lower intelligence, but decent for basics

> [!note]
> Smaller Model less Ram usage 
> Bigger Model better output more RAM usage 
> 👉 If your system is weak → pick Phi or Gemma 2B
> 👉 If you want usable intelligence → Mistral 7B

| Model         | Weight        | Speed        | Intelligence |
|--------------|--------------|--------------|--------------|
| Phi          | Very Light 🪶 | Very Fast ⚡  | Basic 🤏     |
| Gemma 2B     | Light 🪶      | Fast ⚡       | Decent 👍    |
| Mistral 7B   | Medium ⚖️     | Balanced 🚶   | Good 🔥      |
| Llama 3 8B   | Medium+ ⚖️    | Slower 🐢     | Better 🔥🔥   |
| 30B+ Models  | Heavy 🧱      | Very Slow 🐌 | Strong 🧠    |


### Run Model 
> `` ollama run llama3`` 



#### Now what you  see 
`` >>> Hello ``

> Ask what you want , Wait for Response 


### Visions 
1. Run with API
2. Use with programming language or code ( python )
3. Local chatbot UI
4. API wrapper
5. Personal knowledge base (RAG system)
6. Code assistant for your DSA grind


### How to delete Models 

#### Delete a model in Ollama
1. Step 1: See what you’ve hoarded
``ollama list``
> This shows all installed models

2. `` ollama rm model_name ``
> Model will ve removed 
3. Step 3: Verify it’s gone
> ``  ollama list ''

