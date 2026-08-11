# Wan-2.2-I2V-14B-Lightning-NSFW-CAN_AMD
The original files come from the Hugging Face project (open source); after being modified using AI models such as deepseekflash0731 and GLM5.2, they have been adapted for AMD GPUs. Of course, there are still many issues with them. As for the licence, I will add it in the future.
-
# Wan2.2 I2V – AMD GPU Optimised Version

This project is a modified and adapted derivative of the open-source project [cinderholm/wan2-2-i2v-v3] (https://huggingface.co/spaces/cinderholm/wan2-2-i2v-v3) on Hugging Face. Its primary objective is to port the original project to run on **AMD GPUs** and to utilise ROCm to accelerate image-to-video (I2V) tasks.
---

## ⚠️ Important Notice

**This project is a derivative work of the original and must comply with the provisions of the upstream licence.**

- **Original project**: [cinderholm/wan2-2-i2v-v3](https://huggingface.co/spaces/cinderholm/wan2-2-i2v-v3) (Hugging Face Space)
- **Original licence**: Apache-2.0
- **This project’s licence**: **Apache-2.0** (see the [LICENSE](LICENSE) file for details)
- Please note: This project has been specifically optimised for the ‘modelscope’ server domain; running it on a server with a different domain name or IP address may result in errors. Please modify the script yourself before use. This project does not include model files.
- Note: Due to the lack of FP8 quantisation support in AMDGPU, this project will run at full capacity and consume a significant amount of the device’s graphics memory. It is recommended that devices equipped with an AMD graphics card and at least 80Gb of graphics memory attempt to run this project.

### Modification Notes

- This project has undergone code refactoring and adaptation with the assistance of AI-assisted tools (including, but not limited to, DeepSeek-Flash-0731 and GLM-5.2).
- Main modifications:
  - Replaced CUDA-dependent parts of the original project with **ROCm**-compatible implementations.
  - Adjusted the model loading and inference processes to ensure better compatibility with AMD Instinct or Radeon series graphics cards.
  - Optimised memory usage to accommodate the video memory architecture of AMD GPUs.
- **Current Status**: This project remains in the **experimental stage** and may contain unknown bugs, performance instability or compatibility issues. Testing and feedback are welcome, but please do not use this in a production environment.

---

## ✨ Key Features

- ✅ Retains the core functionality of the original project: image-to-video generation
- ✅ Preliminary adaptation for AMD GPUs (ROCm 5.x / 6.x)
- ✅ Retains the original project’s Gradio interface for a quick and easy experience
- ✅ Maintains compatibility with the PyTorch ecosystem as much as possible to minimise changes to usage habits

---

## 📦 System Requirements

- **Operating System**: Linux (Ubuntu 20.04+ recommended); Windows/WSL2 may also work
- **GPU**: AMD GPUs that support ROCm (e.g. Instinct MI series, Radeon RX 6000/7000 series)
- **ROCm version**: 5.7 or higher recommended
- **Python**: 3.9 – 3.11
- **PyTorch**: ROCm version (`torch` and `torchvision` must be installed from the official AMD repository)

---

## 🚀 Installation Guide

```bash
# 1. Clone the repository
git clone https://github.com/iaoz92/Wan-2.2-I2V-14B-Lightning-NSFW-CAN_AMD.git
cd Wan-2.2-I2V-14B-Lightning-NSFW-CAN_AMD

# 2. Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or venv\Scripts\activate  # Windows

# 3. Install the ROCm version of PyTorch (please select according to your ROCm version)
pip install torch torchvision --index-url https://download.pytorch.org/whl/rocm5.7

# 4. Install other dependencies
pip install -r requirements.txt

The End
