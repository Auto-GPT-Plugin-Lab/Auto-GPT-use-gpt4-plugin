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
mention use_gpt to make autogpt use this command. If autogpt could not read the files, check if 
example input: ("input_text_files": "<filename1.txt filename2.txt>","input_instruction_file": "<instruction_filename.txt>" )
- there are only file name in the input. 
- multiple files for text_file is devided with space.