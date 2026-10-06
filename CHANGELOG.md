# MerQur — Sürüm Notları

**MerQur — Bütünleşik Akademik Veri Analizi ve Raporlama Platformu**

> English: [CHANGELOG.en.md](CHANGELOG.en.md)

---

## [1.0.24] — 6 Ekim 2026 · **macOS Açılış Düzeltmesi ve Yeni Örnek Veri Setleri**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

macOS'ta lisans sözleşmesi kabul edildikten sonra programın açılmaması giderildi: ayarlar
artık kullanıcı veri klasöründe tutuluyor, böylece Windows'ta güncellemeden sonra ayarların
sıfırlanması da sona erdi. Örnek veri paketlerine yeni analizler için her alana özgü 15 veri
seti eklendi. Türkçe raporlarda bazı güven aralığı etiketleri düzeltildi.

---

## [1.0.23] — 5 Ekim 2026 · **Daha Sıkı Arayüz ve Doğruluk Düzeltmeleri**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

Arayüz daha sıkı hâle getirildi: seçim kutuları, açılır listeler ve yazılar küçültüldü,
gereksiz kaydırma çubukları kaldırıldı. Harita sekmesindeki iç içe geçen parametreler
düzeltildi. ANCOVA artık varsayılan olarak SPSS/SAS ile aynı Type III kareler toplamını
kullanıyor. Karma modeller, çoklu atama, Mann-Kendall ve mekânsal komşuluk
hesaplarında doğruluk düzeltmeleri yapıldı; seçilen anlamlılık düzeyi daha fazla
analizde dikkate alınıyor.

---

## [1.0.22] — 5 Ekim 2026 · **IRT, Gizil Sınıf, Ekonometri ve Analiz Betikleri**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

Yeni analizler: madde tepki kuramı ve Rasch, gizil sınıf ve gizil profil analizi,
panel veri, araç değişken, eğilim skoru ve fark-içinde-fark, VAR, eşbütünleşme ve GARCH,
karar ağacı ve yapay sinir ağı. Analizler betik olarak kaydedilip yeniden
çalıştırılabiliyor. Yardım belgesi üç dilde güncellendi. Yeni çıktılar R ile doğrulandı.

---

## [1.0.21] — 5 Ekim 2026 · **Meta-Analiz, Tam SEM ve Kriging**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

Yeni analizler: meta-analiz, tam yapısal eşitlik modeli (ölçme değişmezliği ve FIML ile)
ve variogram + kriging. Güç analizi G*Power düzeyine genişletildi; karma modellere hata
kovaryans yapıları, tekrarlı ölçüm ANOVA'ya çok faktörlü desen eklendi. Yeni çıktılar R ile
doğrulandı. Bazı analizlerin varsayılan yöntemi SPSS, R ve SAS ile aynı olacak şekilde
güncellendi; bu analizlerde sonuçlar önceki sürümden farklı olabilir, eski yöntemler
seçenek olarak duruyor. Kurulum güncellemesi sağlamlaştırıldı.

---

## [1.0.20] — 5 Ekim 2026 · **Profesyonel Analiz Seçenekleri Güncellemesi**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

SPSS, R ve SAS'ta bulunan çok sayıda analiz seçeneği, ön kontrol ve çıktı eklendi;
yeni çıktılar R ile doğrulandı. Bazı hesaplama hataları düzeltildi, İngilizce ve
İspanyolca arayüzde regresyon analizindeki çökme giderildi, arayüz kararlılığı artırıldı.

---

## [1.0.19] — 4 Ekim 2026 · **İstatistiksel Doğruluk Güncellemesi**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

Analizler IBM SPSS Statistics 27 ve R 4.5 ile karşılaştırmalı olarak doğrulandı;
bulunan hesaplama ve raporlama farkları giderildi. Genelleştirilmiş karma
modellere (GLMM) en çok olabilirlik (ML, adaptif Gauss-Hermite) tahmini eklendi.

---

## [1.0.18] — 28 Eylül 2026 · **AI Yorumlayıcı + Çok Dillilik Sertleştirmesi**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

### ✨ Yeni — AI Yorumlayıcı
Rapor çıktılarındaki akademik yorumu (Bulgular / Yorum / Sınırlılıklar) bir dil
modeline yazdırma seçeneği eklendi. **Varsayılan olarak KAPALIDIR**; açılmadığı
sürece MerQur önceki sürümlerdeki gibi tamamen çevrimdışı çalışır.

- **Ham veri gönderilmez.** Yalnızca zaten hesaplanmış istatistik özeti
  (analiz adı, n, değişken adları, t/F/p/R² gibi değerler) gönderilir; veri
  setinin satırları, hücre değerleri, dosya yolları ve grafikleri gönderilmez.
- **Sayı denetimi.** Modelin yazdığı her sayı, analiz çıktısına karşı otomatik
  doğrulanır. Kaynakta bulunmayan bir değer varsa yorum tümüyle reddedilir ve
  MerQur'un kural tabanlı yorumu kullanılır. Yani model hesap yapmaz, yalnızca
  verilen sayıların etrafına cümle kurar.
- **Açık rıza.** İlk açılışta, gönderilecek içeriğin tamamını gösteren bir onay
  penceresi çıkar; onaylanmadan hiçbir istek gönderilmez.
- **Akademik bildirim.** AI ile yazılan her yorumun sonuna, dil modeli desteğiyle
  oluşturulduğunu belirten cümle otomatik eklenir.
- **Sağlayıcılar:** Claude (Anthropic), NVIDIA NIM (ücretsiz kotalı) ve DeepSeek.
  Kullanıcı kendi API anahtarını girer; anahtar işletim sisteminin kimlik
  kasasında saklanır, düz metin dosyada tutulmaz.
- İsteğe bağlı **değişken adı maskeleme** (V1, V2 …) — adların kendisi hassas
  bilgi taşıyorsa.

- **Kapsam uyarısı.** AI yorumunun yalnızca fikir vermek amacıyla sunulduğu,
  bilimsel değerlendirme ya da hakem görüşü yerine geçmediği ve kontrol
  edilmeden olduğu gibi kabul edilmemesi gerektiği; hem onay penceresinde,
  hem üretilen yorumun sonunda, hem de yardım belgesinde açıkça belirtilir.

### ✨ Yeni — Yorumu Önizle
Rapor panelinde, işaretli tek kartın akademik yorumunu rapor üretmeden gösteren
düğme. Yorumu hangi motorun (AI / kural tabanlı) ve hangi modelin yazdığını
bildirir, panoya kopyalanabilir.

