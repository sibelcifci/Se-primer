"""Tek komut: python train.py
Sabit tohum (42). Eşik altındaysa hata verip durur, model/ içine hiçbir şey yazılmaz."""
import json, sys
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import StratifiedGroupKFold, cross_val_predict
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, recall_score

SEED = 42
ESIK_DOGRULUK, ESIK_RECALL, ESIK_ONNX_FARK = 0.70, 0.60, 1e-4  # spec.md ile aynı, eğitimden ÖNCE yazıldı
OZELLIKLER = ["seviye", "karar_no", "onceki_yanlis_sayisi", "ipucu_sayisi",
              "ilk10sn_dokunma_sayisi", "ilk10sn_tutor_soru_sayisi"]
HEDEF = "yanlis_karar"
ETIKETLER = ["dogru_karar", "yanlis_karar"]

df = pd.read_csv("data/oturumlar.csv")
X = df[OZELLIKLER].to_numpy(dtype=np.float32)
y = df[HEDEF].to_numpy()
gruplar = df["oturum_id"].to_numpy()

model = make_pipeline(StandardScaler(), LogisticRegression(random_state=SEED, max_iter=1000, class_weight="balanced"))
cv = StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEED)  # aynı oturum iki tarafa düşmez
tahmin = cross_val_predict(model, X, y, cv=cv, groups=gruplar)
dogruluk = float(accuracy_score(y, tahmin))
recall = float(recall_score(y, tahmin, pos_label=1))
taban = float(max(y.mean(), 1 - y.mean()))
print(f"Satır: {len(df)} | oturum: {df.oturum_id.nunique()} | gerçek satır: {(df.kaynak == 'gercek').sum()}")
print(f"Doğruluk: {dogruluk:.3f} (eşik {ESIK_DOGRULUK}) | recall: {recall:.3f} (eşik {ESIK_RECALL}) | en sık sınıf tabanı: {taban:.3f}")

if dogruluk < ESIK_DOGRULUK or recall < ESIK_RECALL:
    sys.exit("EVAL KAPISI: eşik sağlanmadı, model yayınlanmadı. Eşiği düşürme; veriyi/özellikleri gözden geçir.")

model.fit(X, y)

from skl2onnx import convert_sklearn
from skl2onnx.common.data_types import FloatTensorType
import onnxruntime as ort

onx = convert_sklearn(model, initial_types=[("girdi", FloatTensorType([None, len(OZELLIKLER)]))],
                      options={id(model.steps[-1][1]): {"zipmap": False}}, target_opset=17)
sess = ort.InferenceSession(onx.SerializeToString())
onnx_p = sess.run(None, {"girdi": X})[1][:, 1]
sk_p = model.predict_proba(X)[:, 1]
fark = float(np.max(np.abs(onnx_p - sk_p)))
print(f"ONNX - sklearn en büyük fark: {fark:.2e} (eşik {ESIK_ONNX_FARK})")
if fark > ESIK_ONNX_FARK:
    sys.exit("EVAL KAPISI: ONNX farkı eşiği aştı, model yayınlanmadı.")

with open("model/model.onnx", "wb") as f:
    f.write(onx.SerializeToString())
config = {
    "versiyon": "v2.0",
    "ozellikler": OZELLIKLER,           # sıra sözleşmenin parçasıdır
    "girdi_adi": "girdi", "girdi_tipi": "float32",
    "cikti": "olasilik[:,1] = yanlis_karar olasılığı",
    "siniflar": ETIKETLER,
    "risk_esigi": 0.5,
    "metrikler": {"dogruluk": round(dogruluk, 4), "recall_yanlis_karar": round(recall, 4),
                  "taban_dogruluk": round(taban, 4), "onnx_sklearn_max_fark": fark,
                  "cv": "5-kat StratifiedGroupKFold (oturuma göre)", "satir": int(len(df)),
                  "gercek_satir": int((df.kaynak == "gercek").sum())},
    "esikler": {"dogruluk": ESIK_DOGRULUK, "recall": ESIK_RECALL, "onnx_fark": ESIK_ONNX_FARK},
    "random_state": SEED,
}
with open("model/config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, ensure_ascii=False, indent=2)
print("Model yayınlanabilir: model/model.onnx, model/config.json yazıldı.")