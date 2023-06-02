# Plugin to use gpt4 as auto gpt command
add this in .env file
```
## .env of use gpt4 plugin
## this is here because API key will hit rate limits with heavy use. you can change the key for this plugin.
OPENAI_API_KEY_PLUGIN = 
GPT_MODEL_PLUGIN = gpt4
```

## Features(more coming soon!)
- env file system better and easy to edit. 
- alert system when intering invalid model of gpt.

## Installation:
As part of the AutoGPT plugins package, follow the [installation instructions](https://github.com/Significant-Gravitas/Auto-GPT-Plugins) on the Auto-GPT-Plugins GitHub reporistory README page.

## AutoGPT Configuration
Set `ALLOWLISTED_PLUGINS=autogpt-api-tools,example-plugin1,example-plugin2,etc` in your AutoGPT `.env` file.

## Additional tips.
system input of gpt is set to "summarizing" purpose. If you edit the system, then you can make it have a differnt function.(gpt4.py chat_completion())