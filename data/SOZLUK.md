# Veri sözlüğü (`data/oturumlar.csv`)
Her satır bir karardır. Bir oyun (oturum) 3 satır üretir.

| Sütun | Anlam | Birim / değer |
|---|---|---|
| oturum_id | Rastgele üretilen oturum kimliği, kişiyle ilgisi yok | metin |
| kaynak | Verinin kaynağı | `gercek` veya `sentetik` |
| seviye | Girişte seçilen seviye | 0 Yeni başladım, 1 Orta, 2 Deneyimliyim |
| karar_no | Oyundaki karar sırası | 1, 2, 3 |
| onceki_yanlis_sayisi | Bu oturumda o karara kadar verilen yanlış karar sayısı | adet |
| ipucu_sayisi | O ana kadar gösterilen ipucu sayısı | adet |
| ilk10sn_dokunma_sayisi | Sahne açıldıktan sonraki ilk 10 sn'de ekrana dokunma sayısı (kararı veren tıklama hariç) | adet |
| ilk10sn_tutor_soru_sayisi | Aynı pencerede tutor'a sorulan soru sayısı | adet |
| karar_suresi_sn | Sahne açılışından karar anına geçen süre | saniye |
| yanlis_karar | Hedef: karar yanlışsa 1, doğruysa 0 (süre dolması = 1) | 0 / 1 |

`karar_suresi_sn` modelin girdisi değildir: tahmin 10. saniyede yapılır, o an karar süresi henüz bilinmez (sızıntı olur).
Kişisel veri (ad, e-posta, konum, cihaz kimliği) toplanmaz.