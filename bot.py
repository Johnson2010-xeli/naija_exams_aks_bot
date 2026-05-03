import os
import telebot
   TOKEN = os.environ.get('BOT_TOKEN')
   bot = telebot.TeleBot(TOKEN)
  
@bot.message_handler(commands=['start'])  
def send_welcome(message):  
    bot.reply_to(message, "Welcome to Naija Exams Bot 🇳🇬\n\nFree WAEC + NECO CBT practice.\n\nType /indices to start Math")
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
    q = """Q2. NECO 2022: Evaluate 16^¾
A) 8  B) 12  C) 64  D) 4

Reply A, B, C, or D
/solution2 for steps"""
    bot.reply_to(message, q)

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

🎉 Topic complete! You finished Indices.
Type /topics to see more subjects soon"""
    bot.reply_to(message, sol)
@bot.message_handler(func=lambda message: message.text.upper().strip() in ['A','B','C','D'])
def check_all_answers(message):
    ans = message.text.upper().strip()
    if ans == 'B':  # Q3 correct
        bot.reply_to(message, "Correct ✅ That's power rule! Next: /indices4 or /solution3")
    elif ans == 'C':  # Q4 correct  
        bot.reply_to(message, "Correct ✅ Zero power rule! Next: /indices5 or /solution4")
    elif ans == 'A':  # Q1, Q2, Q5 correct
        bot.reply_to(message, "Correct ✅ Fire! Next question or /solution for steps")
    else:
        bot.reply_to(message, "Not quite ❌ Check the rules. Type /solution1, /solution2, etc for steps")
print("Bot running... Don't close Pydroid")  
   if __name__ == "__main__":
       bot.infinity_polling()
