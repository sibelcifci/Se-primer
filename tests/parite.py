"""İkinci tüketici (Test Kahini / Oracle): aynı model.onnx'i Python'da çalıştırır.
  python tests/parite.py uret    -> tests/parite.json dosyasını (5 referans girdi + olasılık) üretir
  python tests/parite.py         -> model.onnx çıktısını parite.json ile karşılaştırır (tolerans 1e-4)"""
import json, sys
import numpy as np
import onnxruntime as ort

TOLERANS = 1e-4
# sıra: seviye, karar_no, onceki_yanlis_sayisi, ipucu_sayisi, ilk10sn_dokunma_sayisi, ilk10sn_tutor_soru_sayisi
GIRDILER = [[0, 1, 0, 1, 0, 0], [0, 2, 1, 2, 3, 0], [1, 2, 1, 0, 4, 0], [2, 3, 2, 0, 6, 0], [2, 1, 0, 0, 0, 1]]

def olasilik(girdiler):
    sess = ort.InferenceSession("model/model.onnx")
    return sess.run(None, {"girdi": np.array(girdiler, dtype=np.float32)})[1][:, 1]

if len(sys.argv) > 1 and sys.argv[1] == "uret":
    p = olasilik(GIRDILER)
    ozellikler = json.load(open("model/config.json", encoding="utf-8"))["ozellikler"]
    veri = {"ozellikler": ozellikler, "tolerans": TOLERANS,
            "olgular": [{"girdi": g, "olasilik": float(x)} for g, x in zip(GIRDILER, p)]}
    json.dump(veri, open("tests/parite.json", "w", encoding="utf-8"), indent=2)
    print("tests/parite.json yazıldı:", [round(float(x), 6) for x in p])
else:
    veri = json.load(open("tests/parite.json", encoding="utf-8"))
    p = olasilik([o["girdi"] for o in veri["olgular"]])
    hata = False
    for o, x in zip(veri["olgular"], p):
        fark = abs(float(x) - o["olasilik"])
        durum = "OK" if fark < veri["tolerans"] else "HATA"
        hata |= durum == "HATA"
        print(f"{o['girdi']} -> {float(x):.6f} (ref {o['olasilik']:.6f}) fark {fark:.1e} {durum}")
    sys.exit(1 if hata else 0)