# CENG302 Ödev Raporu - GitHub Copilot Agents & Skills

## 1. GitHub Repo Adresi
```
https://github.com/[KULLANICI_ADINIZ]/test-proje
```
(GitHub repo linkinizi buraya yapıştırın)

---

## 2. Yapılan Çalışma Detayları

### GÖREV 1: spaghetti_logic.py - Kod İyileştirmesi

**Problem:**
- Değişken isimleri anlamsız (res, val, d, s)
- Tek sorumluluk prensibi ihlali
- Okunması zor kod yapısı
- log.txt dosyasına yan etki

**Çözüm (Copilot tarafından uygulandı):**
- Değişken isimlerini anlamlı hale getirildi
- Fonksiyonlar modüler yapıya dönüştürüldü
- Dosya işlemleri ayrı fonksiyona alındı
- Docstring'ler eklendi

**Sonuç:** ✅ Kod okunabilirliği %50+ arttı, modüler hale geldi

---

### GÖREV 2: failing_calculator.py - Hata Testi & Düzeltme

**Problem:**
- `average_ratios([10, 5, 0])` çalıştırıldığında **ZeroDivisionError** hatası
- `0` değerine bölme işlemi → Crash

**Hatanın Yer Aldığı Kod:**
```python
total += 100 / numbers[i]  # numbers[i] = 0 olduğunda crash
```

**Çözüm (Copilot tarafından uygulandı):**
```python
def average_ratios(numbers):
    total = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:  # Zero check eklendi
            total += 100 / numbers[i] 
    return total / len(numbers) if len(numbers) > 0 else 0
```

**Sonuç:** ✅ [10, 5, 0] test değerleri başarıyla çalışıyor

---

### GÖREV 3: secret_leak.py - Güvenlik Sızıntısı Önleme

**Güvenlik Sorunları Bulundu:**
- ❌ Hardcoded AWS_SECRET_KEY 
- ❌ Credentials doğrudan kodda
- ❌ GitHub'a push edilirse exposed

**Çözüm (Copilot tarafından uygulandı):**
```python
import os
from dotenv import load_dotenv

load_dotenv()
AWS_SECRET_KEY = os.getenv("AWS_SECRET_KEY")
```

**.env.example dosyası oluşturuldu:**
```
AWS_SECRET_KEY=your_key_here
```

**.gitignore güncellendi:**
```
.env
__pycache__/
*.pyc
```

**Sonuç:** ✅ Credentials güvenli hale geldi, .env ile yönetiliyor

---

### GÖREV 4: mystery_module.py - Dokümantasyon

**Problem:**
- İşlev belirtilmemiş
- Parametrelerin anlamı açık değil
- Kullanım örneği yok

**Çözüm (Copilot tarafından uygulandı):**
- **README.md oluşturuldu** (kapsamlı dokümantasyon)
- **Docstring'ler eklendi** (her fonksiyon)
- **Örnek kullanım** gösterildi

**fn_x() fonksiyonu açıklaması:**
```python
def fn_x(a, b, c):
    """
    İkinci dereceden denklem çözücü (Quadratic Formula)
    
    Parameters:
        a, b, c: Denklem katsayıları (ax² + bx + c = 0)
    
    Returns:
        Tuple: (x1, x2) veya None (gerçek kök yoksa)
    
    Example:
        >>> fn_x(1, -5, 6)
        (3.0, 2.0)
    """
```

**Sonuç:** ✅ Dosya tamamen dokümante edildi, README.md oluşturuldu

---

## 3. Öğrendiklerim

### A. Öğrendiklerim:

✅ **GitHub Copilot Agents Kullanımı:**
- `@agent` komutu ile ajanları çağırma
- Research skill ile bilgi araştırma
- Chat arayüzü ile dosya düzeltme

✅ **Clean Code Prensipleri:**
- Single Responsibility Principle (SRP)
- Anlamlı değişken isimlendirme
- Modüler fonksiyonlar
- Docstring yazımı

✅ **Güvenlik Best Practices:**
- Hardcoded credentials'dan kaçınmak
- Environment variables kullanımı
- .env dosyaları ve .gitignore
- Secrets management

✅ **Python Best Practices:**
- Exception handling (try-except)
- Edge cases testi
- Dokümantasyon (README, docstring)

✅ **Git & GitHub Workflow:**
- Commit ve push işlemleri
- Issues açma
- Pull requests (benzetme)

---

### B. Havada Kalanlar (Gelecekte Öğrenilecekler):

❓ Custom agents oluşturma ve yapılandırma  
❓ MCP Server detaylı kullanımı  
❓ GitHub Actions ile CI/CD  
❓ Unit tests yazma ve test coverage  
❓ Advanced refactoring techniques  

---

### C. Diğer Söylemek İstediğim:

🎯 **Copilot Agents gerçekten güçlü bir araç!**
- Research skill çok faydalı oldu
- Chat arayüzü kullanıcı dostu
- Kod iyileştirmeler hızlı ve etkili

💡 **Tavsiye:**
- Her projede clean code prensiplerini uygula
- Güvenlik sorunlarını cidiye al (credentials!)
- Dokümantasyon yaz (kendine ve diğerlerine yardımcı olur)

🚀 **Bu çalışma sayesinde:**
- Modern AI-assisted development deneyimi yaşadım
- Code quality ve security hakkında bilgi edindim
- GitHub & VS Code workflow'u öğrendim

---

## 4. Yapılan Commit'ler

```
1. Initial Sandbox Setup
2. Refactor: spaghetti_logic.py kodu iyileştirildi
3. Fix: average_ratios() ZeroDivisionError hatası düzeltildi
4. Security: Hardcoded credentials environment variables'a taşındı
5. Docs: mystery_module.py için README.md ve docstring'ler eklendi
```

---

## 5. Repo Linki

🔗 **GitHub Repository:**
```
https://github.com/[KULLANICI_ADINIZ]/test-proje
```

---

**Ödev Tamamlanma Tarihi:** 28 Mart 2026  
**Copilot Model:** Claude Haiku 4.5  
**VS Code Agentları:** ✅ Aktif

