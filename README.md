# Pod Day: Telemetri Nöbeti (SE Primer, YZM301)

Hyperloop test gününde telemetri akışı kesilir. Oyuncu 3 teknik karar verir, uygulama kararın sonucunu gösterir. Seviye, rol ve hedefe göre kişiselleşir, AI tutor cevabı vermez, ipucu ve soru verir. Telefonda oynanır.

## Linkler
- Uygulama (AI Studio): [https://pod-day-telemetri-n-beti.ai.studio]
- Demo video : [https://drive.google.com/file/d/1YP-MT_bvnSKZbN2ZnQEx9_ACDYgJ0SWG/view?usp=sharing]

## Repo içeriği
- `spec.md`: problem, kapsam dışı, 5 kabul örneği, akış şeması
- `DESIGN.md` ve `tasarim/`: Stitch tasarım sistemi ve 3 ekran görseli
- `eval.md`: tutor eval (20 cevap, hata türleri, oran)
- `ai-studio-prompt.md`: AI Studio promptu ve tutor sistem promptu
- `cypress/`: E2E testleri

## Çalıştırma
`npm install`, sonra `npm test`. Video `cypress/videos/` altında oluşur.

## Yapmadığım 3 özellik
1. **Kullanıcı hesabı:** bir haftada oyun mantığına ve tutor kalitesine odaklanmak için kapsam dışı bıraktım.
2. **Gerçek telemetri verisi:** takım verisini projeye taşımak güvenlik riski yaratırdı.
3. **İkinci senaryo:** önce tek senaryoyu ve tutor'un cevabı vermemesini doğrulamak istedim.