### 🔧 İyileştirildi
- **Rapor ilerleme göstergesi:** çubuk büyütüldü, sayaç ve durum yazısı eklendi
  ("Yapay zekâ yorumları yazılıyor — 3 / 12 kart", ardından "Rapor dosyası
  yazılıyor").
- **Model yedeklenme zinciri:** sağlayıcıda bir model kaldırılmış veya doluysa
  (404/410/503/zaman aşımı) sıradaki model otomatik denenir. Anahtar ve kota
  hataları zinciri kırar.
- **Modelleri yenile** düğmesi: sağlayıcının güncel model listesini indirir.
- Sağlayıcı hata mesajları anlaşılır hâle getirildi; örneğin Claude API bakiyesi
  yetersizken artık ham hata kodu yerine, Claude.ai/Max aboneliğinin API
  kullanımını kapsamadığını açıklayan bir uyarı gösterilir.
- Ayarlar kaydedilirken, ayar panelinde karşılığı olmayan anahtarların
  korunması sağlandı.

### 🌍 Çok dillilik — kapsamlı sertleştirme
İngilizce ve İspanyolca arayüzde yer yer Türkçe metin göründüğü bildirilmişti.
Bu sürümde uygulamanın **tamamı** tarandı ve kullanıcıya görünen Türkçe
kalıntıların hepsi giderildi.

- **Analiz yardım metinleri:** 39 analizin ⓘ açıklaması (amaç / varsayım /
  yorum) İngilizce ve İspanyolca arayüzde Türkçe çıkıyordu — 117 paragraf
  çevrildi.
- **Analiz çıktıları:** tablo başlıkları, künye satırları, rapor gövdesi ve
  grafik etiketleri.
- **Hata ve uyarı mesajları:** 227 mesaj kalıbı üç dile taşındı.
- **Arayüz:** Veri, Analiz, Harita, Rapor ve Araçlar sekmelerinin tamamı;
  veri hazırlama diyalogları (Eksik Değer, Dönüştür, Sütun Ekle, Bul/Değiştir,
  Sütun Özeti, Bileşik Skor, Fotoğraf İçe Aktar).
- **Rapor çıktısı:** Excel sayfa adları, PDF/DOCX/HTML başlıkları ve —en
  önemlisi— **akademik yorum metninin tamamı** (Bulgular / Yorum /
  Sınırlılıklar). Önceden İngilizce bir raporda tam Türkçe akademik paragraf
  yer alabiliyordu.
- **Harita:** hotspot ve LISA lejantları, mekansal analiz uyarıları.

> Türkçe arayüz aynen korundu. Kullanıcının **kendi verisindeki** Türkçe
> değerler (sütun adları, kategori etiketleri) hiçbir şekilde çevrilmez —
> sıralı (ordinal) değişken tanıma ve kimlik sütunu sezgileri bu değerlere
> dayandığı için bilinçli olarak dokunulmadı.

### 🐞 Düzeltildi
- **CFA / SEM** analizinin ⓘ yardım metni hiçbir dilde görünmüyordu.
- **Kanonik Korelasyon (CCA)** frekans tablosu İngilizce ve İspanyolca
  arayüzde düzgün birleşmiyordu.
- Bir analiz çalıştırıldıktan **sonra** arayüz dili değiştirildiğinde
  Anomali Tespiti, Çapraz Random Karma Model ve Değişken Kümeleme hata
  veriyordu; Ridge/Lasso katsayı grafiği de aynı sebeple çiziliyordu.
- **GAM**, **Diskriminant** ve **Robust Regresyon** panellerinde açılır
  listeden yapılan seçim İngilizce/İspanyolca arayüzde tanınmıyor, sessizce
  varsayılana düşüyordu.
- Rapor dışa aktarımında ve Sütun Ekle penceresinde oluşan iki çökme
  giderildi.

### 📄 Belgeler
- Yardım menüsüne **AI Yorumlayıcı Rehberi** eklendi (TR/EN/ES): API anahtarının
  nereden alınacağı, yaklaşık maliyet, adım adım kurulum, sorun giderme.

---

## [1.0.17] — 22 Ağustos 2026 · **Kritik Açılış Hatası Düzeltmesi**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

### 🐞 Düzeltildi — Uygulama açılışta çökebiliyordu
v1.0.16'da çok dilli arayüz düzenlemeleri sırasında ana pencerede bazı çeviri
çağrıları yanlış ada bağlanmıştı; bu yüzden özellikle **son projeler listesi
boşken** (temiz kurulumda ilk açılışta) uygulama `name '_t' is not defined`
hatasıyla açılamıyordu. Etkilenen tüm noktalar düzeltildi; açılış ve
menü oluşturma yeniden sağlam.

## [1.0.16] — 21 Ağustos 2026 · **İngilizce Sürüm İyileştirmeleri**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

Uluslararası kullanıcılar için İngilizce sürüm baştan sona gözden geçirildi.

### ✨ İyileştirildi — Varsayılan dil İngilizce
- **Kurulum artık her zaman İngilizce başlar.** Lisans sözleşmesi (EULA) kabul
  ekranı da dâhil ilk açılış İngilizce; kullanıcı dilediğinde Ayarlar'dan
  Türkçe/İspanyolca'ya geçebilir. (Varsayılan üç ayrı katmanda İngilizce'ye
  alındı: uygulama ayarı, i18n başlangıç dili ve EULA penceresi.)

### 🐞 Düzeltildi — Arayüzde kalan Türkçe metinler
- Veri panelindeki **arama kutusu** İngilizce modda Türkçe görünüyordu, düzeltildi.
- Diyalog ve panellerde sabit kalmış ~90 Türkçe metin çok dilli (TR/EN/ES) hâle
  getirildi: sözleşme penceresi, güncelleme diyaloğu, sütun/dönüşüm/eksik-değer
  araçları, danışman paneli, çoklu-seçim paneli ve genel butonlar
  (Kapat / Temizle / Ekle / Sil / Uygula / Kopyala / Geri al …).
- Özel-karaktersiz Türkçe kelimelerden kaynaklanan gizli kaçaklar tarandı;
  arayüzde çevrilmemiş metin kalmadı (üç dil sözlüğü tam eşleşir).

## [1.0.15] — 2 Ağustos 2026 · **Çok Dilli Arayüz Düzeltmeleri + LMM Kararlılığı**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır.

### 🐞 Düzeltildi — İngilizce/İspanyolca arayüzde bozuk analizler
Açılır listelerdeki "seçim yok" yer tutucusu çevriliyor (`(yok)` → `(none)` →
`(ninguno)`) ama kod sabit Türkçe metinle karşılaştırıyordu; yer tutucu gerçek
bir sütun adı sanılıyor ve analiz düşüyordu:

- **LMM** → `Random slope '(none - intercept only)' veride yok`
- **Ağırlıklı Ortalama / Frekans / Toplam / Regresyon / Lojistik** →
  `Küme/PSU sütunu bulunamadı: '(none)'`
- Ayrıca **VARCOMP** iç içe faktör, **Rekabet Eden Riskler** grup,
  **Poisson/NegBin** offset, **Survey-PHREG** ağırlık/küme/tabaka,
  **Koşullu Lojit** alternatif sütun, **Yol Analizi** şablon seçimi.

Dilden bağımsız tek kontrol eklendi; Türkçe arayüz etkilenmiyordu, davranışı
değişmez.

### 🐞 Düzeltildi — LMM "Singular matrix" hatası
Karma model optimizerı `lbfgs`'e sabitti; rastgele etki kovaryansı tekile
yaklaştığında analiz hiç çalışmıyordu. Artık `lbfgs → bfgs → powell` sırayla
denenir; aynı model diğer optimizerlarla sorunsuz yakınsıyor.

### 🔀 Değişti — Diskriminant Analizi'nin yeri
LDA/QDA bir sınıflandırma yöntemi olduğu hâlde kenar çubuğunda **İleri Düzey**
altındaydı. **Sınıflandırma** kategorisine, Gradient Boosting'in ardına alındı.
Toplam analiz sayısı değişmedi (110).

---

## [1.0.14] — 28 Haziran 2026 · **Profesyonel Parametre Paneli + İleri Çıktılar + i18n Temizliği**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** ile yeni installer'a yönlenir.

### ✨ Yeni — analizlerin tüm parametreleri kullanıcı tercihine açıldı
SPSS/JASP tarzı; ortak "Gelişmiş Parametreler" çatısıyla:
- **t-testleri (tek/bağımsız/eşli):** hipotez yönü, Welch/Student, Hedges g/Glass Δ/CLES/d_av,
  etki büyüklüğü güven aralığı, Shapiro/K-S/Levene/Bartlett, betimsel, bootstrap GA.
