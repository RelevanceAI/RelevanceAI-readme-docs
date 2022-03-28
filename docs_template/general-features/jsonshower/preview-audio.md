---
title: "Preview Audio"
slug: "preview-audio"
hidden: false
createdAt: "2021-11-22T04:04:32.150Z"
updatedAt: "2022-01-19T05:34:47.591Z"
---
JSONShower supports previewing audio.

You can easily preview audio data if they can be rendered in HTML. This is achievable in 1 line of code as shown below:
```python Python (SDK)
# Create audio documents
audio_documents = []
for i in range(1, 5):
 audio_documents.append({
 'audio': f'https://vecsearch-bucket.s3.us-east-2.amazonaws.com/voices/common_voice_en_{i}.wav',
 'name' : f'common_voice_en_{i}.wav',
 '_id': str(i)
 })

# Preview audio
show_json(
 audio_documents,
 audio_fields=["audio"]
)
```
```python
```
After running this, you should see the following in your Jupyter Notebook:
<figure>
<img src="https://github.com/RelevanceAI/RelevanceAI-readme-docs/blob/v2.0.0/general-features/_assets/preview_audio.png?raw=true" width="475" alt="audio.png" />
<figcaption></figcaption>
<figure>
