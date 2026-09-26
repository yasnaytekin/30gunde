#!/usr/bin/env bash
# Seslendirme modellerini indirir (sherpa-onnx sürümleri, GitHub). Bir kez çalıştırmak yeter.
#   bash modelleri-indir.sh            # Türkçe (Piper fettah) + İngilizce (Kokoro)
#   bash modelleri-indir.sh kontrol    # + Whisper small (ses-kontrol.py için, ~1,3 GB)
set -euo pipefail
cd "$(dirname "$0")"
mkdir -p modeller && cd modeller
URL=https://github.com/k2-fsa/sherpa-onnx/releases/download
al() { [ -d "$2" ] || { echo "indiriliyor: $2"; curl -sSL "$URL/$1/$2.tar.bz2" | tar xj; }; }
al tts-models vits-piper-tr_TR-fettah-medium
al tts-models kokoro-en-v0_19
[ "${1:-}" = kontrol ] && al asr-models sherpa-onnx-whisper-small
echo "modeller hazır: $(pwd)"
