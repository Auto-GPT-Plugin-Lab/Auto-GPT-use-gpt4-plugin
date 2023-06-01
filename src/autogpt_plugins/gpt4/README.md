# Plugin to use gpt4 as auto gpt command
add this in .env file
```
## .env of use gpt4 plugin
## this is here because API key will hit rate limits with heavy use. you can change the key for this plugin.
OPENAI_API_KEY_PLUGIN = 
GPT_MODEL_PLUGIN = gpt4
```

## Features(more coming soon!)
<!-- 
- Convert a PDF file to a text file using the `pdf_to_txt` command
- Convert PDF files to multiple text files when too long
    - This may be useful when you want to read the converted text file with Auto-GPT, to avoid the limitation of the number of tokens -->

## Installation:
As part of the AutoGPT plugins package, follow the [installation instructions](https://github.com/Significant-Gravitas/Auto-GPT-Plugins) on the Auto-GPT-Plugins GitHub reporistory README page.

## AutoGPT Configuration
Set `ALLOWLISTED_PLUGINS=autogpt-api-tools,example-plugin1,example-plugin2,etc` in your AutoGPT `.env` file.

## Additional tips.
<!-- one chunk is set to 4000 tokens. When you use gpt-3.5 4000 maximum token, you should edit varriable "one_chunk" in pdf_to_txt.py. -->