# Mystery Module - Quadratic Equation Solver

## 📋 Proje Açıklaması

`mystery_module.py` ikinci dereceden denklemleri (quadratic equations) çözmek için kullanılan bir Python modülüdür.

### Matematiksel Temel

**Genel Form:** `ax² + bx + c = 0`

Bu modül, verilen `a`, `b` ve `c` katsayılarını kullanarak denklemin köklerini hesaplar.

**Çözüm Yöntemi:** Diskriminant (Δ) kullanarak
- **Δ = b² - 4ac**
- Eğer Δ < 0: Gerçek kök yoktur (kompleks kökler vardır)
- Eğer Δ ≥ 0: Kökler şunlardır:
  - x₁ = (-b + √Δ) / 2a
  - x₂ = (-b - √Δ) / 2a

---

## 🔧 Kurulum

### Gereksinimler
- Python 3.7+
- `math` modülü (Python standart kütüphanesi, kurulum gereksiz)

### Kullanım

1. **Dosyayı projenize ekleyin:**
   ```bash
   # mystery_module.py'i projenize kopyalayın
   ```

2. **Modülü içe aktarın:**
   ```python
   from mystery_module import fn_x
   ```

3. **Fonksiyonu çağırın:**
   ```python
   roots = fn_x(a, b, c)
   ```

---

## 📚 Fonksiyonlar

### `fn_x(a, b, c)`

İkinci dereceden denklemin köklerini hesaplar.

#### Parametreler
| Parametre | Tip | Açıklama |
|-----------|-----|----------|
| `a` | `float` veya `int` | x² katsayısı. **Gerekli:** a ≠ 0 |
| `b` | `float` veya `int` | x katsayısı |
| `c` | `float` veya `int` | Sabit sayı (konstant) |

#### Dönüş Değeri
| Durum | Dönüş | Açıklama |
|-------|-------|----------|
| Gerçek kökler var | `(root1, root2)` | İki veya tekrarlayan kök |
| Gerçek kök yok | `None` | Diskriminant < 0 (kompleks kökler) |

**Dönüş Tipi:** `tuple[float, float] \| None`

#### Örnek Kullanım
```python
# İki farklı gerçek kök
result = fn_x(1, -5, 6)
print(result)  # (3.0, 2.0)

# Gerçek kök yok
result = fn_x(1, 0, 1)
print(result)  # None

# Tekrarlayan kök (Δ = 0)
result = fn_x(1, -4, 4)
print(result)  # (2.0, 2.0)
```

---

## 💡 Örnek Kullanım

### Örnek 1: Basit İkinci Dereceden Denklem

```python
from mystery_module import fn_x

# Denklem: x² - 5x + 6 = 0
# Katsayılar: a=1, b=-5, c=6
roots = fn_x(1, -5, 6)

if roots:
    print(f"Kökler: x₁ = {roots[0]}, x₂ = {roots[1]}")
else:
    print("Gerçek kök yok")
```

**Çıktı:**
```
Kökler: x₁ = 3.0, x₂ = 2.0
```

---

### Örnek 2: Gerçek Kök Olmayan Denklem

```python
from mystery_module import fn_x

# Denklem: x² + 1 = 0 (a=1, b=0, c=1)
roots = fn_x(1, 0, 1)

if roots:
    print(f"Kökler: {roots}")
else:
    print("Gerçek kök yok - kompleks kökler vardır")
```

**Çıktı:**
```
Gerçek kök yok - kompleks kökler vardır
```

---

### Örnek 3: Tekrarlayan Kök (Double Root)

```python
from mystery_module import fn_x

# Denklem: x² - 4x + 4 = 0 (a=1, b=-4, c=4)
roots = fn_x(1, -4, 4)

print(f"Kökler: {roots}")
```

**Çıktı:**
```
Kökler: (2.0, 2.0)
```

---

### Örnek 4: Negatif Katsayılar

```python
from mystery_module import fn_x

# Denklem: 2x² + 3x - 2 = 0 (a=2, b=3, c=-2)
roots = fn_x(2, 3, -2)

if roots:
    print(f"Kökler: x₁ = {roots[0]:.4f}, x₂ = {roots[1]:.4f}")
```

**Çıktı:**
```
Kökler: x₁ = 0.5000, x₂ = -2.0000
```

---

### Örnek 5: Batch İşleme

```python
from mystery_module import fn_x

# Birden fazla denklemi çöz
equations = [
    (1, -5, 6),      # x² - 5x + 6 = 0
    (1, 0, -1),      # x² - 1 = 0
    (1, 2, 1),       # x² + 2x + 1 = 0
    (1, 0, 1),       # x² + 1 = 0
]

for i, (a, b, c) in enumerate(equations, 1):
    roots = fn_x(a, b, c)
    eq_str = f"{a}x² + {b}x + {c} = 0"
    
    if roots:
        print(f"Denklem {i}: {eq_str}")
        print(f"  Kökler: {roots}\n")
    else:
        print(f"Denklem {i}: {eq_str}")
        print(f"  Gerçek kök yok\n")
```

