# -*- coding: utf-8 -*-
"""
魔搭创空间 (ModelScope Studio) 模型一键下载脚本 — WAMU_v3_WAN2.2_I2V_LIGHTNING
=====================================================================
用法（在创空间环境或 Notebook 中）:
    python download_models.py                # 下载主模型 + RIFE 权重
    python download_models.py --with-lora    # 额外预下载全部 NSFW LoRA
    python download_models.py --only-lora    # 只下载 LoRA

说明：
  - 所有下载走 hf-mirror.com 镜像，禁用 Xet 协议（HF_HUB_DISABLE_XET=1），
    规避 cas-server.xethub.hf.co 的 401 错误；
  - 主模型断点续传（snapshot_download 自动 resume）；
  - 目标目录可用环境变量覆盖：
      MODEL_DIR  （默认 /mnt/workspace/wamu_i2v/models/WAMU_v3）
      LORA_DIR   （默认 /mnt/workspace/wamu_i2v/models/loras）
  - 下载完主模型后即可直接 python app.py 启动。
"""
import os
import sys
import argparse
import zipfile

# ── 必须在 import huggingface_hub 之前设置 ──
os.environ.setdefault("HF_ENDPOINT", "https://hf-mirror.com")
os.environ.setdefault("HF_HUB_DISABLE_XET", "1")
os.environ.setdefault("HF_HUB_ENABLE_HF_TRANSFER", "0")

MODEL_DIR = os.environ.get("MODEL_DIR", "/mnt/workspace/wamu_i2v/models/WAMU_v3")
LORA_DIR = os.environ.get("LORA_DIR", "/mnt/workspace/wamu_i2v/models/loras")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RIFE_ZIP_PATH = os.path.join(BASE_DIR, "RIFEv4.26_0921.zip")
RIFE_ENTRY = os.path.join(BASE_DIR, "train_log", "RIFE_HDv3.py")

MAIN_REPO = "thornmaze/WAMU_v3_WAN2.2_I2V_LIGHTNING"
RIFE_REPO = "thornmaze/RIFE"
RIFE_FILENAME = "RIFEv4.26_0921.zip"


def download_main_model():
    from huggingface_hub import snapshot_download
    print(f"\n=== [1/3] 主模型 {MAIN_REPO}")
    print(f"    -> {MODEL_DIR}  (走 hf-mirror.com，禁用 Xet，自动断点续传)")
    os.makedirs(os.path.dirname(MODEL_DIR), exist_ok=True)
    snapshot_download(
        repo_id=MAIN_REPO,
        local_dir=MODEL_DIR,
        max_workers=8,
    )
    print("    [OK] 主模型下载完成")


def download_rife():
    from huggingface_hub import hf_hub_download
    print(f"\n=== [2/3] RIFE 插帧权重 {RIFE_REPO}/{RIFE_FILENAME}")
    if os.path.exists(RIFE_ENTRY):
        print("    [SKIP] train_log/RIFE_HDv3.py 已存在")
        return
    if not os.path.exists(RIFE_ZIP_PATH):
        print("    下载中...")
        hf_hub_download(
            repo_id=RIFE_REPO,
            filename=RIFE_FILENAME,
            local_dir=BASE_DIR,
        )
    print("    解压中...")
    with zipfile.ZipFile(RIFE_ZIP_PATH) as zf:
        zf.extractall(BASE_DIR)
    if not os.path.exists(RIFE_ENTRY):
        raise FileNotFoundError("RIFE 解压后未找到 train_log/RIFE_HDv3.py")
    print("    [OK] RIFE 权重就绪")


def download_loras():
    print(f"\n=== [3/3] NSFW LoRA 全部预下载")
    print(f"    -> {LORA_DIR}")
    sys.path.insert(0, BASE_DIR)
    import lora_loader
    ok, fail = lora_loader.download_all_loras(verbose=True)
    print(f"    [OK] LoRA 完成: {ok} 成功, {fail} 失败")


def main():
    ap = argparse.ArgumentParser(description="WAMU_v3 魔搭一键下载")
    ap.add_argument("--with-lora", action="store_true", help="同时预下载全部 NSFW LoRA")
    ap.add_argument("--only-lora", action="store_true", help="只下载 LoRA")
    args = ap.parse_args()

    if args.only_lora:
        download_loras()
        return

    download_main_model()
    download_rife()
    if args.with_lora:
        download_loras()
    else:
        print("\n=== [3/3] 跳过 LoRA（如需预下载请加 --with-lora）")

    print("\n全部完成！可直接启动: python app.py")
    print(f"  模型目录: {MODEL_DIR}")
    print(f"  LoRA目录: {LORA_DIR}（可选）")


if __name__ == "__main__":
    main()
