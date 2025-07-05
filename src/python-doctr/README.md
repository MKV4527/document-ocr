---
title: AI Powered Document OCR Platform
emoji: 🧠
colorFrom: purple
colorTo: pink
sdk: streamlit
sdk_version: 1.39.0
app_file: app.py
pinned: false
license: apache-2.0
---

# 🧠 AI Powered Document OCR Platform

<p align="center">
  <b>Seamless, high-accuracy OCR for documents and images — powered by deep learning.</b>
</p>

---

## 🚀 What This Project Offers

- ⚡ Pretrained models for fast and accurate OCR
- 📄 Support for both image and PDF input formats
- 🧱 Modular architecture with clear separation of detection and recognition
- 🖼️ Built-in visualization for easy result inspection
- 🧪 Key Information Extraction (KIE) for structured field-level data

---

## 🧠 Model Architectures

### 🔍 Text Detection

These models detect text areas in the document:

- **DBNet** — Real-time scene text detection with differentiable binarization
- **LinkNet** — Lightweight semantic segmentation for fast inference
- **FAST** — Efficient detector for arbitrarily-shaped text

### 🔤 Text Recognition

These models recognize characters from detected text regions:

- **CRNN** — Convolutional recurrent model for sequence prediction
- **SAR** — Attention-based "Show, Attend and Read" recognizer
- **MASTER** — Multi-aspect attention network for irregular text

- **ViTSTR** — Vision Transformer for efficient recognition
- **PARSeq** — Permuted autoregressive model
- **VIPTR** — Vision Permutable Extractor with fast decoding

---

## 🧪 Key Information Extraction (KIE)

KIE models enable field-specific data extraction by allowing multi-class detection (e.g. only detect names, dates, or amounts).

---

## 🧪 Run the Demo Locally

To run the Streamlit demo on your local machine:

```bash
cd demo
pip install -r pt-requirements.txt
streamlit run app.py
