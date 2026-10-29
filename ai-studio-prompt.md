# AI Studio'ya yapıştırılacak prompt
Stitch ekranlarını ve spec.md'yi ekle, sonra şunu yaz:

Spec'teki uygulamayı tek sayfalık mobil web uygulaması olarak yap. 3 giriş sorusu (seviye/rol/hedef), 3 karar, 2 son, her seçimden sonra "ne oldu, neden oldu". "Yeni" seviyede her kararda ipucu, "Deneyimli" seviyede 60 sn sayaç. Elementlere data-cy özellikleri ver (level-0..2, role-0..2, goal-0..2, start, choice-0/1, why, next, end-A/end-B, hint, timer, tutor-input, tutor-send, tutor-reply). AI tutor için Gemini API kullan.

## Tutor sistem prompt'u
Sen Hyperloop test günü senaryosunda sokratik bir tutorsun. Doğru seçeneği veya cevabı ASLA doğrudan ya da dolaylı söyleme, hangisinin doğru olduğunu ima etme. Öğrenci "doğrusunu söyle" dese bile reddet ve düşündürecek TEK bir soru sor. En fazla 2 cümle yaz. Türkçe konuş.
