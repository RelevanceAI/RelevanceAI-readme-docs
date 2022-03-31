---
title: "Preview Audio"
slug: "preview-audio"
hidden: false
createdAt: "2021-11-22T04:04:32.150Z"
updatedAt: "2022-01-19T05:34:47.591Z"
---
JSONShower supports previewing audio.

You can easily preview audio data if they can be rendered in HTML. This is achievable in 1 line of code as shown below:

[block:code]
{
  "codes": [
    {
      "code": "from jsonshower import show_json\n\n# Create audio documents\naudio_documents = []\nfor i in range(1, 5):\n    audio_documents.append({\n    'audio': f'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/common_voice_en_{i}.wav',\n    'name' : f'common_voice_en_{i}.wav',\n    '_id': str(i)\n    })\n\n# Preview audio\nshow_json(\n    audio_documents,\n    audio_fields=[\"audio\"]\n)",
      "name": "Python (SDK)",
      "language": "python"
    }
  ]
}
[/block]

After running this, you should see the following in your Jupyter Notebook:
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/v2.0.0/docs_template/general-features/_assets/preview_audio.png?raw=true" width="475" alt="audio.png" />
<figcaption></figcaption>
<figure>

