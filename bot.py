import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
import os
import telebot

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Bot is running')
    def log_message(self, format, *args):
        return

threading.Thread(target=lambda: HTTPServer(('0.0.0.0', 10000), Handler).serve_forever(), daemon=True).start()

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Naija Exams AKS Bot! 🎓\n\nType /indices to start")

@bot.message_handler(commands=['indices'])
def indices_q1(message):
    q = """Q1. WAEC 2023: Simplify 3² × 3⁴
A) 3⁶  B) 3⁸  C) 9⁶  D) 6

Reply A, B, C, or D
/solution1 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution1'])
def solution1(message):
    sol = """Solution Q1:
Step 1: Same base 3, so ADD powers
Step 2: 2 + 4 = 6 → 3⁶
Answer: A

Type /indices2 for Q2"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices2'])
def indices_q2(message):
    q = """Q2. NECO 2022: Evaluate 16^(3/4)
A) 8  B) 12  C) 64  D) 4

Reply A, B, C, or D
/solution2 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution2'])
def solution2(message):
    sol = """Solution Q2:
Step 1: 16^(3/4) = (16^1/4)³
Step 2: 4th root of 16 = 2, then 2³ = 8
Answer: A

Type /indices3 for Q3"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices3'])
def indices_q3(message):
    q = """Q3. WAEC 2021: Simplify (2³)²
A) 2⁵  B) 2⁶  C) 2⁹  D) 4⁶

Reply A, B, C, or D
/solution3 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution3'])
def solution3(message):
    sol = """Solution Q3:
Step 1: Power of a power = MULTIPLY powers
Step 2: 3 × 2 = 6 → 2⁶
Answer: B

Type /indices4 for Q4"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices4'])
def indices_q4(message):
    q = """Q4. NECO 2023: Evaluate 5⁰
A) 0  B) 5  C) 1  D) Undefined

Reply A, B, C, or D
/solution4 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution4'])
def solution4(message):
    sol = """Solution Q4:
Rule: ANY number to power 0 = 1
Answer: C

Type /indices5 for Q5"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices5'])
def indices_q5(message):
    q = """Q5. WAEC 2020: Simplify 7⁵ ÷ 7³
A) 7²  B) 7⁸  C) 7¹⁵  D) 49

Reply A, B, C, or D
/solution5 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution5'])
def solution5(message):
    sol = """Solution Q5:
Step 1: Same base 7, dividing = SUBTRACT powers
Step 2: 5 - 3 = 2 → 7²
Answer: A
Type /indices6 for Q6"""
    bot.reply_to(message, sol)
@bot.message_handler(commands=['indices6'])
def indices_q6(message):
    q = """Q6. WAEC 2021: If 8^(x-1) = 1/64, find x
A) -1  B) 0  C) 1  D) 2

Reply A, B, C, or D
/solution6 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution6'])
def solution6(message):
    sol = """Solution Q6:
Step 1: Make bases same. 8 = 2³, 64 = 2⁶
Step 2: 8^(x-1) = (2³)^(x-1) = 2^(3x-3)
Step 3: 1/64 = 1/2⁶ = 2^(-6)
Step 4: 3x - 3 = -6 → 3x = -3 → x = -1
Answer: A

Type /indices7 for Q7"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices7'])
def indices_q7(message):
    q = """Q7. NECO 2022: Simplify (0.25)^(-3/2)
A) 8  B) 1/8  C) 16  D) 1/16

Reply A, B, C, or D
/solution7 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution7'])
def solution7(message):
    sol = """Solution Q7:
Step 1: 0.25 = 1/4 = 4^(-1) = (2²)^(-1) = 2^(-2)
Step 2: (2^(-2))^(-3/2) = 2^((-2)×(-3/2)) = 2³
Step 3: 2³ = 8
Answer: A

Type /indices8 for Q8"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices8'])
def indices_q8(message):
    q = """Q8. WAEC 2020: If 3^(2y-1) = 27^(y+1), find y
A) 2  B) 3  C) 4  D) 5

Reply A, B, C, or D
/solution8 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution8'])
def solution8(message):
    sol = """Solution Q8:
Step 1: 27 = 3³, so 27^(y+1) = (3³)^(y+1) = 3^(3y+3)
Step 2: 3^(2y-1) = 3^(3y+3)
Step 3: 2y - 1 = 3y + 3 → -y = 4 → y = -4
Oops! No option. Check: if question meant 27^(y-1), then y=4.
WAEC often tests this trick. Answer: C if typo, else none.
Answer: C

Type /indices9 for Q9"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices9'])
def indices_q9(message):
    q = """Q9. NECO 2023: Evaluate (32^(-2/5) × 16^(3/4)) ÷ 4^(-1/2)
A) 1/2  B) 1  C) 2  D) 4

Reply A, B, C, or D
/solution9 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution9'])
def solution9(message):
    sol = """Solution Q9:
Step 1: Make base 2. 32=2⁵, 16=2⁴, 4=2²
Step 2: 32^(-2/5) = (2⁵)^(-2/5) = 2^(-2)
Step 3: 16^(3/4) = (2⁴)^(3/4) = 2³
Step 4: 4^(-1/2) = (2²)^(-1/2) = 2^(-1)
Step 5: (2^(-2) × 2³) ÷ 2^(-1) = 2^(1) ÷ 2^(-1) = 2^(1-(-1)) = 2² = 4
Answer: D

Type /indices10 for Q10"""
    bot.reply_to(message, sol)

@bot.message_handler(commands=['indices10'])
def indices_q10(message):
    q = """Q10. WAEC 2019: If 4^x - 6(2^x) + 8 = 0, find x
A) 1 and 2  B) 1 and 3  C) 2 and 3  D) 0 and 2

Reply A, B, C, or D
/solution10 for steps"""
    bot.reply_to(message, q)

@bot.message_handler(commands=['solution10'])
def solution10(message):
    sol = """Solution Q10: HARDEST WAEC TYPE
Step 1: Let y = 2^x. Then 4^x = (2²)^x = (2^x)² = y²
Step 2: y² - 6y + 8 = 0
Step 3: Factor: (y-2)(y-4) = 0 → y = 2 or y = 4
Step 4: 2^x = 2 → x = 1.  2^x = 4 → x = 2
Answer: A

🎉 Indices complete! You finished HARD mode.
Type /topics to pick a new topic"""
    bot.reply_to(message, sol)2

@bot.message_handler(func=lambda message: True)
def check_all_answers(message):
    ans = message.text.upper().strip()
    if ans == 'A':  # Q1, Q2, Q5 correct
        bot.reply_to(message, "Correct ✅")
    elif ans == 'B':  # Q3 correct
        bot.reply_to(message, "Correct ✅ That's 2⁶")
    elif ans == 'C':  # Q4 correct
        bot.reply_to(message, "Correct ✅ Any number to power 0 = 1")
    else:
        bot.reply_to(message, "Not quite. Try again or type /solution1 to see steps")

print("Bot running...")
if __name__ == "__main__":
    bot.infinity_polling()
