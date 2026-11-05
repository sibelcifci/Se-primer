# SINAV TASARIMI – Sizinle Uyumlanan Sınav Tasarımı

## Amaç

Bu sınavın amacı, öğrencinin yazılım testi ve makine öğrenmesi kavramlarını ezberleyip ezberlemediğini değil, gerçek bir yazılım senaryosunda bu kavramları kullanarak doğru mühendislik kararları verebilmesini ölçmektir.

## Özgün Sınav Sorusu

Bir yazılım şirketi, kullanıcıların davranışlarına göre hikâyenin zorluk seviyesini ve ipucu sıklığını değiştiren yapay zekâ destekli bir hikâye oyunu geliştirmiştir.

Sistemin önceki sürümünde kararlar sabit kurallarla verilirken yeni sürümde bu kararlar eğitilmiş bir ONNX modeli tarafından verilmektedir.

Yeni model yayına alındıktan sonra bazı kullanıcıların beklenmedik şekilde fazla ipucu aldığı, bazı kullanıcıların ise hiç ipucu alamadığı fark edilmiştir.

Yazılım mühendisi olarak bu sistemin güvenilirliğini nasıl test edersiniz?

Cevabınızda aşağıdaki durumları açıklayınız:

1. Python ortamında çalışan referans model ile uygulama içerisinde çalışan ONNX modelinin aynı girdilerde aynı sonucu verdiğini nasıl kanıtlarsınız?
2. İki sistemin sonuçları arasında küçük farklılıklar oluşursa hata toleransını nasıl belirlersiniz?
3. Yeni modelin devreye alınmasından sonra önceki oyun özelliklerinin bozulmadığını nasıl kontrol edersiniz?
4. Sistemin teknik olarak doğru çalışması ile kullanıcının gerçekten ihtiyacını karşılaması arasındaki farkı nasıl değerlendirirsiniz?
5. Yeni modeli bütün kullanıcılara açmadan önce hangi güvenli dağıtım yöntemlerini tercih edersiniz?

## Beklenen Temel Kavramlar

- **Diferansiyel Test:** Python Oracle ile uygulamadaki ONNX modelinin aynı girdilerde ürettiği sonuçların karşılaştırılması.
- **Test Kahini (Oracle):** Doğru kabul edilen referans çıktıları sağlayan sistem.
- **Hata Toleransı:** İki sistem arasındaki kabul edilebilir sayısal farkın belirlenmesi.
- **Regresyon Testi:** Yeni sürümün önceki özellikleri bozmadığının kontrol edilmesi.
- **Doğrulama (Verification):** Sistemin teknik gereksinimlere uygun geliştirilip geliştirilmediğinin incelenmesi.
- **Geçerleme (Validation):** Geliştirilen sistemin gerçek kullanıcı ihtiyacını karşılayıp karşılamadığının değerlendirilmesi.
- **Güvenli Dağıtım:** Shadow Deployment ve Canary Deployment yöntemleriyle yeni modelin kontrollü biçimde devreye alınması.

## Çeldiriciler ve Ölçülmek İstenenler

- Yalnızca modelin doğruluk oranına bakmanın yeterli olduğunu düşünmek.
- Python ve ONNX sonuçlarının karşılaştırılmasına gerek olmadığını savunmak.
- Küçük sayısal farklılıkları her durumda model hatası olarak değerlendirmek.
- Yeni sürümün yalnızca yeni özelliklerini test edip eski özellikleri göz ardı etmek.
- Teknik olarak çalışan bir sistemin mutlaka kullanıcı ihtiyacını karşıladığını varsaymak.

Bu sorular, öğrencinin kavramları birbirinden ayırabilmesini, hata durumlarını analiz edebilmesini ve gerekçeli mühendislik kararları verebilmesini ölçmeyi amaçlamaktadır.