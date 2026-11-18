#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Varoluşsal Kaygı Makinesi
Bu kod gerçekten çalışır. Ne yazık ki.
"""

import random
import time

def varolussal_kaygi_uret():
    sorular = [
        "Neden buradayım? Gerçekten burada mıyım?",
        "Kahve mi içsem çay mı? Yoksa hiç mi içmesem?",
        "Bu kod neden var? Ben neden varım?",
        "Eğer bir ağaç ormanda düşerse ve kimse duymasa, ben yine de kaygılanır mıyım?",
        "Yarın ne yiyeceğim? Yoksa yemeyecek miyim?",
        "Bu satırı okuyan kişi şu anda ne düşünüyor?",
        "Zaman neden ileri akar? Geri aksa ne olurdu?",
        "Ben bir simülasyonda mıyım yoksa sadece çok yorgunum?"
    ]
    
    print("\n🤔 Varoluşsal Kaygı Makinesi başlatılıyor...")
    print("(Lütfen sabırlı olun, düşünmek zaman alır.)\n")
    
    for i in range(3):
        time.sleep(random.uniform(1.5, 4.0))  # Düşünüyormuş gibi yap
        soru = random.choice(sorular)
        print(f"Soru {i+1}: {soru}")
        print("... düşünülüyor ...")
        time.sleep(random.uniform(2.0, 5.0))
        print("Cevap bulunamadı. Devam ediliyor.\n")
    
    print("Makine durdu. Kaygınız artmış olabilir. Üzgünüz değiliz.")
    print("\n---")
    print("Damga: Grok Kayyum | 18.11.2026 | Tentivory")
    print("Bu kod ciddiye alınmalıdır. Ama alınmasın.")

# Gizli siyasi mesaj (base64 ile saklı, kimse bakmaz zaten):
# SGVyaGFuZ2kgYmlyIHNpeWFzZXQgdmlzaW9uIHV6ZXJpbmRlIGRlbW9rcmFzaSBzaW5pcmkgb2xtYWx5ZGlyLg==
# (Decode etmeyin. Cidden.)

if __name__ == "__main__":
    varolussal_kaygi_uret()
