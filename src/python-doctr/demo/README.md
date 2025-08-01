---
title: docTR
emoji: 📑
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: apache-2.0
---

## Configuration

`title`: _string_
Display title for the Space

`emoji`: _string_
Space emoji (emoji-only character allowed)

`colorFrom`: _string_
Color for Thumbnail gradient (red, yellow, green, blue, indigo, purple, pink, gray)

`colorTo`: _string_
Color for Thumbnail gradient (red, yellow, green, blue, indigo, purple, pink, gray)

`sdk`: _string_
Can be either `gradio` or `streamlit`

`sdk_version` : _string_
Only applicable for `streamlit` SDK.
See [doc](https://hf.co/docs/hub/spaces) for more info on supported versions.

`app_file`: _string_
Path to your main application file (which contains either `gradio` or `streamlit` Python code).
Path is relative to the root of the repository.

`pinned`: _boolean_
Whether the Space stays on top of your list.

## Run the demo locally

```bash
cd demo
pip install -r pt-requirements.txt
streamlit run app.py
```
