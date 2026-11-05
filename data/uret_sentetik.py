"""Sentetik oturum üretici. Çalıştır: python data/uret_sentetik.py
Tohum: 42. Gerçek oturumlar varsa data/gercek.csv içinden okunur ve birleştirilir.
Çıktı: data/oturumlar.csv  (kaynak = gercek | sentetik)"""
import os
import numpy as np
import pandas as pd

SEED = 42
N_OTURUM = 120  # sentetik oturum sayısı (her biri 3 karar)
COLS = ["oturum_id", "kaynak", "seviye", "karar_no", "onceki_yanlis_sayisi", "ipucu_sayisi",
        "ilk10sn_dokunma_sayisi", "ilk10sn_tutor_soru_sayisi", "karar_suresi_sn", "yanlis_karar"]

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def uret():
    rng = np.random.default_rng(SEED)
    rows = []
    for i in range(N_OTURUM):
        oid = f"SNT{i:05d}"
        seviye = int(rng.integers(0, 3))
        yanlis = 0
        ipucu = 0
        for k in range(1, 4):
            if seviye == 0:
                ipucu += 1  # "Yeni başladım": her kararda ipucu görünür
            dokunma = int(rng.poisson(1.5 + 1.2 * yanlis + 0.6 * (seviye == 0)))
            tutor = int(rng.poisson(0.3 + 0.4 * (seviye == 0)))
            # Üretici kuralı: yanlış karar olasılığı bu lojistik formülle belirlenir
            z = -1.4 + 1.3 * yanlis + 0.45 * dokunma - 1.0 * tutor - 0.5 * (seviye == 2) + 0.2 * (k - 1)
            y = int(rng.random() < sigmoid(z))
            sure = round(float(rng.gamma(4 + 2 * (seviye == 0), 3.0)), 1)
            rows.append([oid, "sentetik", seviye, k, yanlis, ipucu, dokunma, tutor, sure, y])
            yanlis += y
    return pd.DataFrame(rows, columns=COLS)

if __name__ == "__main__":
    df = uret()
    if os.path.exists("data/gercek.csv"):
        g = pd.read_csv("data/gercek.csv")
        g["kaynak"] = "gercek"
        df = pd.concat([g[COLS], df], ignore_index=True)
    df.to_csv("data/oturumlar.csv", index=False)
    print(df.groupby("kaynak").agg(satir=("oturum_id", "size"), oturum=("oturum_id", "nunique")))