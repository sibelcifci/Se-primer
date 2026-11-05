# RELEASE.md: pod-day-risk v2.0

## Sürüm
- **v1.0 (Hafta 1):** kural tabanlı uyum. "Yeni başladım" seviyesinde her kararda ipucu, "Deneyimliyim" seviyesinde 60 sn sayaç.
- **v2.0 (Hafta 2):** v1.0'ın üstüne model eklendi. Model, sahne açıldıktan 10 sn sonra yanlış karar olasılığını tahmin eder. Olasılık 0.5 veya üstündeyse tutor kendiliğinden yönlendirici soru sorar ve süre baskısı kalkar.

## Sabitlenmiş sürüm
Uygulama modeli `main` dalından değil, commit'e sabitlenmiş adresten indirir:

`https://huggingface.co/Sibel-55/pod-day-risk/resolve/4739eb3/model.onnx`

Commit: `4739eb3` (Hugging Face: Sibel-55/pod-day-risk). Model dosyaları: `model.onnx`, `config.json`. Metrikler ve eşikler `config.json` ve model kartındadır.

## Geri alma (rollback)
Yayında henüz v2.0'dan önceki bir model sürümü yok, bu yüzden geri dönüş noktası v1.0'daki kural tabanlı davranıştır.
1. Uygulamada `MODEL_ACIK` bayrağı `false` yapılır. Oyun model çağırmadan v1.0 gibi çalışır.
2. Model yüklenemezse (ağ hatası, bozuk dosya) uygulama otomatik olarak aynı yedeğe geçer. Bu davranış spec.md'deki M1 ve M2 kabul örnekleriyle birlikte test edilir.
3. İleride v2.1 çıkıp sorun yaratırsa linkteki commit kodu v2.0'ın kodu olan `4739eb3`'e geri çevrilir. Kod değişikliği gerekmez, yalnızca adres değişir.

## Güvenle devreye alma planı
Aşağıdakiler bir **plandır**. Bu ödevde yalnızca tek bir ortam ve çok az kullanıcı var, aşamalar uygulanmadı.

1. **Shadow (gölge dağıtım):** Model gerçek oyunlarda sessizce çalışır, olasılık hesaplanır ve kaydedilir ama oyunun davranışını değiştirmez. Kaydedilen tahminler, oyuncunun gerçekte yanlış yapıp yapmadığıyla kıyaslanır. Geçme ölçütü: doğruluk ve recall, spec.md'deki eşiklerin altına düşmemeli ve model yükleme hatası görülmemeli.
2. **Canary (kanarya):** Oyuncuların %5'inde model gerçekten tutor'u ve sayacı yönetir. İzlenenler: model yükleme hata oranı, olasılık dağılımının kayması (hep 0 ya da hep 1 çıkmamalı), tutor'un kendiliğinden devreye girme oranı ve oyuncuların oyunu yarıda bırakma oranı.
3. **Aşamalı geçiş (progressive rollout):** %25 → %50 → %100. Her aşamada belirlenen süre izlenir. Herhangi bir izleme ölçütü bozulursa bir önceki aşamaya ya da geri alma adımına dönülür.

## Mimari dağıtım kararı ve ödünleşim matrisi

| Soru | Tarayıcı (`onnxruntime-web`) | Cihaz içi mobil (React Native / Expo, gömülü ONNX) | Kendi sunucum (Render / API) |
|---|---|---|---|
| İnternet zorunlu mu, gecikme nasıl? | Model ilk açılışta bir kez iner (küçük dosya), sonra çıkarım yerelde ve hızlı. Sayfa için internet gerekir. | Model uygulamayla birlikte gelir, internetsiz çalışır, ilk indirme yok. | Her tahminde ağ gecikmesi var. İnternet ve sunucu zorunlu. Ücretsiz katman uyuyabilir. |
| Veri cihazdan çıkar mı? | Hayır. Dokunma sayısı gibi davranış verisi tarayıcıda işlenir. KVKK açısından en rahat seçeneklerden biri. | Hayır, tamamen cihazda. | Evet, davranış verisi sunucuya gider. Aydınlatma ve KVKK yükü artar. |
| Model gizli kalır mı? | Hayır. Model dosyası zaten herkese açık, kullanıcı da indirebilir. | Kısmen. Uygulamanın içinden çıkarılabilir. | Evet, model sunucuda kalır. İstek-yanıt çiftleri üzerinden tersine mühendislik yine mümkündür. |

**Seçim: tarayıcı (`onnxruntime-web`).** Gerekçeler: oyun zaten AI Studio'da web uygulaması olarak yayınlanıyor, model çok küçük, veri cihazdan çıkmıyor ve ek altyapı ya da maliyet gerekmiyor. Modelin açık olması bu projede sorun değil, çünkü içinde gizli bir şey yok ve model kartı zaten herkese açık. Telefonlu bir yarış günü senaryosunda gerçek kapsül altyapısı için cihaz içi mobil seçenek de uygun olurdu, ama bu ödevde mobil uygulama kapsam dışı.