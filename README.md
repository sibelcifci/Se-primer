# Pod Day: Telemetri Nöbeti (SE Primer, YZM301)
Hyperloop test gününde telemetri akışı kesilir; oyuncu 3 teknik karar verir, uygulama sonucu gösterir. Telefonda oynanır.

- Uygulama linki: (AI Studio / yayın linki buraya)
- Demo video: (link buraya)
- Dosyalar: spec.md, DESIGN.md, eval.md, ai-studio-prompt.md, cypress/

## Çalıştırma
`npm install && npm run serve` (bir terminalde), `npm test` (diğerinde). Video: cypress/videos/

## Yapmadığım 3 özellik
1. **Kullanıcı hesabı:** bir haftada oyun mantığına ve tutor kalitesine odaklanmak için kapsam dışı bıraktım.
2. **Gerçek telemetri verisi:** takım verisini projeye taşımak güvenlik riski yaratırdı.
3. **İkinci senaryo:** önce tek senaryoyu ve tutor'un cevabı vermemesini doğrulamak istedim.
