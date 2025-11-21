CAN-BUS (Controller Area Network Bus)



&nbsp;CAN-BUS, mikrodenetleyiciler (örneğin sensörler, motor kontrol üniteleri, batarya yönetimi gibi cihazlar) arasında merkezî bir bilgisayara ihtiyaç duymadan veri alışverişi sağlayan bir iletişim protokolüdür.

&nbsp;Otomotiv sektöründe, özellikle elektrikli araçlarda, gerçek zamanlı veri aktarımı için kullanılır.

Çalışma Prensibi:

Her cihaz (node), verisini CAN hattına (bus) gönderir.





Veriler “ID” etiketleriyle iletilir; bu ID, mesajın önem sırasını belirler.





En düşük ID’ye sahip mesaj öncelikli olarak iletilir (bus arbitration).





Veri çakışması yaşanmaz; sistem “non-destructive arbitration” mantığıyla çalışır.

Kullanım Örneği:

&nbsp;Bir EV şarj istasyonu içinde CAN-BUS;

Akım sensörü, sıcaklık sensörü, güç modülü ve yazılım kontrol birimi arasında iletişimi sağlar.





Bit-wise (bit düzeyinde) işlemlerle çok düşük gecikmeli veri aktarımı yapar.





Avantajları:

Yüksek hız ve güvenilirlik

Hata tespiti (CRC, ACK)

Düşük maliyet ve kablolama basitliği O yüzden CAN-BUS, “akıllı” sistemlerin sinir ağı gibidir — sensörlerden gelen veriyi hızlıca merkeze ulaştırır.