**Çıktı:**
```
Denklem 1: 1x² + -5x + 6 = 0
  Kökler: (3.0, 2.0)

Denklem 2: 1x² + 0x + -1 = 0
  Kökler: (1.0, -1.0)

Denklem 3: 1x² + 2x + 1 = 0
  Kökler: ((-1.0, -1.0))

Denklem 4: 1x² + 0x + 1 = 0
  Gerçek kök yok
```

---

## ⚠️ Önemli Notlar

### 1. **Katsayı a ≠ 0 Olmalı**
Eğer `a = 0` ise, bu ikinci dereceden denklem değil, birinci dereceden denklemdir ve fonksiyon hatalı sonuç verebilir.

```python
# ❌ YANLIŞ
fn_x(0, 5, 6)  # a = 0 olmamalı!

# ✅ DOĞRU
fn_x(1, 5, 6)
```

### 2. **Diskriminant Negatif Olunca None Döner**
Diskriminant (Δ = b² - 4ac) negatif ise fonksiyon `None` döner. Bu, denklemin kompleks kökler olduğu anlamına gelir.

```python
roots = fn_x(1, 0, 1)
if roots is None:
    print("Kompleks kök!")
```

### 3. **Kök Sırası**
Döndürülen tuple'da:
- `roots[0]` = (-b + √Δ) / 2a
- `roots[1]` = (-b - √Δ) / 2a

```python
roots = fn_x(1, -5, 6)
# roots[0] = 3.0 (büyük kök)
# roots[1] = 2.0 (küçük kök)
```

### 4. **Tek/Çift Kökler**
Diskriminant sıfıra eşit olduğunda, her iki kök de aynıdır (tekrarlayan/çift kök).

```python
roots = fn_x(1, -4, 4)
# roots = (2.0, 2.0)  # Tekrarlayan kök
```

---

## 📊 Test Durumları

| Denklem | a | b | c | Beklenen Sonuç | Diskriminant |
|---------|---|---|---|----------------|--------------|
| x² - 5x + 6 = 0 | 1 | -5 | 6 | (3.0, 2.0) | 1 |
| x² + 1 = 0 | 1 | 0 | 1 | None | -4 |
| x² - 4x + 4 = 0 | 1 | -4 | 4 | (2.0, 2.0) | 0 |
| x² - 1 = 0 | 1 | 0 | -1 | (1.0, -1.0) | 4 |
| 2x² - 3x + 1 = 0 | 2 | -3 | 1 | (1.0, 0.5) | 1 |

---

## 🐛 Bilinen Sınırlamalar

1. **Tip Denetimi Yok:** Fonksiyon çalışırken hatalara açıktır
2. **Katsayı Validasyonu Yok:** a = 0 için hata döndürmez
3. **Docstring Yok:** Fonksiyonun amacını açıkça dokumentasyon yok
4. **Type Hints Yok:** IDE desteklenmediği için autocomplete zor

---

## 📝 Geliştirme Önerileri

```python
# Geliştirilmiş Versiyon (Type Hints + Docstring)
from typing import Optional, Tuple
import math

def solve_quadratic_equation(a: float, b: float, c: float) -> Optional[Tuple[float, float]]:
    """
    İkinci dereceden denklemi çözüntü.
    
    Args:
        a: x² katsayısı
        b: x katsayısı
        c: Sabit
        
    Returns:
        Kökler (kök1, kök2) veya gerçek kök yoksa None
        
    Raises:
        ValueError: Eğer a = 0 ise
    """
    if a == 0:
        raise ValueError("a sıfır olamaz - bu ikinci dereceden denklem değildir")
    
    discriminant = b**2 - 4*a*c
    if discriminant < 0:
        return None
    
    sqrt_discriminant = math.sqrt(discriminant)
    root1 = (-b + sqrt_discriminant) / (2*a)
    root2 = (-b - sqrt_discriminant) / (2*a)
    
    return (root1, root2)
```

---

## ✅ Özet

| Özellik | Durum |
|---------|-------|
| **Fonksiyon Adı** | ❌ Belirsiz (fn_x) |
| **Parametre Adları** | ❌ Kısaltılmış (a, b, c, d) |
| **Docstring** | ❌ Yok |
| **Type Hints** | ❌ Yok |
| **Error Handling** | ❌ Yetersiz |
| **Matematiksel Doğruluk** | ✅ Doğru |
| **Kullanışlılık** | ✅ Temel |

---

## 📧 İletişim & Destek

Bu modül hakkında sorularınız varsa, lütfen [proje sahibine](https://github.com/semagllclkk/test-proje) başvurun.
