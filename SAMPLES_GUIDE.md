# MerQur Örnek Veri Setleri Rehberi

20 disiplin × ortalama 8 veri seti = **161 örnek veri seti** + her disiplin için Word rehberi (önerilen analiz akışı).

Her veri setinin yanında **MerQur'da hangi analizi yaptırmak için tasarlandığı** belirtilmiştir.

İndirme: [v1.0.0 release sayfası](https://github.com/omerorucu/merqur/releases/tag/v1.0.0)

---

## 🔧 Mühendislik
**Dosya:** `MerQur_Ornek_Veriler_Muhendislik_v1.0.0.zip` (22 MB · 6 disiplin · 48 veri seti)

### Çevre Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_hava_kalitesi_HKIS` | Tanımlayıcı + zaman serisi · Hava kalitesi indeksi (PM2.5, NO₂, O₃) trendi |
| `02_icme_suyu_kalitesi` | İki yönlü ANOVA · Bölge × mevsim etkisi |
| `03_atiksu_aritma_performans` | Eşleştirilmiş t / Wilcoxon · Giriş-çıkış BOD/COD karşılaştırması |
| `04_endustriyel_baca_emisyon` | Regresyon · Yakıt tipi & yük etkisi |
| `05_toprak_kontaminasyon_mekansal` | Moran's I + hotspot (Getis-Ord Gi*) · Ağır metal kümelenmesi |
| `06_gurultu_haritalama` | KDE yoğunluk haritası + ANOVA · Bölge gürültü düzeyi |
| `07_atik_yonetimi_panel` | Panel veri / mixed model · İl-yıl geri dönüşüm oranları |
| `08_karbon_ayak_izi_LCA` | ANOVA + post-hoc · Ürün/süreç karbon profili |

### Harita Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_gnss_statik_olcum_hata` | Normallik testi + tek örneklem t · GNSS statik hata dağılımı |
| `02_nivelman_agi_LSA` | En küçük kareler dengelemesi · Nivelman ağ kapanması |
| `03_total_station_kalibrasyon` | Lineer regresyon · Total station kalibrasyon eğrisi |
| `04_fotogrametrik_bundel_ayarlama` | Çoklu regresyon + ANOVA · Bundle adjustment artıkları |
| `05_insar_yer_hareketi_zaman_serisi` | Zaman serisi (ARIMA) · InSAR deformasyon trendi |
| `06_lidar_nokta_bulutu_hassasiyet` | Tanımlayıcı + Bland-Altman · Lidar hassasiyet karşılaştırması |
| `07_deformasyon_izleme_baraj_kopru` | Tekrarlı ölçümler ANOVA · Yapı deformasyon zaman serisi |
| `08_uzaktan_algilama_siniflandirma` | Confusion matrix + ROC · Sınıflandırma doğruluğu |

### İnşaat Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_beton_basinc_dayanimi_DOE` | Faktöriyel ANOVA · Karışım tasarımı (DOE) |
| `02_celik_cekme_deneyi` | Lineer regresyon + tanımlayıcı · Çekme eğrisi |
| `03_zemin_mekanigi_SPT_CPT` | Korelasyon + regresyon · SPT-N vs CPT-qc ilişkisi |
| `04_kopru_salinim_sensor_zamanserisi` | FFT/zaman serisi · Köprü doğal frekans |
| `05_bina_sismik_tepki` | İki yönlü ANOVA · Yapı tipi × yer hareketi |
| `06_asfalt_yorulma_sagkalim` | Sağkalım analizi (Kaplan-Meier, Cox) · Yol ömrü |
| `07_yapi_sagligi_izleme_tarihi` | Tekrarlı ölçümler · Yapı SHM zaman serisi |
| `08_santiye_verimliligi` | ANOVA + bootstrap CI · Verimlilik karşılaştırması |

### Jeoloji Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_sondaj_log_stratigrafi` | Tanımlayıcı + kümeleme · Litoloji sınıflandırma |
| `02_heyelan_kutle_hareketi` | Lojistik regresyon + Moran's I · Heyelan riski mekânsal |
| `03_yeralti_suyu_hidrojeoloji` | Korelasyon + zaman serisi · Akifer dinamiği |
| `04_maden_tenor_jeoistatistik` | Variogram / kriging · Cevher tenor mekânsal |
| `05_sismik_yansima_profili` | İşaret işleme + tanımlayıcı · Sismik kesit |
| `06_petrofizik_karot_analizi` | Çoklu regresyon · Porozite-permeabilite |
| `07_volkanik_risk_izleme` | Zaman serisi + sınır aşma · Volkan tetik göstergeleri |
| `08_deprem_katalogu_TR` | KDE + hotspot · Sismik aktivite dağılımı |

### Kimya Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_reaksiyon_kinetigi` | Doğrusal olmayan regresyon · Arrhenius/k modeli |
| `02_rsm_ccd_polimer` | Yanıt yüzeyi metodolojisi (CCD) · Polimer optimizasyonu |
| `03_damitma_kolonu_sureci` | Çoklu regresyon · Damıtma verim modeli |
| `04_petrol_rafineri_kalite` | SPC kontrol grafiği + ANOVA · Ürün kalitesi |
| `05_adsorpsiyon_izoterm` | Doğrusal olmayan regresyon · Langmuir/Freundlich |
| `06_korozyon_hizi` | Sağkalım + regresyon · Malzeme bozunma süresi |
| `07_kataliz_etkinlik` | İki yönlü ANOVA · Katalizör türü × sıcaklık |
| `08_polimer_doe` | Faktöriyel ANOVA · Polimer üretim DOE |

### Makine Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_motor_dinamometre_testi` | Çoklu regresyon · Tork-devir-yakıt ilişkisi |
| `02_malzeme_yorulma_SN` | Doğrusal olmayan regresyon · S-N yorulma eğrisi |
| `03_hvac_cop_testi` | ANOVA + post-hoc · COP karşılaştırma |
| `04_ruzgar_turbini_yillik` | Zaman serisi · Yıllık üretim trendi |
| `05_cnc_yuzey_doe` | Faktöriyel DOE · Yüzey pürüzlülüğü |
| `06_otomotiv_titresim` | FFT + tanımlayıcı · Titreşim spektrumu |
| `07_spc_imalat_kalite` | SPC kontrol grafiği · Süreç kararlılığı |
| `08_gunes_paneli_verim` | Çoklu regresyon · Verim-koşul ilişkisi |

---

## 🏥 Sağlık Bilimleri
**Dosya:** `MerQur_Ornek_Veriler_Saglik_Bilimleri_v1.0.0.zip` (4 MB · 4 disiplin · 32 veri seti)

### Halk Sağlığı

| Veri Seti | Hedef Analiz |
|---|---|
| `01_hemsirelik_RCT_basi_yarasi_onleme` | Bağımsız t + ki-kare · RCT, baskı yarası önleme |
| `02_fizyoterapi_inme_rehabilitasyon_RM` | Tekrarlı ölçümler ANOVA · İnme rehabilitasyon zaman noktaları |
| `03_toplum_tarama_HT_DM_prevalans` | Tanımlayıcı + ki-kare · HT/DM prevalans, demografik |
| `04_beslenme_cluster_RCT_AkdenizDiyeti` | Mixed model (cluster RCT) · Akdeniz diyeti müdahalesi |
| `05_saglik_okuryazarligi_TSOA` | Cronbach α + faktör analizi · TSOA ölçek geçerlik |
| `06_ebelik_emzirme_saglkalim` | Kaplan-Meier + Cox · Emzirme süresi sağkalım |
| `07_is_sagligi_tukenmislik_MBI` | Faktör analizi + regresyon · Maslach Tükenmişlik Envanteri |
| `08_asilama_kapsami_il_yil_panel` | Panel veri + Moran's I · İl bazlı aşı kapsamı |

### Tıp

| Veri Seti | Hedef Analiz |
|---|---|
| `01_RCT_antihipertansif_vs_plasebo` | Bağımsız t + ANCOVA · RCT, başlangıç düzeltmesi |
| `02_kohort_meme_kanseri_saglkalim` | Kaplan-Meier + Cox regresyon · Sağkalım analizi |
| `03_vaka_kontrol_akciger_kanseri` | Lojistik regresyon + OR · Vaka-kontrol çalışması |
| `04_tani_testi_troponin_ROC` | ROC eğrisi + AUC · Tanı testi performansı |
| `05_pre_post_diyabet_HbA1c` | Eşleştirilmiş t · Müdahale öncesi-sonrası |
| `06_epidemiyoloji_COVID_seroprevalans` | Tanımlayıcı + lojistik regresyon · Seroprevalans |
| `07_cocuk_buyume_egrisi_multilevel` | Çok düzeyli model (HLM) · Boylamsal büyüme eğrisi |
| `08_ilac_yan_etki_sikligi` | Ki-kare + Fisher kesin · İlaç yan etki tabloları |

### Veterinerlik

| Veri Seti | Hedef Analiz |
|---|---|
| `01_sut_sigiri_mastitis_risk` | Lojistik regresyon · Mastitis risk faktörleri |
| `02_buzagi_yasatma_saglkalim` | Kaplan-Meier + Cox · Buzağı sağkalım |
| `03_koyun_ureme_verimi` | İki yönlü ANOVA · Koyun üreme parametreleri |
| `04_kus_gribi_HPAI_salgin_paneli` | Panel + zaman serisi · HPAI yayılım |
| `05_kanin_kalp_hastaligi_RCT` | Bağımsız t + ANCOVA · Veteriner RCT |
| `06_antibiyotik_direnc_izolat` | Ki-kare + lojistik · İzolat direnç paterni |
| `07_kedi_vucut_kondisyon_davranis` | Korelasyon + regresyon · Davranış skorları |
| `08_yaban_hayati_telemetri` | KDE + spatial · Yaban hayatı home range |

### Spor Bilimleri

| Veri Seti | Hedef Analiz |
|---|---|
| `01_antrenman_protokolu_karsilastirma` | ANOVA + post-hoc · Protokol etkisi |
| `02_performans_bataryasi` | Çoklu DV ANOVA + Cronbach α · Test bataryası |
| `03_yaralanma_risk_faktorleri` | Lojistik regresyon · Sakatlık öngörü |
| `04_antropometri_performans` | Çoklu regresyon · Beden bileşimi-performans |
| `05_kreatin_crossover` | Crossover + RM ANOVA · Suplement çalışması |
| `06_reaksiyon_suresi_RM` | Tekrarlı ölçümler ANOVA · Reaksiyon süresi |
| `07_egzersiz_akademik_mediation` | Mediation analizi · Egzersiz → akademik başarı |
| `08_super_lig_mac_istatistikleri` | Tanımlayıcı + Poisson regresyon · Maç gol verisi |

---

## 🏛️ Planlama ve Tasarım
**Dosya:** `MerQur_Ornek_Veriler_Planlama_ve_Tasarim_v1.0.0.zip` (10 MB · 3 disiplin · 24 veri seti)

### Peyzaj Mimarlığı

| Veri Seti | Hedef Analiz |
|---|---|
| `01_kentsel_park_anketi` | Likert + faktör analizi + Kruskal-Wallis · Park kullanım anketi |
| `02_yesil_alan_erisilebilirlik` | Mekânsal analiz (KDE + hotspot) · Erişilebilirlik haritalaması |
| `03_agac_saglkalimi` | Kaplan-Meier + Cox · Sokak ağacı sağkalım |
| `04_bitki_yetistirme_deneyi` | İki yönlü ANOVA · Tür × ortam etkileşimi |
| `05_kentsel_isi_adasi` | Mekânsal regresyon + Moran's I · UHI dağılımı |
| `06_peyzaj_tasarim_tercihi` | Conjoint / koşullu lojistik · Tasarım tercih analizi |
| `07_karmasik_anket_TUIK` | Anket tasarımı (ağırlıklı analiz) · TUIK karmaşık örneklem |
| `08_sifa_peyzaji_wellbeing` | Mediation + RM ANOVA · Şifa peyzajı etkisi |

### Mimarlık

| Veri Seti | Hedef Analiz |
|---|---|
| `01_poe_bina_kullanici` | Likert + faktör + ANOVA · Post-Occupancy Evaluation |
| `02_konut_tipi_memnuniyet` | Kruskal-Wallis + post-hoc · Konut tipi karşılaştırma |
| `03_kamusal_mekan_kullanim` | KDE yoğunluk + ki-kare · Mekân kullanım deseni |
| `04_bina_enerji_BEPTR` | Çoklu regresyon · Enerji performans tahmini |
| `05_aydinlatma_RM_ANOVA` | Tekrarlı ölçümler ANOVA · Aydınlatma senaryosu × görev |
| `06_tarihi_cevre_algi` | Faktör analizi + SEM · Algı boyutları |
| `07_ofis_verimliligi` | Çoklu regresyon · Ofis tasarımı-verimlilik |
| `08_yangin_tahliye_simulasyon` | Sağkalım + ANOVA · Tahliye süresi simülasyonu |

### Şehir ve Bölge Planlama

| Veri Seti | Hedef Analiz |
|---|---|
| `01_tuik_il_endeksleri_panel` | Panel veri + Moran's I · İl endeks zaman serisi |
| `02_ulasim_modal_split` | Multinomial lojistik · Ulaşım türü tercihi |
| `03_kentsel_donusum_once_sonra` | Eşleştirilmiş t / Wilcoxon · Müdahale öncesi-sonrası |
| `04_mekansal_esitsizlik_erisim` | Gini + Moran's I · Erişim eşitsizliği |
| `05_konut_piyasasi_kira_hedonik` | Hedonik regresyon · Kira fiyat modeli |
| `06_trafik_sayim_kaza` | Poisson regresyon · Kaza sıklığı modeli |
| `07_sosyal_donati_yeterlilik` | Tanımlayıcı + ki-kare · Donatı yeterlilik analizi |
| `08_iot_sensor_zaman_serisi` | Zaman serisi (ARIMA) · IoT sensör trendi |

---

## 👥 Sosyal Bilimler
**Dosya:** `MerQur_Ornek_Veriler_Sosyal_Bilimler_v1.0.0.zip` (8 MB · 4 disiplin · 32 veri seti)

### Sosyoloji

| Veri Seti | Hedef Analiz |
|---|---|
| `01_yasam_memnuniyeti_TUIK` | Sıralı lojistik · Yaşam memnuniyeti puanı |
| `02_sosyal_sermaye_5il` | İki yönlü ANOVA + faktör · İl × demografik |
| `03_toplumsal_cinsiyet_tutum` | Likert + Cronbach α + ANOVA · Tutum ölçeği |
| `04_goc_adaptasyon_kohort` | Kohort + sağkalım · Göç adaptasyonu |
| `05_evlilik_bosanma_survival` | Kaplan-Meier + Cox · Evlilik süresi |
| `06_egitim_esitsizligi_multilevel` | HLM (3 düzey) · Okul × öğrenci |
| `07_siyasi_tutum_medya` | Multinomial lojistik · Medya × parti tercihi |
| `08_yaslilik_iyilik_hali` | Faktör analizi + SEM · İyilik hali boyutları |

### İşletme

| Veri Seti | Hedef Analiz |
|---|---|
| `01_musteri_memnuniyeti_NPS` | Tanımlayıcı + ki-kare · NPS skoru |
| `02_ab_testi_eticaret` | Bağımsız t + bootstrap CI · A/B test |
| `03_calisan_turnover` | Lojistik regresyon + Cox · Çalışan ayrılma |
| `04_satis_tahmin_zaman_serisi` | ARIMA / mevsimsel · Satış tahmini |
| `05_marka_algisi_aaker` | Faktör analizi + Cronbach α · Marka boyutları |
| `06_pazarlama_mix_panel` | Panel veri · Pazarlama bütçe etkisi |
| `07_kredi_skorlama` | Lojistik regresyon + ROC · Kredi riski |
| `08_360_performans` | Tekrarlı ölçümler + ICC · 360° performans değerlendirme |

### Ekonometri

| Veri Seti | Hedef Analiz |
|---|---|
| `01_panel_il_yil_TUIK` | Sabit/rasgele etki paneli · İl-yıl endeksleri |
| `02_makro_zaman_serisi_aylik` | ARIMA + birim kök testi · Makro değişkenler |
| `03_hane_butce_anketi` | Çoklu regresyon · Hane harcama analizi |
| `04_mincer_ucret_heckman` | Heckman düzeltme · Ücret modeli |
| `05_did_politika_mudahalesi` | Difference-in-differences · Politika etkisi |
| `06_iv_2sls_egitim_getirisi` | Araç değişkenli (2SLS) · Eğitim getirisi |
| `07_rdd_burs_esigi` | Regresyon süreksizliği (RDD) · Burs etkisi |
| `08_bist_garch_volatilite` | GARCH · BIST oynaklık modeli |

### Eğitim Bilimleri

| Veri Seti | Hedef Analiz |
|---|---|
| `01_PISA_benzeri_lise_basari` | HLM (öğrenci × okul) · PISA-tipi başarı |
| `02_ogretim_yontem_RCT` | Bağımsız t + ANCOVA · Yöntem karşılaştırma RCT |
| `03_matematik_tutum_olcegi` | Faktör analizi + Cronbach α · Tutum ölçeği |
| `04_IRT_LGS_madde_analizi` | Madde tepki kuramı (IRT) · Madde analizi |
| `05_akademik_basari_3duzey_HLM` | 3-düzey HLM · İl × okul × öğrenci |
| `06_erken_cocukluk_buyume` | Boylamsal mixed model · Gelişim eğrisi |
| `07_LMS_cevrimici_ogrenme` | Çoklu regresyon · LMS log analizi |
| `08_ogretmen_tukenmislik_MBI` | Faktör analizi + ANOVA · MBI ölçek validasyon |

---

## 🌾 Tarım, Orman ve Doğa Bilimleri
**Dosya:** `MerQur_Ornek_Veriler_Tarim_Orman_Doga_v1.0.0.zip` (3 MB · 3 disiplin · 24 veri seti)

### Orman Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_orman_envanteri` | Tanımlayıcı + ANOVA · Meşçere parametreleri |
| `02_biyokutle_allometri` | Power-law regresyon · Allometrik denklem |
| `03_yangin_risk_il_ay` | Panel + Moran's I · İl bazlı yangın riski |
| `04_yetisme_ortami` | Çoklu regresyon · Bonitet sınıfı |
| `05_agaclandirma_deneyi` | İki yönlü ANOVA · Tür × tekniği |
| `06_orman_sagligi_kuruma` | Lojistik regresyon · Kuruma riski |
| `07_karbon_stoku_toprak` | Mixed model · Toprak C stok modelleme |
| `08_odun_tuketimi_hane` | Çoklu regresyon · Yakacak odun talep |

### Ziraat Mühendisliği

| Veri Seti | Hedef Analiz |
|---|---|
| `01_bugday_cesit_gubre_splitplot` | Split-plot ANOVA · Çeşit × gübre denemesi |
| `02_domates_sera_RM` | Tekrarlı ölçümler ANOVA · Sera büyüme |
| `03_toprak_verimliligi_bolgesel` | Mekânsal kümeleme + Moran's I · Toprak verimliliği |
| `04_sulama_etkinligi_DOE` | Faktöriyel DOE · Sulama × dozaj |
| `05_sut_sigiri_panel` | Panel veri / mixed · Süt verimi paneli |
| `06_hastalik_yayilim_epidemi` | Zaman serisi + spatial · Bitki hastalık epidemisi |
| `07_pestisit_latin_kare` | Latin kare ANOVA · Pestisit denemesi |
| `08_il_yil_iklim_verim_panel` | Panel + iklim sürücüleri · Verim-iklim ilişkisi |

### Biyoloji

| Veri Seti | Hedef Analiz |
|---|---|
| `01_tur_cesitliligi_ekolojisi` | Shannon/Simpson + ANOVA · Çeşitlilik indeksleri |
| `02_hucre_kulturu_dozaj_yanit` | Doğrusal olmayan regresyon · Doz-yanıt EC50 |
| `03_hucre_bolunme_kinetigi` | Üstel regresyon · Hücre bölünme kinetiği |
| `04_rnaseq_ekspresyon` | Çoklu DV t + Bonferroni · Gen ekspresyon farkı |
| `05_bitki_stres_fizyoloji` | İki yönlü ANOVA · Stres × tür etkileşimi |
| `06_balik_populasyon_dinamigi` | Mark-recapture + zaman serisi · Popülasyon |
| `07_kus_halkalama_gocyolu` | Mekânsal analiz (KDE + Moran's I) · Göç yolları |
| `08_mikrobiyom_16S_OTU` | Çok değişkenli + PCoA · OTU tablosu |

---

## 📖 Kullanım

1. İlgili kategori ZIP'ini [release sayfasından](https://github.com/omerorucu/merqur/releases/tag/v1.0.0) indirin.
2. ZIP'i istediğiniz klasöre çıkarın.
3. MerQur'u açın → **Dosya → Veri Dosyası Aç** → ilgili `.xlsx`'i seçin.
4. Her klasörde `MerQur_*_Veri_Setleri_Rehberi.docx` Word dosyası bulunur — önerilen analiz adımlarını ekran görüntüleriyle anlatır.

---

🤖 *Bu rehber MerQur v1.0.0 ile birlikte yayınlanmıştır.*