- **ANOVA ailesi:** tek yön (Welch, ω²/ε²), iki yön (SS I/II/III, post-hoc, η²ₚ/η²/ω²,
  hücre/marjinal ortalama), **ANCOVA** (SS türü, eğim homojenliği, EMM post-hoc),
  **MANOVA** (referans test, Box's M, tek-değişkenli takip), **tekrarlı ölçümler**
  (Greenhouse-Geisser, Mauchly, genelleştirilmiş η², post-hoc).
- **Parametrik olmayan:** Mann-Whitney (yön/süreklilik/yöntem/CLES), Wilcoxon (zero_method),
  Kruskal (ε² + Dunn post-hoc), Friedman (ikili Wilcoxon post-hoc).
- **Korelasyon:** üç yöntemde de p-değeri, yön, p-düzeltme (Bonferroni/Holm/FDR), r için GA.
- **Kategorik:** ki-kare (Yates, G-testi, φ/C, beklenen değerler, standart artıklar).
- **Regresyon:** lineer (robust SE HC0-3, standart β), lojistik (Cox-Snell/Nagelkerke,
  sınıflandırma/AUC, Hosmer-Lemeshow, VIF), Ridge/Lasso (çapraz-doğrulama ile otomatik α).
- **İleri çıktılar:** Cox orantılı-tehlike (Schoenfeld) testi, LMM Nakagawa marjinal/koşullu R²,
  Probit sınıflandırma metrikleri.

### 🔧 Düzeltme
- İngilizce/İspanyolca arayüzde kalan tüm sabit-Türkçe etiketler giderildi: künye
  ("Grup"/"Hedef"/"Test edilen μ"), güven aralığı etiketleri ("%95 GA" → "95% CI"),
  form etiketleri (37) ve açılır liste öğeleri ("Otomatik"/"Yok" vb.). 3 dil senkron (~4408 anahtar).
- Veri seti paketlerine her analiz için "Gelişmiş Parametreler" açıklaması eklendi.

### 🔄 Güncelleme
Bu installer önceki sürümü otomatik kaldırıp v1.0.14'ü aynı dizine yükler; ayarlar,
projeler ve veriler korunur.

---

## [1.0.13] — 25 Haziran 2026 · **İki Yeni Analiz: Gruba Göre Tanımlayıcı + Karma Desen ANOVA**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### ✨ Yeni
- **Gruba göre tanımlayıcı istatistik (SPSS "Split File" mantığı).** Tanımlayıcı İstatistik
  analizine isteğe bağlı **"Gruba göre (Split-File)"** seçici eklendi: bir kategorik değişken
  seçildiğinde sayısal değişkenin tüm tanımlayıcıları (ortalama, SS, medyan, çeyrekler,
  çarpıklık/basıklık, güven aralığı) her grup için ayrı ayrı tek tabloda hesaplanır; gruplara
  göre karşılaştırmalı kutu grafiği üretilir. Güven düzeyi (%90/%95/%99) ayarlanabilir.
- **Karma Desen ANOVA (Split-Plot / Mixed-Design).** Bir denekler-arası faktör (örn.
  deney/kontrol) ile bir denek-içi faktör (örn. ön-test/son-test/izleme) içeren karma desenleri
  analiz eden yeni analiz. Üç etkiyi raporlar: gruplar-arası ana etki, denek-içi ana etki ve
  **grup × zaman etkileşimi**. Küresellik (Mauchly) testi otomatik; ihlalde Greenhouse-Geisser
  düzeltmeli p ve kısmi eta-kare (np²) etki büyüklükleri verilir. Eğitim/psikolojideki
  ön-test/son-test deney-kontrol desenlerinin standart analizidir.

### 🔧 Düzeltme
- İki yeni analizde İngilizce/İspanyolca arayüzde kalan Türkçe ifadeler giderildi; sonuç metni,
  künye, tablo başlıkları, açıklama (ⓘ) ve grafik başlıkları üç dilde senkronlandı.

### 🔄 Güncelleme
Bu installer önceki sürümü otomatik kaldırıp v1.0.13'ü aynı dizine yükler; ayarlar, projeler
ve veriler korunur.

---

## [1.0.12] — 24 Haziran 2026 · **Güven Düzeyi Yaygınlaştırma + Kararlılık**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### ✨ Yeni
- **Ayarlanabilir Güven Düzeyi (%90 / %95 / %99 / Özel) ~67 analize yaygınlaştırıldı.**
  Önceki sürümde 10 parametrik testte olan seçici, artık güven/güvenilirlik aralığı üreten
  analizlerin çoğunda mevcut:
  - **Regresyon:** Lojistik (odds-ratio GA), Probit, Tobit, Log-Linear, Poisson/Negatif
    Binomial, Multinomial, Ordinal, Koşullu Lojit, Quantile, Robust, Doğrusal Olmayan, Bayesçi Doğrusal.
  - **Karma/Anket:** LMM, GEE, GLMM, Ağırlıklı (Survey) Regresyon/Lojistik.
  - **Sağkalım:** Cox, Kaplan-Meier, Parametrik (AFT), Competing Risks, Frailty-Cox,
    Survey-PHREG, Aralık-Sansürlü, Zaman-bağımlı Cox.
  - **Kategorik:** CMH, Fisher (OR), Cohen's Kappa, Ki-Kare Bağımsızlık (2×2 OR), McNemar.
  - **Zaman serisi:** ARIMA, Mann-Kendall/Sen, Üstel Düzleştirme (tahmin bandı).
  - **Diğer:** Bland-Altman, Bootstrap GA, Etki Büyüklüğü, Binom, CFA/Yol Analizi, Kanonik
    Korelasyon, İç İçe/Çapraz LMM, Cronbach α, Karışıklık Matrisi metrikleri, İşaret/Permütasyon
    testleri, Mann-Whitney/Wilcoxon (Hodges-Lehmann), Çapraz Tablo, Tanımlayıcı İstatistikler,
    Çoklu Atama, Likert, Bayesçi Korelasyon.

### 🐛 Düzeltmeler
- **Sessiz çökme giderildi** — Bir analiz çalıştırıp ardından yeni veri içe aktarınca
  (özellikle İstatistik sekmesindeyken) uygulama hata vermeden kapanabiliyordu. Analiz
  çıktısı geçmişinin yeniden kurulması güvenli hale getirildi; ek olarak veri yeniden
  yükleme/sekme geçişi kararlılığı artırıldı.

### 🔄 Güncelleme
Bu installer, MerQur'un önceki sürümünü otomatik kaldırıp v1.0.12'yi aynı dizine yükler.
Ayarlarınız, projeleriniz ve verileriniz korunur.

---

## [1.0.11] — 23 Haziran 2026 · **Güven Düzeyi ve Çoktan Seçmeli İyileştirmeleri**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### ✨ Yeni
- **Güven Düzeyi (ayarlanabilir güven aralığı)** — 10 hipotez/regresyon panelinde
  güven düzeyi seçilebiliyor; sonuç tabloları ve grafiklerde güven aralığı (%90/%95/%99)
  ona göre hesaplanıp etiketleniyor.
- **Manuel Çoklu Yanıt (MR) Set tanımı** — Excel'de zaten ayrıştırılmış sütunlar
  (örn. `Q10_1 … Q10_5`) doğrudan MerQur'a Çoklu Yanıt seti olarak tanıtılabiliyor
  (ham sayım veya 0/1 ikili biçim).

### 🐛 Düzeltmeler
- **Çoktan Seçmeli ayrıştırma** — ayraç seçimi sabitlendi (yanlış ayraç engellendi),
  soru numarası otomatik algılama iyileştirildi, artık (yetim) yardımcı sütunlar
  temizleniyor, düşük frekanslı seçenek eşiği makullendirildi.
- **Çoklu Yanıt Frekans grafiği** — tek renk paletine geçildi (lider çift-renk vurgusu
  kaldırıldı).
- **Dil paketi yüklemesi** — güncelleyicinin bıraktığı eski yerel dil paketi, yeni
  arayüz/sonuç metinlerini ham anahtar olarak gösterebiliyordu; yerleşik paket artık
  eksik anahtarları her durumda dolduruyor (katman birleştirme).
- **Koyu tema okunabilirliği** — Çoktan Seçmeli sütun listelerindeki vurgu renkleri
  (manuel/otomatik/uygulanmış) koyu zeminde okunur açık tonlara geçiyor.
- **Arayüz** — birkaç düzen uyarısı ve takılı pencere referansı giderildi.

### 🔄 Güncelleme
Bu installer, MerQur'un önceki sürümünü otomatik kaldırıp v1.0.11'i aynı dizine yükler.
Ayarlarınız, projeleriniz ve verileriniz korunur.

---

## [1.0.9] — 12 Haziran 2026 · **İyileştirmeler ve Sadeleştirme**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### 🐛 Düzeltmeler
- **Bayesçi Doğrusal Olmayan Regresyon** — Sayısal kararlılık (lojistik/üstel modellerde
  taşma giderildi, veriden türetilen başlangıç değerleriyle güçlü yakınsama).
- **Koşullu Lojit (Seçim Modeli)** — Büyük ölçekli öngörücülerde (fiyat/gelir/mesafe)
  katsayıların sıfırlanması ve uyarı sorunu giderildi (öznitelik ölçekleme).
- **Koşullu Lojistik Regresyon** — Yakınsama uyarısı bastırıldı, tahminler kararlı.

### ✨ İyileştirmeler
- **Sade analiz açıklamaları** — Açıklama metinleri sadeleştirildi.
- **Veri yükleme** — Yüklemede çıkan sütun-öneri penceresi kaldırıldı; aynı tespit
  zaten sağ-tık menüsünde mevcut.
- **Bilgi simgesi (ⓘ)** — Analiz adının soluna alındı, başlık satırı kaydırma gerektirmiyor.
- **Proje dosyası uzantısı** — Artık `.mqr` (eski `.merqur` dosyaları açılmaya devam eder).
- **Çok dilli arayüz** — Sonuç metinleri, tablolar, ipuçları ve grafikler TR/EN/ES tam senkron.

---

## [1.0.8] — 8 Haziran 2026 · **Kararlılık ve İyileştirmeler**

> v1.0.0 ile aynı DOI tescili (2026/18517) altında yayımlanır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### 🐛 Düzeltmeler
- **Açılış kararlılığı** — Açılış ekranının "Hazır." yazısında donup arayüzün
  gelmemesi sorunu giderildi (pencere gösterimi event loop'a alındı + watchdog).
- **Kanonik Korelasyon (CCA)** — Y değişkenleri artık X gibi seçimle ekleniyor;
  analiz düzgün çalışıyor (eskiden Y okunamadığı için çalışmıyordu).
- **Karma Modeller (LMM/GLMM/GEE/Bayesçi Hiyerarşik)** — Sabit etki listesinde
  kategorik değişkenler de seçilebiliyor.
- **Gradient Boosting** — XGBoost yoksa otomatik scikit-learn ("Cannot find
  XGBoost Library" hatası giderildi).
- **Nested LMM** — Varyans tablosu etiketleri seçilen değişken adlarına göre
  gösteriliyor (eski sabit Replikasyon/Populasyon/Aile yerine).
- **Veri tablosu** — Tüm değerleri tam sayı olan sütunlar ondalıksız gösteriliyor
  (397.00 → 397).
- **GLM tablosu** — Poisson/ordinal regresyonda boş "equation" sütunu gizlendi.

### 📦 Yeni Örnek Paketler
- **Enfeksiyon Hastalıkları** — Tüm analizler için enfeksiyon temalı veri seti (TR/EN).
- **Peyzaj — Cochran's Q** — Çok-seçimli formatta yeni örnek veri seti.

---

## [1.0.6] — 2 Haziran 2026 · **Tam Çok Dilli Arayüz + Checkbox Değişken Seçimi**

> Çok dilli arayüz tamamlama güncellemesi. v1.0.0 ile aynı DOI tescili (2026/18517)
> altında yayımlanır. Mevcut kullanıcılar **Yardım → Güncellemeleri Denetle**
> üzerinden yeni installer'a yönlenir.

### 🌍 Tam Çok Dilli Arayüz (TR / EN / ES)

- **89 analiz panelinde** hardcoded Türkçe etiketler i18n anahtar sistemine
  taşındı. EN/ES dilinde uygulamayı kullananlar artık form etiketleri,
  dropdown opsiyonları, sonuç metin başlıkları ve test isimlerini seçili
  dilde görüyor.
- **~256 yeni anahtar × 3 dil = ~768 çeviri girişi** eklendi:
  - **Form etiketleri** (`form_*`): 135+ anahtar
  - **Sonuç formatlayıcısı** (`stats_*`): TEST / Statistic / p-value /
    df / Effect size / %95 CI / GROUP STATS / ANOVA TABLE / POST-HOC /
    DECISION / H₀
  - **Test isimleri** (`test_*`): 17 test adı (Bağımsız t-Testi, Ki-Kare
    Bağımsızlık Testi, MANOVA Wilks' Lambda, vb.)
  - **Etki büyüklüğü** (`es_*`): Küçük / Orta / Büyük / Zayıf / Güçlü
  - **Cohen's Kappa** (`kappa_*`): Anlaşma kalitesi (zayıf → mükemmel)
    + ağırlık türü (yok / lineer / kuadratik)
  - **Dropdown opsiyonları**: Listwise/Pairwise, Type I/III SS,
    Random/Fixed, Ward/Complete/Average/Single, k-means++, Varimax,
    Bayesian modları, Pearson/Spearman/Kendall, vb.
  - **VariableSelector widget**: Tümü/Temizle/Profil + sayım + dialog
  - **Sidebar**: 8 Advanced kategori analiz adı (VARCOMP, Bayesian
    t/Correlation/ANOVA/Hierarchical, SAR/Error/GWR)
  - **Help → Kullanıcı Sözleşmesi** menü öğesi

### ✅ Checkbox Tabanlı Değişken Seçimi

Virgülle ayrılmış değişken listesi yazma yerine **checkbox tıklama** ile
çoklu değişken seçimi:

- **MANOVA** — bağımlı değişkenler artık checkbox listesi
- **Mekansal Hata Modeli (SAR Error)** — bağımsız değişkenler
- **Mekansal Gecikme Modeli (SAR Lag)** — bağımsız değişkenler
- **GWR (Coğrafi Ağırlıklı Regresyon)** — bağımsız değişkenler
- **Hiyerarşik Bayesian Regresyon** — bağımsız değişkenler

**Tümünü Seç / Temizle / Profil Kaydet** butonları ile hızlı çalışma.

### 🐛 Düzeltmeler

- **Yeni dosya açıldığında eski analiz artığı temizleniyor:** Önceki
  dosyada üretilen harita, grafik ve sonuç metinleri yeni dosya açılır
  açılmaz silinir; worker thread'leri durdurulur; method dropdown ve
  parametre formu sıfırlanır.
- **Hiyerarşik Bayesian Regresyon — TypeError:** Aynı isimli yinelenen
  sütunlar (duplicate column names) analizi çökertiyordu (`arg must be
  a list, tuple, 1-d array, or Series`); sütun seçimi yinelenen isimleri
  filtreleyerek düzeltildi.

---

## [1.0.5] — 28 Mayıs 2026 · **Grafiksel Çıktı Açılımı + Çok Dilli Grafikler**

> Görselleştirme odaklı güncelleme. v1.0.0 ile aynı DOI tescili (2026/18517)
> altında yayımlanır. Mevcut kullanıcılar **Yardım → Güncellemeleri Denetle**
> üzerinden yeni installer'a yönlenir.

### 🆕 Grafik Eklenen Analizler (Grafik sekmesi)

- **Hiyerarşik Kümeleme** artık **dendrogram** çiziyor (yaprak etiketleri =
  çeşit/ID adları, Ward renkli kümeler).
- **27 analize grafik eklendi** (önceden hiç grafiği yoktu):
  - **Grup karşılaştırma (boxplot/etkileşim/profil)**: Bağımsız/Eşleştirilmiş/
    Tek-örneklem t-testi, Tek/İki Yönlü ANOVA, Tekrarlı Ölçümler ANOVA,
    Mann-Whitney, Kruskal-Wallis, Wilcoxon, Friedman, MANOVA.
  - **Kategorik (çubuk)**: Ki-Kare Bağımsızlık, Ki-Kare Uyum İyiliği, Çapraz Tablo.
  - **Ordinasyon (2B saçılım/biplot)**: MDS, UMAP, Correspondence, Diskriminant.
  - **Regresyon**: Çoklu Doğrusal (artık grafiği), Lojistik (olasılık dağılımı).
  - **Makine Öğrenmesi**: Random Forest & Gradient Boosting (değişken önemi).
  - **Zaman serisi**: Zaman Serisi & STL (ayrıştırma), ARIMA & Holt-Winters
    (tahmin + %95 GA), Mann-Kendall (Sen eğimi).

### 🌍 Çok Dilli Grafikler (TR / EN / ES)

- **Tüm grafik etiketleri** (başlık, eksen, lejant, anotasyon) artık seçili
  arayüz diline göre çevriliyor — hem yeni eklenen hem de mevcut tüm grafikler
  (PCA, Kaplan-Meier, ROC, Korelasyon, vb.). Dil paketlerine ~175 yeni anahtar.

### 🐛 Düzeltmeler

- **Harita (Harita sekmesi):** KDE/Hotspot haritaları artık tam ekrana oturuyor;
  lejant ve ölçek çubuğu ilk çalıştırmada kaydırma gerekmeden görünüyor (folium
  tam-sayfa render + tam-yükseklik CSS).
- **Grafik düzeni:** colorbar/çok-panelli grafiklerde çıkan "Tight layout not
  applied" uyarısı giderildi (constrained_layout'a geçildi).
- **Tanımlayıcı İstatistikler:** "Çalıştır" artık seçili değişkeni gösteriyor
  (önceden her zaman ilk değişkene dönüyordu).

---

## [1.0.4] — 21 Mayıs 2026 · **Geotag'li Fotoğraflardan İçe Aktar**

> Yeni özellik güncellemesi. v1.0.0 ile aynı DOI tescili (2026/18517)
> altında yayımlanır. Mevcut kullanıcılar **Yardım → Güncellemeleri Denetle**
> üzerinden yeni installer'a yönlenir.

### 🆕 Geotag'li Fotoğraflardan İçe Aktar (Yeni Özellik)

- **Dosya → 📷 Geotag'li Fotoğraflardan İçe Aktar…** (Ctrl+Shift+I).
- Bir klasör seç (alt klasör tarama opsiyonel) — MerQur tüm desteklenen
  görüntü dosyalarının (JPG/JPEG/TIF/TIFF/HEIC/HEIF/PNG/WEBP) EXIF + GPS
  metadata'sını okur ve tek bir tabloya dönüştürür.
- Üretilen 22 sütun: `foto_adi`, `dosya_yolu`, `dosya_boyutu_kb`,
  `genislik_px`, `yukseklik_px`, `cekim_zamani` (DateTimeOriginal),
  `lat`, `lon`, `yukseklik_m`, `yon_derece` (GPSImgDirection),
  `hiz_kmh`, `kamera_uretici`, `kamera_model`, `lens_model`,
  `focal_length_mm`, `apertur_f`, `pozlama_sn`, `iso`, `flash`,
  `beyaz_dengesi`, `geotag_var` (binary).
- DMS → decimal degree GPS dönüşümü, S/W ref → negatif değer.
- Çekim zamanı ISO 8601 datetime; hız KPH'e otomatik dönüştürülür.
- Tarama esnasında ilerleme çubuğu (16 px, petrol yeşili) + dosya adı.
- Özet kutusu: GPS'li/GPS'siz sayım, kamera modeli dağılımı, tarih aralığı,
  klasör yolu.
- İçe aktarımdan sonra DataFrame otomatik olarak Veri/Analiz/Harita
  panellerine akar; **lat/lon otomatik tespit** edilir; Harita sekmesinde
  doğrudan KDE / Hotspot / Moran's I / vektör katman analizleri çalıştırılabilir.
- Tam i18n (TR/EN/ES) — 5 yeni anahtar her dil için.

### 🐛 Düzeltmeler

- `requests` kütüphanesinin urllib3/chardet sürüm uyumsuzluğu uyarısı
  (RequestsDependencyWarning) main.py'de bastırıldı — başlangıçta artık
  zararsız uyarı mesajı yok.

### 📥 İndirilebilir Çıktılar

| Dosya | Boyut |
|---|---|
| `MerQur-1.0.4-windows-x64-Setup.exe` | ~315 MB |
| `MerQur-1.0.4-windows-x64.zip` | ~467 MB |

---

## [1.0.3] — 19 Mayıs 2026 · **Vektör Katmanlar + UX & Bug Hotfix Update**

> Bakım + özellik güncellemesi. v1.0.0 ile aynı DOI tescili (2026/18517)
> altında yayımlanır. Mevcut kullanıcılar **Yardım → Güncellemeleri Denetle**
> üzerinden yeni installer'a yönlenir.

### 🆕 Vektör Katmanlar (Yeni Özellik)

- Harita sekmesinde **SHP / KML / KMZ / GPKG / GeoJSON** overlay desteği.
  Araştırmacı çalışma alanı sınırını, ilgi noktalarını veya akış çizgilerini
  KDE / Hotspot / DBSCAN / Moran's I gibi analizler üzerine bindirir.
- Katman başına kompakt kart: ☑ göster · ad (inline edit) · 🎨 renk swatch ·
  🗑 sil · ◐ İçi dolu (polygon, sınır çizgisi her zaman görünür) · ☑ Lejant.
- Otomatik **CRS dönüşümü** (EPSG:4326 / WGS84) — KMZ otomatik unzip.
- Folium'un hem **standalone HTML** hem **iframe srcdoc** çıktısını
  destekleyen JS injection (folium quirky çift format).
- Lejant yığını: vektör (sağ-üst) + analiz (vektör altında) dikey stack.

### 🔧 UI / UX Düzeltmeleri

- **Harita sekmesi toolbar**: Çalıştır, Haritayı Kaydet, PNG butonları
  sol panelden harita üst-toolbar'ına taşındı (sağa yaslı, diğer analiz
  sekmelerine uyumlu). Sol panelde daha çok yer.
- **Sol panel splitter**: min 280, max 560, varsayılan 340px — kullanıcı
  splitter handle ile genişletebilir.
- **Analiz Yardımcısı** = `data_welcome_dialog` (v1.0.2'de eklenen
  ÖN BİLGİLENDİRME kartlı dialog). Eski AdvisorPanel'in sequential auto-runner
  davranışı kaldırıldı; sadece **öneri** + ne işe yarar açıklaması, otomatik
  çalıştırma yok. Hem otomatik (veri yüklendiğinde) hem manuel (Araçlar →
  Hesaplayıcılar → 🎯 Analiz Yardımcısı) aynı dialog'u açar.
- **ID sütun filtresi**: `ogrenci_id` gibi sütunlar analiz değişkeni olarak
  ÖNERİLMEZ; auto-excluded sütunlar info banner'da gösterilir.
- **Badge "Bilgilendirme"** (önceki "ÖN BİLGİLENDİRME").
- **"Bir daha gösterme"** metni netleştirildi: "Veri yüklendiğinde otomatik
  açılmasın (yine de Araçlar → Analiz Yardımcısı'ndan açabilirsiniz)".
- **🔍 Bul/Değiştir** (Veri sekmesi toolbar): 3 mod (İçerir/Tam hücre/Regex),
  büyük-küçük harf opsiyonu, tüm/seçili sütun kapsamı, undo destekli.

### 🐛 Kritik Bug Düzeltmeleri

- **Harita pan cursor wheel zoom regression**: Mouse wheel zoom sonrası
  pan/grab cursor tüm sekmelerde takılı kalıyordu. **`_override_poll_timer`**
  (200ms) QGuiApplication.mouseButtons() polling — NoButton ise overrideCursor
  stack'inden pan-tipi shape'ler pop edilir, Wait/Busy (analiz kum saati)
  korunur. `_cursor_enforce_timer.stop` SİLİNDİ — timer sürekli çalışır.
- **Data welcome dialog `t` shadow bug**: `for t in column_types.values()`
  döngü değişkeni i18n `t()` fonksiyonunu shadow ediyordu → TypeError silent
  catch → dialog hiç açılmıyordu. Loop değişkeni `ty` olarak değiştirildi.
- **Settings migration**: `_v103b_migrated_welcome` flag ile mevcut
  kullanıcıların `show_data_welcome=False` durumu tek seferlik True'ya çekilir.

### 🌓 Dark Mode + Q1 Grafik Hijyeni

- **Hardcoded beyaz arkaplanlar** (log paneli, info popover, analiz kartı)
  → `palette(base)` + `palette(text)` ile tema-duyarlı.
- **Matplotlib grafikleri her zaman akademik tema** (GUI dark olsa bile).
  Grafikler raporlara/yayınlara gömüldükleri için Q1 standardı (beyaz arkaplan,
  akademik renk paleti, ince gri grid). `apply_dark_theme()` matplotlib için
  artık çağrılmaz.

### 📥 İndirilebilir Çıktılar

| Dosya | Boyut |
|---|---|
| `MerQur-1.0.3-windows-x64-Setup.exe` | ~342 MB |
| `MerQur-1.0.3-windows-x64.zip` | ~515 MB |

---

## [1.0.2] — 18 Mayıs 2026 · **Bayesian + Mekansal Regresyon + SEM Update**

> Özellik güncellemesi. v1.0.0 ile aynı DOI tescili (2026/18517) altında
> yayımlanmıştır. Mevcut kullanıcılar **Yardım → Güncellemeleri Denetle**
> üzerinden yeni installer'a yönlenir.

### 🆕 8 Yeni İleri Düzey Analiz

**Bayesian Dörtlüsü** (PyMC bağımlılığı YOK — pingouin + Empirical Bayes):

- **Bayesian t-Test (BEST)** — Tek/Bağımsız/Eşleştirilmiş t-Test'in
  Bayesyen versiyonu. JZS Cauchy prior, **BF₁₀** + 8 bantlı Jeffreys yorum
  skalası grafik. Mod-aware form (Grup / 2. Ölçüm / μ₀ alanları otomatik
  enable/disable).
- **Bayesian Korelasyon** — Pearson/Spearman/Kendall korelasyonu BF₁₀ ile
  raporlar; "ilişki var / yok" için doğrudan kanıt.
- **Bayesian ANOVA** — 1 yönlü ve 2 yönlü (etkileşim dahil) ANOVA için
  pingouin `bayesfactor_anova` + BIC fallback; her etki için yatay BF
  bar grafiği.
- **Hiyerarşik Bayesian Regresyon** — statsmodels `MixedLM` + Empirical
  Bayes BLUP posteriorları + BIC tabanlı Bayes Faktörü (LMM vs OLS).
  Grup random intercept'lerinin ±%95 güvenilirlik aralıklı **caterpillar
  plot**'u.

**Mekansal Regresyon Üçlüsü** (libpysal + spreg + mgwr):

- **SAR (Spatial Autoregressive Lag)** — `Y = ρWY + Xβ + ε`. KNN /
  DistanceBand komşuluk matrisleri; spreg `ML_Lag`. Katsayı forest plot
  + ρ raporu.
- **Spatial Error Model** — `Y = Xβ + u, u = λWu + ε`. spreg `ML_Error`,
  λ spatial-error parametresi.
- **GWR (Geographically Weighted Regression)** — mgwr `Sel_BW` AICc-optimal
  bandwidth + lokal katsayı tahmini. Lokal R² mekansal scatter haritası,
  her katsayı için min/Q25/medyan/Q75/max + % anlamlı tablosu.

**CFA → SEM Genişletmesi**:

- CFA paneli artık opsiyonel **structural path** alanı kabul eder
  (`"F2 ~ F1; F3 ~ F1 + F2"`). Boş bırakılırsa klasik ölçüm modeli (CFA);
  doluysa **tam SEM** (measurement + structural). semopy çıktısı
  latent~latent satırlarını structural path olarak ayrıştırır.

### 🎨 Veri Karşılama Diyaloğu (Yeni)

- Kullanıcı bir veri seti yüklediğinde **"ÖN BİLGİLENDİRME"** rozetli
  modal karşılama. Sütun tiplerine (numeric / binary / categorical /
  datetime / geo) göre kart düzeninde uygun analiz önerileri: **ikon ·
  başlık · neden · örnek sütun rolleri (Grup/Değer/Hedef/Lat-Lon/...) ·
  "Analiz → ..." yol bilgisi**.
- 13 analiz tipi kapsamı: Tanımlayıcı, Normallik, Korelasyon, Bayesian
  Korelasyon, t-Test, Bayesian t-Test, ANOVA, Ki-Kare, Regresyon, Zaman
  Serisi, Mekansal, Mekansal Regresyon, Hiyerarşik Bayesian / LMM.
- "Bir daha gösterme" tercihi `settings.json`'a yazılır.
- Tam **i18n**: TR/EN/ES (`welcome_*` anahtarları, t() üzerinden).

### 🏷 Sekme Adlandırması

- **"İstatistik" → "Analiz"** (TR), **"Statistics" → "Analyze"** (EN),
  **"Estadística" → "Analizar"** (ES). SPSS/JASP/jamovi'nin
  *Analyze* menüsü ile uyumlu; Bayesian / SEM / Mekansal Regresyon
  gibi modern model sınıflarını da kapsayan daha kısa bir ad.

### 🐛 Bug Fix'leri (v1.0.1 sızıntıları)

- Grafik tabı boş kalma: `TAB_AVAILABILITY` filtresinde 7 yeni
  ASCII_TYPE; `_ANALYSIS_TYPE_MAP` Türkçe→ASCII eşleştirmeleri eklendi;
  Qt sekme geçişi sonrası `QTimer.singleShot(50, canvas.draw)` gecikmeli
  redraw; `ax.set_facecolor("white")` ile dark mode kontrast düzeltmesi.
- BF₁₀ format taşması: `>1e6` veya `<1e-6` için **bilimsel notasyon**
  eşiği; eski raw `200+ haneli` astronomik float çıktısı kaldırıldı.
- VARCOMP nested model spec: outer-as-dummy + nested ID zincirleme
  yaklaşımı sayesinde tüm faktörler `vc_formula` altında, identifiability
  iyileştirildi.

### 📦 Bağımlılıklar

- **Eklenen**: `spreg` 1.9.0 (~5 MB), `mgwr` 2.2.1 (~10 MB).
- **Mevcut kullanılanlar**: `pingouin` (Bayesian BF), `semopy` (SEM),
  `libpysal` (spatial weights), `statsmodels.MixedLM` (Hiyerarşik Bayes).
- **PyMC YOK** — Hiyerarşik Bayesian için Empirical Bayes / BIC
  yaklaşımı; ~500 MB bundle tasarrufu.

### 📥 İndirilebilir Çıktılar

| Dosya | Boyut |
|---|---|
| `MerQur-1.0.2-windows-x64-Setup.exe` | 342 MB |
| `MerQur-1.0.2-windows-x64.zip` | 515 MB |

---

## [1.0.1] — 15 Mayıs 2026 · **VARCOMP + Dark Theme Update**

> Bakım ve özellik güncellemesi. v1.0.0 ile aynı DOI tescili
> (2026/18517) altında yayımlanmıştır. Mevcut kullanıcılar
> **Yardım → Güncellemeleri Denetle** üzerinden yeni installer'a yönlenir.

### 🆕 Yeni Analiz

- **VARCOMP (Varyans Bileşenleri Analizi)** — SAS *PROC VARCOMP*'un Python
  eşdeğeri. Dinamik N-faktör formu (**"+ Faktör Ekle"** butonu ile sınırsız
  faktör), her faktör için **nested / crossed** seçimi, kümülatif nested
  ID zincirleme, **her bileşen için ayrı ICC** ve heritability (h²)
  yorumu, otomatik diagnostik notlar (singular fit, yetersiz seviye,
  confounding uyarısı).

### 🐛 VARCOMP / Mixed Model Kritik Düzeltmeler

- `statsmodels` `lbfgs` optimizer'ının boundary'de `llf=inf` döndürüp
  sonucu sıfıra çekme problemi giderildi (cascade: `bfgs` → `cg`).
- Çok faktörlü modellerde **outer faktör varyansının 0 boundary'e
  takılma** problemi giderildi (*dummy-outer strategy*) — tüm faktörler
  artık vcomp altında, identifiability artırıldı.

### 🌓 Dark Theme

- Tam palette tabanlı **koyu tema** — Ayarlar'dan açılır, açma anında
  hot-reload uygular (yeniden başlatma gerekmez).
- Anket Tasarımcısı, İstatistik kategori sidebar'ı, Kullanıcı Sözleşmesi
  diyaloğu, Veri Sekmesi toolbar — hepsi tema-duyarlı (`palette()` ile
  light/dark otomatik geçer).
- Splash freeze fix: tema değiştirip kaydedildiğinde uygulama eski
  davranışında **"hazırlanıyor..."** ile donuyordu — `core/theme.py`
  modülü `main.py`'den ayrıştırılarak çözüldü.

### 📋 Kullanıcı Sözleşmesi (EULA)

- İlk açılışta **modal EULA diyaloğu** — kabul edilmeden uygulama
  açılmaz. Kabul `settings.json`'a yazılır; sürüm bump'ında yeniden
  istenir. **Yardım menüsü** üzerinden salt-okunur görüntüleme.

### ⏳ Uzun Analizler için Modal İlerleme

- **`gui/analysis_runner.py`** — VARCOMP/LMM/GLMM gibi uzun analizler
  için QThread tabanlı worker + modal ilerleme penceresi. UI artık
  bloklanmıyor; **iptal** butonu desteği. Windows "MerQur yanıt vermiyor"
  uyarısı kalktı.

### 📊 Veri Sekmesi İyileştirmeleri

- 10 buton'lu hızlı eylem toolbar: 🔍 Ara, 📊 Sütun Özeti, 🏷 Kodla,
  🔗 Birleştir, ❌ Eksikleri Yönet, 🔄 Dönüştür, 📤 Dışa Aktar,
  ➕ Sütun Ekle, 🗑 Sütun Sil, ↶ Geri Al, ↷ İleri Al.
- **20 adımlı geri al / ileri al** (Ctrl+Z / Ctrl+Y) — `core/undo_redo.py`.
- **Sürekli / kesikli** numerik alt-tip ayrımı + sütun bazlı ayarlanabilir
  ondalık hassasiyet.
- Kesikli numerik sütunlar (kodlanmış grup ID'leri: `okul_no = 1,2,3 …`)
  artık **VARCOMP / LMM / Crossed LMM / Nested LMM** için random faktör
  olarak seçilebilir.

### 🗃 Yeni Örnek Veri

- **`varcomp_orman_genetik_5faktor.xlsx`** — 5-faktörlü orman ıslahı
  provenance/family trial: 6 saha × 5 popülasyon × 30 aile × 3 blok ×
  3 birey = 1620 gözlem. Gerçek varyans bileşenleri VARCOMP ile
  doğru tahmin edilebilir (test verisi olarak doğrulanmıştır).

### 🌐 Web Sayfası

- Anasayfa rozeti **Sürüm 1.0.1** olarak güncellendi (DOI atfında
  Sürüm 1.0.0 baseline korundu — tescil sürümü).
- `/indir/` sayfası v1.0.1 Setup.exe + ZIP linkleri ile güncel.
- VARCOMP için kapsamlı analiz tanıtım sayfası eklendi:
  `/bilim-dallari/ziraat-orman-su-urunleri/100-varcomp-varyans-bilesenleri/`.
- Anasayfa teşekkür bandına **SDÜ Rektörlüğü** ve **Bilgi İşlem Daire
  Başkanlığı** ile **Python ekosistemi + Visual Studio Code + Anthropic
  Claude Code** geliştirme araçları teşekkürleri eklendi.

---

## [1.0.0] — 11 Mayıs 2026 · **SDÜ Resmi Lansman Sürümü**

> **MerQur** ilk kez **Süleyman Demirel Üniversitesi** ev sahipliğinde
> resmi olarak yayımlanmıştır. T.C. Kültür ve Turizm Bakanlığı
> tarafından **2026/18517 sayılı eser tescili** ile koruma altındadır.
> Resmi adres: **https://merqur.sdu.edu.tr**

---

### 🎯 101 İstatistiksel Analiz

Akademik araştırmanın temel ve ileri istatistik ihtiyaçlarını karşılayan tam set:

- **Tanımlayıcı + Parametrik** (13) — Tanımlayıcı, Normallik, Tek/Bağımsız/Eşleştirilmiş t-test, Tek/İki Yönlü ANOVA, Tekrarlı Ölçümler ANOVA, MANOVA, ANCOVA, Bootstrap CI, Permütasyon, Çoklu Karşılaştırma
- **Non-parametrik** (7) — Mann-Whitney U, Wilcoxon, Kruskal-Wallis, Friedman, Binomial, Sign, Runs
- **Kategorik** (12) — Ki-Kare bağımsızlık/uyum, Fisher Exact, McNemar, Cohen's Kappa, CMH, Log-Linear, Çapraz Tablo, MR Frekans, MR×Kategorik, MR×MR, Cochran's Q
- **Korelasyon + Çok Değişkenli** (6) — Pearson/Spearman/Kendall, Bland-Altman, Effect Size, Kanonik Korelasyon (CCA), Correspondence Analysis, VARCLUS
- **Regresyon** (12) — Çoklu Doğrusal, Lojistik, Poisson, Multinomial, Ordinal, PLS, Probit, Tobit, Bayesian Linear, Non-linear, Ridge, LASSO
- **Aracılık + Karma Modeller** (9) — Mediation, Path Analysis, LMM, **Nested LMM**, **Crossed LMM**, Multiple Imputation, GEE, GLMM, Elastic Net, Robust, Quantile
- **Sınıflandırma + Kümeleme** (13) — ROC, TSS, Karmaşıklık Matrisi, Random Forest, SVM, Gradient Boosting, K-Means, Hiyerarşik, DBSCAN, PCA, t-SNE, MDS, UMAP
- **Güvenilirlik + Ölçek** (5) — Cronbach's α, Likert, EFA, ICC, CFA
- **Survey (Karmaşık Örnekleme)** (5) — Means, Frekans, Total, Regression, Logistic
- **Modern + Sağkalım** (11) — GAM, Diskriminant, Conditional Logit, Kaplan-Meier, Cox, Parametrik AFT, Competing Risks, Time-Dependent Cox, Survey-PHREG, Interval-Censored, Frailty Cox
- **Zaman Serisi + Anomali** (6) — Tanımlayıcı, STL, ARIMA, ETS, Mann-Kendall + Sen, Anomali Tespiti

### 🗺 5 Mekansal Analiz (Map sekmesi)

- **KDE Yoğunluk Haritası** — Otomatik gradient lejant, sıcak nokta gösterimi
- **Hexbin Yoğunluk** — Altıgen ızgara yoğunluk haritası
- **DBSCAN Mekansal Kümeleme** — Coğrafi yoğunluk kümeleri + gürültü ayrımı
- **Hotspot (Getis-Ord G\*)** — İstatistiksel sıcak/soğuk nokta tespiti
- **Moran's I** — Mekansal otokorelasyon + LISA lokal kümeleri

**Veri Keşfi modu:** Mekansal analizden önce noktaları kategorik sütuna göre **otomatik renklendirilmiş** haritada göster (örn. cinsiyet, yaş_grubu). Otomatik lejant, LayerControl, ölçek çubuğu, PNG export.

### 📄 Tek Tıkla APA 7 Raporu

Analiz çıktıları otomatik yorumlanır ve American Psychological Association 7. baskı standardında Word raporuna dönüştürülür. *t*, *p*, *d*, *F*, *r*, *M*, *SD* sembolleri otomatik italikleştirilir. Tablolar ve grafikler raporu kendiliğinden besler.

### 🎨 Chart Studio

30+ grafik tipi: boxplot, violinplot, heatmap, sankey, stacked bar, ridge plot, scatter matrix, dendrogram, parallel coordinates, vb. Başlık ve eksen etiketleri tamamen düzenlenebilir. PNG ve interaktif Plotly HTML çıktı.

### 📋 Anket + Ölçek

Yapılı anket inşa edici, dallandırma mantığı, çoklu cevap soruları, **örneklem büyüklüğü hesaplayıcısı** (kompakt 2-sütun düzen), Likert ölçek analizi (Cronbach's α, EFA, CFA, ICC).

### 🌍 Üç Dilli Arayüz

**Türkçe**, **İngilizce**, **İspanyolca** — sadece menü değil; analiz çıktıları, rapor cümleleri, tablo başlıkları ve hata mesajları tam çevirili. Tek tıkla dil değiştirme.

### 📂 Çoklu Format Desteği

Excel (.xlsx), CSV, SPSS (.sav), Stata (.dta), R (.rdata), Parquet. Yerleşik veri kodlama, eksik değer yönetimi, dönüştürme, birleştirme.

### 🔄 In-app Güncelleme Sistemi

Yardım menüsünden *Güncellemeleri Denetle* ile en son sürümü tek tıkla indir ve kur. Manifest sunucusu **merqur.sdu.edu.tr** üzerinden çalışır — SDÜ kurumsal hizmet.

### 🗺 11 Akademik Sample Paketi

Disiplin bazlı hazır veri setleri (her biri 99 analiz + 5 mekansal × .xlsx + REHBER.docx):

1. **Tıp / Sağlık Bilimleri**
2. **Eğitim Bilimleri / Sosyoloji**
3. **Spor Bilimleri**
4. **Ziraat / Orman Mühendisliği**
5. **Peyzaj Mimarlığı**
6. **Mimarlık · Şehir Bölge Planlama · İç Mimarlık · Endüstri Ürünleri Tasarımı**
7. **Görsel Algı · Görsel Kalite · Duyusal Peyzaj**
8. **Fen Bilimleri / Matematik**
9. **Turizm**
10. **Sosyal-Beşeri / İdari Bilimler**
11. **Karma (multi-disipliner)**

Ek olarak **ortak Tekrarlı Ölçümler ANOVA referans dataseti** (50 katılımcı × 4 zaman, hem wide hem long format).

### 📚 Dokümantasyon

- **Kullanım Kılavuzu** (Yardım menüsünde, 101 analiz sözlüğü dahil)
- **MerQur SAS · SPSS Karşılık Tablosu** (Word, 12 tablo, 104 analizin SAS PROC + SPSS komut karşılıkları)
- **İstatistik Çocuk Sunumu** (PowerPoint, 50 slayt, çocuk diliyle istatistik kavramları)
- **EULA TR + EN** (Markdown + Word) — Akademik kullanım açık, ticari kullanım yazılı izinle, APA 7 atıf zorunlu

### 🏛️ Tescil ve Kurumsal Kimlik

- **T.C. Kültür ve Turizm Bakanlığı Eser Sicil No: 2026/18517**
- **Süleyman Demirel Üniversitesi** kurumsal subdomain: **merqur.sdu.edu.tr**
- Geliştirici: **Ömer K. Örücü** (SDÜ Peyzaj Mimarlığı Bölümü)
- Resmi iletişim: **merqur@sdu.edu.tr**

### 🔧 Teknik Altyapı

- **Python 3.11 / PyQt6** masaüstü uygulaması
- **PyInstaller --onedir** ile bağımsız Windows / macOS / Linux dağıtımı
- **Bundled multiprocessing fix** — libpysal/esda gibi paketler için `freeze_support()` + spawn start method
- **esda analytic-mode** — Hotspot/Moran için crand worker spawn yok, BLAS int64 sorunsuz
- **Map cursor v6** — Multi-layered Chromium WebEngine cursor leak fix (CSS injection + Qt setCursor + CursorChange event filter)
- **QProgressDialog** — Uzun analizler (Nested LMM, Crossed LMM) için modal bekleme dialog'u

---

*Bu sürüm ile MerQur, akademik istatistik camiasına ücretsiz olarak sunulan, Türkiye menşeli ilk kapsamlı veri analizi platformu olarak resmi yayın hayatına başlamıştır.*
